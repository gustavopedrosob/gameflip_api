import subprocess
import os
import requests
import typing
import re
import unidecode
import rocket_league_utils as rl_utils
from rocket_league_utils import color_utils, slot_utils


class DataItem(rl_utils.DataItem):
    def __init__(self, id_: str, name: str, rarity: str, platforms: typing.Tuple[str, ...], icon: str, slot: str,
                 customizable: typing.Optional[bool], unit: typing.Optional[str], colors: typing.Iterable[str] = None):
        self.id = id_
        self.icon = icon
        self.customizable = customizable
        self.unit = unit
        super().__init__(name, slot, rarity, platforms=platforms, colors=colors)

    @staticmethod
    def get_full_icon_url(icon: str) -> str:
        return f"https://gameflip.com/img/items/rocket-league/{icon}"

    @staticmethod
    def get_icon_url(icon: str) -> str:
        return f"/img/items/rocket-league/{icon}"


class ColorfulDataItem(DataItem):
    def __init__(self, id_: str, name: str, rarity: str, platforms: typing.Tuple[str, ...], icon: str, slot: str,
                 customizable: typing.Optional[bool], unit: typing.Optional[str], icons_table: typing.Dict[str, str]):
        self.icons_table = icons_table
        super().__init__(id_, name, rarity, platforms, icon, slot, customizable, unit, icons_table.keys())

    def get_icon_by_color(self, color: str) -> typing.Optional[str]:
        color = color_utils.get_repr(color)
        return self.icons_table.get(color)


class RocketLeagueGameflipAPIException(Exception):
    pass


class ItemNotFound(RocketLeagueGameflipAPIException):
    pass


class RocketLeagueGameflipAPI:
    def __init__(self):
        self.data_items = self.get_data_items()

    @staticmethod
    def get_data_items() -> typing.List[DataItem]:
        response = requests.get("https://gameflip.com/api/gameitem/inventory/812872018935")
        content = response.json()
        data = content["data"]
        items = []
        for item in data:
            platform = item["platform"]
            platforms = rl_utils.PLATFORMS if platform == "all" else (platform,)
            if "colors" in item:
                colors = {color["name"]: color["icon"] for color in item["colors"]}
                items.append(ColorfulDataItem(item["id"], item["name"], item["rarity"], platforms, item["icon"],
                                              item["type"], item.get("customizable"), item.get("unit"), colors))
            else:
                items.append(DataItem(item["id"], item["name"], item["rarity"], platforms, item["icon"],
                                      item["type"], item.get("customizable"), item.get("unit")))
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
        item_data = self.get_data_item(item)
        self.rocket_league_listing(description, item.slot, item_data.name, item_data.id, item.color,
                                   item.certified, price, visibility, quantity, item_data.get_icon_url(item_data.icon),
                                   shipping_within_days, expire_in_days)

    def get_data_item(self, item: rl_utils.ReprItem) -> typing.Union[DataItem, ColorfulDataItem]:
        for data_item in self.data_items:
            if rl_utils.compare_names(item.name, data_item.name) and slot_utils.compare(item.slot, data_item.slot) and \
                    data_item.can_match(item):
                return data_item
        raise rl_utils.ItemNotFound()

    @staticmethod
    def gen_icon_url(name: str, color: str = rl_utils.DEFAULT, format_: typing.Literal["png", "jpg"] = "png") -> str:
        """
        Generates an icon url by formatting string and using logic
        :param name: Item's name
        :param color: Item's color
        :param format_: Item photo url
        :return: An item photo url at gameflip website.
        """
        name = rl_utils.identify_name(name)
        formatted_name = unidecode.unidecode(re.sub("[ -]", "_", name.name).lower())
        if isinstance(name, rl_utils.NameWithKind):
            formatted_name = f"{formatted_name}_{name.complement.lower()}"
        if color_utils.is_exactly(rl_utils.DEFAULT, color):
            url_end = formatted_name
        else:
            color = color_utils.get_repr(color)
            formatted_color = color.replace(" ", "")
            url_end = f"{formatted_name}/{formatted_name}-{formatted_color}"
        return f"https://gameflip.com/img/items/rocket-league/{url_end}.{format_}"
