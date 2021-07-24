---
title: ajoumeow REST API Documentation
description: 미유미유 REST API 문서
date: 2021-02-21
layout: docs
---
[서비스 소개](https://luftaquila.io/works/ajoumeow/){:target="_blank"}{:class='link'}  
<br>

# Auth API
----------
<br>
#### [POST] /auth/login
Logins with ID. Returns JWT token and user data, feeding statistics.

  * **URL Parameters**  
    _None_

  * **Data Parameters**  
      `id: [integer]`
    
  * **Required Headers**  
    _None_
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: [JWT TOKEN],
          data: {
            user: {
              ID: [integer],
              name: [string],
              role: [string]
            },
            semister: [string],
            statistics: [Array]
          }
        }
      ```
    * Error:
      * Code: `400`
      * Content:
      ```yaml
        {
          stat: "error",
          msg: "등록되지 않은 학번입니다.",
          data: "ERR_NOT_REGISTERED"
        }
      ```
      
----------
<br>
#### [POST] /auth/autologin
Logins with JWT Token. Returns user data and feeding statistics.

  * **URL Parameters**  
    _None_

  * **Data Parameters**  
  	_None_
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: {
            user: {
              ID: [integer],
              name: [string],
              role: [string]
            },
            semister: [string],
            statistics: [Array]
          }
        }
      ```
    * Error:
      * Code: `400`
      * Content:
      ```yaml
        {
          stat: "error",
          msg: "등록되지 않은 학번입니다.",
          data: "ERR_NOT_REGISTERED"
        }
      ```
      
<br>
# Record API
-------------
<br>
#### [GET] /record
Returns feeding application records between `startDate` and `endDate`.

  * **URL Parameters**  
    `startDate: [yyyy-mm-dd]`  
    `endDate: [yyyy-mm-dd]`

  * **Data Parameters**  
  	_None_
    
  * **Required Headers**  
    _None_
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: [{ UPDATE_TIME: [update time] }],
          data: [Array]
        }
      ```
      
------------
<br>
#### [POST] /record
Makes new feeding application record.

  * **URL Parameters**  
  _None_

  * **Data Parameters**  
    `ID: [integer]`  
    `name: [string]`  
	  `date: [string]`  
	  `course: [string]`

  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `201`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: { 
          	affectedRows: [integer],
            insertId: [integer],
            warningStatus: [integer]
          }
        }
      ```
    * Error:
      * Code: `400`  
      * Content:
      ```yaml
        {
          stat: "error",
          msg: "이미 신청되었습니다.",
          data: "ERR_DUP_ENTRY"
        }
      ```
      
--------------
<br>
#### [DELETE] /record
Deletes existing feeding application record.

  * **URL Parameters**  
  _None_

  * **Data Parameters**  
    `ID: [integer]`  
    `name: [string]`  
	  `date: [string]`  
	  `course: [string]`
     
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `204`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: { 
          	affectedRows: [integer],
            insertId: [integer],
            warningStatus: [integer]
          }
        }
      ```

-----------
<br>
#### [GET] /record/statistics
Returns statistics data of total activities.

  * **URL Parameters**  
    `type: [ summary | this_feeding | this_total | prev_feeding | total_total | custom_total ]`  
    `value: [yyyy-mm-dd|yyyy-mm-dd]`  
    `value` is required only when type is `custom_total`. Start date and end date separated with `|`

  * **Data Parameters**  
  	_None_
    
  * **Required Headers**  
    _None_
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: [Array]
        }
      ```
    * Error:
      * Code: `400`  
      * Content:
      ```yaml
        {
          stat: "error",
          msg: "유효하지 않은 통계 유형입니다.",
          data: "ERR_INVALID_TYPE"
        }
      ```

-----------
<br>
#### [GET] /record/log
Returns log data of server activities.

  * **URL Parameters**  
    `level: [string]`  
    `type: [string]`  
    `level` and `type` is string separated with `|`

  * **Data Parameters**  
  	_None_
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: [Array]
        }
      ```

<br>
# Verify API
-------------
<br>
#### [GET] /verify
Returns feeding application records and activity verification records between `startDate` and `endDate`.

  * **URL Parameters**  
    `startDate: [yyyy-mm-dd]`  
    `endDate: [yyyy-mm-dd]`

  * **Data Parameters**  
  	_None_
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: [Array],
          data: [Array]
        }
      ```
      
------------
<br>
#### [POST] /verify
Makes new activity verification record.

  * **URL Parameters**  
  _None_

  * **Data Parameters**  
    `data: [string]`  
    * `data` is a stringified Array of `payload`s.  
      `payload: { ID: [integer], date: [string], name: [string], course: [string], score: [string] }`

  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `201`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: [Array]
        }
      ```
      
--------------
<br>
#### [DELETE] /verify
Deletes existing activity verification record.

  * **URL Parameters**  
  _None_

  * **Data Parameters**  
    `data: [string]`  
    * `data` is a stringified Array of `payload`s.  
      `payload: { ID: [integer], date: [string], name: [string], course: [string] }`

  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `204`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: [Array]
        }
      ```

