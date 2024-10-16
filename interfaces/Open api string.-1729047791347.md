
### Open api string.

维护人：bin.chen

#### URL

- 本地环境: `POST` http://172.16.70.107:7700/mock/default/openApi/get2


描述：

ContentType：`application/x-www-form-urlencoded;charset=UTF-8`

#### 请求参数

##### Query Parameter

| 名称 | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| header | object | 否 |  | 请求头. |  |
|   └ requestId | string | 否 | - | 请求ID,由系统生成，允许为空. |  |
| id | string | 否 | - | 请求的主键ID. |  |
| name | string | 否 | - | 请求的名字. | 12 |
| aLong | int64 | 否 | - | No comments found. | 0 |
| localDate | string | 否 | - | No comments found. | yyyy-MM-dd |
| localDateTime | string | 否 | - | No comments found. | yyyy-MM-dd HH:mm:ss |
| localTime | string | 否 | - | No comments found. | HH:mm:ss |

#### 响应参数

| 名称 | 类型 | 必填 | 最大长度 | 描述 | 示例值 |
| --- | --- | --- | --- | --- | --- |
| header | object | 否 |  | 响应头. |  |
|   └ requestId | string | 否 | - | 请求ID,由系统生成，允许为空. |  |
|   └ errorCode | string | 否 | - | 错误码. |  |
|   └ errorMsg | string | 否 | - | 错误信息. |  |
| data | object | 否 |  | 数据. |  |
|   └ header | object | 否 |  | 请求头. |  |
|     └ requestId | string | 否 | - | 请求ID,由系统生成，允许为空. |  |
|   └ id | string | 否 | - | 请求的主键ID. |  |
|   └ name | string | 否 | - | 请求的名字. | 12 |
|   └ aLong | int64 | 否 | - | No comments found. | 0 |
|   └ localDate | string | 否 | - | No comments found. | yyyy-MM-dd |
|   └ localDateTime | string | 否 | - | No comments found. | yyyy-MM-dd HH:mm:ss |
|   └ localTime | string | 否 | - | No comments found. | HH:mm:ss |

#### 响应示例

```
{
    "header": {
        "requestId": "string",
        "errorCode": "string",
        "errorMsg": "string"
    },
    "data": {
        "header": {
            "requestId": "string"
        },
        "id": "string",
        "name": "12",
        "aLong": 0,
        "localDate": "yyyy-MM-dd",
        "localDateTime": "yyyy-MM-dd HH:mm:ss",
        "localTime": "HH:mm:ss"
    }
}
```

#### 错误码

无
