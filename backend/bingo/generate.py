import requests
import json
import os

base_url = 'https://go3.events.sap.com/sapteched/virtual/2023/'

def run():
    token = requests.get(base_url + "reg/flow/loadPage?pageUri=catalog&workflowApiToken=sap.sapteched23.catalog")
    api_token = token.json().get('data').get('widgetConf').get('apiProfileToken')

    response = requests.post(base_url + 'events/api/search',
                              headers={'Content-Type': 'application/x-www-form-urlencoded', 'rfapiprofileid': api_token},
                              data={'type': 'session', 'browserTimezone': 'Europe/Brussels'}) 
    
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, '../data/sessions.json'), "w") as outfile:
        json.dump(response.json(), outfile)