# coding=utf-
import logging
import pika
from pymongo import MongoClient
import time

import datetime

from settings import REQUESTS_QUEUE, MONGO_COLLECTION, MONGO_DB


def callback(ch, method, properties, body):
    mongodb = MongoClient('mongodb', 27017)
    db = mongodb[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    collection.insert_one({
        'resource': repr(body),
        'datetime': datetime.datetime.utcnow()
    })

    logging.log(logging.DEBUG, " [x] Received %r" % body)
    mongodb.close()


if __name__ == '__main__':
    wait = True
    while wait:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters('rabbitmq'))
            wait = False
        except Exception as exc:
            time.sleep(1)
            logging.log(logging.ERROR, str(exc))
    channel = connection.channel()
    channel.queue_declare(queue=REQUESTS_QUEUE)
    channel.basic_consume(
        queue=REQUESTS_QUEUE,
        on_message_callback=callback,
        auto_ack=True)

    logging.log(logging.DEBUG,
                ' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
