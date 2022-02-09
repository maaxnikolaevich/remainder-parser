import json
import requests
from requests.auth import HTTPBasicAuth


def getProducts(ProductEntryCodes):
    request = requests.post('https://pas.sdvor.com/api/search_test/get_mats_store',
                            auth=HTTPBasicAuth('CONTACTCENTR', 'mlnRDy@u%BZTn{EYF%bnuq'),
                            json={"PRODUCTS":
                                      ProductEntryCodes,
                                  "BUSINESS": "SDVR"})
    response = request.content
    response = json.loads(response)
    return response['data']['MATERIALS_STORE']