import pymongo

from constants import CONNECTION_STRING, DATABASE_NAME

class MongoDBSingleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MongoDBSingleton.__instance is None:
            MongoDBSingleton()
        return MongoDBSingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MongoDBSingleton.__instance is not None:
            raise Exception("Singleton class exception!")
        else:
            MongoDBSingleton.__instance = self
            self.client = pymongo.MongoClient(CONNECTION_STRING)
            self.db = self.client[DATABASE_NAME]

    def insert(self, collection_name, record):
        """ Insert a record into the specified collection. """
        collection = self.db[collection_name]
        collection.insert_one(record)
    
    def insert_multiple(self, collection_name, records):
        """ Insert multiple records into the specified collection. """
        collection = self.db[collection_name]
        collection.insert_many(records)

    def delete(self, collection_name, query):
        """ Delete a record from the specified collection based on the query. """
        collection = self.db[collection_name]
        collection.delete_one(query)

    def update(self, collection_name, query, new_values):
        """ Update a record in the specified collection based on the query. """
        collection = self.db[collection_name]
        collection.update_one(query, {"$set": new_values})

    def fetchall(self, collection_name, query=None):
        """ View records from the specified collection based on the query. """
        collection = self.db[collection_name]
        if query:
            return collection.find(query)
        else:
            return collection.find()
        

    def close_connection(self):
        """ Close the MongoDB connection. """
        self.client.close()