from pymongo import MongoClient
from pymongo import ReadPreference
from datetime import datetime, timedelta


class Mongo(MongoClient):
    def __init__(self, username, password, host, db='tags', collection='tweets_pipeline_v2'):

        uri = f"mongodb://{username}:{password}@{host}/{db}"
        super(Mongo, self).__init__(host=uri,
                                    authSource=db,
                                    authMechanism='SCRAM-SHA-256',
                                    port=27017,
                                    replicaset="rs0",
                                    read_preference=ReadPreference.SECONDARY,
                                    )
        self.database = self.get_default_database()
        self.collection = collection

    def pipelined(self, count=True):
        query = {"status": "pipelined"}
        if count:
            return self.database[self.collection].count_documents(query)
        return self.database[self.collection].find(query)

    def feed(self, count=True):
        query = {"status": "graphicone_feed"}
        if count:
            return self.database[self.collection].count_documents(query)
        return self.database[self.collection].find(query)

    def search(self, count=True):
        query = {"status": "graphicone_search"}
        if count:
            return self.database[self.collection].count_documents(query)
        return self.database[self.collection].find(query)

    def left_for_analysts(self, count=True):
        query = {"in_app": {"$exists": False},
                 "status":  "graphicone_feed"}
        if count:
            return self.database[self.collection].count_documents(query)
        return self.database[self.collection].find(query)

    def removed_validators(self, count=True):
        query = {"validator_username": {"$exists": True},
                             "status": "deleted"}
        if count:
            return self.database[self.collection].count_documents(query)
        return self.database[self.collection].find(query)

    def removed_analysts(self, count=True):
        query = {"status": "deleted_from_analytics"}
        if count:
            return self.database[self.collection].count_documents(query)
        return self.database[self.collection].find(query)



# if __name__ == "__main__":
#     _username = "login"
#     _password = "passwd"
#     mongodb_host = "host address"
#
#     mongo_client = Mongo(_username, _password, mongodb_host)
#     print(mongo_client.pipelined())
#     print(mongo_client.search())
#     print(mongo_client.feed())
#     print(mongo_client.left_for_analysts())
#     print(mongo_client.removed_validators())
#     print(mongo_client.removed_analysts())



