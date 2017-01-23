import json
import sys
from watson_developer_cloud import AlchemyDataNewsV1

alchemy_data_news = AlchemyDataNewsV1(api_key='2190f450728492113ce4e5b880a72eefbea73308')

#results = alchemy_data_news.get_news_documents(start='now-7d', end='now')
#print(json.dumps(results, indent=2))

results = alchemy_data_news.get_news_documents(
    start='now-60d',
    end='now',
    return_fields=['enriched.url.title',
                   #'enriched.url.url',
                   #'enriched.url.author',
                   'enriched.url.publicationDate'],
    query_fields={'q.enriched.url.enrichedTitle.entities.entity': '|text=AAPL,type=company|'})
print(json.dumps(results, indent=2))
sys.exit(0)
f = open("/home/kid/Github/Oracle/watson/test.json", 'w')
f.write(str(results))