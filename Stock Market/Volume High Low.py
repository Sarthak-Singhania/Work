from nsepy import get_history
from nse import Nse
import datetime
import pandas as pd
nse=Nse()
f=open('nifty 50 symbols.txt','r')
sym_read=f.read()
sym=sym_read.split()
error_sym=[]
watchlist={}
while True:
    for i in sym:
        live_data=nse.live(i)
        data=get_history(symbol=i,start=datetime.date.today()-datetime.timedelta(1),end=datetime.date.today()-datetime.timedelta(1))
        vol=[x for x in data['Volume']]
        high=[x for x in data['High']]
        low=[x for x in data['Low']]
        try:
            if live_data['totalTradedVolume']>vol[0]:
                if live_data['lastPrice']>high[0] or live_data['lastPrice']<low[0]:
                    watchlist[i]=[live_data['lastPrice'],high[0],low[0]]
        except: error_sym.append(i)
    if len(watchlist)!=0:
        print(pd.DataFrame.from_dict(data=watchlist,orient='index',columns=['LTP','High','Low']))
    else:
       print('Nada')