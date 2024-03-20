#!/Users/navanath.navaskar/rabbitmqenv/bin/python3
# -*- coding=utf-8  


import pika
import threading
import functools
import json
import time


def ack_message(channel, delivery_tag):
    print(f'ack_message thread id: {threading.get_ident()}')
    if channel.is_open:
        channel.basic_ack(delivery_tag)
    else:
        pass


def do_work(channel, delivery_tag, body):
    print(f'do_work thread id: {threading.get_ident()}')
    data = json.loads(body.decode())
    time.sleep(5)
    cb = functools.partial(ack_message, channel, delivery_tag)
    channel.connection.add_callback_threadsafe(cb)


def on_message(channel, method_frame, header_frame, body):
    print(f'on_message thread id: {threading.get_ident()}')
    delivery_tag = method_frame.delivery_tag
    t = threading.Thread(target=do_work, args=(channel, delivery_tag, body))
    t.start()


if __name__ == '__main__':
    queue = "task_queue"
    connection = pika.BlockingConnection(pika.ConnectionParameters('****', "****" , '/', pika.PlainCredentials('lmy', '***'), heartbeat=0))
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue, on_message_callback=on_message)
    channel.start_consuming()