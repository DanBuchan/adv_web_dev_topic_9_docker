# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gene**](DefaultApi.md#create_gene) | **POST** /api/gene/{id}/ | 
[**destroy_gene**](DefaultApi.md#destroy_gene) | **DELETE** /api/gene/{id}/ | 
[**list_genes**](DefaultApi.md#list_genes) | **GET** /api/genes | 
[**retrieve_gene**](DefaultApi.md#retrieve_gene) | **GET** /api/gene/{id}/ | 
[**update_gene**](DefaultApi.md#update_gene) | **PUT** /api/gene/{id}/ | 

# **create_gene**
> InlineResponse200 create_gene(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | A unique integer value identifying this gene.
body = swagger_client.Body1() # Body1 |  (optional)

try:
    api_response = api_instance.create_gene(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_gene: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this gene. | 
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_gene**
> destroy_gene(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | A unique integer value identifying this gene.

try:
    api_instance.destroy_gene(id)
except ApiException as e:
    print("Exception when calling DefaultApi->destroy_gene: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this gene. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_genes**
> list[InlineResponse2001] list_genes()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.list_genes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_genes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_gene**
> InlineResponse200 retrieve_gene(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | A unique integer value identifying this gene.

try:
    api_response = api_instance.retrieve_gene(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_gene: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this gene. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gene**
> InlineResponse200 update_gene(id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | A unique integer value identifying this gene.
body = swagger_client.Body() # Body |  (optional)

try:
    api_response = api_instance.update_gene(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_gene: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique integer value identifying this gene. | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

