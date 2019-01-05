# 节点服务API
### 路径
http://{内网IP}:6000/{api_path}

### 请求出错
统一返回
{"error":  "error message"}

### 区块高度
/block/best/height/

{ "height": 123 }

### 区块信息
/block/{height}/
	
```
{
"block": 
	{"height", "hash", "parent_hash", "timestamp","token_type"},
"trxs":[
	{"trx_id", 
	"fee", 
	"from":[{"address", "value",], 
	"to":["address", "value"}
]
}
实例：
{
  "block": {
    "height": 816806,
    "hash": "000c76a63ff954b19527375ebf523255528ba2d8",
    "parent_hash": "000c76a54a36b2903d6bdbbccf06beffc02c6d0b",
    "timestamp": 1546652090,
    "token_type": "HX"
  },
  "trxs": [
    {
      "trx_id": "b06b3d8e650b6743ab60024d5e7fb63e0fb60fca",
      "fee": 0.001,
      "from": [
        {
          "address": "HXNWziPVC4VdwM2seoKPoxDHqtCgkRcCiKE7",
          "value": 100
        }
      ],
      "to": [
        {
          "address": "HXNUamFdK3tedSMtybR7MUyMMLUHVhZjCzqc",
          "value": 100
        }
      ]
    }
  ]
}

```

### 钱包余额
/balance/


["address",  amount]

实例

[‘HXNUZSB27eoKGki79mioGrS5YyKxdXEzvQu’, 123]

### 发送交易
/transfer/{to_address}/{amount}/

{"trx_id":123}
