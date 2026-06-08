FROM python:3.11-slim

WORKDIR /app

COPY gridfetcher/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY gridfetcher/ .

ENTRYPOINT ["python", "run.py"]
