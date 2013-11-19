import time, datetime, calendar

def combine_and_convert_datetime(date, time):
    ''' combines a date string with a time string, converts to datetime object and sets to unix timestamp '''
    date_to_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    time_to_object = datetime.datetime.strptime(time, '%H:%M').time()
    combined_object = datetime.datetime.combine(date_to_object, time_to_object)
    unix_timestamp = calendar.timegm(datetime.datetime.combine(date_to_object, time_to_object).utctimetuple())
    return unix_timestamp