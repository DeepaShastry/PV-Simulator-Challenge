from datetime import datetime, timedelta
import logging
import os
import random
import pika
import pandas as pd
import csv
import time
import producer

"""
    This class consumes the meter values from the producer class
    and generates timestamp, simulated PV and sum of power values.
    It then writes the output to the csv file.
"""

class Simulator():

    # Initializing class attributes
    def __init__(self,host,queue,output_filename,logfile):
        self.host = host
        self.queue = queue
        self.output_filename = output_filename
        self.logfile = logfile

    
    """
        This method
        -Consumes messages from producer
        -Randomly generates simulated PV value in kW.
           Simulated PV Min = 0kW , Simulated PV Max = 9kW
        -Generates Timestamp 
        -Adds meter and PV values
    """
    def on_message_received(self,ch,method,properties,body):
        # Adding delay (0.05s) to generate different timestamp in the csv file
        time.sleep(0.05)
        meter_power_value = int(body.decode('utf-8'))
        timestamp = datetime.now()
        csvstr = datetime.strftime(timestamp, '%Y-%m-%d, %H:%M:%S')
        simulated_pv = random.randint(0,9000)/1000
        sum_of_powers = meter_power_value + simulated_pv
        record ={
         "Timestamp":csvstr,
         "Meter_Value": meter_power_value,
         "Simulated_PV":simulated_pv,
         "Sum_of_Powers":sum_of_powers
        }
        self.write_to_csv(record)

    # This method writes the results to the .csv file

    def write_to_csv(self,record):
        logging.info("Writing to csv")
        filename = self.output_filename + '.csv'
        file_exists = os.path.isfile(filename)
        with open(filename,'a',newline='') as f:
        # create the csv writer
            writer = csv.DictWriter(f,fieldnames=record.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(record)

    # This method establishes channel and consumes the values from the Producer Queue

    def connect(self):
        try:
            connection_parameters = pika.ConnectionParameters(self.host)
            connection = pika.BlockingConnection(connection_parameters)
            channel = connection.channel()
            channel.queue_declare(queue=self.queue)
            channel.basic_consume(queue=self.queue,auto_ack=True,on_message_callback=self.on_message_received)
            print("Started consuming")
            logging.basicConfig(filename=self.logfile + '.log',filemode='a', encoding='utf-8',level=logging.INFO)
            logging.info("Started Consuming")
            channel.start_consuming()
        except KeyboardInterrupt as ex:
                channel.stop_consuming()
                connection.close()
                logging.info("Operation stoped by user. Connection closed")
        
        except pika.exceptions.ConnectionClosedByBroker as err:
            logging.error("Connection closed by borker exception")
        except pika.exceptions.AMQPConnectionError as err:
            logging.error("Connection Unsuccessful")