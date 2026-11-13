.PHONY: lint
.PHONY: test

lint:
	find src -type f -name "*.py" -exec pylint {} +
	find tests -type f -name "*.py" -exec pylint {} +

test:
	pytest tests/
