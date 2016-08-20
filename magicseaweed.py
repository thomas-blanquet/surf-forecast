import requests


class Magicseaweed():
    api_url = ''

    def __init__(self, api_key):
        self.api_url = "http://magicseaweed.com/api/{0}/forecast"
        self.api_url = self.api_url.format(api_key)

    def get_forecast_at_spot(self, spot_id, local_time='None', units_mesures='eu'):
        data = requests.get('{0}?spot_id={1}&units={2}'.format(self.api_url, spot_id, units_mesures))
        data = data.json()
        return data
