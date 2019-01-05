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


# 业务

### 入账
1. 获取当前高度
2. 如果当前高度是100，你们要求的确认数是6，获取块95的信息
3. 过滤块95中to_address为本系统用户地址的交易，即为转入交易
4. 记录当前处理到95号块，重复上述过程，处理96号块

### 出账
1. 调用发送交易，发送订单，并将返回的交易id保存到发送订单
2. 在上述入账中处理块的循环里，当获取到一个块时，检查该交易是否打包到块中，如果已打包出账成功。
