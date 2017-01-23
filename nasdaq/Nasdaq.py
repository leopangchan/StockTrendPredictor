import re
import xml.etree.cElementTree as ElementTree
import sys
from os import listdir
from os.path import isfile, join
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import cgi
import json
import requests
import datetime
import time


def get_sentiment(name, date, open_path):
    #day = str(time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())).split(".")[0]
    CONST = 28800
    DAY = 86400 #24 hour frame
    day = int(time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())) - CONST

    #convert from string to timestamp

    score = 0
    count = 0

    with open(open_path,'r') as data_file:
        data = json.load(data_file)

    for x in data['result']['docs']:
        if x['timestamp'] - DAY <= day and day <= x['timestamp'] + DAY :
            for y in x['source']['enriched']['url']['entities']:
                score += (y['sentiment']['score'])
                count+=1

    if count == 0:
        return count
    return score/count

def getData(url):
    print("X")
    j=11
    #for i in range(6,6):
    #for j in range[11]:
    values = {'_Token': 'BC2B181CF93B441D8C6342120EB0C971',
              'Symbols': 'MSFT',
              'StartDateTime': '9/1/2016 00:00:00.000',
              'EndDateTime': '9/30/2016 23:59:59.999',
              'MarketCenters': 'Q',
              'TradePrecision': 'Hour',
              'TradePeriod': '1'}
    r = requests.post(url, data=values)
    #print(r.status_code, r.reason)  # HTTP
    f = open('C:/Users/adity/Downloads/NLP/Project_ArticleR/Test/Test_out.txt', 'a')
    f.write(str(r.content))
    #print("search results : ", r.content)
    #print("Done")

def parseData(url,val):
    f=open(url,'r')
    data = json.load(f)
    for key,value in data.items():
        if val == key:
            first=''
            final=''
            for m in value:
                for k, v in m.items():
                    if k=='first':
                        if first=='':
                            first=v
                    if k=='end':
                        if v=='0':
                            continue
                        else:
                            final=v
            #print(key)
            #print("Difference: ",float(first)-float(final))
            return (key + " "+ str(float(first)))

def main(argv):
    if (len(argv) < 4):
        print("Usage : Python Nasdaq.py data_dir Company date")
        return

    data_dir = argv[1]
    url = 'http://ws.nasdaqdod.com/v1/NASDAQAnalytics.asmx/GetSummarizedTrades'

    #with open(data_dir, 'r') as data_f:
        #text = data_f.read()

    #getData(url)

    x=argv[2]
    date=argv[3]

    if(x=='APPLE'):
        comp='AAPL'
    elif (x == 'AMAZON'):
        comp = 'AMZN'
    elif (x == 'ADOBE'):
        comp = 'ADBE'
    elif (x == 'MICROSOFT'):
        comp = 'MSFT'
    elif (x == 'FACEBOOK'):
        comp = 'FB'

    str_NASDAQ = parseData(data_dir +"/"+x+"/"+comp+"_NASDAQ.json", date)
        #str_SENTIMENT = get_sentiment(comp,date,data_dir +"/"+x+"/"+comp++"_IBM.json")

        #print(str_NASDAQ+"sentiment: "+str_SENTIMENT)
    f=open('output.txt','w')
    f.write(str_NASDAQ)

if __name__ == "__main__":
    main(sys.argv)

