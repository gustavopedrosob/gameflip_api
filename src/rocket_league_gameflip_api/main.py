import subprocess
import os
import requests
import tempfile
import io
import shutil
import typing
import re
import unidecode
from PIL import Image
import rocket_league_utils.main as rl_utils

SEVEN = 7
FOURTEEN = 14
THIRTY = 30
FORTY_FIVE = 45
NINETY = 90
ONE_HUNDRED_AND_EIGHTY = 180
EXPIRE_IN_DAYS = [SEVEN, FOURTEEN, THIRTY, FORTY_FIVE, NINETY, ONE_HUNDRED_AND_EIGHTY]

ONE = 1
TWO = 2
THREE = 3
SHIPPING_WITHIN_DAYS = [ONE, TWO, THREE]

DRAFT = "draft"
READY = "ready"
ON_SALE = "onsale"
VISIBILITY = [DRAFT, READY, ON_SALE]


def get_image(url: str):
    buffer = tempfile.SpooledTemporaryFile(max_size=1000000000)
    request = requests.get(url, stream=True)
    downloaded = 0
    for chunk in request.iter_content(chunk_size=1024):
        downloaded += len(chunk)
        buffer.write(chunk)
    buffer.seek(0)
    return Image.open(io.BytesIO(buffer.read()))


def save_image(url: str, path: str):
    request = requests.get(url, stream=True)
    with open(path, 'wb') as file:
        request.raw.decode_content = True
        shutil.copyfileobj(request.raw, file)


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

    def download_item_image(self, item: rl_utils.BaseItem, path: str):
        similar_item = self.get_similar_item(item)
        save_image(f"https://gameflip.com/{similar_item.icon_url}", path)

    def download_item_image_by_name_and_color(self, name: str, folder: str, color: str = rl_utils.DEFAULT,
                                              format_: typing.Literal["png", "jpg"] = "png"):
        icon_url, file_name = self._gen_icon_url_and_file_name(name, color)
        url = f"https://gameflip.com/img/items/rocket-league/{icon_url}.{format_}"
        path = f"{folder}/{file_name}.{format_}"
        save_image(url, path)

    def get_item_image(self, item: rl_utils.BaseItem) -> Image:
        similar_item = self.get_similar_item(item)
        return get_image(f"https://gameflip.com/{similar_item.icon_url}")

    @staticmethod
    def get_item_image_by_name_and_color(name: str, color: str = rl_utils.DEFAULT,
                                         format_: typing.Literal["png", "jpg"] = "png"):
        icon_url, file_name = RocketLeagueGameflipAPI._gen_icon_url_and_file_name(name, color)
        url = f"https://gameflip.com/img/items/rocket-league/{icon_url}.{format_}"
        return get_image(url)

    @staticmethod
    def _gen_icon_url_and_file_name(name: str, color: str = rl_utils.DEFAULT) -> typing.Tuple[str, str]:
        formatted_name = RocketLeagueGameflipAPI._format_name(name)
        if not rl_utils.color_utils.is_exactly(rl_utils.DEFAULT, color):
            color = rl_utils.color_utils.get_repr(color)
            formatted_color = color.replace(" ", "")
            return f"{formatted_name}/{formatted_name}-{formatted_color}", f"{formatted_name}-{formatted_color}"
        return formatted_name, formatted_name

    @staticmethod
    def _format_name(name: str) -> str:
        name = rl_utils.Name(name)
        formatted_name = unidecode.unidecode(re.sub("[ -]", "_", name.name).lower())
        if name.kind is not None:
            return f"{formatted_name}_{name.kind.lower()}"
        return formatted_name
