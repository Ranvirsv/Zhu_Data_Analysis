import os
import re
from pymongo import MongoClient
from configparser import ConfigParser

config = ConfigParser()
config.read("./config.ini")
DataBase = config["DataBase"]
Pass = DataBase["PASS"]
DB_Name = DataBase["DBNAME"]
DB_Collection = DataBase["DBCOLLECTION"]
Data_dir = "../Data"


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = (
        f"mongodb+srv://ranvirsv:{password}@initialsimulations.trxmnax.mongodb.net/"
    )
    # Create a connection using MongoClient.
    client = MongoClient(CONNECTION_STRING)
    return client[DB_Name]


def add_data(database):
    collection = database[DB_Collection]
    for job_folder in os.listdir(Data_dir):
        job_path = os.path.join(Data_dir, job_folder)
        if os.path.isdir(job_path):
            job_data = {"job_id": job_folder, "files": []}
        for file_name in os.listdir(job_path):
            if re.match(r"^(job|Beerling)", file_name):
                continue
            file_path = os.path.join(job_path, file_name)
            with open(file_path, "r") as file:
                content = file.read()
                job_data["files"].append(
                    {"file": file_name, "content": content})
        collection.insert_one(job_data)


def main():
    db = get_database()
    add_data(db)
    print("Data Import Complete.")


if __name__ == "__main__":
    main()
