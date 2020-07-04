# netbox_client.IpamApi

All URIs are relative to *https://netbox.us-east-2.ops.underline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipam_aggregates_create**](IpamApi.md#ipam_aggregates_create) | **POST** /ipam/aggregates/ | 
[**ipam_aggregates_delete**](IpamApi.md#ipam_aggregates_delete) | **DELETE** /ipam/aggregates/{id}/ | 
[**ipam_aggregates_list**](IpamApi.md#ipam_aggregates_list) | **GET** /ipam/aggregates/ | 
[**ipam_aggregates_partial_update**](IpamApi.md#ipam_aggregates_partial_update) | **PATCH** /ipam/aggregates/{id}/ | 
[**ipam_aggregates_read**](IpamApi.md#ipam_aggregates_read) | **GET** /ipam/aggregates/{id}/ | 
[**ipam_aggregates_update**](IpamApi.md#ipam_aggregates_update) | **PUT** /ipam/aggregates/{id}/ | 
[**ipam_ip_addresses_create**](IpamApi.md#ipam_ip_addresses_create) | **POST** /ipam/ip-addresses/ | 
[**ipam_ip_addresses_delete**](IpamApi.md#ipam_ip_addresses_delete) | **DELETE** /ipam/ip-addresses/{id}/ | 
[**ipam_ip_addresses_list**](IpamApi.md#ipam_ip_addresses_list) | **GET** /ipam/ip-addresses/ | 
[**ipam_ip_addresses_partial_update**](IpamApi.md#ipam_ip_addresses_partial_update) | **PATCH** /ipam/ip-addresses/{id}/ | 
[**ipam_ip_addresses_read**](IpamApi.md#ipam_ip_addresses_read) | **GET** /ipam/ip-addresses/{id}/ | 
[**ipam_ip_addresses_update**](IpamApi.md#ipam_ip_addresses_update) | **PUT** /ipam/ip-addresses/{id}/ | 
[**ipam_prefixes_available_ips_create**](IpamApi.md#ipam_prefixes_available_ips_create) | **POST** /ipam/prefixes/{id}/available-ips/ | 
[**ipam_prefixes_available_ips_read**](IpamApi.md#ipam_prefixes_available_ips_read) | **GET** /ipam/prefixes/{id}/available-ips/ | 
[**ipam_prefixes_available_prefixes_create**](IpamApi.md#ipam_prefixes_available_prefixes_create) | **POST** /ipam/prefixes/{id}/available-prefixes/ | A convenience method for returning available child prefixes within a parent.
[**ipam_prefixes_available_prefixes_read**](IpamApi.md#ipam_prefixes_available_prefixes_read) | **GET** /ipam/prefixes/{id}/available-prefixes/ | A convenience method for returning available child prefixes within a parent.
[**ipam_prefixes_create**](IpamApi.md#ipam_prefixes_create) | **POST** /ipam/prefixes/ | 
[**ipam_prefixes_delete**](IpamApi.md#ipam_prefixes_delete) | **DELETE** /ipam/prefixes/{id}/ | 
[**ipam_prefixes_list**](IpamApi.md#ipam_prefixes_list) | **GET** /ipam/prefixes/ | 
[**ipam_prefixes_partial_update**](IpamApi.md#ipam_prefixes_partial_update) | **PATCH** /ipam/prefixes/{id}/ | 
[**ipam_prefixes_read**](IpamApi.md#ipam_prefixes_read) | **GET** /ipam/prefixes/{id}/ | 
[**ipam_prefixes_update**](IpamApi.md#ipam_prefixes_update) | **PUT** /ipam/prefixes/{id}/ | 
[**ipam_rirs_create**](IpamApi.md#ipam_rirs_create) | **POST** /ipam/rirs/ | 
[**ipam_rirs_delete**](IpamApi.md#ipam_rirs_delete) | **DELETE** /ipam/rirs/{id}/ | 
[**ipam_rirs_list**](IpamApi.md#ipam_rirs_list) | **GET** /ipam/rirs/ | 
[**ipam_rirs_partial_update**](IpamApi.md#ipam_rirs_partial_update) | **PATCH** /ipam/rirs/{id}/ | 
[**ipam_rirs_read**](IpamApi.md#ipam_rirs_read) | **GET** /ipam/rirs/{id}/ | 
[**ipam_rirs_update**](IpamApi.md#ipam_rirs_update) | **PUT** /ipam/rirs/{id}/ | 
[**ipam_roles_create**](IpamApi.md#ipam_roles_create) | **POST** /ipam/roles/ | 
[**ipam_roles_delete**](IpamApi.md#ipam_roles_delete) | **DELETE** /ipam/roles/{id}/ | 
[**ipam_roles_list**](IpamApi.md#ipam_roles_list) | **GET** /ipam/roles/ | 
[**ipam_roles_partial_update**](IpamApi.md#ipam_roles_partial_update) | **PATCH** /ipam/roles/{id}/ | 
[**ipam_roles_read**](IpamApi.md#ipam_roles_read) | **GET** /ipam/roles/{id}/ | 
[**ipam_roles_update**](IpamApi.md#ipam_roles_update) | **PUT** /ipam/roles/{id}/ | 
[**ipam_services_create**](IpamApi.md#ipam_services_create) | **POST** /ipam/services/ | 
[**ipam_services_delete**](IpamApi.md#ipam_services_delete) | **DELETE** /ipam/services/{id}/ | 
[**ipam_services_list**](IpamApi.md#ipam_services_list) | **GET** /ipam/services/ | 
[**ipam_services_partial_update**](IpamApi.md#ipam_services_partial_update) | **PATCH** /ipam/services/{id}/ | 
[**ipam_services_read**](IpamApi.md#ipam_services_read) | **GET** /ipam/services/{id}/ | 
[**ipam_services_update**](IpamApi.md#ipam_services_update) | **PUT** /ipam/services/{id}/ | 
[**ipam_vlan_groups_create**](IpamApi.md#ipam_vlan_groups_create) | **POST** /ipam/vlan-groups/ | 
[**ipam_vlan_groups_delete**](IpamApi.md#ipam_vlan_groups_delete) | **DELETE** /ipam/vlan-groups/{id}/ | 
[**ipam_vlan_groups_list**](IpamApi.md#ipam_vlan_groups_list) | **GET** /ipam/vlan-groups/ | 
[**ipam_vlan_groups_partial_update**](IpamApi.md#ipam_vlan_groups_partial_update) | **PATCH** /ipam/vlan-groups/{id}/ | 
[**ipam_vlan_groups_read**](IpamApi.md#ipam_vlan_groups_read) | **GET** /ipam/vlan-groups/{id}/ | 
[**ipam_vlan_groups_update**](IpamApi.md#ipam_vlan_groups_update) | **PUT** /ipam/vlan-groups/{id}/ | 
[**ipam_vlans_create**](IpamApi.md#ipam_vlans_create) | **POST** /ipam/vlans/ | 
[**ipam_vlans_delete**](IpamApi.md#ipam_vlans_delete) | **DELETE** /ipam/vlans/{id}/ | 
[**ipam_vlans_list**](IpamApi.md#ipam_vlans_list) | **GET** /ipam/vlans/ | 
[**ipam_vlans_partial_update**](IpamApi.md#ipam_vlans_partial_update) | **PATCH** /ipam/vlans/{id}/ | 
[**ipam_vlans_read**](IpamApi.md#ipam_vlans_read) | **GET** /ipam/vlans/{id}/ | 
[**ipam_vlans_update**](IpamApi.md#ipam_vlans_update) | **PUT** /ipam/vlans/{id}/ | 
[**ipam_vrfs_create**](IpamApi.md#ipam_vrfs_create) | **POST** /ipam/vrfs/ | 
[**ipam_vrfs_delete**](IpamApi.md#ipam_vrfs_delete) | **DELETE** /ipam/vrfs/{id}/ | 
[**ipam_vrfs_list**](IpamApi.md#ipam_vrfs_list) | **GET** /ipam/vrfs/ | 
[**ipam_vrfs_partial_update**](IpamApi.md#ipam_vrfs_partial_update) | **PATCH** /ipam/vrfs/{id}/ | 
[**ipam_vrfs_read**](IpamApi.md#ipam_vrfs_read) | **GET** /ipam/vrfs/{id}/ | 
[**ipam_vrfs_update**](IpamApi.md#ipam_vrfs_update) | **PUT** /ipam/vrfs/{id}/ | 


# **ipam_aggregates_create**
> Aggregate ipam_aggregates_create(data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableAggregate() # WritableAggregate | 

try:
    api_response = api_instance.ipam_aggregates_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableAggregate**](WritableAggregate.md)|  | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_delete**
> ipam_aggregates_delete(id)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this aggregate.

try:
    api_instance.ipam_aggregates_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this aggregate. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_list**
> InlineResponse20043 ipam_aggregates_list(id=id, date_added=date_added, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, family=family, prefix=prefix, rir_id=rir_id, rir=rir, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, date_added__n=date_added__n, date_added__lte=date_added__lte, date_added__lt=date_added__lt, date_added__gte=date_added__gte, date_added__gt=date_added__gt, rir_id__n=rir_id__n, rir__n=rir__n, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
date_added = 'date_added_example' # str |  (optional)
created = 'created_example' # str |  (optional)
created__gte = 'created__gte_example' # str |  (optional)
created__lte = 'created__lte_example' # str |  (optional)
last_updated = 'last_updated_example' # str |  (optional)
last_updated__gte = 'last_updated__gte_example' # str |  (optional)
last_updated__lte = 'last_updated__lte_example' # str |  (optional)
q = 'q_example' # str |  (optional)
family = 8.14 # float |  (optional)
prefix = 'prefix_example' # str |  (optional)
rir_id = 'rir_id_example' # str |  (optional)
rir = 'rir_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
date_added__n = 'date_added__n_example' # str |  (optional)
date_added__lte = 'date_added__lte_example' # str |  (optional)
date_added__lt = 'date_added__lt_example' # str |  (optional)
date_added__gte = 'date_added__gte_example' # str |  (optional)
date_added__gt = 'date_added__gt_example' # str |  (optional)
rir_id__n = 'rir_id__n_example' # str |  (optional)
rir__n = 'rir__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_aggregates_list(id=id, date_added=date_added, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, family=family, prefix=prefix, rir_id=rir_id, rir=rir, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, date_added__n=date_added__n, date_added__lte=date_added__lte, date_added__lt=date_added__lt, date_added__gte=date_added__gte, date_added__gt=date_added__gt, rir_id__n=rir_id__n, rir__n=rir__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **date_added** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **created__gte** | **str**|  | [optional] 
 **created__lte** | **str**|  | [optional] 
 **last_updated** | **str**|  | [optional] 
 **last_updated__gte** | **str**|  | [optional] 
 **last_updated__lte** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **family** | **float**|  | [optional] 
 **prefix** | **str**|  | [optional] 
 **rir_id** | **str**|  | [optional] 
 **rir** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **date_added__n** | **str**|  | [optional] 
 **date_added__lte** | **str**|  | [optional] 
 **date_added__lt** | **str**|  | [optional] 
 **date_added__gte** | **str**|  | [optional] 
 **date_added__gt** | **str**|  | [optional] 
 **rir_id__n** | **str**|  | [optional] 
 **rir__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_partial_update**
> Aggregate ipam_aggregates_partial_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this aggregate.
data = netbox_client.WritableAggregate() # WritableAggregate | 

try:
    api_response = api_instance.ipam_aggregates_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this aggregate. | 
 **data** | [**WritableAggregate**](WritableAggregate.md)|  | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_read**
> Aggregate ipam_aggregates_read(id)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this aggregate.

try:
    api_response = api_instance.ipam_aggregates_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this aggregate. | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_update**
> Aggregate ipam_aggregates_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this aggregate.
data = netbox_client.WritableAggregate() # WritableAggregate | 

try:
    api_response = api_instance.ipam_aggregates_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this aggregate. | 
 **data** | [**WritableAggregate**](WritableAggregate.md)|  | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_create**
> IPAddress ipam_ip_addresses_create(data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableIPAddress() # WritableIPAddress | 

try:
    api_response = api_instance.ipam_ip_addresses_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableIPAddress**](WritableIPAddress.md)|  | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_delete**
> ipam_ip_addresses_delete(id)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this IP address.

try:
    api_instance.ipam_ip_addresses_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this IP address. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_list**
> InlineResponse20044 ipam_ip_addresses_list(id=id, dns_name=dns_name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, family=family, parent=parent, address=address, mask_length=mask_length, vrf_id=vrf_id, vrf=vrf, device=device, device_id=device_id, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, interface=interface, interface_id=interface_id, assigned_to_interface=assigned_to_interface, status=status, role=role, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, dns_name__n=dns_name__n, dns_name__ic=dns_name__ic, dns_name__nic=dns_name__nic, dns_name__iew=dns_name__iew, dns_name__niew=dns_name__niew, dns_name__isw=dns_name__isw, dns_name__nisw=dns_name__nisw, dns_name__ie=dns_name__ie, dns_name__nie=dns_name__nie, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, vrf_id__n=vrf_id__n, vrf__n=vrf__n, virtual_machine_id__n=virtual_machine_id__n, virtual_machine__n=virtual_machine__n, interface__n=interface__n, interface_id__n=interface_id__n, status__n=status__n, role__n=role__n, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
dns_name = 'dns_name_example' # str |  (optional)
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
family = 8.14 # float |  (optional)
parent = 'parent_example' # str |  (optional)
address = 'address_example' # str |  (optional)
mask_length = 8.14 # float |  (optional)
vrf_id = 'vrf_id_example' # str |  (optional)
vrf = 'vrf_example' # str |  (optional)
device = 'device_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
virtual_machine_id = 'virtual_machine_id_example' # str |  (optional)
virtual_machine = 'virtual_machine_example' # str |  (optional)
interface = 'interface_example' # str |  (optional)
interface_id = 'interface_id_example' # str |  (optional)
assigned_to_interface = 'assigned_to_interface_example' # str |  (optional)
status = 'status_example' # str |  (optional)
role = 'role_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
dns_name__n = 'dns_name__n_example' # str |  (optional)
dns_name__ic = 'dns_name__ic_example' # str |  (optional)
dns_name__nic = 'dns_name__nic_example' # str |  (optional)
dns_name__iew = 'dns_name__iew_example' # str |  (optional)
dns_name__niew = 'dns_name__niew_example' # str |  (optional)
dns_name__isw = 'dns_name__isw_example' # str |  (optional)
dns_name__nisw = 'dns_name__nisw_example' # str |  (optional)
dns_name__ie = 'dns_name__ie_example' # str |  (optional)
dns_name__nie = 'dns_name__nie_example' # str |  (optional)
tenant_group_id__n = 'tenant_group_id__n_example' # str |  (optional)
tenant_group__n = 'tenant_group__n_example' # str |  (optional)
tenant_id__n = 'tenant_id__n_example' # str |  (optional)
tenant__n = 'tenant__n_example' # str |  (optional)
vrf_id__n = 'vrf_id__n_example' # str |  (optional)
vrf__n = 'vrf__n_example' # str |  (optional)
virtual_machine_id__n = 'virtual_machine_id__n_example' # str |  (optional)
virtual_machine__n = 'virtual_machine__n_example' # str |  (optional)
interface__n = 'interface__n_example' # str |  (optional)
interface_id__n = 'interface_id__n_example' # str |  (optional)
status__n = 'status__n_example' # str |  (optional)
role__n = 'role__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_ip_addresses_list(id=id, dns_name=dns_name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, family=family, parent=parent, address=address, mask_length=mask_length, vrf_id=vrf_id, vrf=vrf, device=device, device_id=device_id, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, interface=interface, interface_id=interface_id, assigned_to_interface=assigned_to_interface, status=status, role=role, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, dns_name__n=dns_name__n, dns_name__ic=dns_name__ic, dns_name__nic=dns_name__nic, dns_name__iew=dns_name__iew, dns_name__niew=dns_name__niew, dns_name__isw=dns_name__isw, dns_name__nisw=dns_name__nisw, dns_name__ie=dns_name__ie, dns_name__nie=dns_name__nie, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, vrf_id__n=vrf_id__n, vrf__n=vrf__n, virtual_machine_id__n=virtual_machine_id__n, virtual_machine__n=virtual_machine__n, interface__n=interface__n, interface_id__n=interface_id__n, status__n=status__n, role__n=role__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **dns_name** | **str**|  | [optional] 
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
 **family** | **float**|  | [optional] 
 **parent** | **str**|  | [optional] 
 **address** | **str**|  | [optional] 
 **mask_length** | **float**|  | [optional] 
 **vrf_id** | **str**|  | [optional] 
 **vrf** | **str**|  | [optional] 
 **device** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **virtual_machine_id** | **str**|  | [optional] 
 **virtual_machine** | **str**|  | [optional] 
 **interface** | **str**|  | [optional] 
 **interface_id** | **str**|  | [optional] 
 **assigned_to_interface** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **dns_name__n** | **str**|  | [optional] 
 **dns_name__ic** | **str**|  | [optional] 
 **dns_name__nic** | **str**|  | [optional] 
 **dns_name__iew** | **str**|  | [optional] 
 **dns_name__niew** | **str**|  | [optional] 
 **dns_name__isw** | **str**|  | [optional] 
 **dns_name__nisw** | **str**|  | [optional] 
 **dns_name__ie** | **str**|  | [optional] 
 **dns_name__nie** | **str**|  | [optional] 
 **tenant_group_id__n** | **str**|  | [optional] 
 **tenant_group__n** | **str**|  | [optional] 
 **tenant_id__n** | **str**|  | [optional] 
 **tenant__n** | **str**|  | [optional] 
 **vrf_id__n** | **str**|  | [optional] 
 **vrf__n** | **str**|  | [optional] 
 **virtual_machine_id__n** | **str**|  | [optional] 
 **virtual_machine__n** | **str**|  | [optional] 
 **interface__n** | **str**|  | [optional] 
 **interface_id__n** | **str**|  | [optional] 
 **status__n** | **str**|  | [optional] 
 **role__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_partial_update**
> IPAddress ipam_ip_addresses_partial_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this IP address.
data = netbox_client.WritableIPAddress() # WritableIPAddress | 

try:
    api_response = api_instance.ipam_ip_addresses_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this IP address. | 
 **data** | [**WritableIPAddress**](WritableIPAddress.md)|  | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_read**
> IPAddress ipam_ip_addresses_read(id)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this IP address.

try:
    api_response = api_instance.ipam_ip_addresses_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this IP address. | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_update**
> IPAddress ipam_ip_addresses_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this IP address.
data = netbox_client.WritableIPAddress() # WritableIPAddress | 

try:
    api_response = api_instance.ipam_ip_addresses_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this IP address. | 
 **data** | [**WritableIPAddress**](WritableIPAddress.md)|  | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_available_ips_create**
> list[AvailableIP] ipam_prefixes_available_ips_create(id, data)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.  The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.
data = netbox_client.WritablePrefix() # WritablePrefix | 

try:
    api_response = api_instance.ipam_prefixes_available_ips_create(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_available_ips_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**list[AvailableIP]**](AvailableIP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_available_ips_read**
> list[AvailableIP] ipam_prefixes_available_ips_read(id)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.  The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.

try:
    api_response = api_instance.ipam_prefixes_available_ips_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_available_ips_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 

### Return type

[**list[AvailableIP]**](AvailableIP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_available_prefixes_create**
> list[AvailablePrefix] ipam_prefixes_available_prefixes_create(id, data)

A convenience method for returning available child prefixes within a parent.

The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.
data = netbox_client.WritablePrefix() # WritablePrefix | 

try:
    # A convenience method for returning available child prefixes within a parent.
    api_response = api_instance.ipam_prefixes_available_prefixes_create(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_available_prefixes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**list[AvailablePrefix]**](AvailablePrefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_available_prefixes_read**
> list[AvailablePrefix] ipam_prefixes_available_prefixes_read(id)

A convenience method for returning available child prefixes within a parent.

The advisory lock decorator uses a PostgreSQL advisory lock to prevent this API from being invoked in parallel, which results in a race condition where multiple insertions can occur.

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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.

try:
    # A convenience method for returning available child prefixes within a parent.
    api_response = api_instance.ipam_prefixes_available_prefixes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_available_prefixes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 

### Return type

[**list[AvailablePrefix]**](AvailablePrefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_create**
> Prefix ipam_prefixes_create(data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritablePrefix() # WritablePrefix | 

try:
    api_response = api_instance.ipam_prefixes_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_delete**
> ipam_prefixes_delete(id)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.

try:
    api_instance.ipam_prefixes_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_list**
> InlineResponse20045 ipam_prefixes_list(id=id, is_pool=is_pool, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, family=family, prefix=prefix, within=within, within_include=within_include, contains=contains, mask_length=mask_length, vrf_id=vrf_id, vrf=vrf, region_id=region_id, region=region, site_id=site_id, site=site, vlan_id=vlan_id, vlan_vid=vlan_vid, role_id=role_id, role=role, status=status, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, vrf_id__n=vrf_id__n, vrf__n=vrf__n, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, vlan_id__n=vlan_id__n, role_id__n=role_id__n, role__n=role__n, status__n=status__n, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
is_pool = 'is_pool_example' # str |  (optional)
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
family = 8.14 # float |  (optional)
prefix = 'prefix_example' # str |  (optional)
within = 'within_example' # str |  (optional)
within_include = 'within_include_example' # str |  (optional)
contains = 'contains_example' # str |  (optional)
mask_length = 8.14 # float |  (optional)
vrf_id = 'vrf_id_example' # str |  (optional)
vrf = 'vrf_example' # str |  (optional)
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
vlan_id = 'vlan_id_example' # str |  (optional)
vlan_vid = 8.14 # float |  (optional)
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
status = 'status_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
tenant_group_id__n = 'tenant_group_id__n_example' # str |  (optional)
tenant_group__n = 'tenant_group__n_example' # str |  (optional)
tenant_id__n = 'tenant_id__n_example' # str |  (optional)
tenant__n = 'tenant__n_example' # str |  (optional)
vrf_id__n = 'vrf_id__n_example' # str |  (optional)
vrf__n = 'vrf__n_example' # str |  (optional)
region_id__n = 'region_id__n_example' # str |  (optional)
region__n = 'region__n_example' # str |  (optional)
site_id__n = 'site_id__n_example' # str |  (optional)
site__n = 'site__n_example' # str |  (optional)
vlan_id__n = 'vlan_id__n_example' # str |  (optional)
role_id__n = 'role_id__n_example' # str |  (optional)
role__n = 'role__n_example' # str |  (optional)
status__n = 'status__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_prefixes_list(id=id, is_pool=is_pool, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, family=family, prefix=prefix, within=within, within_include=within_include, contains=contains, mask_length=mask_length, vrf_id=vrf_id, vrf=vrf, region_id=region_id, region=region, site_id=site_id, site=site, vlan_id=vlan_id, vlan_vid=vlan_vid, role_id=role_id, role=role, status=status, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, vrf_id__n=vrf_id__n, vrf__n=vrf__n, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, vlan_id__n=vlan_id__n, role_id__n=role_id__n, role__n=role__n, status__n=status__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **is_pool** | **str**|  | [optional] 
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
 **family** | **float**|  | [optional] 
 **prefix** | **str**|  | [optional] 
 **within** | **str**|  | [optional] 
 **within_include** | **str**|  | [optional] 
 **contains** | **str**|  | [optional] 
 **mask_length** | **float**|  | [optional] 
 **vrf_id** | **str**|  | [optional] 
 **vrf** | **str**|  | [optional] 
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **vlan_id** | **str**|  | [optional] 
 **vlan_vid** | **float**|  | [optional] 
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **tenant_group_id__n** | **str**|  | [optional] 
 **tenant_group__n** | **str**|  | [optional] 
 **tenant_id__n** | **str**|  | [optional] 
 **tenant__n** | **str**|  | [optional] 
 **vrf_id__n** | **str**|  | [optional] 
 **vrf__n** | **str**|  | [optional] 
 **region_id__n** | **str**|  | [optional] 
 **region__n** | **str**|  | [optional] 
 **site_id__n** | **str**|  | [optional] 
 **site__n** | **str**|  | [optional] 
 **vlan_id__n** | **str**|  | [optional] 
 **role_id__n** | **str**|  | [optional] 
 **role__n** | **str**|  | [optional] 
 **status__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_partial_update**
> Prefix ipam_prefixes_partial_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.
data = netbox_client.WritablePrefix() # WritablePrefix | 

try:
    api_response = api_instance.ipam_prefixes_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_read**
> Prefix ipam_prefixes_read(id)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.

try:
    api_response = api_instance.ipam_prefixes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_update**
> Prefix ipam_prefixes_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.
data = netbox_client.WritablePrefix() # WritablePrefix | 

try:
    api_response = api_instance.ipam_prefixes_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_create**
> RIR ipam_rirs_create(data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
data = netbox_client.RIR() # RIR | 

try:
    api_response = api_instance.ipam_rirs_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RIR**](RIR.md)|  | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_delete**
> ipam_rirs_delete(id)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this RIR.

try:
    api_instance.ipam_rirs_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RIR. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_list**
> InlineResponse20046 ipam_rirs_list(id=id, name=name, slug=slug, is_private=is_private, description=description, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, limit=limit, offset=offset)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
is_private = 'is_private_example' # str |  (optional)
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
    api_response = api_instance.ipam_rirs_list(id=id, name=name, slug=slug, is_private=is_private, description=description, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **is_private** | **str**|  | [optional] 
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

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_partial_update**
> RIR ipam_rirs_partial_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this RIR.
data = netbox_client.RIR() # RIR | 

try:
    api_response = api_instance.ipam_rirs_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RIR. | 
 **data** | [**RIR**](RIR.md)|  | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_read**
> RIR ipam_rirs_read(id)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this RIR.

try:
    api_response = api_instance.ipam_rirs_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RIR. | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_update**
> RIR ipam_rirs_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this RIR.
data = netbox_client.RIR() # RIR | 

try:
    api_response = api_instance.ipam_rirs_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RIR. | 
 **data** | [**RIR**](RIR.md)|  | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_create**
> Role ipam_roles_create(data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
data = netbox_client.Role() # Role | 

try:
    api_response = api_instance.ipam_roles_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_delete**
> ipam_roles_delete(id)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this role.

try:
    api_instance.ipam_roles_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this role. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_list**
> InlineResponse20047 ipam_roles_list(id=id, name=name, slug=slug, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, limit=limit, offset=offset)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
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
    api_response = api_instance.ipam_roles_list(id=id, name=name, slug=slug, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_list: %s\n" % e)
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

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_partial_update**
> Role ipam_roles_partial_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this role.
data = netbox_client.Role() # Role | 

try:
    api_response = api_instance.ipam_roles_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this role. | 
 **data** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_read**
> Role ipam_roles_read(id)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this role.

try:
    api_response = api_instance.ipam_roles_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this role. | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_update**
> Role ipam_roles_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this role.
data = netbox_client.Role() # Role | 

try:
    api_response = api_instance.ipam_roles_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this role. | 
 **data** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_create**
> Service ipam_services_create(data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableService() # WritableService | 

try:
    api_response = api_instance.ipam_services_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableService**](WritableService.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_delete**
> ipam_services_delete(id)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this service.

try:
    api_instance.ipam_services_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this service. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_list**
> InlineResponse20048 ipam_services_list(id=id, name=name, protocol=protocol, port=port, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, device_id=device_id, device=device, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, protocol__n=protocol__n, port__n=port__n, port__lte=port__lte, port__lt=port__lt, port__gte=port__gte, port__gt=port__gt, device_id__n=device_id__n, device__n=device__n, virtual_machine_id__n=virtual_machine_id__n, virtual_machine__n=virtual_machine__n, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
protocol = 'protocol_example' # str |  (optional)
port = 'port_example' # str |  (optional)
created = 'created_example' # str |  (optional)
created__gte = 'created__gte_example' # str |  (optional)
created__lte = 'created__lte_example' # str |  (optional)
last_updated = 'last_updated_example' # str |  (optional)
last_updated__gte = 'last_updated__gte_example' # str |  (optional)
last_updated__lte = 'last_updated__lte_example' # str |  (optional)
q = 'q_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
device = 'device_example' # str |  (optional)
virtual_machine_id = 'virtual_machine_id_example' # str |  (optional)
virtual_machine = 'virtual_machine_example' # str |  (optional)
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
protocol__n = 'protocol__n_example' # str |  (optional)
port__n = 'port__n_example' # str |  (optional)
port__lte = 'port__lte_example' # str |  (optional)
port__lt = 'port__lt_example' # str |  (optional)
port__gte = 'port__gte_example' # str |  (optional)
port__gt = 'port__gt_example' # str |  (optional)
device_id__n = 'device_id__n_example' # str |  (optional)
device__n = 'device__n_example' # str |  (optional)
virtual_machine_id__n = 'virtual_machine_id__n_example' # str |  (optional)
virtual_machine__n = 'virtual_machine__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_services_list(id=id, name=name, protocol=protocol, port=port, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, device_id=device_id, device=device, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, protocol__n=protocol__n, port__n=port__n, port__lte=port__lte, port__lt=port__lt, port__gte=port__gte, port__gt=port__gt, device_id__n=device_id__n, device__n=device__n, virtual_machine_id__n=virtual_machine_id__n, virtual_machine__n=virtual_machine__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **protocol** | **str**|  | [optional] 
 **port** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **created__gte** | **str**|  | [optional] 
 **created__lte** | **str**|  | [optional] 
 **last_updated** | **str**|  | [optional] 
 **last_updated__gte** | **str**|  | [optional] 
 **last_updated__lte** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device** | **str**|  | [optional] 
 **virtual_machine_id** | **str**|  | [optional] 
 **virtual_machine** | **str**|  | [optional] 
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
 **protocol__n** | **str**|  | [optional] 
 **port__n** | **str**|  | [optional] 
 **port__lte** | **str**|  | [optional] 
 **port__lt** | **str**|  | [optional] 
 **port__gte** | **str**|  | [optional] 
 **port__gt** | **str**|  | [optional] 
 **device_id__n** | **str**|  | [optional] 
 **device__n** | **str**|  | [optional] 
 **virtual_machine_id__n** | **str**|  | [optional] 
 **virtual_machine__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_partial_update**
> Service ipam_services_partial_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this service.
data = netbox_client.WritableService() # WritableService | 

try:
    api_response = api_instance.ipam_services_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this service. | 
 **data** | [**WritableService**](WritableService.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_read**
> Service ipam_services_read(id)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this service.

try:
    api_response = api_instance.ipam_services_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this service. | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_update**
> Service ipam_services_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this service.
data = netbox_client.WritableService() # WritableService | 

try:
    api_response = api_instance.ipam_services_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this service. | 
 **data** | [**WritableService**](WritableService.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_create**
> VLANGroup ipam_vlan_groups_create(data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableVLANGroup() # WritableVLANGroup | 

try:
    api_response = api_instance.ipam_vlan_groups_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_delete**
> ipam_vlan_groups_delete(id)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN group.

try:
    api_instance.ipam_vlan_groups_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN group. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_list**
> InlineResponse20049 ipam_vlan_groups_list(id=id, name=name, slug=slug, description=description, q=q, region_id=region_id, region=region, site_id=site_id, site=site, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, limit=limit, offset=offset)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
description = 'description_example' # str |  (optional)
q = 'q_example' # str |  (optional)
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
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
region_id__n = 'region_id__n_example' # str |  (optional)
region__n = 'region__n_example' # str |  (optional)
site_id__n = 'site_id__n_example' # str |  (optional)
site__n = 'site__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_vlan_groups_list(id=id, name=name, slug=slug, description=description, q=q, region_id=region_id, region=region, site_id=site_id, site=site, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, description__n=description__n, description__ic=description__ic, description__nic=description__nic, description__iew=description__iew, description__niew=description__niew, description__isw=description__isw, description__nisw=description__nisw, description__ie=description__ie, description__nie=description__nie, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
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
 **region_id__n** | **str**|  | [optional] 
 **region__n** | **str**|  | [optional] 
 **site_id__n** | **str**|  | [optional] 
 **site__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_partial_update**
> VLANGroup ipam_vlan_groups_partial_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN group.
data = netbox_client.WritableVLANGroup() # WritableVLANGroup | 

try:
    api_response = api_instance.ipam_vlan_groups_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN group. | 
 **data** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_read**
> VLANGroup ipam_vlan_groups_read(id)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN group.

try:
    api_response = api_instance.ipam_vlan_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN group. | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_update**
> VLANGroup ipam_vlan_groups_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN group.
data = netbox_client.WritableVLANGroup() # WritableVLANGroup | 

try:
    api_response = api_instance.ipam_vlan_groups_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN group. | 
 **data** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_create**
> VLAN ipam_vlans_create(data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableVLAN() # WritableVLAN | 

try:
    api_response = api_instance.ipam_vlans_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVLAN**](WritableVLAN.md)|  | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_delete**
> ipam_vlans_delete(id)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN.

try:
    api_instance.ipam_vlans_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_list**
> InlineResponse20050 ipam_vlans_list(id=id, vid=vid, name=name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, region_id=region_id, region=region, site_id=site_id, site=site, group_id=group_id, group=group, role_id=role_id, role=role, status=status, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, vid__n=vid__n, vid__lte=vid__lte, vid__lt=vid__lt, vid__gte=vid__gte, vid__gt=vid__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, group_id__n=group_id__n, group__n=group__n, role_id__n=role_id__n, role__n=role__n, status__n=status__n, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
vid = 'vid_example' # str |  (optional)
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
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
status = 'status_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
vid__n = 'vid__n_example' # str |  (optional)
vid__lte = 'vid__lte_example' # str |  (optional)
vid__lt = 'vid__lt_example' # str |  (optional)
vid__gte = 'vid__gte_example' # str |  (optional)
vid__gt = 'vid__gt_example' # str |  (optional)
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
role_id__n = 'role_id__n_example' # str |  (optional)
role__n = 'role__n_example' # str |  (optional)
status__n = 'status__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_vlans_list(id=id, vid=vid, name=name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, region_id=region_id, region=region, site_id=site_id, site=site, group_id=group_id, group=group, role_id=role_id, role=role, status=status, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, vid__n=vid__n, vid__lte=vid__lte, vid__lt=vid__lt, vid__gte=vid__gte, vid__gt=vid__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, group_id__n=group_id__n, group__n=group__n, role_id__n=role_id__n, role__n=role__n, status__n=status__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **vid** | **str**|  | [optional] 
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
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **vid__n** | **str**|  | [optional] 
 **vid__lte** | **str**|  | [optional] 
 **vid__lt** | **str**|  | [optional] 
 **vid__gte** | **str**|  | [optional] 
 **vid__gt** | **str**|  | [optional] 
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
 **role_id__n** | **str**|  | [optional] 
 **role__n** | **str**|  | [optional] 
 **status__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_partial_update**
> VLAN ipam_vlans_partial_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN.
data = netbox_client.WritableVLAN() # WritableVLAN | 

try:
    api_response = api_instance.ipam_vlans_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN. | 
 **data** | [**WritableVLAN**](WritableVLAN.md)|  | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_read**
> VLAN ipam_vlans_read(id)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN.

try:
    api_response = api_instance.ipam_vlans_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN. | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_update**
> VLAN ipam_vlans_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN.
data = netbox_client.WritableVLAN() # WritableVLAN | 

try:
    api_response = api_instance.ipam_vlans_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN. | 
 **data** | [**WritableVLAN**](WritableVLAN.md)|  | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_create**
> VRF ipam_vrfs_create(data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableVRF() # WritableVRF | 

try:
    api_response = api_instance.ipam_vrfs_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVRF**](WritableVRF.md)|  | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_delete**
> ipam_vrfs_delete(id)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VRF.

try:
    api_instance.ipam_vrfs_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VRF. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_list**
> InlineResponse20051 ipam_vrfs_list(id=id, name=name, rd=rd, enforce_unique=enforce_unique, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, rd__n=rd__n, rd__ic=rd__ic, rd__nic=rd__nic, rd__iew=rd__iew, rd__niew=rd__niew, rd__isw=rd__isw, rd__nisw=rd__nisw, rd__ie=rd__ie, rd__nie=rd__nie, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
rd = 'rd_example' # str |  (optional)
enforce_unique = 'enforce_unique_example' # str |  (optional)
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
rd__n = 'rd__n_example' # str |  (optional)
rd__ic = 'rd__ic_example' # str |  (optional)
rd__nic = 'rd__nic_example' # str |  (optional)
rd__iew = 'rd__iew_example' # str |  (optional)
rd__niew = 'rd__niew_example' # str |  (optional)
rd__isw = 'rd__isw_example' # str |  (optional)
rd__nisw = 'rd__nisw_example' # str |  (optional)
rd__ie = 'rd__ie_example' # str |  (optional)
rd__nie = 'rd__nie_example' # str |  (optional)
tenant_group_id__n = 'tenant_group_id__n_example' # str |  (optional)
tenant_group__n = 'tenant_group__n_example' # str |  (optional)
tenant_id__n = 'tenant_id__n_example' # str |  (optional)
tenant__n = 'tenant__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_vrfs_list(id=id, name=name, rd=rd, enforce_unique=enforce_unique, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, created=created, created__gte=created__gte, created__lte=created__lte, last_updated=last_updated, last_updated__gte=last_updated__gte, last_updated__lte=last_updated__lte, q=q, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, rd__n=rd__n, rd__ic=rd__ic, rd__nic=rd__nic, rd__iew=rd__iew, rd__niew=rd__niew, rd__isw=rd__isw, rd__nisw=rd__nisw, rd__ie=rd__ie, rd__nie=rd__nie, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **rd** | **str**|  | [optional] 
 **enforce_unique** | **str**|  | [optional] 
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
 **rd__n** | **str**|  | [optional] 
 **rd__ic** | **str**|  | [optional] 
 **rd__nic** | **str**|  | [optional] 
 **rd__iew** | **str**|  | [optional] 
 **rd__niew** | **str**|  | [optional] 
 **rd__isw** | **str**|  | [optional] 
 **rd__nisw** | **str**|  | [optional] 
 **rd__ie** | **str**|  | [optional] 
 **rd__nie** | **str**|  | [optional] 
 **tenant_group_id__n** | **str**|  | [optional] 
 **tenant_group__n** | **str**|  | [optional] 
 **tenant_id__n** | **str**|  | [optional] 
 **tenant__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_partial_update**
> VRF ipam_vrfs_partial_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VRF.
data = netbox_client.WritableVRF() # WritableVRF | 

try:
    api_response = api_instance.ipam_vrfs_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VRF. | 
 **data** | [**WritableVRF**](WritableVRF.md)|  | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_read**
> VRF ipam_vrfs_read(id)



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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VRF.

try:
    api_response = api_instance.ipam_vrfs_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VRF. | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_update**
> VRF ipam_vrfs_update(id, data)





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
api_instance = netbox_client.IpamApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VRF.
data = netbox_client.WritableVRF() # WritableVRF | 

try:
    api_response = api_instance.ipam_vrfs_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VRF. | 
 **data** | [**WritableVRF**](WritableVRF.md)|  | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

