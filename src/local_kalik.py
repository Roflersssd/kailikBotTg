import json

import mpu
import requests

from config import HOME_EMOJI, DIRECT_GEO_API, REVERT_GEO_API, MESSAGES_PATH


class Kalik(object):
    def __init__(self, data: dict):
        self.message = data['message']
        self.geo_pos = GeoData(self._kalik_address)

    @property
    def _kalik_address(self):
        return self.message.split(HOME_EMOJI)[-1]


class GeoData:
    def __init__(self, address: str = None, lat: float = None, lon: float = None):
        if address is not None:
            response = requests.get(REVERT_GEO_API.format(address))
        elif lat is not None and lon is not None:
            response = requests.get(DIRECT_GEO_API.format(lat, lon))
        else:
            raise Exception('Error: ncorrect arguments for GeoData')

        if response.status_code != 200:
            raise Exception(f'Error: bad request {response.status_code}')

        data = json.loads(response.text)['result']['items'][0]
        self._address = data['full_name']
        self._lat = data['point']['lat']
        self._lon = data['point']['lon']

    @property
    def lat(self):
        return self._lat

    @property
    def lon(self):
        return self._lon

    @property
    def address(self):
        return self._address


def get_distance(p1: GeoData, p2: GeoData):
    return mpu.haversine_distance((p1.lat, p1.lon), (p2.lat, p2.lon))


def get_all_kaliks_from_json():
    with open(MESSAGES_PATH) as f:
        messages = json.load(f)
    all_kaliks = []
    for message in messages:
        if 'message' in message.keys() and message['message']:
            all_kaliks.append(Kalik(message))
    return all_kaliks


def get_nearest_kalik(person_geo: GeoData):
    closer_kalik = min(get_all_kaliks_from_json(), key=lambda x: get_distance(x.geo_pos, person_geo))
    return closer_kalik.message
