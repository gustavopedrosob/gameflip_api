import datetime
import typing
import requests
from gameflip_api.enums import ShippingPaidBy, Category, Platform, UPC, ListingStatus
import pyotp


class PriceRange:
    def __init__(self, min_price: int, max_price: int):
        """
        :param min_price: An int higher than 75
        :param max_price: An int higher than 75
        """
        self.__min_price = min_price
        self.__max_price = max_price

    def __str__(self):
        return f"{self.__min_price},{self.__max_price}"


class DateRange:
    def __init__(self, min_date: datetime.datetime, max_date: datetime.datetime):
        self.__min_date = min_date
        self.__max_date = max_date

    def __str__(self):
        return f"{self.__format_date(self.__min_date)},{self.__format_date(self.__max_date)}"

    @staticmethod
    def __format_date(date: datetime.datetime):
        return date.isoformat(timespec='milliseconds') + "Z"


class GameflipAPI:
    __api = 'https://production-gameflip.fingershock.com/api/v1'


    def __init__(self, api_key: str, secret: str) -> None:
        if not api_key:
            raise ValueError("API key is required.")
        if not secret:
            raise ValueError("Secret is required.")
        self.__api_key = api_key
        self.__secret = secret
        self.__totp = pyotp.TOTP(secret)

    def profile(self, id_: str = 'me') -> requests.Response:
        if not id_:
            raise ValueError("Id is required.")
        headers = {"Authorization": f"GFAPI {self.__api_key}:{self.__totp.now()}"}
        response = requests.get(f"{self.__api}/account/{id_}/profile", headers=headers)
        return response

    def wallet_history(self) -> requests.Response:
        headers = {"Authorization": f"GFAPI {self.__api_key}:{self.__totp.now()}"}
        response = requests.get(f"{self.__api}/account/me/wallet_history", headers=headers)
        return response

    @staticmethod
    def get_rldata_items() -> requests.Response:
        response = requests.get("https://gameflip.com/api/gameitem/inventory/812872018935")
        return response

    @classmethod
    def listing(
            cls,
            term: typing.Optional[str] = None,
            category: typing.Optional[Category] = None,
            platform: typing.Optional[Platform] = None,
            genre: typing.Optional[str] = None,
            upc: typing.Optional[UPC] = None,
            shipping_paid_by: typing.Optional[ShippingPaidBy] = None,
            digital: typing.Optional[bool] = None,
            status: typing.Optional[ListingStatus] = None,
            owner: typing.Optional[str] = None,
            condition: typing.Optional[str] = None,
            condition_min: typing.Optional[str] = None,
            price: typing.Optional[PriceRange] = None,
            created: typing.Optional[DateRange] = None,
            updated: typing.Optional[DateRange] = None,
            expiration: typing.Optional[DateRange] = None,
            seller_online_until: typing.Optional[datetime.datetime] = None,
            tags: typing.Optional[str] = None,
            start: typing.Optional[int] = None
    ) -> requests.Response:
        """Makes a get to /api/v1/listing

        Args:
            term: Searches listing name and description and generates relevance score
            category: Filters category
            platform: Filters platform
            genre: Filters genre
            upc: Filters UPC (Universal Product Code), games in this case
            shipping_paid_by: Filters shipping paid by
            digital: Filters if it's a digital listing
            status: Filters status
            owner: Filters owner
            condition: Filters condition
            condition_min: Filters condition (any one value defined for condition)
            price: Filters price
            created: Filters in a range when it has been created
            updated: Filters in a range when it has been updated
            expiration: Filters in a range for its expiration
            seller_online_until: Filters sellers online
            tags: A special term filter which also allows logical AND using the carrot ^ operator in addition
                to logical OR with comma ,
                Precenence is given to OR operations over AND so that a filter like tags=a,b^c^d,e will match all
                listings that have (a OR b) AND (c) AND (d OR e).
            start: Gets listing by page number

        Returns:
            dict: Returns json listing from site
        """
        params = {}
        if term is not None: params["term"] = term
        if category is not None: params["category"] = category.value
        if platform is not None: params["platform"] = platform.value
        if genre is not None: params["genre"] = genre
        if upc is not None: params["upc"] = upc.value
        if shipping_paid_by is not None: params["shipping_paid_by"] = shipping_paid_by.value
        if digital is not None: params["digital"] = digital
        if status is not None: params["status"] = status.value
        if owner is not None: params["owner"] = owner
        if condition is not None: params["condition"] = condition
        if condition_min is not None: params["condition_min"] = condition_min
        if price is not None: params["price"] = str(price)
        if created is not None: params["created"] = str(created)
        if updated is not None: params["updated"] = str(updated)
        if expiration is not None: params["created"] = str(expiration)
        if seller_online_until is not None:
            params["seller_online_until"] = seller_online_until.isoformat(timespec='milliseconds') + "Z"
        if tags is not None: params["tags"] = tags
        if start is not None: params["start"] = start
        response = requests.get(f"{cls.__api}/listing", params)
        return response