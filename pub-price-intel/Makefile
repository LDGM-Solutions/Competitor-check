.PHONY: install format lint test scrape match

install:
	pip install -r requirements.txt
	playwright install --with-deps
format:
	black .
lint:
	flake8 scrapers matcher parser cli.py
test:
	pytest
scrape:
	python cli.py scrape
match:
	python cli.py match
