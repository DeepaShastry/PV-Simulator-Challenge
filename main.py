import configparser
import producer
import consumer
import logging

"""
This is the entry point of the program
 -It reads values from the Config.txt file
 -Creates intances of Meter and Simulator class
"""

def main():
    parser = configparser.ConfigParser()
    parser.read("Config.txt")
    host = parser.get("Config","host")
    queue = parser.get("Config","queue")
    output_filename = parser.get("Config","output_filename")
    log_filename = parser.get("Config","log_filename")
    meter = producer.Meter(host,queue,log_filename)
    meter.generate_meter_values()
    simulator = consumer.Simulator(host,queue,output_filename,log_filename)
    simulator.connect()

if __name__ == "__main__":
    main()