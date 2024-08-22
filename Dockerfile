FROM python

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_DEBUG=True

COPY . .

RUN apt-get update && apt-get install -y postgresql-client
RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80" ]

EXPOSE 80:80
