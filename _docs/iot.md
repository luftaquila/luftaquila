---
title: iot REST API Documentation
description: IoT 허브 REST API 문서
date: 2021-07-06
layout: post
---
[서비스 소개](https://luftaquila.io/works/iot/){:target="_blank"}{:class='link'}  
<br>

# #Auth API
----------
<br>
#### [POST] /api/login
Make login with ID and password. Returns JWT.

* **Parameters**  
  
| Name | Type | In | Description |
|:----:|:----:|:--:|:------------|
|`id`|string|body|`Required`. Login ID for control hub.|
|`pw`|string|body|`Required`. Login password for control hub.|
    
<br>
* **Response**
  * Success:
    * Code: `201`  
    * Content: `[JWT]`
  * Error:
    * Code: `401`
    * Content: _None_
      
----------
<br>
#### [POST] /api/autologin
Make login JWT. Returns id

* **Parameters**  
  
| Name | Type | In | Description |
|:----:|:----:|:--:|:------------|
|`jwt`|string|body|`Required`. Previously signed JWT for control hub.|
    
<br>
* **Response**
  * Success:
    * Code: `201`  
    * Content: 
    ```yaml
      {
        id: [string],
        exp: [integer],
        iat: [integer]
      }
    ```
  * Error:
    * Code: `401`
    * Content: _None_
      
<br>
# #Device API
----------
<br>
#### [GET] /device/:deviceId
Get device status.

* **Parameters**: _None_

<br>
* **Response**
  * Success:
    * Code: `201`  
    * Content:  
      
| Device Type | Type | Content |
|:-----------:|:----:|:--------|
|passiveSwitch|string|`{ power: [bool] }`|
  
* 
  * Error:
    * Code: `404`
    * Content: _None_
      
----------
<br>
#### [POST] /device/:deviceId
Write device status.

* **Parameters**:
###### passiveSwitch  

| Name | Type | In | Description |
|:----:|:----:|:--:|:------------|
|`toggle`|bool|body|If `true`, toggles device's power status.|
|`power`|bool|body|Set device's power status.|

    
<br>
* **Response**
  * Success:
    * Code: `201`  
    * Content: _None_
  * Error:
    * Code: `404`
    * Content: _None_
