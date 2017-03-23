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

#get a list of the enabled feeds listed in the file
def getFeeds():
    with open('./feeds.json') as feeds_file:    
        feeds = json.load(feeds_file)
    
    #print feeds['feeds']
    
    return feeds['feeds']
 
#get a list of all the adafruit feeds  
def getAdafruitFeeds():
    
    count = 0
    
    feeds = aio.feeds()
    
    feedList = {}
    feedList["feeds"] = {}
    
    for feed in feeds:
        feedList["feeds"][count] = {}
        feedList["feeds"][count]["name"] = feed.name
        feedList["feeds"][count]["key"] = feed.key
        count = count + 1
    
    #print feedList
    feedList = feedList['feeds']
    #print feedList
    return feedList

#lookup the current values of the listed feeds in Adafruit
def getFeedStatus(feeds):
    feedValues = []
    
    data = {}
    data["feeds"] = {}
    
    #for feed in feeds:
    for index, feed in enumerate(feeds):    
        data["feeds"][index] = {}
        
        print feed["key"]
        temp = aio.receive(feed["key"])
        #feedValues.append([feed['name'], temp.value])
        
        data["feeds"][index]["key"] = feed["key"]
        data["feeds"][index]["value"] = temp.value
    
    #json_data = json.dumps(data)
    
    #print type(data)
    
    return data
    
def updateFeedsList(updateFeeds):
    updateFeeds
    enabledFeeds = getFeeds()
    #print enabledFeeds
    availableFeeds = getAdafruitFeeds()
    #print availableFeeds
    