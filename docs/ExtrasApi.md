# netbox_client.ExtrasApi

All URIs are relative to *https://netbox.us-east-2.ops.underline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extras_config_contexts_create**](ExtrasApi.md#extras_config_contexts_create) | **POST** /extras/config-contexts/ | 
[**extras_config_contexts_delete**](ExtrasApi.md#extras_config_contexts_delete) | **DELETE** /extras/config-contexts/{id}/ | 
[**extras_config_contexts_list**](ExtrasApi.md#extras_config_contexts_list) | **GET** /extras/config-contexts/ | 
[**extras_config_contexts_partial_update**](ExtrasApi.md#extras_config_contexts_partial_update) | **PATCH** /extras/config-contexts/{id}/ | 
[**extras_config_contexts_read**](ExtrasApi.md#extras_config_contexts_read) | **GET** /extras/config-contexts/{id}/ | 
[**extras_config_contexts_update**](ExtrasApi.md#extras_config_contexts_update) | **PUT** /extras/config-contexts/{id}/ | 
[**extras_custom_field_choices_list**](ExtrasApi.md#extras_custom_field_choices_list) | **GET** /extras/_custom_field_choices/ | 
[**extras_custom_field_choices_read**](ExtrasApi.md#extras_custom_field_choices_read) | **GET** /extras/_custom_field_choices/{id}/ | 
[**extras_export_templates_create**](ExtrasApi.md#extras_export_templates_create) | **POST** /extras/export-templates/ | 
[**extras_export_templates_delete**](ExtrasApi.md#extras_export_templates_delete) | **DELETE** /extras/export-templates/{id}/ | 
[**extras_export_templates_list**](ExtrasApi.md#extras_export_templates_list) | **GET** /extras/export-templates/ | 
[**extras_export_templates_partial_update**](ExtrasApi.md#extras_export_templates_partial_update) | **PATCH** /extras/export-templates/{id}/ | 
[**extras_export_templates_read**](ExtrasApi.md#extras_export_templates_read) | **GET** /extras/export-templates/{id}/ | 
[**extras_export_templates_update**](ExtrasApi.md#extras_export_templates_update) | **PUT** /extras/export-templates/{id}/ | 
[**extras_graphs_create**](ExtrasApi.md#extras_graphs_create) | **POST** /extras/graphs/ | 
[**extras_graphs_delete**](ExtrasApi.md#extras_graphs_delete) | **DELETE** /extras/graphs/{id}/ | 
[**extras_graphs_list**](ExtrasApi.md#extras_graphs_list) | **GET** /extras/graphs/ | 
[**extras_graphs_partial_update**](ExtrasApi.md#extras_graphs_partial_update) | **PATCH** /extras/graphs/{id}/ | 
[**extras_graphs_read**](ExtrasApi.md#extras_graphs_read) | **GET** /extras/graphs/{id}/ | 
[**extras_graphs_update**](ExtrasApi.md#extras_graphs_update) | **PUT** /extras/graphs/{id}/ | 
[**extras_image_attachments_create**](ExtrasApi.md#extras_image_attachments_create) | **POST** /extras/image-attachments/ | 
[**extras_image_attachments_delete**](ExtrasApi.md#extras_image_attachments_delete) | **DELETE** /extras/image-attachments/{id}/ | 
[**extras_image_attachments_list**](ExtrasApi.md#extras_image_attachments_list) | **GET** /extras/image-attachments/ | 
[**extras_image_attachments_partial_update**](ExtrasApi.md#extras_image_attachments_partial_update) | **PATCH** /extras/image-attachments/{id}/ | 
[**extras_image_attachments_read**](ExtrasApi.md#extras_image_attachments_read) | **GET** /extras/image-attachments/{id}/ | 
[**extras_image_attachments_update**](ExtrasApi.md#extras_image_attachments_update) | **PUT** /extras/image-attachments/{id}/ | 
[**extras_object_changes_list**](ExtrasApi.md#extras_object_changes_list) | **GET** /extras/object-changes/ | 
[**extras_object_changes_read**](ExtrasApi.md#extras_object_changes_read) | **GET** /extras/object-changes/{id}/ | 
[**extras_reports_list**](ExtrasApi.md#extras_reports_list) | **GET** /extras/reports/ | 
[**extras_reports_read**](ExtrasApi.md#extras_reports_read) | **GET** /extras/reports/{id}/ | 
[**extras_reports_run**](ExtrasApi.md#extras_reports_run) | **POST** /extras/reports/{id}/run/ | 
[**extras_scripts_list**](ExtrasApi.md#extras_scripts_list) | **GET** /extras/scripts/ | 
[**extras_scripts_read**](ExtrasApi.md#extras_scripts_read) | **GET** /extras/scripts/{id}/ | 
[**extras_tags_create**](ExtrasApi.md#extras_tags_create) | **POST** /extras/tags/ | 
[**extras_tags_delete**](ExtrasApi.md#extras_tags_delete) | **DELETE** /extras/tags/{id}/ | 
[**extras_tags_list**](ExtrasApi.md#extras_tags_list) | **GET** /extras/tags/ | 
[**extras_tags_partial_update**](ExtrasApi.md#extras_tags_partial_update) | **PATCH** /extras/tags/{id}/ | 
[**extras_tags_read**](ExtrasApi.md#extras_tags_read) | **GET** /extras/tags/{id}/ | 
[**extras_tags_update**](ExtrasApi.md#extras_tags_update) | **PUT** /extras/tags/{id}/ | 


# **extras_config_contexts_create**
> ConfigContext extras_config_contexts_create(data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableConfigContext() # WritableConfigContext | 

try:
    api_response = api_instance.extras_config_contexts_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableConfigContext**](WritableConfigContext.md)|  | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_delete**
> extras_config_contexts_delete(id)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this config context.

try:
    api_instance.extras_config_contexts_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config context. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_list**
> InlineResponse20037 extras_config_contexts_list(id=id, name=name, is_active=is_active, q=q, region_id=region_id, region=region, site_id=site_id, site=site, role_id=role_id, role=role, platform_id=platform_id, platform=platform, cluster_group_id=cluster_group_id, cluster_group=cluster_group, cluster_id=cluster_id, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, role_id__n=role_id__n, role__n=role__n, platform_id__n=platform_id__n, platform__n=platform__n, cluster_group_id__n=cluster_group_id__n, cluster_group__n=cluster_group__n, cluster_id__n=cluster_id__n, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, tag__n=tag__n, limit=limit, offset=offset)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
is_active = 'is_active_example' # str |  (optional)
q = 'q_example' # str |  (optional)
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
platform_id = 'platform_id_example' # str |  (optional)
platform = 'platform_example' # str |  (optional)
cluster_group_id = 'cluster_group_id_example' # str |  (optional)
cluster_group = 'cluster_group_example' # str |  (optional)
cluster_id = 'cluster_id_example' # str |  (optional)
tenant_group_id = 'tenant_group_id_example' # str |  (optional)
tenant_group = 'tenant_group_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
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
region_id__n = 'region_id__n_example' # str |  (optional)
region__n = 'region__n_example' # str |  (optional)
site_id__n = 'site_id__n_example' # str |  (optional)
site__n = 'site__n_example' # str |  (optional)
role_id__n = 'role_id__n_example' # str |  (optional)
role__n = 'role__n_example' # str |  (optional)
platform_id__n = 'platform_id__n_example' # str |  (optional)
platform__n = 'platform__n_example' # str |  (optional)
cluster_group_id__n = 'cluster_group_id__n_example' # str |  (optional)
cluster_group__n = 'cluster_group__n_example' # str |  (optional)
cluster_id__n = 'cluster_id__n_example' # str |  (optional)
tenant_group_id__n = 'tenant_group_id__n_example' # str |  (optional)
tenant_group__n = 'tenant_group__n_example' # str |  (optional)
tenant_id__n = 'tenant_id__n_example' # str |  (optional)
tenant__n = 'tenant__n_example' # str |  (optional)
tag__n = 'tag__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_config_contexts_list(id=id, name=name, is_active=is_active, q=q, region_id=region_id, region=region, site_id=site_id, site=site, role_id=role_id, role=role, platform_id=platform_id, platform=platform, cluster_group_id=cluster_group_id, cluster_group=cluster_group, cluster_id=cluster_id, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, tag=tag, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, region_id__n=region_id__n, region__n=region__n, site_id__n=site_id__n, site__n=site__n, role_id__n=role_id__n, role__n=role__n, platform_id__n=platform_id__n, platform__n=platform__n, cluster_group_id__n=cluster_group_id__n, cluster_group__n=cluster_group__n, cluster_id__n=cluster_id__n, tenant_group_id__n=tenant_group_id__n, tenant_group__n=tenant_group__n, tenant_id__n=tenant_id__n, tenant__n=tenant__n, tag__n=tag__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **is_active** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **platform_id** | **str**|  | [optional] 
 **platform** | **str**|  | [optional] 
 **cluster_group_id** | **str**|  | [optional] 
 **cluster_group** | **str**|  | [optional] 
 **cluster_id** | **str**|  | [optional] 
 **tenant_group_id** | **str**|  | [optional] 
 **tenant_group** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
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
 **region_id__n** | **str**|  | [optional] 
 **region__n** | **str**|  | [optional] 
 **site_id__n** | **str**|  | [optional] 
 **site__n** | **str**|  | [optional] 
 **role_id__n** | **str**|  | [optional] 
 **role__n** | **str**|  | [optional] 
 **platform_id__n** | **str**|  | [optional] 
 **platform__n** | **str**|  | [optional] 
 **cluster_group_id__n** | **str**|  | [optional] 
 **cluster_group__n** | **str**|  | [optional] 
 **cluster_id__n** | **str**|  | [optional] 
 **tenant_group_id__n** | **str**|  | [optional] 
 **tenant_group__n** | **str**|  | [optional] 
 **tenant_id__n** | **str**|  | [optional] 
 **tenant__n** | **str**|  | [optional] 
 **tag__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_partial_update**
> ConfigContext extras_config_contexts_partial_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this config context.
data = netbox_client.WritableConfigContext() # WritableConfigContext | 

try:
    api_response = api_instance.extras_config_contexts_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config context. | 
 **data** | [**WritableConfigContext**](WritableConfigContext.md)|  | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_read**
> ConfigContext extras_config_contexts_read(id)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this config context.

try:
    api_response = api_instance.extras_config_contexts_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config context. | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_update**
> ConfigContext extras_config_contexts_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this config context.
data = netbox_client.WritableConfigContext() # WritableConfigContext | 

try:
    api_response = api_instance.extras_config_contexts_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config context. | 
 **data** | [**WritableConfigContext**](WritableConfigContext.md)|  | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_custom_field_choices_list**
> extras_custom_field_choices_list()





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))

try:
    api_instance.extras_custom_field_choices_list()
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_custom_field_choices_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_custom_field_choices_read**
> extras_custom_field_choices_read(id)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.extras_custom_field_choices_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_custom_field_choices_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_create**
> ExportTemplate extras_export_templates_create(data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
data = netbox_client.WritableExportTemplate() # WritableExportTemplate | 

try:
    api_response = api_instance.extras_export_templates_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_delete**
> extras_export_templates_delete(id)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this export template.

try:
    api_instance.extras_export_templates_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_list**
> InlineResponse20038 extras_export_templates_list(id=id, content_type=content_type, name=name, template_language=template_language, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, content_type__n=content_type__n, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, template_language__n=template_language__n, limit=limit, offset=offset)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)
name = 'name_example' # str |  (optional)
template_language = 'template_language_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
content_type__n = 'content_type__n_example' # str |  (optional)
name__n = 'name__n_example' # str |  (optional)
name__ic = 'name__ic_example' # str |  (optional)
name__nic = 'name__nic_example' # str |  (optional)
name__iew = 'name__iew_example' # str |  (optional)
name__niew = 'name__niew_example' # str |  (optional)
name__isw = 'name__isw_example' # str |  (optional)
name__nisw = 'name__nisw_example' # str |  (optional)
name__ie = 'name__ie_example' # str |  (optional)
name__nie = 'name__nie_example' # str |  (optional)
template_language__n = 'template_language__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_export_templates_list(id=id, content_type=content_type, name=name, template_language=template_language, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, content_type__n=content_type__n, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, template_language__n=template_language__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **template_language** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **content_type__n** | **str**|  | [optional] 
 **name__n** | **str**|  | [optional] 
 **name__ic** | **str**|  | [optional] 
 **name__nic** | **str**|  | [optional] 
 **name__iew** | **str**|  | [optional] 
 **name__niew** | **str**|  | [optional] 
 **name__isw** | **str**|  | [optional] 
 **name__nisw** | **str**|  | [optional] 
 **name__ie** | **str**|  | [optional] 
 **name__nie** | **str**|  | [optional] 
 **template_language__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_partial_update**
> ExportTemplate extras_export_templates_partial_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this export template.
data = netbox_client.WritableExportTemplate() # WritableExportTemplate | 

try:
    api_response = api_instance.extras_export_templates_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 
 **data** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_read**
> ExportTemplate extras_export_templates_read(id)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this export template.

try:
    api_response = api_instance.extras_export_templates_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_update**
> ExportTemplate extras_export_templates_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this export template.
data = netbox_client.WritableExportTemplate() # WritableExportTemplate | 

try:
    api_response = api_instance.extras_export_templates_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 
 **data** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_create**
> Graph extras_graphs_create(data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
data = netbox_client.Graph() # Graph | 

try:
    api_response = api_instance.extras_graphs_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Graph**](Graph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_delete**
> extras_graphs_delete(id)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this graph.

try:
    api_instance.extras_graphs_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_list**
> InlineResponse20039 extras_graphs_list(id=id, type=type, name=name, template_language=template_language, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, type__n=type__n, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, template_language__n=template_language__n, limit=limit, offset=offset)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
type = 'type_example' # str |  (optional)
name = 'name_example' # str |  (optional)
template_language = 'template_language_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
type__n = 'type__n_example' # str |  (optional)
name__n = 'name__n_example' # str |  (optional)
name__ic = 'name__ic_example' # str |  (optional)
name__nic = 'name__nic_example' # str |  (optional)
name__iew = 'name__iew_example' # str |  (optional)
name__niew = 'name__niew_example' # str |  (optional)
name__isw = 'name__isw_example' # str |  (optional)
name__nisw = 'name__nisw_example' # str |  (optional)
name__ie = 'name__ie_example' # str |  (optional)
name__nie = 'name__nie_example' # str |  (optional)
template_language__n = 'template_language__n_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_graphs_list(id=id, type=type, name=name, template_language=template_language, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, type__n=type__n, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, template_language__n=template_language__n, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **template_language** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **type__n** | **str**|  | [optional] 
 **name__n** | **str**|  | [optional] 
 **name__ic** | **str**|  | [optional] 
 **name__nic** | **str**|  | [optional] 
 **name__iew** | **str**|  | [optional] 
 **name__niew** | **str**|  | [optional] 
 **name__isw** | **str**|  | [optional] 
 **name__nisw** | **str**|  | [optional] 
 **name__ie** | **str**|  | [optional] 
 **name__nie** | **str**|  | [optional] 
 **template_language__n** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_partial_update**
> Graph extras_graphs_partial_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this graph.
data = netbox_client.Graph() # Graph | 

try:
    api_response = api_instance.extras_graphs_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 
 **data** | [**Graph**](Graph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_read**
> Graph extras_graphs_read(id)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this graph.

try:
    api_response = api_instance.extras_graphs_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_update**
> Graph extras_graphs_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this graph.
data = netbox_client.Graph() # Graph | 

try:
    api_response = api_instance.extras_graphs_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 
 **data** | [**Graph**](Graph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_create**
> ImageAttachment extras_image_attachments_create(data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
data = netbox_client.ImageAttachment() # ImageAttachment | 

try:
    api_response = api_instance.extras_image_attachments_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageAttachment**](ImageAttachment.md)|  | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_delete**
> extras_image_attachments_delete(id)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this image attachment.

try:
    api_instance.extras_image_attachments_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_list**
> InlineResponse20040 extras_image_attachments_list(limit=limit, offset=offset)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_image_attachments_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_partial_update**
> ImageAttachment extras_image_attachments_partial_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this image attachment.
data = netbox_client.ImageAttachment() # ImageAttachment | 

try:
    api_response = api_instance.extras_image_attachments_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 
 **data** | [**ImageAttachment**](ImageAttachment.md)|  | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_read**
> ImageAttachment extras_image_attachments_read(id)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this image attachment.

try:
    api_response = api_instance.extras_image_attachments_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_update**
> ImageAttachment extras_image_attachments_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this image attachment.
data = netbox_client.ImageAttachment() # ImageAttachment | 

try:
    api_response = api_instance.extras_image_attachments_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 
 **data** | [**ImageAttachment**](ImageAttachment.md)|  | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_object_changes_list**
> InlineResponse20041 extras_object_changes_list(id=id, user=user, user_name=user_name, request_id=request_id, action=action, changed_object_type=changed_object_type, changed_object_id=changed_object_id, object_repr=object_repr, q=q, time=time, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, user__n=user__n, user_name__n=user_name__n, user_name__ic=user_name__ic, user_name__nic=user_name__nic, user_name__iew=user_name__iew, user_name__niew=user_name__niew, user_name__isw=user_name__isw, user_name__nisw=user_name__nisw, user_name__ie=user_name__ie, user_name__nie=user_name__nie, action__n=action__n, changed_object_type__n=changed_object_type__n, changed_object_id__n=changed_object_id__n, changed_object_id__lte=changed_object_id__lte, changed_object_id__lt=changed_object_id__lt, changed_object_id__gte=changed_object_id__gte, changed_object_id__gt=changed_object_id__gt, object_repr__n=object_repr__n, object_repr__ic=object_repr__ic, object_repr__nic=object_repr__nic, object_repr__iew=object_repr__iew, object_repr__niew=object_repr__niew, object_repr__isw=object_repr__isw, object_repr__nisw=object_repr__nisw, object_repr__ie=object_repr__ie, object_repr__nie=object_repr__nie, limit=limit, offset=offset)



Retrieve a list of recent changes.

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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
user = 'user_example' # str |  (optional)
user_name = 'user_name_example' # str |  (optional)
request_id = 'request_id_example' # str |  (optional)
action = 'action_example' # str |  (optional)
changed_object_type = 'changed_object_type_example' # str |  (optional)
changed_object_id = 'changed_object_id_example' # str |  (optional)
object_repr = 'object_repr_example' # str |  (optional)
q = 'q_example' # str |  (optional)
time = 'time_example' # str |  (optional)
id__n = 'id__n_example' # str |  (optional)
id__lte = 'id__lte_example' # str |  (optional)
id__lt = 'id__lt_example' # str |  (optional)
id__gte = 'id__gte_example' # str |  (optional)
id__gt = 'id__gt_example' # str |  (optional)
user__n = 'user__n_example' # str |  (optional)
user_name__n = 'user_name__n_example' # str |  (optional)
user_name__ic = 'user_name__ic_example' # str |  (optional)
user_name__nic = 'user_name__nic_example' # str |  (optional)
user_name__iew = 'user_name__iew_example' # str |  (optional)
user_name__niew = 'user_name__niew_example' # str |  (optional)
user_name__isw = 'user_name__isw_example' # str |  (optional)
user_name__nisw = 'user_name__nisw_example' # str |  (optional)
user_name__ie = 'user_name__ie_example' # str |  (optional)
user_name__nie = 'user_name__nie_example' # str |  (optional)
action__n = 'action__n_example' # str |  (optional)
changed_object_type__n = 'changed_object_type__n_example' # str |  (optional)
changed_object_id__n = 'changed_object_id__n_example' # str |  (optional)
changed_object_id__lte = 'changed_object_id__lte_example' # str |  (optional)
changed_object_id__lt = 'changed_object_id__lt_example' # str |  (optional)
changed_object_id__gte = 'changed_object_id__gte_example' # str |  (optional)
changed_object_id__gt = 'changed_object_id__gt_example' # str |  (optional)
object_repr__n = 'object_repr__n_example' # str |  (optional)
object_repr__ic = 'object_repr__ic_example' # str |  (optional)
object_repr__nic = 'object_repr__nic_example' # str |  (optional)
object_repr__iew = 'object_repr__iew_example' # str |  (optional)
object_repr__niew = 'object_repr__niew_example' # str |  (optional)
object_repr__isw = 'object_repr__isw_example' # str |  (optional)
object_repr__nisw = 'object_repr__nisw_example' # str |  (optional)
object_repr__ie = 'object_repr__ie_example' # str |  (optional)
object_repr__nie = 'object_repr__nie_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_object_changes_list(id=id, user=user, user_name=user_name, request_id=request_id, action=action, changed_object_type=changed_object_type, changed_object_id=changed_object_id, object_repr=object_repr, q=q, time=time, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, user__n=user__n, user_name__n=user_name__n, user_name__ic=user_name__ic, user_name__nic=user_name__nic, user_name__iew=user_name__iew, user_name__niew=user_name__niew, user_name__isw=user_name__isw, user_name__nisw=user_name__nisw, user_name__ie=user_name__ie, user_name__nie=user_name__nie, action__n=action__n, changed_object_type__n=changed_object_type__n, changed_object_id__n=changed_object_id__n, changed_object_id__lte=changed_object_id__lte, changed_object_id__lt=changed_object_id__lt, changed_object_id__gte=changed_object_id__gte, changed_object_id__gt=changed_object_id__gt, object_repr__n=object_repr__n, object_repr__ic=object_repr__ic, object_repr__nic=object_repr__nic, object_repr__iew=object_repr__iew, object_repr__niew=object_repr__niew, object_repr__isw=object_repr__isw, object_repr__nisw=object_repr__nisw, object_repr__ie=object_repr__ie, object_repr__nie=object_repr__nie, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_object_changes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **user** | **str**|  | [optional] 
 **user_name** | **str**|  | [optional] 
 **request_id** | **str**|  | [optional] 
 **action** | **str**|  | [optional] 
 **changed_object_type** | **str**|  | [optional] 
 **changed_object_id** | **str**|  | [optional] 
 **object_repr** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **time** | **str**|  | [optional] 
 **id__n** | **str**|  | [optional] 
 **id__lte** | **str**|  | [optional] 
 **id__lt** | **str**|  | [optional] 
 **id__gte** | **str**|  | [optional] 
 **id__gt** | **str**|  | [optional] 
 **user__n** | **str**|  | [optional] 
 **user_name__n** | **str**|  | [optional] 
 **user_name__ic** | **str**|  | [optional] 
 **user_name__nic** | **str**|  | [optional] 
 **user_name__iew** | **str**|  | [optional] 
 **user_name__niew** | **str**|  | [optional] 
 **user_name__isw** | **str**|  | [optional] 
 **user_name__nisw** | **str**|  | [optional] 
 **user_name__ie** | **str**|  | [optional] 
 **user_name__nie** | **str**|  | [optional] 
 **action__n** | **str**|  | [optional] 
 **changed_object_type__n** | **str**|  | [optional] 
 **changed_object_id__n** | **str**|  | [optional] 
 **changed_object_id__lte** | **str**|  | [optional] 
 **changed_object_id__lt** | **str**|  | [optional] 
 **changed_object_id__gte** | **str**|  | [optional] 
 **changed_object_id__gt** | **str**|  | [optional] 
 **object_repr__n** | **str**|  | [optional] 
 **object_repr__ic** | **str**|  | [optional] 
 **object_repr__nic** | **str**|  | [optional] 
 **object_repr__iew** | **str**|  | [optional] 
 **object_repr__niew** | **str**|  | [optional] 
 **object_repr__isw** | **str**|  | [optional] 
 **object_repr__nisw** | **str**|  | [optional] 
 **object_repr__ie** | **str**|  | [optional] 
 **object_repr__nie** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_object_changes_read**
> ObjectChange extras_object_changes_read(id)



Retrieve a list of recent changes.

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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this object change.

try:
    api_response = api_instance.extras_object_changes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_object_changes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this object change. | 

### Return type

[**ObjectChange**](ObjectChange.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_reports_list**
> extras_reports_list()



Compile all reports and their related results (if any). Result data is deferred in the list view.

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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))

try:
    api_instance.extras_reports_list()
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_reports_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_reports_read**
> extras_reports_read(id)



Retrieve a single Report identified as \"<module>.<report>\".

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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.extras_reports_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_reports_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_reports_run**
> extras_reports_run(id)



Run a Report and create a new ReportResult, overwriting any previous result for the Report.

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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.extras_reports_run(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_reports_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_scripts_list**
> extras_scripts_list()





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))

try:
    api_instance.extras_scripts_list()
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_scripts_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_scripts_read**
> extras_scripts_read(id)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.extras_scripts_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_scripts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_create**
> Tag extras_tags_create(data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
data = netbox_client.Tag() # Tag | 

try:
    api_response = api_instance.extras_tags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_delete**
> extras_tags_delete(id)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tag.

try:
    api_instance.extras_tags_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tag. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_list**
> InlineResponse20042 extras_tags_list(id=id, name=name, slug=slug, color=color, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, color__n=color__n, color__ic=color__ic, color__nic=color__nic, color__iew=color__iew, color__niew=color__niew, color__isw=color__isw, color__nisw=color__nisw, color__ie=color__ie, color__nie=color__nie, limit=limit, offset=offset)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
color = 'color_example' # str |  (optional)
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
color__n = 'color__n_example' # str |  (optional)
color__ic = 'color__ic_example' # str |  (optional)
color__nic = 'color__nic_example' # str |  (optional)
color__iew = 'color__iew_example' # str |  (optional)
color__niew = 'color__niew_example' # str |  (optional)
color__isw = 'color__isw_example' # str |  (optional)
color__nisw = 'color__nisw_example' # str |  (optional)
color__ie = 'color__ie_example' # str |  (optional)
color__nie = 'color__nie_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_tags_list(id=id, name=name, slug=slug, color=color, q=q, id__n=id__n, id__lte=id__lte, id__lt=id__lt, id__gte=id__gte, id__gt=id__gt, name__n=name__n, name__ic=name__ic, name__nic=name__nic, name__iew=name__iew, name__niew=name__niew, name__isw=name__isw, name__nisw=name__nisw, name__ie=name__ie, name__nie=name__nie, slug__n=slug__n, slug__ic=slug__ic, slug__nic=slug__nic, slug__iew=slug__iew, slug__niew=slug__niew, slug__isw=slug__isw, slug__nisw=slug__nisw, slug__ie=slug__ie, slug__nie=slug__nie, color__n=color__n, color__ic=color__ic, color__nic=color__nic, color__iew=color__iew, color__niew=color__niew, color__isw=color__isw, color__nisw=color__nisw, color__ie=color__ie, color__nie=color__nie, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **color** | **str**|  | [optional] 
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
 **color__n** | **str**|  | [optional] 
 **color__ic** | **str**|  | [optional] 
 **color__nic** | **str**|  | [optional] 
 **color__iew** | **str**|  | [optional] 
 **color__niew** | **str**|  | [optional] 
 **color__isw** | **str**|  | [optional] 
 **color__nisw** | **str**|  | [optional] 
 **color__ie** | **str**|  | [optional] 
 **color__nie** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_partial_update**
> Tag extras_tags_partial_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tag.
data = netbox_client.Tag() # Tag | 

try:
    api_response = api_instance.extras_tags_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tag. | 
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_read**
> Tag extras_tags_read(id)



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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tag.

try:
    api_response = api_instance.extras_tags_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tag. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_update**
> Tag extras_tags_update(id, data)





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
api_instance = netbox_client.ExtrasApi(netbox_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tag.
data = netbox_client.Tag() # Tag | 

try:
    api_response = api_instance.extras_tags_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tag. | 
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

