# Rack

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**facility_id** | **str** | Locally-assigned identifier | [optional] 
**display_name** | **str** |  | [optional] 
**site** | [**NestedSite**](NestedSite.md) |  | 
**group** | [**NestedRackGroup**](NestedRackGroup.md) |  | [optional] 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**status** | [**Status4**](Status4.md) |  | [optional] 
**role** | [**NestedRackRole**](NestedRackRole.md) |  | [optional] 
**serial** | **str** |  | [optional] 
**asset_tag** | **str** | A unique tag used to identify this rack | [optional] 
**type** | [**Type6**](Type6.md) |  | [optional] 
**width** | [**Width**](Width.md) |  | [optional] 
**u_height** | **int** | Height in rack units | [optional] 
**desc_units** | **bool** | Units are numbered top-to-bottom | [optional] 
**outer_width** | **int** | Outer dimension of rack (width) | [optional] 
**outer_depth** | **int** | Outer dimension of rack (depth) | [optional] 
**outer_unit** | [**OuterUnit**](OuterUnit.md) |  | [optional] 
**comments** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**custom_fields** | **object** |  | [optional] 
**created** | **date** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**device_count** | **int** |  | [optional] 
**powerfeed_count** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


