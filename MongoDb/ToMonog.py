from pymongo import MongoClient
from configparser import ConfigParser

config = ConfigParser()
password = config['PASSWORD']['PASS']


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb+srv://ranvirsv:{password}@initialsimulations.trxmnax.mongodb.net/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client['AllJobsIT126']


def add_data(database):
    pass


def main():
    # TODO create a workflow to get all documents from Data and store in MongoDb
    pass


if __name__ == '__main__':
    main()
