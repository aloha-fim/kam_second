FROM python:3.10.4-buster



ENV PYTHONUNBUFFERED True

ENV APP_HOME /back-end
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 --timeout 0 app:app