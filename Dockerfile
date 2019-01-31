FROM python:3.7-alpine

WORKDIR /usr/src/app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD *.py .

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
