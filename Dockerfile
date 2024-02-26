FROM python:3.8.13-alpine3.16

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY application application
COPY wsgi.py config.py ./

CMD [ "python" , "wsgi.py" ]
