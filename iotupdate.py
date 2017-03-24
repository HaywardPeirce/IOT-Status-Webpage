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

#update a feed value
def updateFeedState(feed, value):
    cloudValue = getAdafruitStatus(feed)
    
    #if the value needs to get updated
    if cloudValue != str(value):
        setAdafruitStatus(feed, value)

#retrieve the value of a feed in adafruit.io
def getAdafruitStatus(feed):
    feedStatus = aio.receive(feed)
    return feedStatus
    
#set the value for a feed in adafruit.io
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
    
    #loop through the feeds and read in the values to variables
    for feed in feeds:
        feedList["feeds"][count] = {}
        feedList["feeds"][count]["name"] = feed.name
        feedList["feeds"][count]["key"] = feed.key
        count = count + 1
    
    feedList = feedList['feeds']
    
    #return the list of adafruit feeds
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
    
    return data
    
def updateFeedsList(updateFeeds):
    updateFeeds
    enabledFeeds = getFeeds()
    #print enabledFeeds
    availableFeeds = getAdafruitFeeds()
    #print availableFeeds
    