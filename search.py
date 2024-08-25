import json
from pprint import pprint
import os
import time

from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

class Search:
    def __init__(self):
        # self.es = Elasticsearch(cloud_id=os.environ['ELASTIC_CLOUD_ID'], api_key=os.environ['ELASTIC_API_KEY']) # Elastic Cloud
        self.es = Elasticsearch('http://localhost:9200') # Local Docker instance
        client_info = self.es.info()
        print('Connected to Elasticsearch!')
        pprint(client_info.body)

    def create_index(self):
        self.es.indices.delete(index='my_documents', ignore_unavailable=True)
        self.es.indices.create(index='my_documents')
    
    def insert_document(self, document):
        return self.es.index(index='my_documents', body=document)

    def insert_documents(self, documents):
        operations = []
        for document in documents:
            operations.append({'index': {'_index': 'my_documents'}})
            operations.append(document)
        return self.es.bulk(operations=operations)

    def reindex(self):
        self.create_index()
        with open('data.json', 'rt') as f:
            documents = json.loads(f.read())
        return self.insert_documents(documents)
