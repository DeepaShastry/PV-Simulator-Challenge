from datetime import datetime
import random
import pika
from random import randint 
import logging
import consumer

"""
    This class 
    -Establishes new channel and creates new Queue 
    -Generates random meter values between 0 to 9000
"""

class Meter():
    def __init__(self,host,queue,logfile):
        self.host = host
        self.queue = queue
        self.logfile = logfile

    def generate_meter_values(self):
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=self.host)
        )
      
        logging.basicConfig(filename=self.logfile + '.log',filemode='w', encoding='utf-8',level=logging.INFO)
        logging.info("Establishing Channel")
        channel = connection.channel()
        channel.queue_declare(queue=self.queue)
        for i in range(0,1000):
            values = random.randint(0,9000)
            channel.basic_publish(exchange='', routing_key=self.queue, body=str(values))
            logging.info(f"[x] Sent {values}" )
    
        connection.close()


