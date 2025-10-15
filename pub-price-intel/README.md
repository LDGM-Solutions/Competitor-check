# Pub Price Intelligence

This project provides a reproducible workflow for scraping drinks offers from various Glasgow venues, normalising product information, and matching the results against a canonical product catalog. The pipeline is designed to be orchestrated from the command line, but can also be scheduled using Prefect.

## Components

- **Scrapers** – Headless Playwright-based scrapers that download offer data.
- **Parser** – Utilities that clean and normalise scraped data.
- **Matcher** – Command-line interface to match offers to catalog SKUs using YAML rules.
- **Ops** – Prefect flows for orchestration and scheduling.

Refer to `cli.py` for the entrypoint that ties everything together.
