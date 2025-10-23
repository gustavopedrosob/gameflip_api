import datetime
import os
from pprint import pprint

from gameflip_api import GameflipAPI

date = datetime.datetime.now().isoformat(timespec='milliseconds') + "Z"

min_date = datetime.datetime.now()
max_date = datetime.datetime.now()
min_date = min_date - datetime.timedelta(minutes=1)

listing = GameflipAPI.listings(digital=True, seller_online_until=datetime.datetime.now())

gameflip_api = GameflipAPI(os.getenv('key_api'), os.getenv('secret'))
pprint(gameflip_api.profile())