# Blockchain数据服务

## 数据服务
说明：

数据服务包含两大类API，账户相关的API和地址相关的API。账户相关的API都是私有API，都要做数据签名和用户认证.地址相关的API是公有API,无需签名和用户认证.

a. 金额单位
    金额为1，表示1btc或者1eth等

b. 返回格式
    posts数据，返回和回调数据都是JSON格式，具体API返回数据会放在data字段中 
```
{
'code': 0表示成功，其他为出错码
'data': api具体返回数据
'message': 可读的出错信息
}
```

### 加密和用户认证
秘钥是用RSA算法生成，客户持有公钥，服务器端持有私钥。

管理员会替用户注册账户，并给用户user_id 和pub_key。

1.请求服务器时使用pub_key做数据签名

用户请求服务器需要在请求的header中带一个auth参数,auth的生成方法如下

需要的数据：user_id, pub_key, data, expire

expire是过期时间

data是需要post的数据，get时data为None

    ```python
    生成待加密字符串
    data_bytes = json.dumps(data, sort_keys=True).encode() # 对data做序列化：data升序排列，取json值
    data_sha256 = SHA256.new(data_bytes).digest() # sha256对data做hash
    expire = now().shift(minutes=30).timestamp # 30分钟后过期
    to_sign = ('%s:%s:'%(self.user_id, expire)).encode() + data_sha256 # user_id:expire:data_sha256组成待签名字符串

    使用公钥加密
    sign = pub_key.encrypt(to_sign) # 使用公钥加密待签名字符串
    auth = user_id:expire:sign.hex() # userid:expire:sign.hex连接组成auth
    ```
实例：
私钥为：
b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC2hbhi7pszx5eN6xqdGBUi4dDmNq7Cy//VoMTJVRoblwLQwZ+J\nKzi5uOfqxdDtJyso+DQzw1Oo0XZtLKSyY7CMnzjfwbRMzP5Zt4c2mvU+aL16Aat5\nriAgJqXS3tTHjulxTQMlTh9jMXc7PgqITBy4IkeVamvNdumEJ9kzldJzqwIDAQAB\nAoGAB8g6WYtJNjbN3LZA3xJjoFDzRtPC0eQxyqpg3uh67+D9CiGthC3eUCHDFok2\ni4bnZJVLtdURd11gSKe0PqcfzrK6/VJDsdMqrwjVScJfg9cihJxBrRDCZh/Lo9hl\nLQxg2LA0I1nOQx+mV9fYv8CmMoeynrn+g4VlOTVWq8hVS2UCQQC9b1LJTEK23oS9\nEPa6E7Bd/wzWygTKRmptUojjcSWvrFs5wRZ0sRtJxob6kjb6tTze4QWXyO0HzzCV\n7cbqHkktAkEA9qiUWklHYo/J0zxudeJiogUE9wpmVDxZm1Zyb/P9BQoutc+AsoJY\nm4evthAPWUHaCL9n0SNga16344Jr8+KHNwJAMg1L7mv75J1+rQXiat/w5aUSG15d\nTaS1UhVQneezcWs031mpOUPiVefimiov5KYmYy1JcQVhu4J+795XhFxkMQJBAJpy\n8voZ+o4X9UvFAnHkgNhtBi/enjbO11kyZ1P81olqV9dWiIK+pdc1vmvlYIcGeg2S\nNOK7ISv6UnEugIRlaz8CQHEBL0amsKHI8GQlkvyVYkvAOHQS5IQrAXrwwQ/1wBU2\nK6620df7f7ZqZINR50neOsVVhUJNXsW5rx0EI418P7w=\n-----END RSA PRIVATE KEY-----'
公钥为
b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2hbhi7pszx5eN6xqdGBUi4dDm\nNq7Cy//VoMTJVRoblwLQwZ+JKzi5uOfqxdDtJyso+DQzw1Oo0XZtLKSyY7CMnzjf\nwbRMzP5Zt4c2mvU+aL16Aat5riAgJqXS3tTHjulxTQMlTh9jMXc7PgqITBy4IkeV\namvNdumEJ9kzldJzqwIDAQAB\n-----END PUBLIC KEY-----'

