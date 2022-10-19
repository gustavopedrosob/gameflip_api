from rl_gameflip_api.item_data import ItemData
from rl_gameflip_api.gameflip_rl_items_request import GameflipRlItemsRequest
from rl_data_utils.names.names import ABCNames, get_items_by_name
from rl_data_utils.rarities.rarities import ABCRarities, get_items_by_rarity
from rl_data_utils.types.types import ABCTypes, get_items_by_type
from rl_data_utils.colors.list_colors import ABCListColors, get_items_by_color
from rl_data_utils.decorators import rl_data_smart_attributes
from rl_data_utils.items.items_database import ABCItemsDatabase


class Items(ABCItemsDatabase, ABCNames, ABCRarities, ABCTypes, ABCListColors):
    def __init__(self, items: list[ItemData]):
        self.items = items

    def get_items(self):
        return self.items

    def set_items(self, items):
        self.items = items

    @staticmethod
    def from_request(request: GameflipRlItemsRequest = None):
        if request is None:
            request = GameflipRlItemsRequest()
        return Items([ItemData(**item) for item in request.get_data()])

    @rl_data_smart_attributes()
    def get_items_data_by(self, name, rarity="", type_="", color=""):
        items = self.get_items()
        if color:
            items = get_items_by_color(color, items)
        if type_:
            items = get_items_by_type(type_, items)
        if rarity:
            items = get_items_by_rarity(rarity, items)
        return get_items_by_name(name, items)