-----------
<br>
#### [GET] /verify/latest
Returns latest verification's date.

  * **URL Parameters**  
  	_None_

  * **Data Parameters**  
  	_None_
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: [string]
        }
      ```
      
------------
<br>
#### [GET] /verify/1365
Returns generated 1365 verification pdf document.

  * **URL Parameters**  
    `month: [yyyy-mm]`  
    `namelist: [string]`

  * **Data Parameters**  
  	_None_
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**  
    `stream`
      
------------
<br>
# Settings API
-------------
<br>
#### [GET] /settings/:name
Returns value of requested settings.

  * **URL Parameters**  
    `name: [string]`  

  * **Data Parameters**  
  	_None_
    
  * **Required Headers**  
  	_None_
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: [string]
        }
      ```

-----------
<br>
#### [PUT] /settings/:name
Updates value of settings.

  * **URL Parameters**  
    `name: [string]`  

  * **Data Parameters**  
    `data: [string]`  
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: { 
          	affectedRows: [integer],
            insertId: [integer],
            warningStatus: [integer]
          }
        }
      ```

<br>
# Users API
-------------
<br>
#### [GET] /users/list
Returns list of members that matches `semister` parameter.  
If `semister` value is _all_, returns list of namelist tables.

  * **URL Parameters**  
    `semister: [string]`  

  * **Data Parameters**  
    _None_
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: [Array]
        }
      ```
      
----------
<br>
#### [GET] /users/name
Returns info of single user by name.

  * **URL Parameters**  
    `query: [string]`  

  * **Data Parameters**  
    _None_
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: [Array]
        }
      ```
      
----------
<br>
#### [POST] /users/id
Add new user.

  * **URL Parameters**  
    _None_

  * **Data Parameters**  
    `단과대학: [string]`  
    `학과: [string]`  
    `학번: [string]`  
    `이름: [string]`  
    `전화번호: [string]`  
    `생년월일: [string]`  
    `1365 아이디: [string]`  
    `가입 학기: [string]`  
    `직책: [string]`  
    `new: [bool]`  
    
  * **Required Headers**  
    _None_
    
  * **Response**
    * Success:
      * Code: `201`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: { 
          	affectedRows: [integer],
            insertId: [integer],
            warningStatus: [integer]
          }
        }
      ```
    * Error:
      * Code: `400`  
      * Content:
      ```yaml
        {
          stat: "error",
          msg: "지난 학기에 가입한 적이 있습니다.<br>기존 회원으로 등록해 주세요.",
          data: "ERR_REGISTERED_BEFORE"
        }
      ```
      * Code: `400`  
      * Content:
      ```yaml
        {
          stat: "error",
          msg: "기존 회원이 아닙니다.<br>신입 회원으로 등록해 주세요.",
          data: "ERR_NEVER_REGISTERED"
        }
      ```
      * Code: `400`  
      * Content:
      ```yaml
        {
          stat: "error",
          msg: "이미 이번 학기 회원으로 등록되셨습니다.'",
          data: "ERR_ALREADY_REGISTERED"
        }
      ```
      
----------
<br>
#### [PUT] /users/id
Updates user info.

  * **URL Parameters**  
    _None_

  * **Data Parameters**  
    `college: [string]`  
    `department: [string]`  
    `name: [string]`  
    `phone: [string]`  
    `birthday: [string]`  
    `1365ID: [string]`  
    `role: [string]`  
    `register: [string]`  
    `ID: [integer]`  
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: { 
          	affectedRows: [integer],
            insertId: [integer],
            warningStatus: [integer]
          }
        }
      ```
      
----------
<br>
#### [DELETE] /users/id
Deletes user info.

  * **URL Parameters**  
    _None_

  * **Data Parameters**  
    `ID: [integer]`  
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `204`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: { 
          	affectedRows: [integer],
            insertId: [integer],
            warningStatus: [integer]
          }
        }
      ```
    * Error:
      * Code: `400`  
      * Content:
      ```yaml
        {
          stat: "error",
          msg: "No matching ID",
          data: "ERR_NO_MATCHING_ID"
        }
      ```
    
-----------  
<br>
#### [GET] /users/register
Returns list of register applications that matches `semister` parameter.  
If `semister` value is _all_, returns list of register namelist tables.

  * **URL Parameters**  
    `semister: [string]`  

  * **Data Parameters**  
    _None_
    
  * **Required Headers**  
    `x-access-token: [JWT TOKEN]`
    
  * **Response**
    * Success:
      * Code: `200`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: [Array]
        }
      ```
    
-----------  
<br>
#### [POST] /users/register
Add new register application.

  * **URL Parameters**  
    _None_

  * **Data Parameters**  
    `단과대학: [string]`  
    `학과: [string]`  
    `학번: [string]`  
    `이름: [string]`  
    `전화번호: [string]`  
    `생년월일: [string]`  
    `1365 아이디: [string]`  
    `가입 학기: [string]`  
    `직책: [string]`  
    `new: [bool]`  
    
  * **Required Headers**  
    _None_
    
  * **Response**
    * Success:
      * Code: `201`  
      * Content:
      ```yaml
        {
          stat: "success",
          msg: null,
          data: { 
          	affectedRows: [integer],
            insertId: [integer],
            warningStatus: [integer]
          }
        }
      ```
    * Error:
      * Code: `400`  
      * Content:
      ```yaml
        {
          stat: "error",
          msg: "이미 가입 신청하셨습니다!<br>조금만 기다리시면 임원진이 연락을 드릴 거에요.",
          data: "ERR_ALREADY_REGISTERED"
        }
      ```
