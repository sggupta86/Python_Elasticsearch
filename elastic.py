import json
from elasticsearch import Elasticsearch
es_host="https://ekta-demo.es.us-central1.gcp.cloud.es.io:9243"
es_user="elastic"
es_password="eWEs05nQlvlF91hRpVMiDF5u"
my_instance= Elasticsearch(es_host,http_auth=(es_user,es_password),use_ssl=True, verify_certs=False)

if not my_instance:
    print("connection not")
else:
    print("connection done")    

def search_es(es_query):
    response = my_instance.search(index="app_wallet_01", body=es_query)
    return response

es_query={
    "query":{
        "match_all":{}
    }
}

es_result = search_es(es_query)
print(str(es_result))
print(json.dumps(es_result, indent=2))


 