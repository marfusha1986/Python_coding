
import requests
from pprint import pprint

SHEET_ENDPOINT = 'https://api.sheety.co/e949145671599e5a02c18729f8be5618/flightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        #pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price':{
                    'iataCode':city['iataCode']
                }
            }
            response = requests.put(
                url=f'{SHEET_ENDPOINT}/{city["id"]}',
                json=new_data
            )
            print(response.text)