FROM python:3.8

WORKDIR /workdir

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir  -r requirements.txt

COPY . .

CMD ["python", "start-spider.py"]