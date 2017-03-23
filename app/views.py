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
    
@app.route('/switch', methods=['GET', 'POST'])
def switch():
    # add in for receiving multiple different values
    getFeedname = request.args.get('feedname')
    #argument = request.args.get()
    print 'getFeedname: '
    print getFeedname
    getState = request.args.get('state')
    print 'getState: '
    print getState
    postState = request.form.get('state')
    print 'postState: '
    print postState
    postFeedname = request.form.get('feedname')
    print 'postFeedname: '
    print postFeedname
    #if switch_state == 'false': switch_state = False
    
    #check for presence of POST data, and if it exists: submit it
    if postFeedname and postState is not None:
        print 'updating status using POST data'
        iotupdate.updateFeedState(postFeedname, postState)
        
    elif getFeedname and getState is not None:
        print 'updating status using GET data'
        iotupdate.updateFeedState(getFeedname, getState)
    
    feeds = iotupdate.getFeeds()
    
    feedStatus = iotupdate.getFeedStatus(feeds)
    
    #print feedStatus
    
    #print type(feedStatus)
    
    return render_template("switch.html", feeds = feeds, feedStatus=feedStatus)
    
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