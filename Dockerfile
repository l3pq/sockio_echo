FROM python:3.11-slim

WORKDIR /app

COPY poetry.lock pyproject.toml main.py ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Uruchom aplikację przy starcie kontenera
CMD ["python", "./main.py"]
