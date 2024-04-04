# Kafka - Python
This repository contains a working example of the [Apache Kafka](https://kafka.apache.org/) message bus, that I created for our group project called '[Dverse](https://fuas-dverse.github.io/)' that we are making in our sixth semester at Fontys.


## Prerequisites
To run this project, there are a few things that need to be installed on your computer:
- Docker
- Python


## Set up
The first step to run this application is to clone / or download the repository to your local computer.


To clone via Git:
1. Navigate to the folder where the application will be cloned.
2. Open CMD (or any other console application) inside this folder.
3. Run command `git clone https://github.com/RenoMuijsenberg/Kafka-Python.git`
4. Run command `cd Kafka-Python` to navigate into the cloned folder.


> [!warning]
> From this point out make sure that Docker is running on your system!


After cloning the repository, we wanted to start the docker services via the docker compose file:
1. Run command: `docker-compose up -d` to start Zookeeper, Kafka and Kafka UI.
2. To verify, navigate to [http://localhost:8080/](http://localhost:8080/). This should open up the Kafka UI. Where will see that one cluster is online called `wizard_test`.


The Kafka service is now all set up and locally running on your system!


## Running Code
Once everything is set up, it is time to open the code of the project. Do this in the IDE that you are most familiar with, for myself this will be PyCharm. If the CMD from before is still open, I can run the command `pycharm .` to open up the folder inside PyCharm.

1. Create a virtual environment (.venv) inside the project. Either automatically by IDE or manually [create .venv](https://docs.python.org/3/library/venv.html).
2. Activate the .venv by running the command `.\.venv\Scripts\activate`
3. And install the packages by running `pip install -r \requirements.txt`

After having installed the packages, we first need to run the producers, as this script will start producing messages for a certain topic. After the producer is running, we can start the consumer to listen to this certain topic which will result in the messages being received by the consumer.
