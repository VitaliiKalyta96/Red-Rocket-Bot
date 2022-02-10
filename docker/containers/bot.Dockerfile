FROM python:3.9.7-buster

#RUN apt-get update && apt-get install -y gettext

WORKDIR /application
COPY ./requirements/bot.txt /application/bot.txt
#COPY ./wait-for-it.sh /app_bot/wait-for-it.sh
RUN chmod -R 0777 *
RUN pip install --upgrade pip
RUN pip install -r bot.txt

CMD docker/scripts/wait-for-it.sh db:3306 -- python3 src/bot/bot.py
