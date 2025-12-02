import os
from pprint import pprint
from dotenv import load_dotenv
from gameflip_api.api import GameflipAPI

load_dotenv()

print("Listing results:")

listing_response = GameflipAPI.listing_search(digital=True, limit=1)
pprint(listing_response.json())

gameflip_api = GameflipAPI(os.getenv('GFAPI_KEY'), os.getenv('GFAPI_SECRET'))

print("My profile info:")

pprint(gameflip_api.profile().json())