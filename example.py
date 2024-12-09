import datetime
from pprint import pprint

from src.gameflip_api import GameflipAPI

date = datetime.datetime.now().isoformat(timespec='milliseconds') + "Z"

min_date = datetime.datetime.now()
max_date = datetime.datetime.now()
min_date = min_date - datetime.timedelta(minutes=1)

listing = GameflipAPI.listing(digital=True, seller_online_until=datetime.datetime.now())
pprint(listing)
print(date)