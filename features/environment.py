import os
import sys
import json
from dotenv import dotenv_values, load_dotenv

load_dotenv()

import logging
from requests import Session
from requests.auth import HTTPBasicAuth

import features.Steps.json_responses as json_responses

# Set Logging
logging.basicConfig(level=logging.INFO)


default_env = {
    'baseURL': 'https://api.aircall.io/v1',
    'contactsSearchURL' : 'https://api.aircall.io/v1/contacts/search'
}


tagOptions = ' --tags=@search '
featureFilePath = './features/ '


def before_all(context):
    context.settings = dotenv_values(".env")
    for k, v in default_env.items():
        os.environ.setdefault(k, v)
    #context.baseURL = context.settings['AIR_BASE_URL']
    #context.contactsSearchURL = context.settings['CONTACTS_SEARCH_URL']
    context.headers = {}
    context.authorized_session = HTTPBasicAuth(context.settings['API_ID'], context.settings['API_TOKEN'])
    context.json_responses = json_responses