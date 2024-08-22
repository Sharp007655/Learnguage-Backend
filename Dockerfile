FROM python

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_DEBUG=True

COPY . .

RUN apt-get update && apt-get install -y postgresql-client default-jdk
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80" ]

EXPOSE 80:80