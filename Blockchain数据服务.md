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
管理员会替用户注册账户，并给用户user_id 和pub_key

1.请求服务器时使用pub_key做数据签名

    用户请求服务器需要在请求的header中带一个auth参数,auth的生成方法如下

    需要的数据：user_id, pub_key, data, expire

    expire是过期时间

    data是需要post的数据，get时data为None

    ```python
    生成待加密字符串
    data_bytes = json.dumps(data, sort_keys=True).encode() # data升序排列，取json值
    data_sha256 = sha256(data_bytes) # sha256对data做hash
    expire = now().shift(minutes=30).timestamp # 30分钟后过期
    to_sign = ('%s:%s:'%(self.user_id, expire)).encode() + data_sha256 # user_id:expire:data_sha256组成待签名字符串

    使用公钥加密
    sign = pub_key.encrypt(to_sign) # 使用公钥加密待签名字符串
    auth = user_id:expire:sign # userid:expire:sign连接组成auth
    ```
    

2.服务器发送通知时, 客户端使用pub_key校验数据发送方身份

    服务器通知客户端时，会使用如上相同的方法构造一个待签名的字符串，然后使用自己的私钥签名。客户端用自己的公钥校验就可以了


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

