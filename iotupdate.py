import json
import os
import os.path

# Import library and create instance of REST client.
from Adafruit_IO import Client

file = open('./adafruitKey.txt', 'r')
apikey = file.readline().replace("\n", '')
file.close()
print apikey
aio = Client(apikey)

#setAdafruitKey()

def updateFeedState(feed, value):
    cloudValue = getAdafruitStatus(feed)
    
    #if the value needs to get updated
    if cloudValue != str(value):
        setAdafruitStatus(feed, value)

def getAdafruitStatus(feed):
    feedStatus = aio.receive(feed)
    return feedStatus
    
def setAdafruitStatus(feed, value):
    aio.send(feed, value)

def getFeeds():
    with open('./feeds.json') as feeds_file:    
        feeds = json.load(feeds_file)
    
    #print feeds['feeds']
    
    return feeds['feeds']
    
def getFeedStatus(feeds):
    feedValues = []
    
    friends = '{"name": "Fred", "id": 1}'


    friends_obj = json.loads(friends)
    
    
    data = {}
    data["feeds"] = {}
    
    #for feed in feeds:
    for index, feed in enumerate(feeds):    
        data["feeds"][index] = {}
        #print feed["name"]
        
        temp = aio.receive(feed["name"])
        #feedValues.append([feed['name'], temp.value])
        
        data["feeds"][index]["name"] = feed["name"]
        data["feeds"][index]["value"] = temp.value
    
    json_data = json.dumps(data)
    
    #print type(data)
    
    return data