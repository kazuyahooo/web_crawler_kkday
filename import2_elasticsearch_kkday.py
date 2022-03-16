from elasticsearch import Elasticsearch, helpers
import json

event_mapping = {
    "properties":{
       "booking_date":{
          "type":"date",
       },
       "cat_key":{
          "type":"text",
          "fields":{
             "keyword":{
                "type":"keyword",
                "ignore_above":256
             }
          }
       },
       "cities":{
          "type":"text",
          "fields":{
             "keyword":{
                "type":"keyword",
                "ignore_above":256
             }
          }
       },
       "country":{
          "type":"text",
          "fields":{
             "keyword":{
                "type":"keyword",
                "ignore_above":256
             }
          }
       },
       "introduction":{
          "type":"text",
          "fields":{
             "keyword":{
                "type":"keyword",
                "ignore_above":256
             }
          }
       },
       "link":{
          "type":"text",
       },
       "price":{
          "type":"long"
       },
       "rating_count":{
          "type":"long"
       },
       "rating_star":{
          "type":"float"
       },
       "title":{
          "type":"text",
          "fields":{
             "keyword":{
                "type":"keyword",
                "ignore_above":256
             }
          }
       }
    }
}

def read_data():
   with open('./data/output0315.json', encoding='utf-8') as f:
      row = json.load(f)
      for i in row:
         yield i


def load2_elasticsearch():
   # index_name = 'kkday_activities'
   index_name = 'kkday'
   #type = 'one_to_one'
   es = Elasticsearch()
     
   # Create Index
   if not es.indices.exists(index=index_name):
       es.indices.create(index=index_name)
   print('Index created!')

   # Put mapping into index
   if not es.indices.exists_type(index=index_name, doc_type='_doc'):
       es.indices.put_mapping(index=index_name, body=event_mapping, doc_type='_doc', include_type_name=True)
   print('Mappings created!')

   # Import data to elasticsearch
   helpers.bulk(es, read_data(), doc_type='_doc', index=index_name)
   print('success')

load2_elasticsearch()
