# IOT-Status-Webpage

A status page for IoT devices.

The page makes use of the Flask Python framework to be able to trigger python scripts using elements on a webpage. 

TODO:
- options for setting up relay management:
    - always trigger change in adafruit
    - use `GPIO.input(18)` to check the state of an extingly configured pin, then go and change adafruit. (need to manage comflicts)
- need to lookup values in adafruit to show what is to be displayed on the page, which ones to lookup?
- settings page to pull values from adafruit, allow slection, have that write to `feeds.json` file.

# Resources
The information about setting up a Flask Website was found [here](http://damyanon.net/getting-started-with-flask-on-cloud9/), [here](https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework), and [here](http://flask.pocoo.org/docs/0.11/quickstart/).

How to retrieve parameters from a URL in Flask was found [here](https://stackoverflow.com/questions/11774265/flask-how-do-you-get-a-query-string-from-flask)