FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV TEST_INPUT="show me my files"

CMD ["python3", "-m", "unixgpt.__main__", "${TEST_INPUT}"]