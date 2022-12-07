import subprocess
import os
import requests
import typing
import re
import unidecode
import rocket_league_utils as rl_utils


class Item(rl_utils.IdentityItem):
    def __init__(self, id_: str, name: str, rarity: str, platform: str, icon: str, slot: str, icon_url: str,
                 customizable: typing.Optional[bool] = None, unit: typing.Optional[str] = None,
                 color: str = rl_utils.DEFAULT):
        self.id = id_
        self.platform = platform
        self.icon = icon
        self.customizable = customizable
        self.unit = unit
        self.icon_url = icon_url
        self.color = color
        super().__init__(name, rarity, slot)


class RocketLeagueGameflipAPIException(Exception):
    pass


class NoSimilarItem(RocketLeagueGameflipAPIException):
    pass


class RocketLeagueGameflipAPI:
    def __init__(self):
        self.items = self.get_items_data()

    @staticmethod
    def get_items_data() -> typing.List[Item]:
        response = requests.get("https://gameflip.com/api/gameitem/inventory/812872018935")
        content = response.json()
        data = content["data"]
        items = []
        for item in data:
            if "colors" in item:
                for color in item["colors"]:
                    items.append(Item(item["id"], item["name"], item["rarity"], item["platform"], color["icon"],
                                      item["type"], color["icon_url"], item.get("customizable"), item.get("unit"),
                                      color["name"]))
            items.append(Item(item["id"], item["name"], item["rarity"], item["platform"], item["icon"],
                              item["type"], item["icon_url"], item.get("customizable"), item.get("unit")))
        return items

    @staticmethod
    def rocket_league_listing(
            description: str,
            slot: str,
            title: str = "",
            id_: str = "",
            color: str = "",
            certified: str = "",
            price: int = 75,
            visibility: typing.Literal["draft", "onsale", "ready"] = "onsale",
            quantity: int = 1,
            photo_url: str = "",
            shipping_within_days: typing.Literal[1, 2, 3] = 1,
            expire_in_days: typing.Literal[7, 14, 30, 45, 90, 180] = 30):
        args = ["node", "rl_listing.js", photo_url, title, description, str(price), id_, slot,
                str(quantity), str(shipping_within_days), str(expire_in_days), visibility, color, certified]
        process = subprocess.Popen(args, shell=False, env=os.environ.copy())
        process.wait()

    def rocket_league_listing_item(self, item: rl_utils.BaseItem, description: str, price: int = 75,
                                   visibility: typing.Literal["draft", "onsale", "ready"] = "onsale",
                                   quantity: int = 1, shipping_within_days: typing.Literal[1, 2, 3] = 1,
                                   expire_in_days: typing.Literal[7, 14, 30, 45, 90, 180] = 30):
        similar_item = self.get_similar_item(item)
        self.rocket_league_listing(description, item.slot, similar_item.name, similar_item.id, item.color,
                                   item.certified, price, visibility, quantity, similar_item.icon_url,
                                   shipping_within_days, expire_in_days)

    def get_similar_item(self, item: rl_utils.BaseItem) -> Item:
        for item_ in self.items:
            if item.compare_identity(item_) and rl_utils.color_utils.compare(item_.color, item.color):
                return item_
        raise NoSimilarItem()

    @staticmethod
    def get_icon_url(name: str, color: str = rl_utils.DEFAULT, format_: typing.Literal["png", "jpg"] = "png") -> str:
        name = rl_utils.Name(name)
        formatted_name = unidecode.unidecode(re.sub("[ -]", "_", name.name).lower())
        if name.kind is None:
            formatted_name = formatted_name
        else:
            formatted_name = f"{formatted_name}_{name.kind.lower()}"
        if rl_utils.color_utils.is_exactly(rl_utils.DEFAULT, color):
            url_end = formatted_name
        else:
            color = rl_utils.color_utils.get_repr(color)
            formatted_color = color.replace(" ", "")
            url_end = f"{formatted_name}/{formatted_name}-{formatted_color}.{format_}"
        return f"https://gameflip.com/img/items/rocket-league/{url_end}"
