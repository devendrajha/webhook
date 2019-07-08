from pymongo import MongoClient


class Connection():

    def __init__(self):
        pass

    def open_connection(self):
        try:
            conn = MongoClient('localhost', 27017)
            #your database name
            db = conn.local
            return db
        except Exception as e:
            print('[ERROR]: ', e)
            return('[ERROR] - Error to connect in database.')

    def get_collection(self):
        db = self.open_connection()
        try:
            #your collection name
            return db.flexDB
        except Exception:
            return '[ERROR] - Error to get collection of database.'
