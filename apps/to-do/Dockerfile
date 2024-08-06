FROM python:3.12-alpine

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./app /code/app

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
