FROM python:3.13-slim

WORKDIR /app

COPY task_report.py .

RUN mkdir -p /app/data

ENV OUTPUT_DIR=/app/data

VOLUME ["/app/data"]

CMD ["python", "task_report.py"]