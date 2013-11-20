from config import config_settings
import logging
import tweepy

logging.basicConfig(level=logging.DEBUG)

def search_twitter(count, latitude, longitude):
    auth1 = tweepy.auth.OAuthHandler(config_settings['TWEEPY_CONSUMER_KEY'], config_settings['TWEEPY_CONSUMER_SECRET'])
    auth1.set_access_token(config_settings['TWEEPY_ACCESS_TOKEN'], config_settings['TWEEPY_ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth1)

    list_of_tweets = []

    for tweet in tweepy.Cursor(
        api.search,
        q='',
        geocode='%s,%s,2mi' % (latitude, longitude),
        result_type='recent',
        include_entities=True).items(count):
        try:
            latitude = tweet.coordinates['coordinates'][1]
            longitude = tweet.coordinates['coordinates'][0]
            tweet_dict = {'result_type': 'tweet', 'user': tweet.user.screen_name, 'user_full_name': tweet.user.name, 'link': tweet.id, 'image_source': None, 'caption': tweet.text, 'latitude': latitude, 'longitude': longitude, 'time_date': tweet.created_at}
            list_of_tweets.append(tweet_dict)
        except:
            pass

    return list_of_tweets

if __name__ == '__main__':
    search_twitter(5, '40.7070539', '-74.0130016')