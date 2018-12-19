# Blockchain数据服务

### 钱包
1. 公司账户注册
2. 地址创建
3. 地址管理
4. 发送服务
 
### 数据服务
说明：
a. 所有金额都使用各币种的基础单位，1btc， 1eth 等，不是最小单位
b. 返回封装
返回和回调数据都是JSON格式，具体API返回数据会放在data字段中 
```
{
'code': 0表示成功，其他为出错码
'data': api具体返回数据
'message': 可读的出错信息
}
```

1. 公司账户注册
2. 地址注册
3. 公司注册地址查询
4. 地址余额查询
path: 	/{coin_name}/balance/{address}/  
 
return:
```json
{
'coin_name':
'address':
'amount': 
}
```
5. 地址流水查询
path: 	/{coin_name}/transactions/{address}/ 
 
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
6. 地址utxo查询，用于交易构造
path:	/{coin_name}/utxos/{address}/
 
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
7. 地址nonce查询，用于交易构造

8. 地址变动推送
post数据格式
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
9. 公司区块链浏览器

