from django.conf import settings
import tbaapiv3client
from tbaapiv3client.rest import ApiException

def get_event(eventkey):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_event(eventkey)
        info = api_response
        return info
    except ApiException as e:
        return None

def get_events_by_year(year):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_events_by_year(year)
        info = api_response
        return info
    except ApiException as e:
        return None

def get_events_by_year_keys(year):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_events_by_year_keys(year)
        info = api_response
        return info
    except ApiException as e:
        return None

def get_all_event_keys():
    keys = {}
    for year in range(2016, 2020):
        keys[year] = get_events_by_year_keys(year)

    return keys

def get_events_by_year_simple(year):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_events_by_year_simple(year)
        info = api_response
        return info
    except ApiException as e:
        return None

def get_event_teams(eventkey):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_event_teams(eventkey)
        info = api_response
        return info
    except ApiException as e:
        return None

def get_event_matches(eventkey):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_event_matches(eventkey)
        info = api_response
        return info
    except ApiException as e:
        return None

def get_all_events_simple():
    events = {}
    for year in range(2016, 2020):
        events[year] = get_events_by_year_simple(year)

    return events
