FROM python:3-alpine

COPY hello.py /app/hello.py

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python","-u","hello.py"]