# ModelsDrone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | [**ModelsDroneCost**](ModelsDroneCost.md) |  | [optional] 
**id** | **str** |  | [optional] 
**instruction_index** | **int** | InstructionIndex provides a numeric index into the current instruction of the drone&#x27;s plan that is being executed. | 
**name** | **str** | Name of the drone. For your purposes. | 
**plan** | **list[str]** | Plan for drone to fly. Must be at least one instruction long and the last instruction must be a landing command. | [optional] 
**status** | **str** | Status of the drone. Must be one of: at-home, starting-up, en-route, landing, missing | [optional] 
**type** | **str** | Type of drone. Must be one of: quadcopter-small, quadcopter-large, plane-small, single-rotor-large | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

