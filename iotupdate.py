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