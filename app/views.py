# views.py

from flask import render_template
from flask import request
from app import app
import json

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import your module
import iotupdate

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")
    
#page to change the state of the relays
@app.route('/switch', methods=['GET', 'POST'])
def switch():
    
    #get swtich states from the GET values
    #TODO: add in for receiving multiple different values
    getFeedname = request.args.get('feedname')
    #argument = request.args.get()
    print 'getFeedname: '
    print getFeedname
    getState = request.args.get('state')
    print 'getState: '
    print getState
    
    #get switch states from the POST data
    postState = request.form.get('state')
    print 'postState: '
    print postState
    postFeedname = request.form.get('feedname')
    print 'postFeedname: '
    print postFeedname
    
    #check for presence of POST data, and if it exists: submit it
    if postFeedname and postState is not None:
        print 'updating status using POST data'
        iotupdate.updateFeedState(postFeedname, postState)
    
    #only if there is no POST data submit the GET data 
    elif getFeedname and getState is not None:
        print 'updating status using GET data'
        iotupdate.updateFeedState(getFeedname, getState)
    
    #get a list of the enabled feeds listed in the file 
    feeds = iotupdate.getFeeds()
    
    #get the adafruit statuses of the configured feeds
    feedStatus = iotupdate.getFeedStatus(feeds)
    
    #return the page template, and pass in the list of feeds and the status of the feeds
    return render_template("switch.html", feeds = feeds, feedStatus=feedStatus)

#page for configuring the settings for this admin app. 
#TODO: functionality like changing which feeds are subscribed to
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    
    requestFeeds = request.form
    for key in requestFeeds:
        print key
        print 'form key '+requestFeeds[key]
    
    #postFeedname = request.form.get('feedname')
    #print 'postFeedname: '
    #print postFeedname
    
    #print argument
    if requestFeeds is not "":
        print 'updating status'
        iotupdate.updateFeedsList(requestFeeds)
    
    enabledFeeds = iotupdate.getFeeds()
    
    feedStatus = iotupdate.getFeedStatus(enabledFeeds)

    feedsList = iotupdate.getAdafruitFeeds()
    
    #print feedsList[0]
    
    print enabledFeeds[0]['key']
    
    #print type(feedStatus)
    
    return render_template("settings.html", feedsList = feedsList, feedStatus=feedStatus, enabledFeeds=enabledFeeds)