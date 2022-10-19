from requests import get


class GameflipRlItemsRequest:
    def __init__(self):
        self.response = get('https://gameflip.com/api/gameitem/inventory/812872018935')

    def get_json(self):
        return self.response.json()

    def get_data(self):
        return self.get_json()['data']
