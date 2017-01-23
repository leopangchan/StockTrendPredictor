import json
from watson_developer_cloud import AlchemyDataNewsV1
import sys
import time
import datetime
import xml.etree.ElementTree as xmlParser
from bs4 import  BeautifulSoup as bs


def collectNews(company, timeBegin, timeEnd):
    #change the key for the API in here. This is the AlchemyDataNews
    KEY = '2190f450728492113ce4e5b880a72eefbea73308'
    alchemy_data_news = AlchemyDataNewsV1(api_key=KEY)
    #timeBegin = str(time.mktime(datetime.datetime.strptime(timeBegin, "%d/%m/%Y").timetuple())).split(".")[0]
    #timeEnd = str(time.mktime(datetime.datetime.strptime(timeEnd, "%d/%m/%Y").timetuple())).split(".")[0]

    #print(timeBegin)
    #print(timeEnd)
    #timeBegin ='now-60d'
    #timeEnd = 'now'
    #results = alchemy_data_news.get_news_documents(start='now-60d', end='now', time_slice='12h')
    # print(json.dumps(results, indent=2))

    company_query = '|text=' + company + ',type=company|'
    results = alchemy_data_news.get_news_documents(
    start='now-60d',
    end='now',
    return_fields=['enriched.url.title',
                   #'enriched.url.url',
                   #'enriched.url.author',
                   #'enriched.url.publicationDate',
                   'enriched.url.entities.entity.sentiment.type',
                   #'enriched.url.keywords.keyword.sentiment.mixed'
                   'enriched.url.entities.entity.sentiment.score'
                   ],
    query_fields={'q.enriched.url.enrichedTitle.entities.entity': company_query})

    r = json.dumps(results, indent=2)
    return r


def parseNews(name):
    """
    :param file: json file
    :return: sentiment analysis
    """
    score = 0
    count = 0

    if name == "AAPL":
        open_path = '/home/kid/Github/Oracle/watson/' + "apple.json"
    elif name == "IBM":
        open_path = '/home/kid/Github/Oracle/watson/' + "ibm.json"
    elif name == "AMZN":
        open_path = '/home/kid/Github/Oracle/watson/' + "amazon.json"
    elif name == "VRX":
        open_path = '/home/kid/Github/Oracle/watson/' + "valeant.json"
    elif name == "FIT":
        open_path = '/home/kid/Github/Oracle/watson/' + "fitbit.json"
    elif name == "UWTI":
        open_path = '/home/kid/Github/Oracle/watson/' + "oil.json"


    with open(open_path,'r') as data_file:
        data = json.load(data_file)

    for x in data['result']['docs']:
        for y in x['source']['enriched']['url']['entities']:
            score += (y['sentiment']['score'])
            count+=1


    return score/count


def predictionSentiment(company):
    """
    Get the news from the most recent 2 days
    :param company:
    :return:
    """
    #change the key for the API in here. This is the AlchemyDataNews
    KEY = '2190f450728492113ce4e5b880a72eefbea73308'
    alchemy_data_news = AlchemyDataNewsV1(api_key=KEY)
    timeBegin ='now-2d'
    timeEnd = 'now'
    company_query = '|text=' + company + ',type=company|'
    results = alchemy_data_news.get_news_documents(
    start=timeBegin,
    end=timeEnd,
    return_fields=['enriched.url.title',
                   'enriched.url.entities.entity.sentiment.type',
                   'enriched.url.entities.entity.sentiment.score'
                   ],
    query_fields={'q.enriched.url.enrichedTitle.entities.entity': company_query})
    r = json.dumps(results, indent=2)
    f = open("/home/kid/Github/Oracle/watson/jsonp2.json", 'w')
    f.write(str(r))

def main(argv):

    company = "Amazon"
    #format dd/mm/Y

    #API call has problem
    json_file = collectNews(company, "now-30d", "now")
    f = open("/home/kid/Github/Oracle/watson/jsonp.json", 'w')
    f.write(str(json_file))

    """
    #with open("/home/kid/Github/Oracle/watson/jsonp.json", 'w') as outfile:
    #    json.dump(json_file, outfile)
    """

    predictionSentiment(company)
    print ("Complete Data Collecting")
    #print parseNews("IBM")

if __name__ == "__main__":
    main(sys.argv)


