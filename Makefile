#!make
VERSION := $(shell grep '__version__' src/aios3/__about__.py | cut -d= -f2 | sed 's/\"//g; s/ //')
export VERSION

.HELP: version ## Show the current version
version:
	echo ${VERSION}

.HELP: ver-bug ## Bump the version for a bug
ver-bug:
	bash ./scripts/verup.sh bug

.HELP: ver-feature ## Bump the version for a feature
ver-feature:
	bash ./scripts/verup.sh feature

.HELP: ver-release ## Bump the version for a release
ver-release:
	bash ./scripts/verup.sh release

.HELP: reqs  ## Upgrade requirements including pre-commit
reqs:
	pre-commit autoupdate
	uv lock --upgrade

.PHONY: docs # mark as phony so it always runs even we have a docs folder
.HELP: docs  ## Docs preview English
docs:
	./scripts/docstrings.sh
	open -a "Google Chrome" http://127.0.0.1:8000/aios3/
	scripts/docs-render-config.sh en
	mkdocs serve -f docs/_mkdocs.yml

.HELP: docs-ru  ## Docs preview Russian
docs-ru:
	./scripts/docstrings.sh
	open -a "Google Chrome" http://127.0.0.1:8000/aios3/
	scripts/docs-render-config.sh ru
	mkdocs serve -f docs/_mkdocs.yml

.HELP: help  ## Display this message
help:
	@grep -E \
		'^.HELP: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".HELP: |## "}; {printf "\033[36m%-19s\033[0m %s\n", $$2, $$3}'
