import json
import xml.etree.ElementTree as xmlParser
from StringIO import StringIO
import os

def startSpider(root):
    jsonStock = {}
    for child in root.iter("SummarizedTradeCollection"):
        for grandChild in child.iter("SummarizedTrade"):
            currentDate = getDate(grandChild.find("Time"));
            currentDate = str(currentDate)

            if(currentDate != None):
                if (bool(jsonStock) == False):
                    print currentDate
                    jsonStock = {currentDate:
                    [{"hour": getHour(grandChild.find("Time")),
                     "first": getFirstPrice(grandChild.find("First")),
                     "end": getEndPrice(grandChild.find("Last")),
                     "high": getHigh(grandChild.find("High")),
                     "low": getLow(grandChild.find("Low"))
                     }]}
                elif (currentDate not in jsonStock):
                    print currentDate
                    jsonStock.update({currentDate:
                    [{"hour": getHour(grandChild.find("Time")),
                     "first": getFirstPrice(grandChild.find("First")),
                     "end": getEndPrice(grandChild.find("Last")),
                     "high": getHigh(grandChild.find("High")),
                     "low": getLow(grandChild.find("Low"))
                     }]})
                else:
                    jsonStock[currentDate].append(
                    {"hour": getHour(grandChild.find("Time")),
                     "first": getFirstPrice(grandChild.find("First")),
                     "end": getEndPrice(grandChild.find("Last")),
                     "high": getHigh(grandChild.find("High")),
                     "low": getLow(grandChild.find("Low"))
                     });
    return jsonStock

def getHour(child):
    if (child.tag == "Time"):
        return child.text[10:-4]
    else:
        raise Exception("Expected a <Time> tag");


def getDate(child):
    if (child.tag == "Time"):
        return child.text[:-13]
    else:
        raise Exception("Expected a <Time> tag");

def getFirstPrice(child):
    if (child.tag == "First"):
        return child.text
    else:
        raise Exception("Expected a <First> tag");

def getEndPrice(child):
    if (child.tag == "Last"):
        return child.text
    else:
        raise Exception("Expected a <Last> tag");

def getHigh(child):
    if (child.tag == "High"):
        return child.text
    else:
        raise Exception("Expected a <High> tag");

def getLow(child):
    if (child.tag == "Low"):
        return child.text
    else:
        raise Exception("Expected a <Low> tag");


if __name__ == "__main__":
    allJsonStock = {}
    # path = "../3monthsData/"
    path = "../Four Sets/"
    '''
    path = "../Four Sets/"
    for file in os.listdir(path):
        tree = xmlParser.parse(os.path.join(path, file))
        allJsonStock.update(startSpider(tree.getroot()));
    '''

    fb_path = path + "FB/"
    for file in os.listdir(fb_path):
        tree = xmlParser.parse(os.path.join(fb_path, file))
        allJsonStock.update(startSpider(tree.getroot()));
    with open("../Completed JSON/FB_OUT.json", "w") as outfile:
        outfile.write(json.dumps(allJsonStock, sort_keys=True, indent=4, separators=(',', ': ')));

    adbe_path = path + "ADBE/"
    for file in os.listdir(adbe_path):
        tree = xmlParser.parse(os.path.join(adbe_path, file))
        allJsonStock.update(startSpider(tree.getroot()));
    with open("../Completed JSON/ADBE_OUT.json", "w") as outfile:
        outfile.write(json.dumps(allJsonStock, sort_keys=True, indent=4, separators=(',', ': ')));

    tree = xmlParser.parse(os.path.join(path, "AMZN.xml"))
    allJsonStock.update(startSpider(tree.getroot()));
    with open("../Completed JSON/AMZN_OUT.json", "w") as outfile:
        outfile.write(json.dumps(allJsonStock, sort_keys=True, indent=4, separators=(',', ': ')));

    msft_path = path + "MSFT/"
    for file in os.listdir(msft_path):
        tree = xmlParser.parse(os.path.join(msft_path, file))
        allJsonStock.update(startSpider(tree.getroot()));
    with open("../Completed JSON/MSFT_OUT.json", "w") as outfile:
        outfile.write(json.dumps(allJsonStock, sort_keys=True, indent=4, separators=(',', ': ')));
