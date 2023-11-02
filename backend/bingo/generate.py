#import requests
import json

base_url = 'https://go3.events.sap.com/sapteched/virtual/2023/'

def run():
    with open('data/sessions.json', 'r') as f:
        data = json.load(f)
        for i in data.get('sectionList'):
            print(len(i.get('items')))

    # token = requests.get(base_url + "reg/flow/loadPage?pageUri=catalog&workflowApiToken=sap.sapteched23.catalog")
    # api_token = token.json().get('data').get('widgetConf').get('apiProfileToken')

    # response = requests.post(base_url + 'events/api/search',
    #                          headers={'Content-Type': 'application/x-www-form-urlencoded', 'rfapiprofileid': api_token},
    #                          data={'type': 'session', 'browserTimezone': 'Europe/Brussels'}) 

    # response = requests.post(base_url + 'events/api/attributes',
    #                          headers={'Content-Type': 'application/x-www-form-urlencoded', 'rfapiprofileid': api_token},
    #                          data={'type': 'session', 'browserTimezone': 'Europe/Brussels'}) 
    # print(response.json())