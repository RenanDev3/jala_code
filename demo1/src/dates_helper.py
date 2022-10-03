'''
This function returns a list of dicts, given a range of dates using
the args start_date and end_date, the function will generate all the
dates between these input and creates a dict for each date generated.
Each dict has two (key, value) pairs: {'date' : date, 'value' : default_value}.
Each date corresponds to the date created previously and the default_value is
the same value of the arg 'default_value'.
'''
# import a library to handle time operations
from datetime import datetime as dt, timedelta
DATE_FORMAT = '%m/%d/%Y'

'''
Receives two parameters (star_date, end_date) and returns a list of each date
in this range, counted day by day.
The range of date is inserted by the args start_date and end_date of
the range.
The only format of args suported by this function are strings as it follows: 'dd/mm/yyy'
Returns None if any other type is used.
'''
def get_dates_in_interval(start_date, end_date):
    try:
        start = dt.strptime(start_date, DATE_FORMAT)
        end = dt.strptime(end_date, DATE_FORMAT)
        if start and end and start<=end:
            delta = (end - start).days
            date_list = [(dt.strftime(( start+timedelta(days=i) ), DATE_FORMAT).lstrip('0'))
            for i in range(delta+1)]
        else:
            date_list = None
        print(date_list)
        return date_list
    except Exception as e:
        print(e)
        return None


'''
Main function of the application. Receives all the parameters
and return a list of dicts.
Calls the function get_dates_in_interval to generate the list of dates.
'''
def get_default_date_data(start_date, end_date, default_value):
    date_dict = []
    date_list = get_dates_in_interval(start_date, end_date)
    if date_list is None:
        return []
    for date in date_list:
        data = {'date' : date, 'participants' : default_value}
        date_dict.append(data)
    return date_dict

    