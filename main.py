import os
from magicseaweed import Magicseaweed

magicseaweed = Magicseaweed(os.environ['MSW_KEY'])
forecast = magicseaweed.get_forecast_at_spot('1556')