FROM python:3.9

WORKDIR /home/

RUN git clone https://github.com/Jodayday/webtoon.git

WORKDIR /home/webtoon/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=settings.settings.prod


EXPOSE 8000

CMD ["bash","-c","python manage.py collectstatic --noinput && python manage.py migrate && gunicorn settings.wsgi --bind 0.0.0.0:8000"]
