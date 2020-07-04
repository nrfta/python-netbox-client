# WritableDeviceInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**device** | **int** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**enabled** | **bool** |  | [optional] 
**lag** | **int** |  | [optional] 
**mtu** | **int** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**mgmt_only** | **bool** | This interface is used only for out-of-band management | [optional] 
**description** | **str** |  | [optional] 
**connected_endpoint_type** | **str** |  | [optional] 
**connected_endpoint** | **dict(str, str)** |  Return the appropriate serializer for the type of connected object.  | [optional] 
**connection_status** | **bool** |  | [optional] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**mode** | **str** |  | [optional] 
**untagged_vlan** | **int** |  | [optional] 
**tagged_vlans** | **list[int]** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**count_ipaddresses** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


