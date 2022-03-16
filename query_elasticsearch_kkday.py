from elasticsearch import Elasticsearch
import json

def kkday_query(match, field, query):
    es = Elasticsearch()

    index_name = 'kkday'

    # Query DSL
    search_params = {
        "query": {
            match : {field: query}
        },
        "size": 5
    }
    #Search document
    result = es.search(index=index_name, doc_type='_doc', body=search_params)
    result = result['hits']['hits']
    result = json.dumps(result, indent=2, ensure_ascii = False)
    print(result)
    
comparison = {1:'title',2:'introduction',3:'country',4:'cities',5:'price',6:'rating_count',7:'rating_star',8:'cat_key',9:'booking_date',10:'link'}
allornot = {1:'match', 2:'match_phrase'}
while True:
    try:
        field = int(input('(1 Title, 2 Introduction, 3 Country, 4 Cities, 5 Price, 6 Rating Count, 7 Rating Star, 8 Category,  9 Booking date, 10 Link, 11 Exit Loop)\nPlease enter the number to pick field: '))
        if field == 11: break
        if field <= 0 or field >=12: raise Exception
        match = int(input('Choose query method (1 Match Word, 2 Match Phrase): '))
        if match != 1 and match != 2: raise Exception
        query = input('Please Enter a keyword: ')
        kkday_query(allornot[match], comparison[field], query)
        print('Query is done!')
    except:
        print('Please pick a valid number!!!')
        continue
    
