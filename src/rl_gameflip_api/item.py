from io import BytesIO
from tempfile import SpooledTemporaryFile
from PIL import Image
from requests import get
from shutil import copyfileobj
from dataclasses import dataclass, field
from rl_data_utils.name.name import ABCName
from rl_data_utils.rarity.rarity import ABCRarity
from rl_data_utils.type.type import ABCType
from rl_data_utils.color.color import ABCColor


def get_image(url: str):
    buffer = SpooledTemporaryFile(max_size=1000000000)
    request = get(url, stream=True)
    downloaded = 0
    for chunk in request.iter_content(chunk_size=1024):
        downloaded += len(chunk)
        buffer.write(chunk)
    buffer.seek(0)
    return Image.open(BytesIO(buffer.read()))


def save_image(url, path):
    request = get(url, stream=True)
    with open(path, 'wb') as file:
        request.raw.decode_content = True
        copyfileobj(request.raw, file)


@dataclass
class Item(ABCName, ABCRarity, ABCType, ABCColor):
    id: str
    name: str
    rarity: str
    platform: str
    icon: str
    type: str
    icon_url: str
    color: str
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

    def get_color(self):
        return self.color

    def set_color(self, color: str):
        self.color = color

    def get_image(self) -> Image:
        return get_image("https://gameflip.com" + self.icon_url)

    def save_image(self, path):
        return save_image("https://gameflip.com" + self.icon_url, path)
