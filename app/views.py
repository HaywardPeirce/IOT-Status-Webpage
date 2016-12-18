# views.py

from flask import render_template
from flask import request
from app import app

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
    feedname = request.args.get('feedname')
    #argument = request.args.get()
    print 'getFeedname: '
    print feedname
    state = request.args.get('state')
    print 'getState: '
    print state
    postState = request.form.get('state')
    print 'postState: '
    print postState
    postFeedname = request.form.get('feedname')
    print 'postFeedname: '
    print postFeedname
    #if switch_state == 'false': switch_state = False
    
    #print argument
    if feedname and state:
        iotupdate.updateFeedState(feedname, state)
    
    feeds = iotupdate.getFeeds()
    
    return render_template("switch.html", feeds = feeds)