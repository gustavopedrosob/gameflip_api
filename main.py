import subprocess
import os
import requests
import json
import ss


class Argument:
    NULL = False
    VALUES = ()

    def __init__(self, value: str or int):
        self.value = value

    def validate(self):
        if self.value == "" and not self.NULL:
            raise ValueError(f"The {self.__class__.__name__} argument can't be null.")
        if self.value and self.value not in self.VALUES:
            raise ValueError(f"The {self.__class__.__name__} argument can be ({', '.join(self.VALUES)}), not {self.value}.")


class Visibility(Argument):
    VALUES = ("draft", "ready", "onsale")


class Types(Argument):
    VALUES = ('decal', 'banner', 'topper', 'avatar-border', 'paint-finish', 'boost', 'trail', 'body', 'blueprint',
              'goal', 'engine-audio', 'credit', 'crate', 'custom', 'wheel', 'antenna')

    def to_tag_value(self):
        self.value: str
        tag = self.value.capitalize()
        return tag.replace("-", " ")


class Colors(Argument):
    NULL = True
    VALUES = ("Black", "Burnt Sienna", "Cobalt", "Crimson", "Forest Green", "Grey", "Lime", "Orange", "Pink", "Purple",
              "Saffron", "Sky Blue", "Titanium White")


class ShippingWithinDays(Argument):
    VALUES = (1, 2, 3)


class Certification(Argument):
    NULL = True
    VALUES = ("Acrobat", "Aviator", "Goalkeeper", "Guardian", "Juggler", "Paragon", "Playmaker", "Scorer", "Show Off",
              "Sniper", "Striker", "Sweeper", "Tactician", "Turtle", "Victor")


class ExpireInDays(Argument):
    VALUES = (7, 14, 30, 45, 90, 180)


class ItemGameflipApi:
    def __init__(self, id, name, rarity, platform, icon, type, icon_url, customizable=None, unit=None, colors=None):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.platform = platform
        self.icon = icon
        self.unit = unit
        self.type = type
        self.icon_url = icon_url
        self.customizable = customizable
        self.colors = colors

    def get_color(self, color: str) -> dict:
        return list(filter(lambda c: c["name"] == color, self.colors))[0]

    def is_painted(self) -> bool:
        return True if self.colors else False


class NameNotExists(Exception):
    def __init__(self, message):
        super().__init__(message)


class ItemHaventType(Exception):
    def __init__(self, message):
        super().__init__(message)


'''
LEIA ANTES DE FAZER UMA ALTERAÇÃO DO CÓDIGO!!!
- Embora a função check_name ocupe mais código ela é importante por questão de performasse do programa.

'''


def check_name(function):
    def new_func(self, name, *args):
        if name in self.names:
            return function(self, name, *args)
        else:
            similar = ss.more_similar(name, list(self.names))
            raise NameNotExists(f"The name {name} not exists, try ({', '.join(similar)})")

    return new_func


class GameflipItemsRequest:
    def __init__(self):
        self.items = self.request_all_item_information()
        self.names = self.get_all_names()

    def get_all_names(self) -> set[str]:
        return {item.name for item in self.items}

    @check_name
    def get_items_by_name(self, name) -> list[ItemGameflipApi]:
        result = filter(lambda item: item.name == name, self.items)
        return list(result)

    def get_item_by_name(self, name) -> ItemGameflipApi:
        return self.get_items_by_name(name)[0]

    @check_name
    def get_item_by_name_and_type(self, name, type_) -> ItemGameflipApi:
        Types(type_).validate()
        items = self.get_items_by_name(name)
        result = filter(lambda item: item.type == type_, items)
        try:
            return list(result)[0]
        except IndexError:
            types = {item.type for item in items}
            raise ItemHaventType(f"The item {name} havent type {type_}, try ({', '.join(types)}).")

    @staticmethod
    def request_all_item_information_json() -> dict:
        request = requests.get("https://gameflip.com/api/gameitem/inventory/812872018935")
        return json.loads(request.text)

    @classmethod
    def request_all_item_information(cls) -> list[ItemGameflipApi]:
        j = cls.request_all_item_information_json()
        items = j["data"]
        return [ItemGameflipApi(**i) for i in items]


class GameflipApi:
    def __init__(self):
        self.gameflip_items_request = GameflipItemsRequest()

    def rl_listing(self,
                   name: str,
                   description: str,
                   type_: str,
                   title: str = "",
                   id_: str = "",
                   color: str = "",
                   certification: str = "",
                   price: int = 75,
                   visibility: str = "onsale",
                   quantity: int = 1,
                   photo_url: str = "",
                   shipping_within_days: int = 1,
                   expire_in_days: int = 30
                   ):
        types = Types(type_)
        Colors(color).validate()
        Certification(certification).validate()
        ShippingWithinDays(shipping_within_days).validate()
        Visibility(visibility).validate()

        item = None
        if not photo_url:
            photo_url, item = self.get_item_attribute("icon_url", name, type_, item)
            if color and item.is_painted():
                photo_url = "https://gameflip.com" + item.get_color(color)["icon_url"]
            else:
                photo_url = "https://gameflip.com" + photo_url
        if not id_:
            id_, item = self.get_item_attribute("id", name, type_, item)
        if not title:
            title = name

        args = ["node", "rl_listing.js", photo_url, title, description, str(price), id_, types.to_tag_value(),
                str(quantity), str(shipping_within_days), str(expire_in_days), visibility, color, certification]

        process = subprocess.Popen(args, shell=False, env=os.environ.copy())
        process.wait()

    def get_item_attribute(self, attribute: str, name: str, type_: str, item: ItemGameflipApi or None = None) -> tuple:
        if item is None:
            item = self.gameflip_items_request.get_item_by_name_and_type(name, type_)
        return getattr(item, attribute), item


if __name__ == '__main__':
    with open("description.txt", "r", encoding="utf8") as file:
        description = file.read()
    gapi = GameflipApi()
    gapi.rl_listing("3-Lobe", description, "wheel", color="Saffron", certification="Sweeper", visibility="onsale")
