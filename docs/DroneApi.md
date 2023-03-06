# swagger_client.DroneApi

All URIs are relative to *http://http://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_drone**](DroneApi.md#create_drone) | **POST** /drones | Creates a new drone resource
[**delete_drone**](DroneApi.md#delete_drone) | **DELETE** /drones/{id} | Removes a drone from your collection.
[**list_drones**](DroneApi.md#list_drones) | **GET** /drones | Lists all drones in your collection.
[**read_drone**](DroneApi.md#read_drone) | **GET** /drones/{id} | Get status of a drone by id
[**update_drone**](DroneApi.md#update_drone) | **PUT** /drones/{id} | Change config for drone by id

# **create_drone**
> ModelsDrone create_drone(body)

Creates a new drone resource

Starts up a new drone with the provided plan. This will begin billing.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DroneApi(swagger_client.ApiClient(configuration))
body = swagger_client.ModelsDrone() # ModelsDrone | Drone configuration. Must include a plan. Must not include a status or cost

try:
    # Creates a new drone resource
    api_response = api_instance.create_drone(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DroneApi->create_drone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsDrone**](ModelsDrone.md)| Drone configuration. Must include a plan. Must not include a status or cost | 

### Return type

[**ModelsDrone**](ModelsDrone.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_drone**
> delete_drone(id)

Removes a drone from your collection.

Delete a drone. Any drones being removed must be already in status \"at-home\".

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DroneApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Drone ID

try:
    # Removes a drone from your collection.
    api_instance.delete_drone(id)
except ApiException as e:
    print("Exception when calling DroneApi->delete_drone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Drone ID | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drones**
> dict(str, ModelsDrone) list_drones()

Lists all drones in your collection.

List all Drones.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DroneApi(swagger_client.ApiClient(configuration))

try:
    # Lists all drones in your collection.
    api_response = api_instance.list_drones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DroneApi->list_drones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, ModelsDrone)**](ModelsDrone.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_drone**
> ModelsDrone read_drone(id)

Get status of a drone by id

Returns a detailed description of the drone's current status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DroneApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Drone ID

try:
    # Get status of a drone by id
    api_response = api_instance.read_drone(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DroneApi->read_drone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Drone ID | 

### Return type

[**ModelsDrone**](ModelsDrone.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_drone**
> ModelsDrone update_drone(body, id)

Change config for drone by id

Updates the configuration for a drone. Returns a detailed description of the drone's current status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DroneApi(swagger_client.ApiClient(configuration))
body = swagger_client.ModelsDrone() # ModelsDrone | Drone configuration. Must include a plan. Must not include a status or cost
id = 'id_example' # str | Drone ID

try:
    # Change config for drone by id
    api_response = api_instance.update_drone(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DroneApi->update_drone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsDrone**](ModelsDrone.md)| Drone configuration. Must include a plan. Must not include a status or cost | 
 **id** | **str**| Drone ID | 

### Return type

[**ModelsDrone**](ModelsDrone.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

