from nsepy import get_history
from nse import Nse
import datetime
from time import sleep
f=open('symbols of nifty 500.txt','r')
sym=f.read()
codes=list(sym.split())
avg={}
max_vol={}
min_vol={}
error_sym=[]
#Historical Data
for i in codes:
    data=get_history(symbol=i, start=datetime.date.today()-datetime.timedelta(30), end=datetime.date.today())
    vol=[x for x in data['Volume']]
    if len(vol)!=0:
        avg_vol=sum(vol)/len(vol)
        avg[i]=avg_vol
        max_vol[i]=max(vol)
        min_vol[i]=min(vol)
    else:
        error_sym.append(codes.pop(codes.index(i)))
while True:
    nse=Nse()
    highest_vol=[]
    for i in codes:
        live_data=nse.live(i)
        try:
            if live_data["totalTradedVolume"]>avg[i] and live_data["totalTradedVolume"]>max_vol[i]:
                print('Yes:',i)
                highest_vol.append(i)
        except KeyError:
            error_sym.append(i)
    watchlist={}
    delivery={}
    del i
    for i in highest_vol:
        live_data=nse.live(i)
        if live_data["totalTradedVolume"]>max_vol[i]:
            watchlist[i]=[live_data["lastPrice"],live_data["high52"]]
            delivery[i]=live_data['deliveryToTradedQuantity']

    #Watchlist
    # while True:
        
    #     price=nse.live(watchlist[0])
    #     print(price['lastPrice'])
    #     if price['lastPrice']>price["high52"]:
    #         print('BUY!!!!!!!!!')
    #     sleep(1)
    print('Watchlist:',watchlist)
    print('Delivery Percent:',delivery)
