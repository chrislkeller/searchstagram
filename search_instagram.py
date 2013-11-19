from config import config_settings
from instagram.client import InstagramAPI

def search_instagram(term_to_query, count, latitude, longitude, min_timestamp, max_timestamp):
    ''' query instagram for images '''

    # create a holding container for what the api returns
    list_of_images = []

    api = InstagramAPI(client_id=config_settings['INSTAGRAM_CLIENT_ID'], client_secret=config_settings['INSTAGRAM_CLIENT_SECRET'])

    # search and set to variable
    instagram_media = api.media_search(term_to_query, count, latitude, longitude, min_timestamp, max_timestamp)

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

    return list_of_images
