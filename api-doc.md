# api-doc     
#rylink     
# EOS RAM 市场     
  
**同其他api一样，所有返回都包在{"code": "10000", "message": "", "data": response}中**    
**返回单位： 所有ram都用kb，所有eos都是1eos，所有百分比都是1%**    
     
### 实时价格     
**method:**  GET     
**url：**   /api/eosram/price/real_time/     
**para：** 无     
**response:**     
```json
{     
"ram_prc":0.31,  # eos/kb     
"eos_prc":9.00,  # usd/eos     
"time_tag":13000000     #  数据获取时间，int     
}     
```
     
     
### 价格统计     
**method:**  GET     
**url：**   /api/eosram/price/info/     
**para：** 无     
**response:**     
```json
{     
"1m_chg":-0.31,       
"10m_chg": 0.13,     
"60m_chg": 0.1,     
"rsrv_ram_pct": 75.72,     
"rsrv_ram": 50.11,     
"max_ram": 60.44,     
"avg_ram_prc":0.32,     
"time_tag":13000000 ,     
}     
```
     
     
### 近期价格     
**method:**  GET     
**url：**   /api/eosram/price/history/[10m | 1h | 24h | 7d | all]/     
**para：** 无     
**response:**     
```json
{     
"records": [{     
    "price": 0.17,     
    "time_tag": 13000000,     
},…], # 29 条     
"time_tag": 13000000,     
}     
```
**error**     
```json
{  
    "code": "10601",  
    "message": "查询日期有误"  
}  
```
     
### 交易记录     
全市场最近30条交易记录     
**method:**  GET     
**url：**   /api/eosram/trade_record/latest/     
**para：** 无     
**response:**     
```json
{     
"records": [{     
    "time_tag": 13000000,     
    "name": "guojing12345",     
    "action": [0|1],        # 0:买， 1：卖     
    "eos"：10.12，     
},…], # 30 条     
"time_tag": 13000000,     
}     
```
     
     
### 大户排行     
全市场TOP30的大户     
**method:**  GET     
**url：**   /api/eosram/trade_record/tuhao/     
**para：** 无     
**response:**     
```json
{     
"records": [{     
    "rank": 1,     
    "name":"wangruixiwww",     
    "ram":1880000  # KB     
    "price":0.6,     
},…], # 30 条     
"top_100_pct":  44.33,     
"top_100_prc":  0.22,     
"time_tag": 13000000,     
}     
```
     
### 30日资金统计     
最近30日资金统计     
**method:**  GET     
**url：**   /api/eosram/trade_record/daily_info/     
**para：** 无     
**response:**     
```json
{     
"records": [{     
    "date_tag": "07-18",     
    "vol": 415.4 ,       
    "buy_vol": 207.9,     
    "sell_vol":207.5,     
    "incr_vol":-0.4,     
},…], # 30 条     
"time_tag": 1300000,  
}     
```
     
     
### 个人交易信息查询     
个人最近30条交易信息，RAM持仓，RAM持仓成本，EOS持仓     
**method:**  GET     
**url：**   /api/eosram/trade_record/user_info/{eos_account}/     
**para：** 无     
**response:**     
```json
{     
"records": [{     
    "time_tag": 13000000,     
    "name": "guojing12345",     
    "action": [0|1],        # 0:买， 1：卖     
    "eos"：10.12，     
},…], # 30 条     
"ram_vol":  44.33,  #KB     
"ram_prc":  0.2233, # eos/kb     
"eos_vol":  100.22,     
"time_tag": 13000000,     
}     
```
**error**    
```json
{  
    "code": "10601",  
    "message": "查无此人"  
}  
```
