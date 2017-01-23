import json
import xml.etree.ElementTree as xmlParser

def startSpider(root):
    jsonStr = None
    for child in root.iter("SummarizedTradeCollection"):
        jsonStr = []
        for grandChild in child.iter("SummarizedTrade"):
            currentDate = getDate(grandChild.find("Time"));
            currentDate = str(currentDate)
            #print("1st: ",currentDate)

            if(currentDate != None):
                if (bool(jsonStr) == False):
                    jsonStr = {currentDate: currentDate}
                else:
                    jsonStr.update({currentDate: currentDate})
                #print(jsonStr)
    print json.dumps(jsonStr, sort_keys=True, indent=4, separators=(',', ': '))


def getHour(child):
    if (child.tag == "Time"):
        return child.text[10:-4]
    else:
        raise Exception("Expected a <Time> tag");


def getDate(child):
    if (child.tag == "Time"):
        #print child.text
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
    tree = xmlParser.parse("newest.xml")
    startSpider(tree.getroot())
