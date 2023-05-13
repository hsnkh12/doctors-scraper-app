FROM python:3.9-alpine

WORKDIR /src

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /src

CMD ["celery","-A","src.celery","worker","--loglevel=info"]