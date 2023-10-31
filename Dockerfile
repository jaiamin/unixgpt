FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV USER_INPUT=""

CMD ["python3", "unixgpt/__main__.py", ${USER_INPUT}]