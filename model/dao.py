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
                #document["_insertid"]=int(time.time())
                self.collection.insert_one(document)
                return True
            except Exception as e:
                print('[ERROR]: Error to insert data in database. \n ', e)
                return False


    def delete_document(self, sku):
        try:
            self.collection.delete_many({"data.sku": sku})
            print('[INFO]: All Record deleted successfully of sku',sku)
            return True
        except Exception as e:
            print('[ERROR]: Error to delete data of database. \n', e)
            return False
        
    def delete_document_cuid(self, cuid):
        try:
            self.collection.delete_many({"cuId": cuid})
            print('[INFO]: All Record deleted successfully of cuId',cuid)
            return True
        except Exception as e:
            print('[ERROR]: Error to delete data of database. \n', e)
            return False

    def delete_document_deviceid(self, deviceId):
        try:
            self.collection.delete_many({"data.deviceId": deviceId})
            print('[INFO]: All Record deleted successfully of deviceId',deviceId)
            return True
        except Exception as e:
            print('[ERROR]: Error to delete data of database. \n', e)
            return False
