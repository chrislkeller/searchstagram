# -*- coding: utf-8 -*-
from config import config_settings
import os
import time, datetime, calendar, csv, logging
from collections import OrderedDict

logging.basicConfig(level=logging.DEBUG)

PROJ_PATH, _ = os.path.split(os.path.abspath(os.path.realpath(__file__)))
EXPORT_FOLDER = os.path.join(PROJ_PATH, 'exports')

instagram_results = [{'caption': '#TBT. How funny do I look @juicycinn \U0001f602\U0001f602\U0001f602\U0001f602\U0001f602\U0001f602 wanna be rider.......', 'link': 'http://instagram.com/p/g-azBEFfC6/', 'image_source': 'http://distilleryimage2.s3.amazonaws.com/791f200052a111e387ee1245c8458940_8.jpg', 'latitude': 40.710254903, 'result_type': 'instagram', 'time_date': datetime.datetime(2013, 11, 21, 11, 38, 42), 'user_full_name': 'Cubangirly13', 'longitude': -74.013283504, 'user': 'cubangirly13'}]

tweet_results = [{'image_source': None, 'longitude': -73.9829391, 'user_full_name': 'Bonisha', 'caption': '@CUNTroversial_ http://t.co/FYspWmaLy2', 'link': '403492917417115648', 'user': 'ebwit', 'latitude': 40.6969332, 'time_date': datetime.datetime(2013, 11, 21, 11, 59, 42), 'result_type': 'tweet'}]

def combine_and_convert_datetime(date, time):
    ''' combines a date string with a time string, converts to datetime object and sets to unix timestamp '''
    date_to_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    time_to_object = datetime.datetime.strptime(time, '%H:%M').time()
    combined_object = datetime.datetime.combine(date_to_object, time_to_object)
    unix_timestamp = calendar.timegm(datetime.datetime.combine(date_to_object, time_to_object).utctimetuple())
    return unix_timestamp

def write_to_csv(instagram_results, tweet_results):

    merged_results_list = instagram_results + tweet_results

    csv_headers = [
        'user',
        'user_full_name',
        'caption',
        'link',
        'image_source',
        'latitude',
        'longitude',
        'result_type',
        'time_date',
    ]

    # opens csv file to write headers
    with open(EXPORT_FOLDER + '/data-export.csv', 'wb', buffering=0) as newCsvFile:
        dataForCsv = csv.writer(newCsvFile, delimiter=',', quoting=csv.QUOTE_ALL)

        dataForCsv.writerow(csv_headers)

        for result in merged_results_list:

            if result.has_key('caption') and result['caption'] is not None:
                caption = result['caption'].encode('utf-8').strip()
            else:
                caption = None

            if result.has_key('link') and result['link'] is not None:
                link = result['link']
            else:
                link = None

            if result.has_key('image_source') and result['image_source'] is not None:
                image_source = result['image_source']
            else:
                image_source = None

            if result.has_key('latitude') and result['latitude'] is not None:
                latitude = result['latitude']
            else:
                latitude = None

            if result.has_key('result_type') and result['result_type'] is not None:
                result_type = result['result_type']
            else:
                result_type = None

            if result.has_key('time_date') and result['time_date'] is not None:
                time_date = result['time_date']
            else:
                time_date = None

            if result.has_key('user_full_name') and result['user_full_name'] is not None:
                user_full_name = result['user_full_name'].encode('utf-8').strip()
            else:
                user = None

            if result.has_key('longitude') and result['longitude'] is not None:
                longitude = result['longitude']
            else:
                longitude = None

            if result.has_key('user') and result['user'] is not None:
                user = result['user'].encode('utf-8').strip()
            else:
                user = None

            csv_row = [
                user,
                user_full_name,
                caption,
                link,
                image_source,
                latitude,
                longitude,
                result_type,
                time_date,
            ]

            dataForCsv.writerow(csv_row)

        newCsvFile.close()

if __name__ == '__main__':
    write_to_csv(instagram_results, tweet_results)