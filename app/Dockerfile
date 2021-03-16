FROM python:3
WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

CMD ["/usr/local/bin/gunicorn", "--config", "gunicorn_config.py" , "runserver:app"]