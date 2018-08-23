# ry-doc


同其他api一样，所有返回都包在{"code": "10000", "message": "", "data": response}中
返回单位： 所有ram都用kb，所有eos都是1eos，所有百分比都是1%

# 钱包配置
- 需要开放chain_api_plugin, wallet_api_plugin, history_api_plugin
- 调小钱包unlock的time，默认15分钟，改为1秒
- 修改标准的keos的，支持钱包创建时设置密码(这个已经做了)

# 交易类
第一期交易都用cleos去实现，第二期采用 构建 签名 广播的模式,
参考：https://steemit.com/eos/@noprom/using-eos-rpc-api-to-transfer-eos

### 转账
cleos transfer <转出账户名> <转入账户名> '0.0001 EOS' '<备注信息>' -p <转出账户名>
### 收款
无API
### 资源交易
- 内存交易
cleos system buyram <付钱账户名> <获得ram账户名> "0.01 EOS” -p <付钱账户名>
cleos system sellram <出售ram账户名> 4000 -p <出售ram账户名>
上面的4000的单位是bytes
- cpu交易, 网络交易
第一个eos是买网络，第二个买CPU,不买写0
cleos system delegatebw <付钱账户名> <获得资源账户名> "0.5 EOS" "0 EOS" -p <付钱账户名>
cleos system undelegatebw <出售资源账户名> <获得资源账户名> "0.5 EOS" "0 EOS" -p <出售资源账户名>


# 查询类
### 账户信息
chain_api: /v1/chain/get_currency_balance -X POST -d '{"code":"eosio.token","account":"hoowalletpro", "symbol":"EOS"}'
### 账户交易记录
chain_api: /v1/history/get_actions -X POST -d {"account_name":"hoowalletpro","pos":1,"offset":2} 
### 账户cpu,ram,net信息
chain_api: /v1/chain/get_account -X POST -d '{"account_name":"hoowalletpro"}'
### EOS汇率
从火币获取
### ram价格，使用率
chain_api: /v1/chain/get_table_rows -X POST -d '{"scope":"eosio", "code":"eosio", "table":"rammarket", "json": true}'
### getTableRows
chain_api: /v1/chain/get_table_rows -X POST -d '{"scope":"inita", "code":"currency", "table":"account", "json": true}'

# 钱包类
统一使用用户eos account name 作为wellet name
### 钱包创建
默认不支持设置password，我们已经修改标准的keosd，让他支持设置password
chain_api: /v1/wallet/create -X POST -d '["eos_account_name", "password"]'
### 钱包导入
chain_api: /v1/wallet/import_key -X POST -d '["eos_account_name", "private_key"]'
### 钱包解锁
chain_api: /v1/wallet/unlock -X POST -d '["eos_account_name", "password"]'
### 钱包签名
chain_api: 先用cleos实现转账，无需签名

