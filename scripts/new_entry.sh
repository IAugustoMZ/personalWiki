#!/usr/bin/env bash
# Interactively create a new wiki markdown entry by cloning the last entry
# in a chosen leaf folder and bumping its sequence number.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXCLUDED_DIRS=("artifacts" "questions" ".git" ".claude")

is_excluded() {
    local name="$1"
    for ex in "${EXCLUDED_DIRS[@]}"; do
        [[ "$name" == "$ex" ]] && return 0
    done
    return 1
}

# List immediate subdirectories of $1, excluding top-level excluded dirs
# only when $1 is the repo root.
list_dirs() {
    local base="$1"
    local is_root="$2"
    local d name
    for d in "$base"/*/; do
        [[ -d "$d" ]] || continue
        name="$(basename "$d")"
        if [[ "$is_root" == "true" ]] && is_excluded "$name"; then
            continue
        fi
        printf '%s\n' "$name"
    done
}

# Returns 0 (true) if the folder contains at least one .md file other than README.md
has_markdown_entries() {
    local dir="$1"
    local f base
    for f in "$dir"/*.md; do
        [[ -e "$f" ]] || continue
        base="$(basename "$f")"
        [[ "$base" == "README.md" ]] && continue
        return 0
    done
    return 1
}

# Prompt user to pick one of the given options via numeric menu.
# $1: prompt label, $2: "true"/"false" whether option 0 = go up, rest: options
prompt_menu() {
    local label="$1"
    local allow_up="$2"
    shift 2
    local options=("$@")
    local i choice

    echo "" >&2
    echo "== $label ==" >&2
    if [[ "$allow_up" == "true" ]]; then
        echo "  0) .. (go up)" >&2
    fi
    for i in "${!options[@]}"; do
        printf "  %d) %s\n" "$((i + 1))" "${options[$i]}" >&2
    done

    while true; do
        read -rp "Select an option: " choice >&2
        if [[ "$allow_up" == "true" && "$choice" == "0" ]]; then
            echo "__UP__"
            return
        fi
        if [[ "$choice" =~ ^[0-9]+$ ]] && (( choice >= 1 && choice <= ${#options[@]} )); then
            echo "${options[$((choice - 1))]}"
            return
        fi
        echo "Invalid selection, try again." >&2
    done
}

# --- Step 1-4: navigate the folder tree until a leaf (markdown) folder is found ---
current_path="$REPO_ROOT"
at_root=true

while true; do
    if [[ "$at_root" == "false" ]] && has_markdown_entries "$current_path"; then
        break
    fi

    mapfile -t subdirs < <(list_dirs "$current_path" "$at_root")

    if [[ ${#subdirs[@]} -eq 0 ]]; then
        if has_markdown_entries "$current_path"; then
            break
        fi
        echo "No subfolders or markdown entries found in: $current_path" >&2
        exit 1
    fi

    allow_up="true"
    [[ "$current_path" == "$REPO_ROOT" ]] && allow_up="false"

    rel_display="${current_path#"$REPO_ROOT"/}"
    [[ "$current_path" == "$REPO_ROOT" ]] && rel_display="(root)"

    selection="$(prompt_menu "Select folder inside: $rel_display" "$allow_up" "${subdirs[@]}")"

    if [[ "$selection" == "__UP__" ]]; then
        current_path="$(dirname "$current_path")"
        at_root=false
        [[ "$current_path" == "$REPO_ROOT" ]] && at_root=true
        continue
    fi

    current_path="$current_path/$selection"
    at_root=false
done

echo "" >&2
echo "Target folder: ${current_path#"$REPO_ROOT"/}" >&2

# --- Step 5: identify the last file, its numbering and naming pattern ---
shopt -s nullglob
md_files=("$current_path"/*.md)
shopt -u nullglob

entries=()
for f in "${md_files[@]}"; do
    base="$(basename "$f")"
    [[ "$base" == "README.md" ]] && continue
    entries+=("$base")
done

if [[ ${#entries[@]} -eq 0 ]]; then
    echo "No existing markdown entries found in $current_path to use as a template." >&2
    exit 1
fi

# Sort by leading numeric prefix to find the highest-numbered entry.
last_file=""
last_num=-1
for base in "${entries[@]}"; do
    if [[ "$base" =~ ^([0-9]+)_ ]]; then
        num="${BASH_REMATCH[1]}"
        num_val=$((10#$num))
        if (( num_val > last_num )); then
            last_num=$num_val
            last_file="$base"
        fi
    fi
done

if [[ -z "$last_file" ]]; then
    echo "Could not detect a numbered file pattern (expected files like NN_tag_DDMMYYYY.md) in $current_path" >&2
    exit 1
fi

# Parse pattern: <digits>_<middle-parts>_<DDMMYYYY>.md
if [[ ! "$last_file" =~ ^([0-9]+)_(.+)_([0-9]{8})\.md$ ]]; then
    echo "File '$last_file' does not match expected pattern NN_..._DDMMYYYY.md" >&2
    exit 1
fi

old_num="${BASH_REMATCH[1]}"
middle="${BASH_REMATCH[2]}"
num_width=${#old_num}
new_num_val=$((10#$old_num + 1))
new_num="$(printf "%0${num_width}d" "$new_num_val")"

echo "Last entry: $last_file" >&2
echo "Next number: $new_num" >&2

# --- Step 6: ask the user for the new entry date ---
while true; do
    read -rp "Enter the entry date (DDMMYYYY): " new_date
    if [[ "$new_date" =~ ^[0-9]{8}$ ]]; then
        break
    fi
    echo "Invalid format. Please use DDMMYYYY (e.g. 11082025)." >&2
done

# --- Step 7: copy the last file into the new file name ---
new_file="${new_num}_${middle}_${new_date}.md"
new_path="$current_path/$new_file"

if [[ -e "$new_path" ]]; then
    echo "Target file already exists: $new_path" >&2
    exit 1
fi

cp "$current_path/$last_file" "$new_path"

echo "" >&2
echo "Created: ${new_path#"$REPO_ROOT"/}" >&2
