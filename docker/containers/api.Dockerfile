FROM python:3.9.7-buster

RUN apt-get update && apt-get install -y gettext

WORKDIR /application

#ENV PYTHONPATH "${PYTHONPATH}:/red-rocket"

COPY ./requirements/api.txt /application/api.txt
COPY ./docker/scripts/wait-for-it.sh /application/wait-for-it.sh
RUN chmod -R 0777 *
RUN pip install -r api.txt

CMD ./docker/scripts/wait-for-it.sh db:3306 -- python3 ./src/api/app.py
