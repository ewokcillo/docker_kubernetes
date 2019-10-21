# coding=utf-
from faker import Faker
from flask import Flask, request
import pika

import json
from random import randint

from settings import IP_HOST, PORT_HOST, REQUESTS_QUEUE, ERRORS_QUEUE


app = Flask(__name__)


@app.route('/api/<resource>', methods=['GET'])
def get_resource(resource):
    fake = Faker()
    json_data = [
        {
            'name': fake.name(),
            'company': fake.company(),
            'email': fake.company_email(),
            'country': fake.country(),
            'credit_card_number': fake.credit_card_number()
        } for x in range(5, randint(6, 20))]

    connection = pika.BlockingConnection(
        pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue=REQUESTS_QUEUE)
    channel.basic_publish(exchange='',
                          routing_key=REQUESTS_QUEUE,
                          body=request.url)
    connection.close()

    return json.dumps(json_data)


if __name__ == '__main__':
    app.debug = True
    app.run(IP_HOST, PORT_HOST)
