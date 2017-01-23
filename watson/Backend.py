import sys
import datetime
import time
import json

def get_sentiment(name, date):
    #day = str(time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())).split(".")[0]
    CONST = 28800
    DAY = 86400 #24 hour frame
    day = int(time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y").timetuple())) - CONST

    #convert from string to timestamp

    score = 0
    count = 0

    if name == "AAPL":
        open_path = "/home/kid/Github/Oracle/watson/apple/apple.json"
    elif name == "FB":
        open_path = "/home/kid/Github/Oracle/watson/facebook/facebook.json"
    elif name == "AMZN":
        open_path = "/home/kid/Github/Oracle/watson/amazon/amazon.json"
    elif name == "ADBE":
        open_path = "/home/kid/Github/Oracle/watson/adobe/adobe.json"
    elif name == "MSFT":
        open_path = "/home/kid/Github/Oracle/watson/microsoft/microsoft.json"

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

def main(argv):
    #format dd/mm/Y
    print get_sentiment("AAPL", '13/11/2016')

if __name__ == "__main__":
    main(sys.argv)
