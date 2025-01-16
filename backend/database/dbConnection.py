import pymongo


class MongoDBConnection:
    url = "mongodb+srv://prabhkaur:4Xcf7U3tYq1aR1Fh@cluster0.xymgg.mongodb.net/"
    dbName = "Kalavayhu"

    def __init__(self, uri: str = url, dbName: str = dbName):
        """Initializes the MongoDB connection."""
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[dbName]

    def get_database(self):
        """Returns the database instance."""
        return self.db
