FROM python:3

WORKDIR /code

RUN pip install python-binance

COPY . .

CMD ["python","main.py"]
