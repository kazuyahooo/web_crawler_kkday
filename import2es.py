from elasticsearch import Elasticsearch, helpers
import csv, json

# Create the elasticsearch client.
es = Elasticsearch(host = "localhost", port = 9200)

# Open csv file and bulk upload
with open('./data/output0315.json', encoding='utf-8') as f:
    reader = json.load(f)
    print(len(reader))
    helpers.bulk(es, reader, index='kkday')