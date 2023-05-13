from .modules.db import DB
from celery import Celery


app = Celery('scraper', broker='amqps://gessyzwa:dmsvx0drMBCx3Dyg6BAcdCEwzirV81i6@rattlesnake.rmq.cloudamqp.com/gessyzwa',task_serializer='json')
