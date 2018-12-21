# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:20:49 2018

Introducing TuShare Library to save my ass on data source issues.

@author: szlsd
"""

class TuShareCon():
    import tushare as ts

    def __init__(self, token):
        # initializing with token
        self.token = token
        self.ts.set_token(self.token)
        self.pro = self.ts.pro_api()

    def GetStkInfo(self):
        # Get basic information of stocks
        return(self.pro.stock_basic())
    
    def GetTradingDate(self, exchange = 'SSE', tradedates = ['20180101','20180630']):    
        # Get trading days given exchange name.
        return(self.pro.query('trade_cal', start_date = tradedates[0], end_date = tradedates[1]))
    
    def GetStkList(self, exchg = '', liststatus = 'L', fields = 'ts_code, symbol,name,area,industry,list_date'):
        # Get listing stocks
        return(self.pro.query('stock_basic', exchange = exchg, fields = fields))

    def GetBarStk(self, freq = 'daily', ts_code = None, trade_date = None, tradedates = ['20180101', '20180630']):
        
        if ts_code == None:
            return(self.pro.query(freq, trade_date = trade_date))
        else:
            return(self.pro.query(freq, ts_code = ts_code, start_date = tradedates[0],  end_date = tradedates[1]))
            
    
    #Todo 1. 财务报表数据接入
    #Todo 1.1 经典因子数据录入
    
    def GetAdjBarStk(self, ts_code = None, adj = 'hfq', trade_date = None, tradedates = ['20180101', '20180630']):
        # 市值因子相关 - 复权市值
        return(self.ts.pro_bar(pro_api = self.pro, ts_code = ts_code, adj = adj, start_date = tradedates[0], end_date = tradedates[1]))
    
    def GetDailyBasicStk(self, mode = 'daily_basic', ts_code = '', 
                         trade_date = '20180726', 
                         fields = 'ts_code,trade_date,turnover_rate,volume_ratio,pe,pb,ps,ps_ttm,total_share,float_share,free_share,total_mv,circ_mv'):
        
        return(self.pro.query(mode, ts_code = ts_code, trade_date = trade_date, fields = fields))
        
    #Todo 1.2 其他财务数据录入
    