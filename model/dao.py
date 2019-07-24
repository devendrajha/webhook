import time
from . import Connection


class Dao():

    collection = None

    def __init__(self):
        conn = Connection()
        self.collection = conn.get_collection()

    def find_document(self, sku=None):
        if sku is None:
            try:
                return list(self.collection.find({}, {'_id': False}))
            except Exception as e:
                print('[ERROR]: Error to get all datas of database. \n', e)
                return None
        else:
            try:
                return list(self.collection.find({"data.sku": sku}, {'_id': False}))
            except Exception as e:
                print('[ERROR]: ', e)
                return None

    def insert_document(self, document):
            try:
                #document["create_date"]=int(time.time())
                self.collection.insert_one(document)
                return True
            except Exception as e:
                print('[ERROR]: Error to insert data in database. \n ', e)
                return False


    def delete_document(self, sku):
        print("sku",sku)
        try:
            self.collection.delete_many({"data.sku": sku})
            print('[INFO]: Record deleted successfully')
            return True
        except Exception as e:
            print('[ERROR]: Error to delete data of database. \n', e)
            return False
