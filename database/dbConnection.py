import pymongo


class MongoDBConnection:
    url="mongodb+srv://pinkal145:SJxoGnA5KPjebItw@cluster.nk3ok.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    dbName = "Kalavayhu"

    def __init__(self, uri: str = url, dbName: str = dbName):
        """Initializes the MongoDB connection."""
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[dbName]

    def get_database(self):
        """Returns the database instance."""
        return self.db


