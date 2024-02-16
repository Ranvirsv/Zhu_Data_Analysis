import os
from pymongo import MongoClient
from configparser import ConfigParser

config = ConfigParser()
config.read('./config.ini')
DataBase = config['DataBase']
Pass = DataBase['PASS']
DB_Name = DataBase['DBNAME']
DB_Collection = DataBase['DBCOLLECTION']


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb+srv://ranvirsv:{password}@initialsimulations.trxmnax.mongodb.net/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client['AllJobsIT126']


def add_data(database):
    # TODO: write a function to get the data from Data folder and store it in a stucture
    pass


def convert_to_json(data):
    # TODO: Function to convert the data(Probably from Pandas Dataframe) to JSON format
    pass


def main():
    # TODO create a workflow to get all documents from Data and store in MongoDb
    pass


if __name__ == '__main__':
    main()
