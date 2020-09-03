FROM python:3.8-slim

WORKDIR /workdir

COPY requirements.txt requirements.txt

RUN apt-get update

RUN apt-get install -y gcc

RUN pip install --no-cache-dir  -r requirements.txt

COPY . .

CMD ["python", "start-spider.py"]