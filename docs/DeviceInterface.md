# DeviceInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**device** | [**NestedDevice**](NestedDevice.md) |  | 
**name** | **str** |  | 
**type** | [**Type2**](Type2.md) |  | 
**enabled** | **bool** |  | [optional] 
**lag** | [**NestedInterface**](NestedInterface.md) |  | [optional] 
**mtu** | **int** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**mgmt_only** | **bool** | This interface is used only for out-of-band management | [optional] 
**description** | **str** |  | [optional] 
**connected_endpoint_type** | **str** |  | [optional] 
**connected_endpoint** | **dict(str, str)** |  Return the appropriate serializer for the type of connected object.  | [optional] 
**connection_status** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**mode** | [**Mode**](Mode.md) |  | [optional] 
**untagged_vlan** | [**NestedVLAN**](NestedVLAN.md) |  | [optional] 
**tagged_vlans** | [**list[NestedVLAN]**](NestedVLAN.md) |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**count_ipaddresses** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


