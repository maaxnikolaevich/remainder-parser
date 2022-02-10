import json
import requests
from requests.auth import HTTPBasicAuth


def get_products_by_store(product_entry_codes):
    request = requests.post('https://pas.sdvor.com/api/search_test/get_mats_store',
                            auth=HTTPBasicAuth('CONTACTCENTR', 'mlnRDy@u%BZTn{EYF%bnuq'),
                            json={"PRODUCTS": product_entry_codes,
                                  "BUSINESS": "SDVR"})
    response = request.content
    response = json.loads(response)
    return response['data']['MATERIALS_STORE']


def get_products_by_asort(product_entry_codes):
    request = requests.post('https://pas.sdvor.com/api/search_test/get_mats_asort',
                            auth=HTTPBasicAuth('CONTACTCENTR', 'mlnRDy@u%BZTn{EYF%bnuq'),
                            json={"PRODUCTS": product_entry_codes,
                                  "BUSINESS": "SDVR"})
    response = request.content
    response = json.loads(response)
    print(response['data']['MATERIALS_ASORT'])
