from src.dates_helper import get_dates_in_interval
from src.dates_helper import get_default_date_data


def test_get_dates_in_interval_returns_none():
    start_date = None
    end_date = None

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is None


def test_get_dates_in_interval_returns_single_element_list():
    start_date = '9/12/2022'
    end_date = '9/12/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is not None, 'Expected non null list'
    assert '9/12/2022' in dates, f'Expected {start_date} in list'


def test_get_dates_in_interval_returns_list():
    start_date = '9/12/2022'
    end_date = '9/15/2022'

    dates = get_dates_in_interval(start_date, end_date)
    assert dates is not None, 'Expected non null list'
    assert '9/12/2022' in dates
    assert '9/13/2022' in dates
    assert '9/14/2022' in dates
    assert '9/15/2022' in dates


# Added four new test_functions
def test_invalid_input_value_get_interval():
    start_date = 'abc'
    end_date = 'defghi'
    dates = get_dates_in_interval(start_date, end_date)
    assert dates is None


def test_invalid_input_type_get_interval():
    start_date = {}
    end_date = []
    dates = get_dates_in_interval(start_date, end_date)
    assert dates is None


def test_invalid_input_value_get_default_value():
    start_date = 'abc'
    end_date = 'defghi'
    default_value = 'pytest'
    dates = get_default_date_data(start_date, end_date, default_value)
    assert dates == []


def test_invalid_input_type_get_default_value():
    start_date = {}
    end_date = []
    default_value = (0, 0)
    dates = get_default_date_data(start_date, end_date, default_value)
    assert dates == []
