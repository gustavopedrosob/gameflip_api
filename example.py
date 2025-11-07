import datetime
import os
from pprint import pprint

from gameflip_api import GameflipAPI

listing = GameflipAPI.listing_search(digital=True, seller_online_until=datetime.datetime.now())

gameflip_api = GameflipAPI(os.getenv('key_api'), os.getenv('secret'))
pprint(gameflip_api.profile())