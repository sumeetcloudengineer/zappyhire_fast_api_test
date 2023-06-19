FROM python:3.10-alpine

WORKDIR /zappyhire_fast_api_test

COPY ./requirements.txt /zappyhire_fast_api_test/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /zappyhire_fast_api_test/requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]