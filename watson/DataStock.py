import re
import xml.etree.cElementTree as ElementTree
import sys
from os import listdir
from os.path import isfile, join
#from urllib.parse import urlencode
#from urllib.request import Request, urlopen
import cgi
import json
import requests
def getData(url):
    for i in range(6):
        for j in range(1,12):
            values = {'_Token': 'BC2B181CF93B441D8C6342120EB0C971',
                      'Symbols': 'AAPL,ADBE',
                      'StartDateTime': str(j)+'/1/201'+str(i)+' 00:00:00.000',
                      'EndDateTime': str(j)+'/28/201'+str(i)+' 23:59:59.999',
                      'MarketCenters': 'Q',
                      'TradePrecision': 'Hour',
                      'TradePeriod': '1'}
            r = requests.post(url, values)
            print(r.status_code, r.reason)  # HTTP
            f = open('DataStock', 'w')
            f.write(str(r.content))
            #print("search results : ", r.content)
            print("Done")

def main(argv):
    url = 'http://ws.nasdaqdod.com/v1/NASDAQAnalytics.asmx/GetSummarizedTrades'
    getData(url)

if __name__ == "__main__":
    main(sys.argv)