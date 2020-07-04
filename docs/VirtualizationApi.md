# netbox_client.VirtualizationApi

All URIs are relative to *https://netbox.us-east-2.ops.underline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualization_cluster_groups_create**](VirtualizationApi.md#virtualization_cluster_groups_create) | **POST** /virtualization/cluster-groups/ | 
[**virtualization_cluster_groups_delete**](VirtualizationApi.md#virtualization_cluster_groups_delete) | **DELETE** /virtualization/cluster-groups/{id}/ | 
[**virtualization_cluster_groups_list**](VirtualizationApi.md#virtualization_cluster_groups_list) | **GET** /virtualization/cluster-groups/ | 
[**virtualization_cluster_groups_partial_update**](VirtualizationApi.md#virtualization_cluster_groups_partial_update) | **PATCH** /virtualization/cluster-groups/{id}/ | 
[**virtualization_cluster_groups_read**](VirtualizationApi.md#virtualization_cluster_groups_read) | **GET** /virtualization/cluster-groups/{id}/ | 
[**virtualization_cluster_groups_update**](VirtualizationApi.md#virtualization_cluster_groups_update) | **PUT** /virtualization/cluster-groups/{id}/ | 
[**virtualization_cluster_types_create**](VirtualizationApi.md#virtualization_cluster_types_create) | **POST** /virtualization/cluster-types/ | 
[**virtualization_cluster_types_delete**](VirtualizationApi.md#virtualization_cluster_types_delete) | **DELETE** /virtualization/cluster-types/{id}/ | 
[**virtualization_cluster_types_list**](VirtualizationApi.md#virtualization_cluster_types_list) | **GET** /virtualization/cluster-types/ | 
[**virtualization_cluster_types_partial_update**](VirtualizationApi.md#virtualization_cluster_types_partial_update) | **PATCH** /virtualization/cluster-types/{id}/ | 
[**virtualization_cluster_types_read**](VirtualizationApi.md#virtualization_cluster_types_read) | **GET** /virtualization/cluster-types/{id}/ | 
[**virtualization_cluster_types_update**](VirtualizationApi.md#virtualization_cluster_types_update) | **PUT** /virtualization/cluster-types/{id}/ | 
[**virtualization_clusters_create**](VirtualizationApi.md#virtualization_clusters_create) | **POST** /virtualization/clusters/ | 
[**virtualization_clusters_delete**](VirtualizationApi.md#virtualization_clusters_delete) | **DELETE** /virtualization/clusters/{id}/ | 
[**virtualization_clusters_list**](VirtualizationApi.md#virtualization_clusters_list) | **GET** /virtualization/clusters/ | 
[**virtualization_clusters_partial_update**](VirtualizationApi.md#virtualization_clusters_partial_update) | **PATCH** /virtualization/clusters/{id}/ | 
[**virtualization_clusters_read**](VirtualizationApi.md#virtualization_clusters_read) | **GET** /virtualization/clusters/{id}/ | 
[**virtualization_clusters_update**](VirtualizationApi.md#virtualization_clusters_update) | **PUT** /virtualization/clusters/{id}/ | 
[**virtualization_interfaces_create**](VirtualizationApi.md#virtualization_interfaces_create) | **POST** /virtualization/interfaces/ | 
[**virtualization_interfaces_delete**](VirtualizationApi.md#virtualization_interfaces_delete) | **DELETE** /virtualization/interfaces/{id}/ | 
[**virtualization_interfaces_list**](VirtualizationApi.md#virtualization_interfaces_list) | **GET** /virtualization/interfaces/ | 
[**virtualization_interfaces_partial_update**](VirtualizationApi.md#virtualization_interfaces_partial_update) | **PATCH** /virtualization/interfaces/{id}/ | 
[**virtualization_interfaces_read**](VirtualizationApi.md#virtualization_interfaces_read) | **GET** /virtualization/interfaces/{id}/ | 
[**virtualization_interfaces_update**](VirtualizationApi.md#virtualization_interfaces_update) | **PUT** /virtualization/interfaces/{id}/ | 
[**virtualization_virtual_machines_create**](VirtualizationApi.md#virtualization_virtual_machines_create) | **POST** /virtualization/virtual-machines/ | 
[**virtualization_virtual_machines_delete**](VirtualizationApi.md#virtualization_virtual_machines_delete) | **DELETE** /virtualization/virtual-machines/{id}/ | 
[**virtualization_virtual_machines_list**](VirtualizationApi.md#virtualization_virtual_machines_list) | **GET** /virtualization/virtual-machines/ | 
[**virtualization_virtual_machines_partial_update**](VirtualizationApi.md#virtualization_virtual_machines_partial_update) | **PATCH** /virtualization/virtual-machines/{id}/ | 
[**virtualization_virtual_machines_read**](VirtualizationApi.md#virtualization_virtual_machines_read) | **GET** /virtualization/virtual-machines/{id}/ | 
[**virtualization_virtual_machines_update**](VirtualizationApi.md#virtualization_virtual_machines_update) | **PUT** /virtualization/virtual-machines/{id}/ | 


# **virtualization_cluster_groups_create**
> ClusterGroup virtualization_cluster_groups_create(data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
data = netbox_client.ClusterGroup() # ClusterGroup | 

try:
    api_response = api_instance.virtualization_cluster_groups_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ClusterGroup**](ClusterGroup.md)|  | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_delete**
> virtualization_cluster_groups_delete(id)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster group.

try:
    api_instance.virtualization_cluster_groups_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster group. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_list**
> InlineResponse20056 virtualization_cluster_groups_list(id=id, name=name, slug=slug, description=description, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, limit=limit, offset=offset)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
description = 'description_example' # str |  (optional)
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
description__n = 'description__n_example' # str |  (optional)
description__ic = 'description__ic_example' # str |  (optional)
description__nic = 'description__nic_example' # str |  (optional)
description__iew = 'description__iew_example' # str |  (optional)
description__niew = 'description__niew_example' # str |  (optional)
description__isw = 'description__isw_example' # str |  (optional)
description__nisw = 'description__nisw_example' # str |  (optional)
description__ie = 'description__ie_example' # str |  (optional)
description__nie = 'description__nie_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_cluster_groups_list(id=id, name=name, slug=slug, description=description, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
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
 **description__n** | **str**|  | [optional] 
 **description__ic** | **str**|  | [optional] 
 **description__nic** | **str**|  | [optional] 
 **description__iew** | **str**|  | [optional] 
 **description__niew** | **str**|  | [optional] 
 **description__isw** | **str**|  | [optional] 
 **description__nisw** | **str**|  | [optional] 
 **description__ie** | **str**|  | [optional] 
 **description__nie** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_partial_update**
> ClusterGroup virtualization_cluster_groups_partial_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster group.
data = netbox_client.ClusterGroup() # ClusterGroup | 

try:
    api_response = api_instance.virtualization_cluster_groups_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster group. | 
 **data** | [**ClusterGroup**](ClusterGroup.md)|  | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_read**
> ClusterGroup virtualization_cluster_groups_read(id)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster group.

try:
    api_response = api_instance.virtualization_cluster_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster group. | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_update**
> ClusterGroup virtualization_cluster_groups_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster group.
data = netbox_client.ClusterGroup() # ClusterGroup | 

try:
    api_response = api_instance.virtualization_cluster_groups_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster group. | 
 **data** | [**ClusterGroup**](ClusterGroup.md)|  | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_create**
> ClusterType virtualization_cluster_types_create(data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
data = netbox_client.ClusterType() # ClusterType | 

try:
    api_response = api_instance.virtualization_cluster_types_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ClusterType**](ClusterType.md)|  | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_delete**
> virtualization_cluster_types_delete(id)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster type.

try:
    api_instance.virtualization_cluster_types_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster type. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_list**
> InlineResponse20057 virtualization_cluster_types_list(id=id, name=name, slug=slug, description=description, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, limit=limit, offset=offset)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
description = 'description_example' # str |  (optional)
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
description__n = 'description__n_example' # str |  (optional)
description__ic = 'description__ic_example' # str |  (optional)
description__nic = 'description__nic_example' # str |  (optional)
description__iew = 'description__iew_example' # str |  (optional)
description__niew = 'description__niew_example' # str |  (optional)
description__isw = 'description__isw_example' # str |  (optional)
description__nisw = 'description__nisw_example' # str |  (optional)
description__ie = 'description__ie_example' # str |  (optional)
description__nie = 'description__nie_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_cluster_types_list(id=id, name=name, slug=slug, description=description, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
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
 **description__n** | **str**|  | [optional] 
 **description__ic** | **str**|  | [optional] 
 **description__nic** | **str**|  | [optional] 
 **description__iew** | **str**|  | [optional] 
 **description__niew** | **str**|  | [optional] 
 **description__isw** | **str**|  | [optional] 
 **description__nisw** | **str**|  | [optional] 
 **description__ie** | **str**|  | [optional] 
 **description__nie** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_partial_update**
> ClusterType virtualization_cluster_types_partial_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster type.
data = netbox_client.ClusterType() # ClusterType | 

try:
    api_response = api_instance.virtualization_cluster_types_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster type. | 
 **data** | [**ClusterType**](ClusterType.md)|  | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_read**
> ClusterType virtualization_cluster_types_read(id)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster type.

try:
    api_response = api_instance.virtualization_cluster_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster type. | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_update**
> ClusterType virtualization_cluster_types_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster type.
data = netbox_client.ClusterType() # ClusterType | 

try:
    api_response = api_instance.virtualization_cluster_types_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster type. | 
 **data** | [**ClusterType**](ClusterType.md)|  | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_create**
> Cluster virtualization_clusters_create(data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableCluster() # WritableCluster | 

try:
    api_response = api_instance.virtualization_clusters_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableCluster**](WritableCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_delete**
> virtualization_clusters_delete(id)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster.

try:
    api_instance.virtualization_clusters_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_list**
> InlineResponse20058 virtualization_clusters_list(id=id, name=name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, region_id=region_id, region=region, site_id=site_id, site=site, group_id=group_id, group=group, type_id=type_id, type=type, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, group_id__n=group_id__n, group__n=group__n, type_id__n=type_id__n, type__n=type__n, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
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
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
group_id = 'group_id_example' # str |  (optional)
group = 'group_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
type = 'type_example' # str |  (optional)
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
tenant_group_id__n = 'tenant_group_id__n_example' # str |  (optional)
tenant_group__n = 'tenant_group__n_example' # str |  (optional)
tenant_id__n = 'tenant_id__n_example' # str |  (optional)
tenant__n = 'tenant__n_example' # str |  (optional)
region_id__n = 'region_id__n_example' # str |  (optional)
region__n = 'region__n_example' # str |  (optional)
site_id__n = 'site_id__n_example' # str |  (optional)
site__n = 'site__n_example' # str |  (optional)
group_id__n = 'group_id__n_example' # str |  (optional)
group__n = 'group__n_example' # str |  (optional)
type_id__n = 'type_id__n_example' # str |  (optional)
type__n = 'type__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_clusters_list(id=id, name=name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, region_id=region_id, region=region, site_id=site_id, site=site, group_id=group_id, group=group, type_id=type_id, type=type, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, group_id__n=group_id__n, group__n=group__n, type_id__n=type_id__n, type__n=type__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
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
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **group_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
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
 **tenant_group_id__n** | **str**|  | [optional] 
 **tenant_group__n** | **str**|  | [optional] 
 **tenant_id__n** | **str**|  | [optional] 
 **tenant__n** | **str**|  | [optional] 
 **region_id__n** | **str**|  | [optional] 
 **region__n** | **str**|  | [optional] 
 **site_id__n** | **str**|  | [optional] 
 **site__n** | **str**|  | [optional] 
 **group_id__n** | **str**|  | [optional] 
 **group__n** | **str**|  | [optional] 
 **type_id__n** | **str**|  | [optional] 
 **type__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_partial_update**
> Cluster virtualization_clusters_partial_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster.
data = netbox_client.WritableCluster() # WritableCluster | 

try:
    api_response = api_instance.virtualization_clusters_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster. | 
 **data** | [**WritableCluster**](WritableCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_read**
> Cluster virtualization_clusters_read(id)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster.

try:
    api_response = api_instance.virtualization_clusters_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_update**
> Cluster virtualization_clusters_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster.
data = netbox_client.WritableCluster() # WritableCluster | 

try:
    api_response = api_instance.virtualization_clusters_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster. | 
 **data** | [**WritableCluster**](WritableCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_create**
> VirtualMachineInterface virtualization_interfaces_create(data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableVirtualMachineInterface() # WritableVirtualMachineInterface | 

try:
    api_response = api_instance.virtualization_interfaces_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_delete**
> virtualization_interfaces_delete(id)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.

try:
    api_instance.virtualization_interfaces_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_list**
> InlineResponse20059 virtualization_interfaces_list(id=id, name=name, enabled=enabled, mtu=mtu, q=q, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, mac_address=mac_address, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, mtu__n=mtu__n, mtu__lte=mtu__lte, mtu__lt=mtu__lt, mtu__gte=mtu__gte, mtu__gt=mtu__gt, virtual_machine_id__n=virtual_machine_id__n, virtual_machine__n=virtual_machine__n, mac_address__n=mac_address__n, mac_address__ic=mac_address__ic, mac_address__nic=mac_address__nic, mac_address__iew=mac_address__iew, mac_address__niew=mac_address__niew, mac_address__isw=mac_address__isw, mac_address__nisw=mac_address__nisw, mac_address__ie=mac_address__ie, mac_address__nie=mac_address__nie, limit=limit, offset=offset)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
enabled = 'enabled_example' # str |  (optional)
mtu = 'mtu_example' # str |  (optional)
q = 'q_example' # str |  (optional)
virtual_machine_id = 'virtual_machine_id_example' # str |  (optional)
virtual_machine = 'virtual_machine_example' # str |  (optional)
mac_address = 'mac_address_example' # str |  (optional)
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
mtu__n = 'mtu__n_example' # str |  (optional)
mtu__lte = 'mtu__lte_example' # str |  (optional)
mtu__lt = 'mtu__lt_example' # str |  (optional)
mtu__gte = 'mtu__gte_example' # str |  (optional)
mtu__gt = 'mtu__gt_example' # str |  (optional)
virtual_machine_id__n = 'virtual_machine_id__n_example' # str |  (optional)
virtual_machine__n = 'virtual_machine__n_example' # str |  (optional)
mac_address__n = 'mac_address__n_example' # str |  (optional)
mac_address__ic = 'mac_address__ic_example' # str |  (optional)
mac_address__nic = 'mac_address__nic_example' # str |  (optional)
mac_address__iew = 'mac_address__iew_example' # str |  (optional)
mac_address__niew = 'mac_address__niew_example' # str |  (optional)
mac_address__isw = 'mac_address__isw_example' # str |  (optional)
mac_address__nisw = 'mac_address__nisw_example' # str |  (optional)
mac_address__ie = 'mac_address__ie_example' # str |  (optional)
mac_address__nie = 'mac_address__nie_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_interfaces_list(id=id, name=name, enabled=enabled, mtu=mtu, q=q, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, mac_address=mac_address, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, mtu__n=mtu__n, mtu__lte=mtu__lte, mtu__lt=mtu__lt, mtu__gte=mtu__gte, mtu__gt=mtu__gt, virtual_machine_id__n=virtual_machine_id__n, virtual_machine__n=virtual_machine__n, mac_address__n=mac_address__n, mac_address__ic=mac_address__ic, mac_address__nic=mac_address__nic, mac_address__iew=mac_address__iew, mac_address__niew=mac_address__niew, mac_address__isw=mac_address__isw, mac_address__nisw=mac_address__nisw, mac_address__ie=mac_address__ie, mac_address__nie=mac_address__nie, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **enabled** | **str**|  | [optional] 
 **mtu** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **virtual_machine_id** | **str**|  | [optional] 
 **virtual_machine** | **str**|  | [optional] 
 **mac_address** | **str**|  | [optional] 
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
 **mtu__n** | **str**|  | [optional] 
 **mtu__lte** | **str**|  | [optional] 
 **mtu__lt** | **str**|  | [optional] 
 **mtu__gte** | **str**|  | [optional] 
 **mtu__gt** | **str**|  | [optional] 
 **virtual_machine_id__n** | **str**|  | [optional] 
 **virtual_machine__n** | **str**|  | [optional] 
 **mac_address__n** | **str**|  | [optional] 
 **mac_address__ic** | **str**|  | [optional] 
 **mac_address__nic** | **str**|  | [optional] 
 **mac_address__iew** | **str**|  | [optional] 
 **mac_address__niew** | **str**|  | [optional] 
 **mac_address__isw** | **str**|  | [optional] 
 **mac_address__nisw** | **str**|  | [optional] 
 **mac_address__ie** | **str**|  | [optional] 
 **mac_address__nie** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_partial_update**
> VirtualMachineInterface virtualization_interfaces_partial_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.
data = netbox_client.WritableVirtualMachineInterface() # WritableVirtualMachineInterface | 

try:
    api_response = api_instance.virtualization_interfaces_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 
 **data** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_read**
> VirtualMachineInterface virtualization_interfaces_read(id)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.

try:
    api_response = api_instance.virtualization_interfaces_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_update**
> VirtualMachineInterface virtualization_interfaces_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.
data = netbox_client.WritableVirtualMachineInterface() # WritableVirtualMachineInterface | 

try:
    api_response = api_instance.virtualization_interfaces_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 
 **data** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_create**
> VirtualMachineWithConfigContext virtualization_virtual_machines_create(data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableVirtualMachineWithConfigContext() # WritableVirtualMachineWithConfigContext | 

try:
    api_response = api_instance.virtualization_virtual_machines_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_delete**
> virtualization_virtual_machines_delete(id)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this virtual machine.

try:
    api_instance.virtualization_virtual_machines_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this virtual machine. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_list**
> InlineResponse20060 virtualization_virtual_machines_list(id=id, name=name, cluster=cluster, vcpus=vcpus, memory=memory, disk=disk, local_context_data=local_context_data, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, status=status, cluster_group_id=cluster_group_id, cluster_group=cluster_group, cluster_type_id=cluster_type_id, cluster_type=cluster_type, cluster_id=cluster_id, region_id=region_id, region=region, site_id=site_id, site=site, role_id=role_id, role=role, platform_id=platform_id, platform=platform, mac_address=mac_address, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, cluster__n=cluster__n, vcpus__n=vcpus__n, vcpus__lte=vcpus__lte, vcpus__lt=vcpus__lt, vcpus__gte=vcpus__gte, vcpus__gt=vcpus__gt, memory__n=memory__n, memory__lte=memory__lte, memory__lt=memory__lt, memory__gte=memory__gte, memory__gt=memory__gt, disk__n=disk__n, disk__lte=disk__lte, disk__lt=disk__lt, disk__gte=disk__gte, disk__gt=disk__gt, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, status__n=status__n, cluster_group_id__n=cluster_group_id__n, cluster_group__n=cluster_group__n, cluster_type_id__n=cluster_type_id__n, cluster_type__n=cluster_type__n, cluster_id__n=cluster_id__n, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, role_id__n=role_id__n, role__n=role__n, platform_id__n=platform_id__n, platform__n=platform__n, mac_address__n=mac_address__n, mac_address__ic=mac_address__ic, mac_address__nic=mac_address__nic, mac_address__iew=mac_address__iew, mac_address__niew=mac_address__niew, mac_address__isw=mac_address__isw, mac_address__nisw=mac_address__nisw, mac_address__ie=mac_address__ie, mac_address__nie=mac_address__nie, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
cluster = 'cluster_example' # str |  (optional)
vcpus = 'vcpus_example' # str |  (optional)
memory = 'memory_example' # str |  (optional)
disk = 'disk_example' # str |  (optional)
local_context_data = 'local_context_data_example' # str |  (optional)
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
status = 'status_example' # str |  (optional)
cluster_group_id = 'cluster_group_id_example' # str |  (optional)
cluster_group = 'cluster_group_example' # str |  (optional)
cluster_type_id = 'cluster_type_id_example' # str |  (optional)
cluster_type = 'cluster_type_example' # str |  (optional)
cluster_id = 'cluster_id_example' # str |  (optional)
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
platform_id = 'platform_id_example' # str |  (optional)
platform = 'platform_example' # str |  (optional)
mac_address = 'mac_address_example' # str |  (optional)
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
cluster__n = 'cluster__n_example' # str |  (optional)
vcpus__n = 'vcpus__n_example' # str |  (optional)
vcpus__lte = 'vcpus__lte_example' # str |  (optional)
vcpus__lt = 'vcpus__lt_example' # str |  (optional)
vcpus__gte = 'vcpus__gte_example' # str |  (optional)
vcpus__gt = 'vcpus__gt_example' # str |  (optional)
memory__n = 'memory__n_example' # str |  (optional)
memory__lte = 'memory__lte_example' # str |  (optional)
memory__lt = 'memory__lt_example' # str |  (optional)
memory__gte = 'memory__gte_example' # str |  (optional)
memory__gt = 'memory__gt_example' # str |  (optional)
disk__n = 'disk__n_example' # str |  (optional)
disk__lte = 'disk__lte_example' # str |  (optional)
disk__lt = 'disk__lt_example' # str |  (optional)
disk__gte = 'disk__gte_example' # str |  (optional)
disk__gt = 'disk__gt_example' # str |  (optional)
tenant_group_id__n = 'tenant_group_id__n_example' # str |  (optional)
tenant_group__n = 'tenant_group__n_example' # str |  (optional)
tenant_id__n = 'tenant_id__n_example' # str |  (optional)
tenant__n = 'tenant__n_example' # str |  (optional)
status__n = 'status__n_example' # str |  (optional)
cluster_group_id__n = 'cluster_group_id__n_example' # str |  (optional)
cluster_group__n = 'cluster_group__n_example' # str |  (optional)
cluster_type_id__n = 'cluster_type_id__n_example' # str |  (optional)
cluster_type__n = 'cluster_type__n_example' # str |  (optional)
cluster_id__n = 'cluster_id__n_example' # str |  (optional)
region_id__n = 'region_id__n_example' # str |  (optional)
region__n = 'region__n_example' # str |  (optional)
site_id__n = 'site_id__n_example' # str |  (optional)
site__n = 'site__n_example' # str |  (optional)
role_id__n = 'role_id__n_example' # str |  (optional)
role__n = 'role__n_example' # str |  (optional)
platform_id__n = 'platform_id__n_example' # str |  (optional)
platform__n = 'platform__n_example' # str |  (optional)
mac_address__n = 'mac_address__n_example' # str |  (optional)
mac_address__ic = 'mac_address__ic_example' # str |  (optional)
mac_address__nic = 'mac_address__nic_example' # str |  (optional)
mac_address__iew = 'mac_address__iew_example' # str |  (optional)
mac_address__niew = 'mac_address__niew_example' # str |  (optional)
mac_address__isw = 'mac_address__isw_example' # str |  (optional)
mac_address__nisw = 'mac_address__nisw_example' # str |  (optional)
mac_address__ie = 'mac_address__ie_example' # str |  (optional)
mac_address__nie = 'mac_address__nie_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_virtual_machines_list(id=id, name=name, cluster=cluster, vcpus=vcpus, memory=memory, disk=disk, local_context_data=local_context_data, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, status=status, cluster_group_id=cluster_group_id, cluster_group=cluster_group, cluster_type_id=cluster_type_id, cluster_type=cluster_type, cluster_id=cluster_id, region_id=region_id, region=region, site_id=site_id, site=site, role_id=role_id, role=role, platform_id=platform_id, platform=platform, mac_address=mac_address, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, cluster__n=cluster__n, vcpus__n=vcpus__n, vcpus__lte=vcpus__lte, vcpus__lt=vcpus__lt, vcpus__gte=vcpus__gte, vcpus__gt=vcpus__gt, memory__n=memory__n, memory__lte=memory__lte, memory__lt=memory__lt, memory__gte=memory__gte, memory__gt=memory__gt, disk__n=disk__n, disk__lte=disk__lte, disk__lt=disk__lt, disk__gte=disk__gte, disk__gt=disk__gt, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, status__n=status__n, cluster_group_id__n=cluster_group_id__n, cluster_group__n=cluster_group__n, cluster_type_id__n=cluster_type_id__n, cluster_type__n=cluster_type__n, cluster_id__n=cluster_id__n, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, role_id__n=role_id__n, role__n=role__n, platform_id__n=platform_id__n, platform__n=platform__n, mac_address__n=mac_address__n, mac_address__ic=mac_address__ic, mac_address__nic=mac_address__nic, mac_address__iew=mac_address__iew, mac_address__niew=mac_address__niew, mac_address__isw=mac_address__isw, mac_address__nisw=mac_address__nisw, mac_address__ie=mac_address__ie, mac_address__nie=mac_address__nie, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **cluster** | **str**|  | [optional] 
 **vcpus** | **str**|  | [optional] 
 **memory** | **str**|  | [optional] 
 **disk** | **str**|  | [optional] 
 **local_context_data** | **str**|  | [optional] 
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
 **status** | **str**|  | [optional] 
 **cluster_group_id** | **str**|  | [optional] 
 **cluster_group** | **str**|  | [optional] 
 **cluster_type_id** | **str**|  | [optional] 
 **cluster_type** | **str**|  | [optional] 
 **cluster_id** | **str**|  | [optional] 
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **platform_id** | **str**|  | [optional] 
 **platform** | **str**|  | [optional] 
 **mac_address** | **str**|  | [optional] 
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
 **cluster__n** | **str**|  | [optional] 
 **vcpus__n** | **str**|  | [optional] 
 **vcpus__lte** | **str**|  | [optional] 
 **vcpus__lt** | **str**|  | [optional] 
 **vcpus__gte** | **str**|  | [optional] 
 **vcpus__gt** | **str**|  | [optional] 
 **memory__n** | **str**|  | [optional] 
 **memory__lte** | **str**|  | [optional] 
 **memory__lt** | **str**|  | [optional] 
 **memory__gte** | **str**|  | [optional] 
 **memory__gt** | **str**|  | [optional] 
 **disk__n** | **str**|  | [optional] 
 **disk__lte** | **str**|  | [optional] 
 **disk__lt** | **str**|  | [optional] 
 **disk__gte** | **str**|  | [optional] 
 **disk__gt** | **str**|  | [optional] 
 **tenant_group_id__n** | **str**|  | [optional] 
 **tenant_group__n** | **str**|  | [optional] 
 **tenant_id__n** | **str**|  | [optional] 
 **tenant__n** | **str**|  | [optional] 
 **status__n** | **str**|  | [optional] 
 **cluster_group_id__n** | **str**|  | [optional] 
 **cluster_group__n** | **str**|  | [optional] 
 **cluster_type_id__n** | **str**|  | [optional] 
 **cluster_type__n** | **str**|  | [optional] 
 **cluster_id__n** | **str**|  | [optional] 
 **region_id__n** | **str**|  | [optional] 
 **region__n** | **str**|  | [optional] 
 **site_id__n** | **str**|  | [optional] 
 **site__n** | **str**|  | [optional] 
 **role_id__n** | **str**|  | [optional] 
 **role__n** | **str**|  | [optional] 
 **platform_id__n** | **str**|  | [optional] 
 **platform__n** | **str**|  | [optional] 
 **mac_address__n** | **str**|  | [optional] 
 **mac_address__ic** | **str**|  | [optional] 
 **mac_address__nic** | **str**|  | [optional] 
 **mac_address__iew** | **str**|  | [optional] 
 **mac_address__niew** | **str**|  | [optional] 
 **mac_address__isw** | **str**|  | [optional] 
 **mac_address__nisw** | **str**|  | [optional] 
 **mac_address__ie** | **str**|  | [optional] 
 **mac_address__nie** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_partial_update**
> VirtualMachineWithConfigContext virtualization_virtual_machines_partial_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this virtual machine.
data = netbox_client.WritableVirtualMachineWithConfigContext() # WritableVirtualMachineWithConfigContext | 

try:
    api_response = api_instance.virtualization_virtual_machines_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this virtual machine. | 
 **data** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_read**
> VirtualMachineWithConfigContext virtualization_virtual_machines_read(id)



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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this virtual machine.

try:
    api_response = api_instance.virtualization_virtual_machines_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this virtual machine. | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_update**
> VirtualMachineWithConfigContext virtualization_virtual_machines_update(id, data)





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
api_instance = netbox_client.VirtualizationApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this virtual machine.
data = netbox_client.WritableVirtualMachineWithConfigContext() # WritableVirtualMachineWithConfigContext | 

try:
    api_response = api_instance.virtualization_virtual_machines_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this virtual machine. | 
 **data** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

