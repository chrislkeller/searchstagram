searchstagram
=============

Riffing of the [QIS tool](https://github.com/propublica/qis) from [ProPublica](http://www.propublica.org/nerds/item/a-super-simple-tool-to-search-instagram-by-time-and-location), searchstagram is a quick Flask application to search Instagram's API by user location or submitted address

* Create a file called ```config.py``` and add the following. Add your INSTAGRAM_CLIENT_ID and INSTAGRAM_CLIENT_SECRET in place of the # signs.

        config_settings = {
            'INSTAGRAM_CLIENT_ID': '#',
            'INSTAGRAM_CLIENT_SECRET': '#',
        }