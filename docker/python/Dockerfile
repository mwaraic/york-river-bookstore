FROM python:3.8

COPY / bookstore

WORKDIR /bookstore

RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]