.PHONY: help new-entry docs docs-build clean

help:
	@echo "personalWiki - Available Commands"
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  new-entry      Create a new wiki markdown entry"
	@echo "  docs           Serve the documentation site with live reload (http://127.0.0.1:8000)"
	@echo "  docs-build     Build the documentation site with strict link checks"
	@echo "  help           Show this help message"

new-entry:
	@./scripts/new_entry.sh

docs:
	poetry run mkdocs serve

docs-build:
	poetry run mkdocs build --strict

.DEFAULT_GOAL := help
