test:
	poetry run pytest

run:
	poetry run python eclair_python/bindings.py

format:
	poetry run isort eclair_python/ tests/
	poetry run black eclair_python/ tests/

# TODO add lint (also to .PHONY)
# lint:
# 	poetry run ruff check

# Only needed if you don't use direnv
shell:
	poetry shell

# TODO remove recursively in all subdirs
clean:
	find eclair_python/ tests/ -type f | grep -E ".*.pyc$$" | xargs rm

.PHONY: test run format shell clean
