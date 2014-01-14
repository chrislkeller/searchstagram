searchstagram
=============

Riffing of the [QIS tool](https://github.com/propublica/qis) from [Al Shaw](https://twitter.com/A_L) and [ProPublica](http://www.propublica.org/nerds/item/a-super-simple-tool-to-search-instagram-by-time-and-location), searchstagram is a quick Flask/backbone.js application to search Instagram's API by a user's location or a submitted address.

![ScreenShot](https://raw.github.com/chrislkeller/searchstagram/master/static/images/screenshot.png)

**Getting Setup**

* Download the zip or clone the repo locally

* Install the requirements from ```requirements.txt``` into a virtual enviroment, or just straight into the system environment if you prefer.

        pip install -r requirements.txt

* If you don't already, register for an Instagram account, and then register a [Instagram client application](http://instagram.com/developer/clients/register/). I set my OAuth redirect_uri to http://localhost:5000/.

* Create a file called ```config.py``` in the same folder as ```app.py```. Add the following code with your INSTAGRAM_CLIENT_ID and INSTAGRAM_CLIENT_SECRET in place of the # signs.

        config_settings = {
            'INSTAGRAM_CLIENT_ID': '#',
            'INSTAGRAM_CLIENT_SECRET': '#',
        }

* Change into the searchstagram directory, run ```python __init__.py``` and visit ```http://127.0.0.1:5000/``` in your browswer.

* Type in an address to search, or use your current location.

**Articles written using Searchstagram**

* [What does LA look like at 10 pm?](http://www.scpr.org/news/2014/01/08/41410/what-does-la-look-like-at-10-pm-photos/)