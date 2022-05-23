# PV-Simulator-Challenge

Pre-requisites
1. Install RabbitMQ
   Guide for installation
   Windows - https://www.rabbitmq.com/download.html
   Debian and Ubuntu - https://www.rabbitmq.com/install-debian.html#installation-methods

2. This program uses python pika libraries, to install pika run the below command
   Windows - pip install pika
   Ubuntu  - sudo apt-get install -y python-pika

3. Python version used - 3.10.3
4. RabbitMQ server version used - 3.10.1


Setps to Run the program
1. Start the RabitMQ server
Windows 
 - Navigate to sbin folder in RabbitMQ server installation path and run the batch file "rabbitmq-server.bat"
   For e.g : ...\rabbitmq-server-windows-3.10.1\rabbitmq_server-3.10.1\sbin>rabbitmq-server.bat
 - Broker server starts once this message appears -  "Starting broker... completed with 3 plugins"
 - Once the broker server has started , open the browser and type "http://localhost:15672/" in the search bar.
 - On the RabbitMQ login webpage enter the following default credentials
   Username - guest
   Password - guest

2. If the host name and RabbitMQ queue name needs to modified then modify "host" and "queue" values in Config.txt file before running the program

3. Run main.py from the windows or Ubuntu terminal
 e.g python main.py

3. The logs can be viewed in the same directory with the file name being "pvsimulator.log"
4. The resuls are generated in "pvsimulator.csv"

Note:
This program takes ~1 mins to run as the producer generates 1000 random meter values and these values are witten to the .csv file with a time interval of 0.05s. This delay of 0.05s has been introduced just to mock values at different timestamp.
The delay can be removed in the real time scenarios where the meter provides household electricity consumption values continously throughout the day.
