import re
import xml.etree.cElementTree as ElementTree
import sys
from os import listdir
from os.path import isfile, join
#from urllib5.parse import urlencode
#from urllib.request import Request, urlopen
import cgi
import json

import requests

def getData(url):
    print ("Start")
    #post or get in here?
    r = requests.get(url)
    print(r.status_code, r.reason)  # HTTP
    f = open('DataNews', 'w')
    f.write(str(r.content))
    #print("search results : ", r.content)
    print("Done")

def main(argv):


    print("Usage : Python Nasdaq.py data_dir")

    url = 'https://gateway-a.watsonplatform.net/calls/data/GetNews' \
          '?apikey=d4a97f67bd08aa3720bd3be9dc5c92ad720f16fa&outputMode=json&start=now-1d&end=now&count=100&q' \
          '.enriched.url.enrichedTitle.relations.' \
          'relation=|action.verb.text=acquire,object.' \
          'entities.entity.type=Company|&return=enriched.url.title'
    getData(url)

if __name__ == "__main__":
    main(sys.argv)