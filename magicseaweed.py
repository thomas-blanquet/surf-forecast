import requests
import calendar
from datetime import datetime, timedelta


class Magicseaweed():
    api_url = ''

    def __init__(self, api_key):
        self.api_url = "http://magicseaweed.com/api/{0}/forecast"
        self.api_url = self.api_url.format(api_key)

    def near_report(self, time):
        """
        Get the next available forecast
        """
        while time.hour % 3 != 0:
            time = time + timedelta(hours=1)
        return datetime(time.year, time.month, time.day, time.hour, 0, 0)

    def get_forecast_at_spot(self, spot_id, local_time='None', units_mesures='eu'):
        """
        :param spot_id: The spot ID from magicseaweed.com
        :param local_time: time (datetime.utcnow())
        :param units_mesures: default eu to have european units
        :return: dict corresponding of next forecast available
        """
        # Request to MSW API
        data = requests.get('{0}?spot_id={1}&units={2}'.format(self.api_url, spot_id, units_mesures))
        data = data.json()
        timestamp = calendar.timegm(self.near_report(local_time).timetuple())

        for forecast in data:
            if forecast['localTimestamp'] == timestamp:
                return forecast
        return None

