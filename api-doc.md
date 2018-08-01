# api-doc   
#rylink   
# EOS RAM 市场   
   
### 实时价格   
**method:**  GET   
**url：**	/api/eosram/price/real_time   
**para：** 无   
**response:**   
{   
‘ram_price’:0.31,  //	eos/kb   
‘time_tag’:13000000 	//	数据获取时间，int   
}   
   
   
### 价格统计   
**method:**  GET   
**url：**	/api/eosram/price/info/   
**para：**无   
**response:**   
{   
‘15m_chg’:-0.31,     
‘1h_chg’: 0.13,   
‘24h_chg’: 0.1,   
’rsrv_ram_pct’: 75.72,   
?   
‘avg_ram_prc’:0.32,   
‘time_tag’:13000000 ,   
}   
   
   
### 近期价格   
**method:**  GET   
**url：**	/api/eosram/price/history/[2h | 1d | 7d | 30d]/   
**para：**无   
**response:**   
{   
records: [{   
	‘price’: 0.17,   
	‘time_tag’: 13000000,   
},…], // 30 条   
’time_tag’:	13000000,   
}   
   
   
### 交易记录   
全市场最近30条交易记录   
**method:**  GET   
**url：**	/api/eosram/trade_record/latest/   
**para：**无   
**response:**   
{   
records: [{   
	‘time_tag’: 13000000,   
	‘name’: guojing12345,   
	‘action’: [0|1],		// 0:买， 1：卖   
	‘eos’：10.12，   
},…], // 30 条   
’time_tag’:	13000000,   
}   
   
   
### 大户排行   
全市场TOP30的大户   
**method:**  GET   
**url：**	/api/eosram/trade_record/tuhao/   
**para：**无   
**response:**   
{   
records: [{   
	‘rank’: 1,   
	‘name’:’wangruixiwww’,   
	‘ram’:1.88,	// GB   
	‘price’:0.6,   
},…], // 30 条   
’top_100_pct’:	44.33,   
’top_100_prc’: 	0.22,   
’time_tag’:	13000000,   
}   
   
### 资金统计   
今日资金统计   
**method:**  GET   
**url：**	/api/eosram/trade_record/today_info/   
**para：**无   
**response:**   
{   
‘hst_vol’: 251.9,	 //	万EOS   
‘today_sell_vol’:115.1,   
‘today_buy_vol’:136.8,   
’today_incr_vol’: -130,   
’time_tag’:	13000000,   
}   
   
### 资金统计   
最近30日资金统计   
**method:**  GET   
**url：**	/api/eosram/trade_record/daily_info/   
**para：**无   
**response:**   
{   
records: [{   
	‘date_tag’: ’07-18’,   
	‘vol’: 415.4 ,     
	‘buy_vol’: 207.9,   
	‘sell_vol’:207.5,   
	‘incr_vol’:-0.4,   
},…], // 30 条   
}   
   
   
### 个人交易信息查询   
个人最近30条交易信息，RAM持仓，RAM持仓成本，EOS持仓   
**method:**  GET   
**url：**	/api/eosram/trade_record/personal_info/{user_id}/   
**para：**无   
**response:**   
{   
records: [{   
	‘time_tag’: 13000000,   
	‘name’: guojing12345,   
	‘action’: [0|1],		// 0:买， 1：卖   
	‘eos’：10.12，   
},…], // 30 条   
‘ram_vol’:	44.33, 	//KB   
‘ram_prc’:	0.2233,	// eos/kb   
‘eos_vol’: 	100.22,   
’time_tag’:	13000000,   
}   