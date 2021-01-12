from pymongo import MongoClient

class MongoDB(object):
    """Class to connect to MongoDB"""
    def __init__(self):
        _client = MongoClient('localhost', 27017)
        self.db = _client['bankaya']
    
