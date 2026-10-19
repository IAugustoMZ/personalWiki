.PHONY: help new-entry clean

help:
	@echo "personalWiki - Available Commands"
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  new-entry      Create a new wiki markdown entry"
	@echo "  help           Show this help message"

new-entry:
	@./scripts/new_entry.sh

.DEFAULT_GOAL := help
