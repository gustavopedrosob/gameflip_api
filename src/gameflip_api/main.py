import requests

class GameflipAPI:
    def __init__(self, apikey, totp):
        pass

    @staticmethod
    def get_rldata_items() -> dict:
        response = requests.get("https://gameflip.com/api/gameitem/inventory/812872018935")
        return response.json()
