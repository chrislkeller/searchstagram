# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from flask.ext.assets import Environment, Bundle
from config import config_settings
from search_functions import combine_and_convert_datetime
from search_instagram import search_instagram
from search_twitter import search_twitter
import webassets
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_url_path='/static')
assets = Environment(app)

# combine and compress scripts
js = Bundle(
    'scripts/libs/jquery.min.js',
    'scripts/libs/leaflet.js',
    'scripts/libs/leaflet.markercluster.js',
    'scripts/libs/modernizr.min.js',
    'scripts/libs/underscore-min.js',
    'scripts/libs/backbone-min.js',
    'scripts/libs/moment.min.js',
    'scripts/libs/jquery.address.min.js',
    'scripts/libs/bootstrap.min.js',
    'scripts/libs/jquery.geocomplete.min-1.4.js',
    'scripts/app.js',
    filters='rjsmin',
    output='scripts/libs.js'
)
assets.register('js_libs', js)

css = Bundle(
    'css/bootstrap.min.css',
    'css/leaflet.min.css',
    'css/MarkerCluster.css',
    'css/style.css',
    filters='cssmin',
    output='css/min.css'
)
assets.register('css_all', css)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search-query')
def search_query():

    # make sure we have a quantity to return
    if request.args.get('count') is not None:
        try:
            count = int(request.args.get('count'))
        except:
            count = 12
    else:
        count = 12

    # limit display to 100 images
    if count > 100:
        count = 100
    else:
        count = count

    # convert our URL params to proper data types
    term_to_query = ''
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    radius = request.args.get('radius')
    start_date = request.args.get('startdate')
    start_time = request.args.get('starttime')
    end_date = request.args.get('enddate')
    end_time = request.args.get('endtime')
    min_timestamp = combine_and_convert_datetime(start_date, start_time)
    max_timestamp = combine_and_convert_datetime(end_date, end_time)

    instagram_result = search_instagram(
        term_to_query,
        count, latitude,
        longitude,
        '2mi',
        min_timestamp,
        max_timestamp
    )

    tweet_results = search_twitter(
        term_to_query,
        count,
        latitude,
        longitude,
        '2mi',
        min_timestamp,
        max_timestamp
    )

    return jsonify(
        zoom = 14,
        number_of_results = count,
        geolatitude = latitude,
        geolongitude = longitude,
        result = instagram_result,
        tweets = tweet_results
    )

if __name__ == '__main__':
    app.run(debug=config_settings['DEBUG'])