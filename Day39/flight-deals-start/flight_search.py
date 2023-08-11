import requests
from flight_data import FlightData

TEQUILA_ENDPOINT="https://api.tequila.kiwi.com/"
TEQUILA_API_KEY='kUyt5ic2Z_OIandzceV0trSiTwGw6tCp'


class FlightSearch:

    def get_destination_code(self,city_name):
       location_endpoint = f'{TEQUILA_ENDPOINT}/locations/query'
       headers = {'apikey':TEQUILA_API_KEY}
       query = {'term':city_name,'location_types':'city'}
       response = requests.get(url=location_endpoint,headers=headers,params=query)
       results = response.json()['locations']
       code = results[0]['code']
       return code

    def check_flights(self,origin_city_code,destination_city_code,from_time,to_time):
        headers = {
            'apikey':TEQUILA_API_KEY
        }
        query = {
            'fly_from':origin_city_code,
            'fly_to':destination_city_code,
            'date_from':from_time.strftime('%d/%m/%Y'),
            'date_to':to_time.strftime('%d/%m/%Y'),
            'nights_in_dst_from':7,
            'nights_to_dst_to':28,
            'flight_type':'round',
            'one_for_city':1,
            "max_stopovers":0,
            'adults':2,
            'children':1,
            'curr':'TRY'
        }

        response = requests.get(url=f'{TEQUILA_ENDPOINT}v2/search',
                              headers = headers,
                              params=query,

                             )

        try:
            data = response.json()['data']
        except IndexError:
            print(f'No flights found for {destination_city_code}.')

        flight_data = FlightData(
            price = data['price'],
            origin_city=data['cityFrom'],
            origin_airport=data['flyFrom'],
            destination_city=data['cityTo'],
            destination_airport=data['flyTo'],
            out_date=data['route'][0]['local_departure'].split('T')[0],
            return_date = data['route'][1]['local_departure'].split('T')[0],
        )

        print(f'{flight_data.destination_city}:${flight_data.price}')
        return flight_data











