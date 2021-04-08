from config import config
from elasticsearch import Elasticsearch

class ElasticSearchUtility:
    def __init__(self):
        pass
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def post_documents(self, data):
        self.es.index(index="ruchis_tweeter_data",body=data)