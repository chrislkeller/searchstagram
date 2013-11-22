# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask, jsonify, render_template, request, Response, send_from_directory
from flask.ext.assets import Environment, Bundle
from config import config_settings
from search_functions import combine_and_convert_datetime, write_to_csv
from search_instagram import search_instagram
from search_twitter import search_twitter
from concurrent import futures
import webassets

logging.basicConfig(level=logging.DEBUG)

PROJ_PATH, _ = os.path.split(os.path.abspath(os.path.realpath(__file__)))
EXPORT_FOLDER = os.path.join(PROJ_PATH, 'exports')

app = Flask(__name__, static_url_path='/static')
app.config['ASSETS_DEBUG'] = config_settings['DEBUG']
app.config['EXPORT_FOLDER'] = EXPORT_FOLDER

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
    'scripts/models/map.js',
    'scripts/models/marker.js',
    'scripts/models/result.js',
    'scripts/collections/markers.js',
    'scripts/collections/results.js',
    'scripts/views/addressForm.js',
    'scripts/views/initPage.js',
    'scripts/views/locationForm.js',
    'scripts/views/mapView.js',
    'scripts/views/markerView.js',
    'scripts/views/processData.js',
    'scripts/views/result.js',
    'scripts/views/results.js',
    filters='rjsmin',
    output='scripts/libs.js',
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

    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        instagram_api = executor.submit(
            search_instagram,
                term_to_query,
                count, latitude,
                longitude,
                '2mi',
                min_timestamp,
                max_timestamp
        )

        tweet_api = executor.submit(
            search_twitter,
                term_to_query,
                count,
                latitude,
                longitude,
                '2mi',
                min_timestamp,
                max_timestamp
        )

        instagram_results = instagram_api.result()
        tweet_results = tweet_api.result()

    write_to_csv(instagram_results, tweet_results)

    return jsonify(
        zoom = 14,
        number_of_results = count,
        geolatitude = latitude,
        geolongitude = longitude,
        result = instagram_results,
        tweets = tweet_results
    )

@app.route('/download-csv')
def download_csv():

    return send_from_directory(
        app.config['EXPORT_FOLDER'],
        'data-export.csv',
        as_attachment=True,
        mimetype='Document'
    )

    '''
    csv = "nicklaskingo"
    response = make_response(csv)
    response.headers["Content-Disposition"] = "attachment; filename=books.csv"
    return response

    return Response(
        mimetype='text/docuemnt',
        headers={'Content-Disposition': 'attachment; filename=data-export.csv'})

    return jsonify(
        message = 'Your file is downloading'
    )
    '''

if __name__ == '__main__':
    app.run(debug=config_settings['DEBUG'])