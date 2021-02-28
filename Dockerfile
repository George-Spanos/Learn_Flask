FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY . /app
CMD [ "python","app.py" ]