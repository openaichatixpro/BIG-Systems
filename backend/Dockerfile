FROM python:3.10-slim

WORKDIR /app

# system deps (if any)
RUN apt-get update && apt-get install -y --no-install-recommends \
                                                                                                    build-essential \
                                                                                                    curl \
                                                                                                    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
EXPOSE 3001

CMD ["python", "processor.py", "--watch-folder", "${WATCH_FOLDER:-/data}", "--output", "${OUTPUT_FOLDER:-/output}", "--batch-size", "${BATCH_SIZE:-50000}"]
