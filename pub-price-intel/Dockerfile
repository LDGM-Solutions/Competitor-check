FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install --with-deps

COPY . .

ENV PYTHONPATH=/app

ENTRYPOINT ["python", "cli.py"]
CMD ["scrape"]
