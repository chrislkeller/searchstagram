# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from config import config_settings
from instagram.client import InstagramAPI
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_url_path='/static')

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
    term_to_query = str(request.args.get('term'))
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))

    # create a holding container for what the api returns
    list_of_images = []
    api = InstagramAPI(client_id=config_settings['INSTAGRAM_CLIENT_ID'], client_secret=config_settings['INSTAGRAM_CLIENT_SECRET'])

    # search and set to variable
    instagram_media = api.media_search(term_to_query, count, latitude, longitude)

    # loop through what the search returned
    for media in instagram_media:

        # lets skip anything that doesn't have an address
        if media.location.point.latitude is not None and media.location.point.longitude is not None:
            latitude = media.location.point.latitude
            longitude = media.location.point.longitude
        else:
            pass

        if media.user.username is not None:
            user = media.user.username
        else:
            user = None

        if media.user.full_name is not None:
            user_full_name = media.user.full_name
        else:
            user_full_name = None

        if media.link is not None:
            link = media.link
        else:
            link = None

        if media.images['standard_resolution'].url is not None:
            image_source = media.images['standard_resolution'].url
        else:
            image_source = None

        if media.created_time is not None:
            time_date = media.created_time
        else:
            time_date = None

        if media.caption is not None:
            caption = media.caption.text
        else:
            caption = None

        image_dict = {'user': user, 'user_full_name': user_full_name, 'link': link, 'image_source': image_source, 'caption': caption, 'latitude': latitude, 'longitude': longitude, 'time_date': time_date}

        list_of_images.append(image_dict)

    return jsonify(number_of_results=count, geolatitude=latitude, geolongitude=longitude, result=list_of_images)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)