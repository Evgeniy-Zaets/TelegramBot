FROM python:3.10

WORKDIR /telegram_bot

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY bot .

RUN python3 -m venv /telegram_bot/venv

RUN . /telegram_bot/venv/bin/activate

# Install dependencies:
RUN pip install -r requirements.txt