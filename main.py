import os
from magicseaweed import Magicseaweed

forecast = Magicseaweed(os.environ['MSW_KEY'])
forecast.get_forecast_at_spot('1556')