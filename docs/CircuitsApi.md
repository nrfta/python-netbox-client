# netbox_client.CircuitsApi

All URIs are relative to *https://netbox.us-east-2.ops.underline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**circuits_circuit_terminations_create**](CircuitsApi.md#circuits_circuit_terminations_create) | **POST** /circuits/circuit-terminations/ | 
[**circuits_circuit_terminations_delete**](CircuitsApi.md#circuits_circuit_terminations_delete) | **DELETE** /circuits/circuit-terminations/{id}/ | 
[**circuits_circuit_terminations_list**](CircuitsApi.md#circuits_circuit_terminations_list) | **GET** /circuits/circuit-terminations/ | 
[**circuits_circuit_terminations_partial_update**](CircuitsApi.md#circuits_circuit_terminations_partial_update) | **PATCH** /circuits/circuit-terminations/{id}/ | 
[**circuits_circuit_terminations_read**](CircuitsApi.md#circuits_circuit_terminations_read) | **GET** /circuits/circuit-terminations/{id}/ | 
[**circuits_circuit_terminations_update**](CircuitsApi.md#circuits_circuit_terminations_update) | **PUT** /circuits/circuit-terminations/{id}/ | 
[**circuits_circuit_types_create**](CircuitsApi.md#circuits_circuit_types_create) | **POST** /circuits/circuit-types/ | 
[**circuits_circuit_types_delete**](CircuitsApi.md#circuits_circuit_types_delete) | **DELETE** /circuits/circuit-types/{id}/ | 
[**circuits_circuit_types_list**](CircuitsApi.md#circuits_circuit_types_list) | **GET** /circuits/circuit-types/ | 
[**circuits_circuit_types_partial_update**](CircuitsApi.md#circuits_circuit_types_partial_update) | **PATCH** /circuits/circuit-types/{id}/ | 
[**circuits_circuit_types_read**](CircuitsApi.md#circuits_circuit_types_read) | **GET** /circuits/circuit-types/{id}/ | 
[**circuits_circuit_types_update**](CircuitsApi.md#circuits_circuit_types_update) | **PUT** /circuits/circuit-types/{id}/ | 
[**circuits_circuits_create**](CircuitsApi.md#circuits_circuits_create) | **POST** /circuits/circuits/ | 
[**circuits_circuits_delete**](CircuitsApi.md#circuits_circuits_delete) | **DELETE** /circuits/circuits/{id}/ | 
[**circuits_circuits_list**](CircuitsApi.md#circuits_circuits_list) | **GET** /circuits/circuits/ | 
[**circuits_circuits_partial_update**](CircuitsApi.md#circuits_circuits_partial_update) | **PATCH** /circuits/circuits/{id}/ | 
[**circuits_circuits_read**](CircuitsApi.md#circuits_circuits_read) | **GET** /circuits/circuits/{id}/ | 
[**circuits_circuits_update**](CircuitsApi.md#circuits_circuits_update) | **PUT** /circuits/circuits/{id}/ | 
[**circuits_providers_create**](CircuitsApi.md#circuits_providers_create) | **POST** /circuits/providers/ | 
[**circuits_providers_delete**](CircuitsApi.md#circuits_providers_delete) | **DELETE** /circuits/providers/{id}/ | 
[**circuits_providers_graphs**](CircuitsApi.md#circuits_providers_graphs) | **GET** /circuits/providers/{id}/graphs/ | 
[**circuits_providers_list**](CircuitsApi.md#circuits_providers_list) | **GET** /circuits/providers/ | 
[**circuits_providers_partial_update**](CircuitsApi.md#circuits_providers_partial_update) | **PATCH** /circuits/providers/{id}/ | 
[**circuits_providers_read**](CircuitsApi.md#circuits_providers_read) | **GET** /circuits/providers/{id}/ | 
[**circuits_providers_update**](CircuitsApi.md#circuits_providers_update) | **PUT** /circuits/providers/{id}/ | 


# **circuits_circuit_terminations_create**
> CircuitTermination circuits_circuit_terminations_create(data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableCircuitTermination() # WritableCircuitTermination | 

try:
    api_response = api_instance.circuits_circuit_terminations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_delete**
> circuits_circuit_terminations_delete(id)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit termination.

try:
    api_instance.circuits_circuit_terminations_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_list**
> InlineResponse200 circuits_circuit_terminations_list(term_side=term_side, port_speed=port_speed, upstream_speed=upstream_speed, xconnect_id=xconnect_id, q=q, circuit_id=circuit_id, site_id=site_id, site=site, term_side__n=term_side__n, port_speed__n=port_speed__n, port_speed__lte=port_speed__lte, port_speed__lt=port_speed__lt, port_speed__gte=port_speed__gte, port_speed__gt=port_speed__gt, upstream_speed__n=upstream_speed__n, upstream_speed__lte=upstream_speed__lte, upstream_speed__lt=upstream_speed__lt, upstream_speed__gte=upstream_speed__gte, upstream_speed__gt=upstream_speed__gt, xconnect_id__n=xconnect_id__n, xconnect_id__ic=xconnect_id__ic, xconnect_id__nic=xconnect_id__nic, xconnect_id__iew=xconnect_id__iew, xconnect_id__niew=xconnect_id__niew, xconnect_id__isw=xconnect_id__isw, xconnect_id__nisw=xconnect_id__nisw, xconnect_id__ie=xconnect_id__ie, xconnect_id__nie=xconnect_id__nie, circuit_id__n=circuit_id__n, site_id__n=site_id__n, site__n=site__n, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
term_side = 'term_side_example' # str |  (optional)
port_speed = 'port_speed_example' # str |  (optional)
upstream_speed = 'upstream_speed_example' # str |  (optional)
xconnect_id = 'xconnect_id_example' # str |  (optional)
q = 'q_example' # str |  (optional)
circuit_id = 'circuit_id_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
term_side__n = 'term_side__n_example' # str |  (optional)
port_speed__n = 'port_speed__n_example' # str |  (optional)
port_speed__lte = 'port_speed__lte_example' # str |  (optional)
port_speed__lt = 'port_speed__lt_example' # str |  (optional)
port_speed__gte = 'port_speed__gte_example' # str |  (optional)
port_speed__gt = 'port_speed__gt_example' # str |  (optional)
upstream_speed__n = 'upstream_speed__n_example' # str |  (optional)
upstream_speed__lte = 'upstream_speed__lte_example' # str |  (optional)
upstream_speed__lt = 'upstream_speed__lt_example' # str |  (optional)
upstream_speed__gte = 'upstream_speed__gte_example' # str |  (optional)
upstream_speed__gt = 'upstream_speed__gt_example' # str |  (optional)
xconnect_id__n = 'xconnect_id__n_example' # str |  (optional)
xconnect_id__ic = 'xconnect_id__ic_example' # str |  (optional)
xconnect_id__nic = 'xconnect_id__nic_example' # str |  (optional)
xconnect_id__iew = 'xconnect_id__iew_example' # str |  (optional)
xconnect_id__niew = 'xconnect_id__niew_example' # str |  (optional)
xconnect_id__isw = 'xconnect_id__isw_example' # str |  (optional)
xconnect_id__nisw = 'xconnect_id__nisw_example' # str |  (optional)
xconnect_id__ie = 'xconnect_id__ie_example' # str |  (optional)
xconnect_id__nie = 'xconnect_id__nie_example' # str |  (optional)
circuit_id__n = 'circuit_id__n_example' # str |  (optional)
site_id__n = 'site_id__n_example' # str |  (optional)
site__n = 'site__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.circuits_circuit_terminations_list(term_side=term_side, port_speed=port_speed, upstream_speed=upstream_speed, xconnect_id=xconnect_id, q=q, circuit_id=circuit_id, site_id=site_id, site=site, term_side__n=term_side__n, port_speed__n=port_speed__n, port_speed__lte=port_speed__lte, port_speed__lt=port_speed__lt, port_speed__gte=port_speed__gte, port_speed__gt=port_speed__gt, upstream_speed__n=upstream_speed__n, upstream_speed__lte=upstream_speed__lte, upstream_speed__lt=upstream_speed__lt, upstream_speed__gte=upstream_speed__gte, upstream_speed__gt=upstream_speed__gt, xconnect_id__n=xconnect_id__n, xconnect_id__ic=xconnect_id__ic, xconnect_id__nic=xconnect_id__nic, xconnect_id__iew=xconnect_id__iew, xconnect_id__niew=xconnect_id__niew, xconnect_id__isw=xconnect_id__isw, xconnect_id__nisw=xconnect_id__nisw, xconnect_id__ie=xconnect_id__ie, xconnect_id__nie=xconnect_id__nie, circuit_id__n=circuit_id__n, site_id__n=site_id__n, site__n=site__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_side** | **str**|  | [optional] 
 **port_speed** | **str**|  | [optional] 
 **upstream_speed** | **str**|  | [optional] 
 **xconnect_id** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **circuit_id** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **term_side__n** | **str**|  | [optional] 
 **port_speed__n** | **str**|  | [optional] 
 **port_speed__lte** | **str**|  | [optional] 
 **port_speed__lt** | **str**|  | [optional] 
 **port_speed__gte** | **str**|  | [optional] 
 **port_speed__gt** | **str**|  | [optional] 
 **upstream_speed__n** | **str**|  | [optional] 
 **upstream_speed__lte** | **str**|  | [optional] 
 **upstream_speed__lt** | **str**|  | [optional] 
 **upstream_speed__gte** | **str**|  | [optional] 
 **upstream_speed__gt** | **str**|  | [optional] 
 **xconnect_id__n** | **str**|  | [optional] 
 **xconnect_id__ic** | **str**|  | [optional] 
 **xconnect_id__nic** | **str**|  | [optional] 
 **xconnect_id__iew** | **str**|  | [optional] 
 **xconnect_id__niew** | **str**|  | [optional] 
 **xconnect_id__isw** | **str**|  | [optional] 
 **xconnect_id__nisw** | **str**|  | [optional] 
 **xconnect_id__ie** | **str**|  | [optional] 
 **xconnect_id__nie** | **str**|  | [optional] 
 **circuit_id__n** | **str**|  | [optional] 
 **site_id__n** | **str**|  | [optional] 
 **site__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_partial_update**
> CircuitTermination circuits_circuit_terminations_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit termination.
data = netbox_client.WritableCircuitTermination() # WritableCircuitTermination | 

try:
    api_response = api_instance.circuits_circuit_terminations_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 
 **data** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_read**
> CircuitTermination circuits_circuit_terminations_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit termination.

try:
    api_response = api_instance.circuits_circuit_terminations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_update**
> CircuitTermination circuits_circuit_terminations_update(id, data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit termination.
data = netbox_client.WritableCircuitTermination() # WritableCircuitTermination | 

try:
    api_response = api_instance.circuits_circuit_terminations_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 
 **data** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_create**
> CircuitType circuits_circuit_types_create(data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
data = netbox_client.CircuitType() # CircuitType | 

try:
    api_response = api_instance.circuits_circuit_types_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CircuitType**](CircuitType.md)|  | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_delete**
> circuits_circuit_types_delete(id)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit type.

try:
    api_instance.circuits_circuit_types_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_list**
> InlineResponse2001 circuits_circuit_types_list(id=id, name=name, slug=slug, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
q = 'q_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
name__n = 'name__n_example' # str |  (optional)
name__ic = 'name__ic_example' # str |  (optional)
name__nic = 'name__nic_example' # str |  (optional)
name__iew = 'name__iew_example' # str |  (optional)
name__niew = 'name__niew_example' # str |  (optional)
name__isw = 'name__isw_example' # str |  (optional)
name__nisw = 'name__nisw_example' # str |  (optional)
name__ie = 'name__ie_example' # str |  (optional)
name__nie = 'name__nie_example' # str |  (optional)
slug__n = 'slug__n_example' # str |  (optional)
slug__ic = 'slug__ic_example' # str |  (optional)
slug__nic = 'slug__nic_example' # str |  (optional)
slug__iew = 'slug__iew_example' # str |  (optional)
slug__niew = 'slug__niew_example' # str |  (optional)
slug__isw = 'slug__isw_example' # str |  (optional)
slug__nisw = 'slug__nisw_example' # str |  (optional)
slug__ie = 'slug__ie_example' # str |  (optional)
slug__nie = 'slug__nie_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.circuits_circuit_types_list(id=id, name=name, slug=slug, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **name__n** | **str**|  | [optional] 
 **name__ic** | **str**|  | [optional] 
 **name__nic** | **str**|  | [optional] 
 **name__iew** | **str**|  | [optional] 
 **name__niew** | **str**|  | [optional] 
 **name__isw** | **str**|  | [optional] 
 **name__nisw** | **str**|  | [optional] 
 **name__ie** | **str**|  | [optional] 
 **name__nie** | **str**|  | [optional] 
 **slug__n** | **str**|  | [optional] 
 **slug__ic** | **str**|  | [optional] 
 **slug__nic** | **str**|  | [optional] 
 **slug__iew** | **str**|  | [optional] 
 **slug__niew** | **str**|  | [optional] 
 **slug__isw** | **str**|  | [optional] 
 **slug__nisw** | **str**|  | [optional] 
 **slug__ie** | **str**|  | [optional] 
 **slug__nie** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_partial_update**
> CircuitType circuits_circuit_types_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit type.
data = netbox_client.CircuitType() # CircuitType | 

try:
    api_response = api_instance.circuits_circuit_types_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 
 **data** | [**CircuitType**](CircuitType.md)|  | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_read**
> CircuitType circuits_circuit_types_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit type.

try:
    api_response = api_instance.circuits_circuit_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_update**
> CircuitType circuits_circuit_types_update(id, data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit type.
data = netbox_client.CircuitType() # CircuitType | 

try:
    api_response = api_instance.circuits_circuit_types_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 
 **data** | [**CircuitType**](CircuitType.md)|  | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_create**
> Circuit circuits_circuits_create(data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableCircuit() # WritableCircuit | 

try:
    api_response = api_instance.circuits_circuits_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableCircuit**](WritableCircuit.md)|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_delete**
> circuits_circuits_delete(id)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit.

try:
    api_instance.circuits_circuits_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_list**
> InlineResponse2002 circuits_circuits_list(id=id, cid=cid, install_date=install_date, commit_rate=commit_rate, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, provider_id=provider_id, provider=provider, type_id=type_id, type=type, status=status, site_id=site_id, site=site, region_id=region_id, region=region, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, cid__n=cid__n, cid__ic=cid__ic, cid__nic=cid__nic, cid__iew=cid__iew, cid__niew=cid__niew, cid__isw=cid__isw, cid__nisw=cid__nisw, cid__ie=cid__ie, cid__nie=cid__nie, install_date__n=install_date__n, install_date__lte=install_date__lte, install_date__lt=install_date__lt, install_date__gte=install_date__gte, install_date__gt=install_date__gt, commit_rate__n=commit_rate__n, commit_rate__lte=commit_rate__lte, commit_rate__lt=commit_rate__lt, commit_rate__gte=commit_rate__gte, commit_rate__gt=commit_rate__gt, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, provider_id__n=provider_id__n, provider__n=provider__n, type_id__n=type_id__n, type__n=type__n, status__n=status__n, site_id__n=site_id__n, site__n=site__n, region_id__n=region_id__n, region__n=region__n, tag__n=tag__n, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
cid = 'cid_example' # str |  (optional)
install_date = 'install_date_example' # str |  (optional)
commit_rate = 'commit_rate_example' # str |  (optional)
tenant_group_id = 'tenant_group_id_example' # str |  (optional)
tenant_group = 'tenant_group_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
created = 'created_example' # str |  (optional)
created__gte = 'created__gte_example' # str |  (optional)
created__lte = 'created__lte_example' # str |  (optional)
last_updated = 'last_updated_example' # str |  (optional)
last_updated__gte = 'last_updated__gte_example' # str |  (optional)
last_updated__lte = 'last_updated__lte_example' # str |  (optional)
q = 'q_example' # str |  (optional)
provider_id = 'provider_id_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
type = 'type_example' # str |  (optional)
status = 'status_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
cid__n = 'cid__n_example' # str |  (optional)
cid__ic = 'cid__ic_example' # str |  (optional)
cid__nic = 'cid__nic_example' # str |  (optional)
cid__iew = 'cid__iew_example' # str |  (optional)
cid__niew = 'cid__niew_example' # str |  (optional)
cid__isw = 'cid__isw_example' # str |  (optional)
cid__nisw = 'cid__nisw_example' # str |  (optional)
cid__ie = 'cid__ie_example' # str |  (optional)
cid__nie = 'cid__nie_example' # str |  (optional)
install_date__n = 'install_date__n_example' # str |  (optional)
install_date__lte = 'install_date__lte_example' # str |  (optional)
install_date__lt = 'install_date__lt_example' # str |  (optional)
install_date__gte = 'install_date__gte_example' # str |  (optional)
install_date__gt = 'install_date__gt_example' # str |  (optional)
commit_rate__n = 'commit_rate__n_example' # str |  (optional)
commit_rate__lte = 'commit_rate__lte_example' # str |  (optional)
commit_rate__lt = 'commit_rate__lt_example' # str |  (optional)
commit_rate__gte = 'commit_rate__gte_example' # str |  (optional)
commit_rate__gt = 'commit_rate__gt_example' # str |  (optional)
tenant_group_id__n = 'tenant_group_id__n_example' # str |  (optional)
tenant_group__n = 'tenant_group__n_example' # str |  (optional)
tenant_id__n = 'tenant_id__n_example' # str |  (optional)
tenant__n = 'tenant__n_example' # str |  (optional)
provider_id__n = 'provider_id__n_example' # str |  (optional)
provider__n = 'provider__n_example' # str |  (optional)
type_id__n = 'type_id__n_example' # str |  (optional)
type__n = 'type__n_example' # str |  (optional)
status__n = 'status__n_example' # str |  (optional)
site_id__n = 'site_id__n_example' # str |  (optional)
site__n = 'site__n_example' # str |  (optional)
region_id__n = 'region_id__n_example' # str |  (optional)
region__n = 'region__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.circuits_circuits_list(id=id, cid=cid, install_date=install_date, commit_rate=commit_rate, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, provider_id=provider_id, provider=provider, type_id=type_id, type=type, status=status, site_id=site_id, site=site, region_id=region_id, region=region, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, cid__n=cid__n, cid__ic=cid__ic, cid__nic=cid__nic, cid__iew=cid__iew, cid__niew=cid__niew, cid__isw=cid__isw, cid__nisw=cid__nisw, cid__ie=cid__ie, cid__nie=cid__nie, install_date__n=install_date__n, install_date__lte=install_date__lte, install_date__lt=install_date__lt, install_date__gte=install_date__gte, install_date__gt=install_date__gt, commit_rate__n=commit_rate__n, commit_rate__lte=commit_rate__lte, commit_rate__lt=commit_rate__lt, commit_rate__gte=commit_rate__gte, commit_rate__gt=commit_rate__gt, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, provider_id__n=provider_id__n, provider__n=provider__n, type_id__n=type_id__n, type__n=type__n, status__n=status__n, site_id__n=site_id__n, site__n=site__n, region_id__n=region_id__n, region__n=region__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **cid** | **str**|  | [optional] 
 **install_date** | **str**|  | [optional] 
 **commit_rate** | **str**|  | [optional] 
 **tenant_group_id** | **str**|  | [optional] 
 **tenant_group** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **created__gte** | **str**|  | [optional] 
 **created__lte** | **str**|  | [optional] 
 **last_updated** | **str**|  | [optional] 
 **last_updated__gte** | **str**|  | [optional] 
 **last_updated__lte** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **provider_id** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **cid__n** | **str**|  | [optional] 
 **cid__ic** | **str**|  | [optional] 
 **cid__nic** | **str**|  | [optional] 
 **cid__iew** | **str**|  | [optional] 
 **cid__niew** | **str**|  | [optional] 
 **cid__isw** | **str**|  | [optional] 
 **cid__nisw** | **str**|  | [optional] 
 **cid__ie** | **str**|  | [optional] 
 **cid__nie** | **str**|  | [optional] 
 **install_date__n** | **str**|  | [optional] 
 **install_date__lte** | **str**|  | [optional] 
 **install_date__lt** | **str**|  | [optional] 
 **install_date__gte** | **str**|  | [optional] 
 **install_date__gt** | **str**|  | [optional] 
 **commit_rate__n** | **str**|  | [optional] 
 **commit_rate__lte** | **str**|  | [optional] 
 **commit_rate__lt** | **str**|  | [optional] 
 **commit_rate__gte** | **str**|  | [optional] 
 **commit_rate__gt** | **str**|  | [optional] 
 **tenant_group_id__n** | **str**|  | [optional] 
 **tenant_group__n** | **str**|  | [optional] 
 **tenant_id__n** | **str**|  | [optional] 
 **tenant__n** | **str**|  | [optional] 
 **provider_id__n** | **str**|  | [optional] 
 **provider__n** | **str**|  | [optional] 
 **type_id__n** | **str**|  | [optional] 
 **type__n** | **str**|  | [optional] 
 **status__n** | **str**|  | [optional] 
 **site_id__n** | **str**|  | [optional] 
 **site__n** | **str**|  | [optional] 
 **region_id__n** | **str**|  | [optional] 
 **region__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_partial_update**
> Circuit circuits_circuits_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit.
data = netbox_client.WritableCircuit() # WritableCircuit | 

try:
    api_response = api_instance.circuits_circuits_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 
 **data** | [**WritableCircuit**](WritableCircuit.md)|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_read**
> Circuit circuits_circuits_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit.

try:
    api_response = api_instance.circuits_circuits_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_update**
> Circuit circuits_circuits_update(id, data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit.
data = netbox_client.WritableCircuit() # WritableCircuit | 

try:
    api_response = api_instance.circuits_circuits_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 
 **data** | [**WritableCircuit**](WritableCircuit.md)|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_create**
> Provider circuits_providers_create(data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
data = netbox_client.Provider() # Provider | 

try:
    api_response = api_instance.circuits_providers_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Provider**](Provider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_delete**
> circuits_providers_delete(id)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.

try:
    api_instance.circuits_providers_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_graphs**
> Provider circuits_providers_graphs(id)



A convenience method for rendering graphs for a particular provider.

### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.

try:
    api_response = api_instance.circuits_providers_graphs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_list**
> InlineResponse2003 circuits_providers_list(id=id, name=name, slug=slug, asn=asn, account=account, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, region_id=region_id, region=region, site_id=site_id, site=site, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, asn__n=asn__n, asn__lte=asn__lte, asn__lt=asn__lt, asn__gte=asn__gte, asn__gt=asn__gt, account__n=account__n, account__ic=account__ic, account__nic=account__nic, account__iew=account__iew, account__niew=account__niew, account__isw=account__isw, account__nisw=account__nisw, account__ie=account__ie, account__nie=account__nie, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, tag__n=tag__n, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
asn = 'asn_example' # str |  (optional)
account = 'account_example' # str |  (optional)
created = 'created_example' # str |  (optional)
created__gte = 'created__gte_example' # str |  (optional)
created__lte = 'created__lte_example' # str |  (optional)
last_updated = 'last_updated_example' # str |  (optional)
last_updated__gte = 'last_updated__gte_example' # str |  (optional)
last_updated__lte = 'last_updated__lte_example' # str |  (optional)
q = 'q_example' # str |  (optional)
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
name__n = 'name__n_example' # str |  (optional)
name__ic = 'name__ic_example' # str |  (optional)
name__nic = 'name__nic_example' # str |  (optional)
name__iew = 'name__iew_example' # str |  (optional)
name__niew = 'name__niew_example' # str |  (optional)
name__isw = 'name__isw_example' # str |  (optional)
name__nisw = 'name__nisw_example' # str |  (optional)
name__ie = 'name__ie_example' # str |  (optional)
name__nie = 'name__nie_example' # str |  (optional)
slug__n = 'slug__n_example' # str |  (optional)
slug__ic = 'slug__ic_example' # str |  (optional)
slug__nic = 'slug__nic_example' # str |  (optional)
slug__iew = 'slug__iew_example' # str |  (optional)
slug__niew = 'slug__niew_example' # str |  (optional)
slug__isw = 'slug__isw_example' # str |  (optional)
slug__nisw = 'slug__nisw_example' # str |  (optional)
slug__ie = 'slug__ie_example' # str |  (optional)
slug__nie = 'slug__nie_example' # str |  (optional)
asn__n = 'asn__n_example' # str |  (optional)
asn__lte = 'asn__lte_example' # str |  (optional)
asn__lt = 'asn__lt_example' # str |  (optional)
asn__gte = 'asn__gte_example' # str |  (optional)
asn__gt = 'asn__gt_example' # str |  (optional)
account__n = 'account__n_example' # str |  (optional)
account__ic = 'account__ic_example' # str |  (optional)
account__nic = 'account__nic_example' # str |  (optional)
account__iew = 'account__iew_example' # str |  (optional)
account__niew = 'account__niew_example' # str |  (optional)
account__isw = 'account__isw_example' # str |  (optional)
account__nisw = 'account__nisw_example' # str |  (optional)
account__ie = 'account__ie_example' # str |  (optional)
account__nie = 'account__nie_example' # str |  (optional)
region_id__n = 'region_id__n_example' # str |  (optional)
region__n = 'region__n_example' # str |  (optional)
site_id__n = 'site_id__n_example' # str |  (optional)
site__n = 'site__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.circuits_providers_list(id=id, name=name, slug=slug, asn=asn, account=account, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, region_id=region_id, region=region, site_id=site_id, site=site, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, asn__n=asn__n, asn__lte=asn__lte, asn__lt=asn__lt, asn__gte=asn__gte, asn__gt=asn__gt, account__n=account__n, account__ic=account__ic, account__nic=account__nic, account__iew=account__iew, account__niew=account__niew, account__isw=account__isw, account__nisw=account__nisw, account__ie=account__ie, account__nie=account__nie, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **asn** | **str**|  | [optional] 
 **account** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **created__gte** | **str**|  | [optional] 
 **created__lte** | **str**|  | [optional] 
 **last_updated** | **str**|  | [optional] 
 **last_updated__gte** | **str**|  | [optional] 
 **last_updated__lte** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **name__n** | **str**|  | [optional] 
 **name__ic** | **str**|  | [optional] 
 **name__nic** | **str**|  | [optional] 
 **name__iew** | **str**|  | [optional] 
 **name__niew** | **str**|  | [optional] 
 **name__isw** | **str**|  | [optional] 
 **name__nisw** | **str**|  | [optional] 
 **name__ie** | **str**|  | [optional] 
 **name__nie** | **str**|  | [optional] 
 **slug__n** | **str**|  | [optional] 
 **slug__ic** | **str**|  | [optional] 
 **slug__nic** | **str**|  | [optional] 
 **slug__iew** | **str**|  | [optional] 
 **slug__niew** | **str**|  | [optional] 
 **slug__isw** | **str**|  | [optional] 
 **slug__nisw** | **str**|  | [optional] 
 **slug__ie** | **str**|  | [optional] 
 **slug__nie** | **str**|  | [optional] 
 **asn__n** | **str**|  | [optional] 
 **asn__lte** | **str**|  | [optional] 
 **asn__lt** | **str**|  | [optional] 
 **asn__gte** | **str**|  | [optional] 
 **asn__gt** | **str**|  | [optional] 
 **account__n** | **str**|  | [optional] 
 **account__ic** | **str**|  | [optional] 
 **account__nic** | **str**|  | [optional] 
 **account__iew** | **str**|  | [optional] 
 **account__niew** | **str**|  | [optional] 
 **account__isw** | **str**|  | [optional] 
 **account__nisw** | **str**|  | [optional] 
 **account__ie** | **str**|  | [optional] 
 **account__nie** | **str**|  | [optional] 
 **region_id__n** | **str**|  | [optional] 
 **region__n** | **str**|  | [optional] 
 **site_id__n** | **str**|  | [optional] 
 **site__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_partial_update**
> Provider circuits_providers_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.
data = netbox_client.Provider() # Provider | 

try:
    api_response = api_instance.circuits_providers_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 
 **data** | [**Provider**](Provider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_read**
> Provider circuits_providers_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.

try:
    api_response = api_instance.circuits_providers_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_update**
> Provider circuits_providers_update(id, data)





### Example
```python
from __future__ import print_function
import time
import netbox_client
from netbox_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = netbox_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = netbox_client.CircuitsApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.
data = netbox_client.Provider() # Provider | 

try:
    api_response = api_instance.circuits_providers_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 
 **data** | [**Provider**](Provider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