假定user_id=1,data={"k2":"v2", "k1":"v1"}, expire=1551144911则
data_bytes=b'{"k1": "v1", "k2": "v2"}', 
data_sha256=b'\x90|\x93I\xee(?\x0c\xb6\x151b+\xc0\xbb>H#_;\t4\xd6\x9a\x83\x11\x1e5v\xa9\x0c9', 
to_sign=b'1:1551144911:\x90|\x93I\xee(?\x0c\xb6\x151b+\xc0\xbb>H#_;\t4\xd6\x9a\x83\x11\x1e5v\xa9\x0c9'
sign = b'6qKA,?\xb5\xab\x06i\xaf\xd0\\v\x81\x8f\xbe\x18.;\xd8\x8aG\xf4\xca2\xcb\x03K\xcb\xa8\x96\xc0\x8dW\x04\xa8\xf7\x08\xb8\x03\x90eXF\x04[+\\P-\x04\xe6\xd4\x10<c\xf5\xf8\xe3\xe8\xa2q\xe6\x9f\xec.\xa9e\x81\xff\x0b;\x9f>z8r\xd1\xae(\x00\x02\x12\xcbm\xfd\xdc\xe3\xf8I\xf3\xe3\\j+<\x1a\xc2\x88\xc1\xea2\x1f\xe6\x94\x14<\xaf\xc2s\xecF6~\x9e\xfb\x99(\x81\x1bJE\xb1\x1d\x8b\xeaI'
 uth='1:1551144911:14179476d8d13f6bc93de43fc4b691d6ca5f27b98b0c7a30388aed20b367f7e45ba7aeb8914001af7c8ddcdf1f726ec8959794ae2231471e4e2882372a8c51b78149016488a04322191c4cf2bba18a0369fe01ad99b7007b202253baeb71b11e19daefbd046a02adfa4b2d277356d618710d46bddaf876ae4fd095bc0ddbdbc9'   

2.服务器发送通知时, 客户端使用pub_key校验数据发送方身份

服务器通知客户端时，会使用如上相同的方法构造一个待签名的字符串，然后使用自己的私钥签名。客户端用自己的公钥校验就可以了

服务器回调时也会带上auth头，客户端从中取出expire和sign，data是服务器post的数据

```python
assert now > expire # 校验超时
data_bytes = json.dumps(data, sort_keys=True).encode() # 同上对data做序列化
data_sha256 = SHA256.new(data_bytes).digest() # 同上使用sha256对data做hash
to_sign = ('%s:%s:'%(user_id, expire)).encode() + data_sha256 # 同上获取待签名字符串，服务器的user_id固定为0
sign_hex = bytes.fromhex(sign) # sign从hex转为bytes
pub_key_verify(pub_key, to_sign, sign_hex) # 公钥校验签名
```




### 账户API
1. 账户注册

    现阶段由管理员手动注册,注册成功后会给用户user_id 和 pub_key,用于身份认证和加密

2. 账户配置查询

path:   /user/conf

return:
```json
{
'user_id',
'trx_notify_url',
'description',
}
```

3. 账户配置修改

path:   /user/conf/set

post data:

```json
{'trx_notify_url',
'description'
}
```

return:
```json
{
'user_id',
'trx_notify_url',
'description',
}
```

4. 账户地址查询

path:   /user/address/{coin_name}

return:
```json
{
'address': [...]
}
```

5. 账户地址注册

path: /user/address/add/{coin_name}

post data:
```json
{'address': [...]}
```

return:
```json
{
'count'
}
```

6. 账户地址删除

path: /user/address/rm/{coin_name}

post data:
```json
{'address': [...]}
```

return:
```json
{
'count'
}
```

7. 账户余额查询

path: /user/balance/{coin_name}

return:
```json
{
'coin_name1': amount1,
'coin_name2': amount2
...
}
```

8. 账户交易推送

```
{
'coin_name',
'block_height', 
'block_hash'
'block_timstamp'
'tx_hash', 
'is_in': 是转入还是转出, 
'fee', 
'from':[{'address', 'amount'}], 
'to':[{'address', 'amount', 'memo'}]
}
```

9. 账户区块链浏览器

开发中

### 地址API
1. 地址余额查询

path: 	/{address}/balance/{coin_name}  
 
return:
```json
{
'coin_name':
'address':
'amount': 
}
```
2. 地址流水查询

path: 	/{address}/transactions/{coin_name}
 
return:
```json
{
'coin_name'
'address'
'transactions':
[
{
'block_height', 
'block_hash'
'block_timstamp'
'tx_hash', 
'is_in': 是转入还是转出, 
'fee', 
'from':[{'address', 'amount'}], 
'to':[{'address', 'amount', 'memo'}]
},
...]
}
```
3. 地址utxo查询，用于交易构造

path:	/{address}/utxos/{coin_name}
 
return:
```json
{
'coin_name'
'address'
utxos:
[
{

'tx_hash':,
'tx_out_n':, 
'amount'
},
...]
}
```

5. 地址nonce查询，用于交易构造

开发中

