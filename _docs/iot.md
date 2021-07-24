---
title: iot REST API Documentation
description: IoT 허브 REST API 문서
date: 2021-07-06
layout: docs
---
[서비스 소개](https://luftaquila.io/works/iot/){:target="_blank"}{:class='link'}  
<br>

# #Auth API
----------
<br>

### [POST] /api/login
Make login with ID and password. Returns JWT.

#### Parameters  
  
| Name | Type | In | Description |
|:----:|:----:|:--:|:------------|
|`id`|string|body|`Required`. Login ID for control hub.|
|`pw`|string|body|`Required`. Login password for control hub.|

<br>
#### Response
  * **Success**:
    * Code: `201`  
    * Content: `<JWT|string>`
  * **Error**:
  
| Code | Content |
|:----:|:--------|
|401|`authentication failed`|

<br>

----------

<br>

### [POST] /api/autologin
Make login JWT. Returns id

#### Parameters
  
| Name | Type | In | Description |
|:----:|:----:|:--:|:------------|
|`jwt`|string|header|`Required`. Previously signed JWT for control hub.|
    
<br>
#### Response
  * **Success**:
    * Code: `201`  
    * Content: 
    ```yaml
      {
        id: [string],
        exp: [integer],
        iat: [integer]
      }
    ```
  * **Error**:
  
| Code | Content |
|:----:|:--------|
|401|`authentication failed`|
      
<br>
# #Device API
----------
<br>

### [GET] /device/all
Get registered devices list

#### Parameters
  
| Name | Type | In | Description |
|:----:|:----:|:--:|:------------|
|`jwt`|string|header|`Required`. Previously signed JWT for control hub.|

<br>
#### Response
  * **Success**:
    * Code: `200`  
    * Content:
    ```yaml
      [
        {
          id: <device id|string>,
          status: <device status|json>,
          online: <divice online status|bool>
        }
        ...
      ]
    ```

  * **Error**:
  
| Code | Content |
|:----:|:--------|
|401|`authentication failed`|
      
<br>

----------

<br>

### [GET] /device/:deviceId
Get device status.

#### Parameters: _None_

#### Response
  * **Success**:
    * Code: `200`  
    * Content:
    ```yaml
      {
        id: <device id|string>,
        status: <device status|json>,
        online: <divice online status|bool>
      }
    ```
  
  * **Error**:

| Code | Content |
|:----:|:--------|
|400|`Invalid request parameters`|
|404|`device <deviceId> not found`|

<br>
    
#### Response's < device status > contents     

| Device Type | Content |
|:-----------:|:--------|
|passiveSwitch|`{ power: [bool] }`|
|passiveTactSwitch|`{ }`|
|ledDisplay| not supported |

<br>

----------

<br>

### [POST] /device/:deviceId
Write device status.

#### Parameters:

* **Common**  
All requests requires jwt token.
  
| Name | Type | In | Description |
|:----:|:----:|:--:|:------------|
|`jwt`|string|header|`Required`. Previously signed JWT for control hub.|

<br>
* **passiveSwitch**

| Name | Type | In | Description |
|:----:|:----:|:--:|:------------|
|`toggle`|bool|body|If `true`, toggles device's power status.|
|`power`|bool|body|Set device's power status.|

<br>
* **passiveTactSwitch**

| Name | Type | In | Description |
|:----:|:----:|:--:|:------------|
|`push`|bool|body|If `true`, pushes switch of device|

<br>
#### Response
  * **Success**:
    * Code: `201`  
    * Content: `{ status: <device status|json> }`
  * **Error**:
  
| Code | Content |
|:----:|:--------|
|400|`Invalid request parameters`|
|401|`device <deviceId> not found`|
|404|`device <deviceId> not found`|
|503|`device <deviceId> is offline`|

