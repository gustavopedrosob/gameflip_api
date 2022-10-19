from dataclasses import dataclass, field
from rl_data_utils.name.name import ABCName
from rl_data_utils.rarity.rarity import ABCRarity
from rl_data_utils.type.type import ABCType
from rl_data_utils.color.list_color import ABCListColor
from rl_gameflip_api.item import Item
from rl_data_utils.color import is_default
from rl_data_utils.item.item_data import ABCItemData


@dataclass
class ItemData(ABCItemData, ABCName, ABCRarity, ABCType, ABCListColor):
    id: str
    name: str
    rarity: str
    platform: str
    icon: str
    type: str
    icon_url: str
    colors: list = field(default_factory=list)
    customizable: bool = field(default=None)
    unit: str = field(default='')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_rarity(self):
        return self.rarity

    def set_rarity(self, rarity: str):
        self.rarity = rarity

    def get_type(self):
        return self.type

    def set_type(self, type_: str):
        self.type = type_

    def get_list_color(self) -> list[str]:
        return [color['name'] for color in self.colors]

    def get_color_info(self, color: str) -> dict:
        for data in self.colors:
            if data['name'] == color:
                return data

    def is_painted(self) -> bool:
        return bool(self.colors)

    def to_item(self, color: str = None):
        if color and not is_default(color):
            data_color = self.get_color_info(color)
            icon = data_color['icon']
            icon_url = data_color['icon_url']
        else:
            color = "Default"
            icon = self.icon
            icon_url = self.icon_url
        return Item(self.id, self.name, self.rarity, self.platform, icon, self.type, icon_url, color, self.customizable,
                    self.unit)
