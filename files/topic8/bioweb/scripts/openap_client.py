from __future__ import print_function
from pprint import pprint
import time
import swagger_client
from swagger_client.rest import ApiException

configuration = swagger_client.Configuration()
configuration.host = 'http://127.0.0.1:8080'
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

## pprint(dir(api_instance))
try:
    gene_list = api_instance.list_genes()
    pprint(gene_list)
except ApiException as e:
    print("Exception when calling DefaultApi->list_genes: %s\n" % e)

for gene in gene_list:
    print("Getting Gene ID:" + str(gene.id))
    try:
        api_response = api_instance.retrieve_gene(gene.id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->retrieve_gene: %s\n" % e)
