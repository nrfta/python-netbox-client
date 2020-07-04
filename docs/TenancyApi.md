# netbox_client.TenancyApi

All URIs are relative to *https://netbox/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenancy_tenant_groups_create**](TenancyApi.md#tenancy_tenant_groups_create) | **POST** /tenancy/tenant-groups/ | 
[**tenancy_tenant_groups_delete**](TenancyApi.md#tenancy_tenant_groups_delete) | **DELETE** /tenancy/tenant-groups/{id}/ | 
[**tenancy_tenant_groups_list**](TenancyApi.md#tenancy_tenant_groups_list) | **GET** /tenancy/tenant-groups/ | 
[**tenancy_tenant_groups_partial_update**](TenancyApi.md#tenancy_tenant_groups_partial_update) | **PATCH** /tenancy/tenant-groups/{id}/ | 
[**tenancy_tenant_groups_read**](TenancyApi.md#tenancy_tenant_groups_read) | **GET** /tenancy/tenant-groups/{id}/ | 
[**tenancy_tenant_groups_update**](TenancyApi.md#tenancy_tenant_groups_update) | **PUT** /tenancy/tenant-groups/{id}/ | 
[**tenancy_tenants_create**](TenancyApi.md#tenancy_tenants_create) | **POST** /tenancy/tenants/ | 
[**tenancy_tenants_delete**](TenancyApi.md#tenancy_tenants_delete) | **DELETE** /tenancy/tenants/{id}/ | 
[**tenancy_tenants_list**](TenancyApi.md#tenancy_tenants_list) | **GET** /tenancy/tenants/ | 
[**tenancy_tenants_partial_update**](TenancyApi.md#tenancy_tenants_partial_update) | **PATCH** /tenancy/tenants/{id}/ | 
[**tenancy_tenants_read**](TenancyApi.md#tenancy_tenants_read) | **GET** /tenancy/tenants/{id}/ | 
[**tenancy_tenants_update**](TenancyApi.md#tenancy_tenants_update) | **PUT** /tenancy/tenants/{id}/ | 


# **tenancy_tenant_groups_create**
> TenantGroup tenancy_tenant_groups_create(data)





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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableTenantGroup() # WritableTenantGroup | 

try:
    api_response = api_instance.tenancy_tenant_groups_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableTenantGroup**](WritableTenantGroup.md)|  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_delete**
> tenancy_tenant_groups_delete(id)





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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant group.

try:
    api_instance.tenancy_tenant_groups_delete(id)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_list**
> InlineResponse20054 tenancy_tenant_groups_list(id=id, name=name, slug=slug, description=description, q=q, parent_id=parent_id, parent=parent, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, parent_id__n=parent_id__n, parent__n=parent__n, limit=limit, offset=offset)



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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
description = 'description_example' # str |  (optional)
q = 'q_example' # str |  (optional)
parent_id = 'parent_id_example' # str |  (optional)
parent = 'parent_example' # str |  (optional)
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
parent_id__n = 'parent_id__n_example' # str |  (optional)
parent__n = 'parent__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.tenancy_tenant_groups_list(id=id, name=name, slug=slug, description=description, q=q, parent_id=parent_id, parent=parent, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, parent_id__n=parent_id__n, parent__n=parent__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **parent_id** | **str**|  | [optional] 
 **parent** | **str**|  | [optional] 
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
 **parent_id__n** | **str**|  | [optional] 
 **parent__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_partial_update**
> TenantGroup tenancy_tenant_groups_partial_update(id, data)





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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant group.
data = netbox_client.WritableTenantGroup() # WritableTenantGroup | 

try:
    api_response = api_instance.tenancy_tenant_groups_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 
 **data** | [**WritableTenantGroup**](WritableTenantGroup.md)|  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_read**
> TenantGroup tenancy_tenant_groups_read(id)



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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant group.

try:
    api_response = api_instance.tenancy_tenant_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_update**
> TenantGroup tenancy_tenant_groups_update(id, data)





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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant group.
data = netbox_client.WritableTenantGroup() # WritableTenantGroup | 

try:
    api_response = api_instance.tenancy_tenant_groups_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 
 **data** | [**WritableTenantGroup**](WritableTenantGroup.md)|  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_create**
> Tenant tenancy_tenants_create(data)





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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableTenant() # WritableTenant | 

try:
    api_response = api_instance.tenancy_tenants_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableTenant**](WritableTenant.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_delete**
> tenancy_tenants_delete(id)





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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.

try:
    api_instance.tenancy_tenants_delete(id)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_list**
> InlineResponse20055 tenancy_tenants_list(id=id, name=name, slug=slug, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, group_id=group_id, group=group, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, group_id__n=group_id__n, group__n=group__n, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
created = 'created_example' # str |  (optional)
created__gte = 'created__gte_example' # str |  (optional)
created__lte = 'created__lte_example' # str |  (optional)
last_updated = 'last_updated_example' # str |  (optional)
last_updated__gte = 'last_updated__gte_example' # str |  (optional)
last_updated__lte = 'last_updated__lte_example' # str |  (optional)
q = 'q_example' # str |  (optional)
group_id = 'group_id_example' # str |  (optional)
group = 'group_example' # str |  (optional)
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
group_id__n = 'group_id__n_example' # str |  (optional)
group__n = 'group__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.tenancy_tenants_list(id=id, name=name, slug=slug, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, group_id=group_id, group=group, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, group_id__n=group_id__n, group__n=group__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **created__gte** | **str**|  | [optional] 
 **created__lte** | **str**|  | [optional] 
 **last_updated** | **str**|  | [optional] 
 **last_updated__gte** | **str**|  | [optional] 
 **last_updated__lte** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **group_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
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
 **group_id__n** | **str**|  | [optional] 
 **group__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_partial_update**
> Tenant tenancy_tenants_partial_update(id, data)





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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.
data = netbox_client.WritableTenant() # WritableTenant | 

try:
    api_response = api_instance.tenancy_tenants_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 
 **data** | [**WritableTenant**](WritableTenant.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_read**
> Tenant tenancy_tenants_read(id)



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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.

try:
    api_response = api_instance.tenancy_tenants_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_update**
> Tenant tenancy_tenants_update(id, data)





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
api_instance = netbox_client.TenancyApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.
data = netbox_client.WritableTenant() # WritableTenant | 

try:
    api_response = api_instance.tenancy_tenants_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 
 **data** | [**WritableTenant**](WritableTenant.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

