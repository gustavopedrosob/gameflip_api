from rl_gameflip_api.items import Items
from rl_gameflip_api.item_data import Item
from subprocess import Popen
from os import environ


class GameflipRlListing:
    def __init__(self):
        self.items = Items.from_request()

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

        process = Popen(args, shell=False, env=environ.copy())
        process.wait()

    def get_item_attribute(self, attribute: str, name: str, type_: str, item: Item or None = None) -> tuple:
        if item is None:
            item = self.items.get_item_by_name_and_type(name, type_)
        return getattr(item, attribute), item
