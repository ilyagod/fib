#!/usr/bin/env python
import os
import sys

import mq


number = sys.argv[1]
channel = mq.get_channel()

channel.basic_publish(exchange='', routing_key=os.getenv('RABBITMQ_QUEUE'), body=number)
