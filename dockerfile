FROM python:3-alpine

#
RUN apk update

RUN mkdir -p /usr/www
WORKDIR /usr/www

#
COPY ./requirements.txt ./requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#
COPY . .

#
#CMD ["uvicorn", "app.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#RUN python3 app/app/main.py