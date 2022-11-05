FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN ln -snf /usr/share/zoneinfo/"Asia/Tehran" /etc/localtime && echo "Asia/Tehran" > /etc/timezone
WORKDIR /reminder
COPY requirements.txt /reminder
RUN pip install -r requirements.txt
COPY . /reminder

CMD celery -A reminder  beat -l info  &  celery -A reminder worker -l info & python /reminder/manage.py migrate && python /reminder/manage.py runserver 0.0.0.0:8000
