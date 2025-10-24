import datetime
import typing
import requests
from gameflip_api.enums import ShippingPaidBy, Category, Platform, UPC, ListingStatus
import pyotp

from gameflip_api.params import GameflipAPIParams, IdParam, ListingsParams, PriceRange, DatetimeRange


class GameflipAPI:
    __api = 'https://production-gameflip.fingershock.com/api/v1'

    def __init__(self, api_key: str, secret: str) -> None:
        """
        Generates the totp to get authorization for requests.
        :param api_key: API Key is located at developer tab on your profile.
        :param secret: The secret is generated on API Key creation.
        """
        GameflipAPIParams(api_key=api_key, secret=secret)
        self.__api_key = api_key
        self.__secret = secret
        self.__totp = pyotp.TOTP(secret)

    def __get_auth_header(self) -> dict:
        return {"Authorization": f"GFAPI {self.__api_key}:{self.__totp.now()}"}

    def profile(self, id_: str = 'me') -> requests.Response:
        """
        Makes a request to the gameflip API to fetch user profile information, which you can get your own information.
        :param id_: The id is on the url of any profile, it usually starts with 'us-east' and ends with a bunt of numbers.
        To fetch data from your own profile you can set the id with 'me'.
        :raise pydantic.error_wrappers.ValidationError: If id_ is empty or not a string.
        :return: requests.Response
        """
        IdParam(id_=id_)
        return requests.get(f"{self.__api}/account/{id_}/profile", headers=self.__get_auth_header())

    def wallet_history(self) -> requests.Response:
        """
        Makes a request to the gameflip API to fetch your wallet history.
        :return: requests.Response
        """
        return requests.get(f"{self.__api}/account/me/wallet_history", headers=self.__get_auth_header())

    @staticmethod
    def get_rldata_items() -> requests.Response:
        """
        Makes a request to the gameflip API to fetch Rocket League items data.
        :return: requests.Response
        """
        return requests.get("https://gameflip.com/api/gameitem/inventory/812872018935")

    @classmethod
    def listing_search(
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
            created: typing.Optional[DatetimeRange] = None,
            updated: typing.Optional[DatetimeRange] = None,
            expiration: typing.Optional[DatetimeRange] = None,
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
            requests.Response: Returns a response object
        """
        listings_params = ListingsParams(term=term, category=category, platform=platform, genre=genre, upc=upc,
                                         shipping_paid_by=shipping_paid_by, digital=digital, status=status, owner=owner,
                                         condition=condition, condition_min=condition_min, price=price, created=created,
                                         updated=updated, expiration=expiration,
                                         seller_online_until=seller_online_until, tags=tags, start=start)
        return requests.get(f"{cls.__api}/listing", listings_params.model_dump(exclude_none=True))

    @classmethod
    def listing_of(cls, id_: str):
        """
        Makes a request to the gameflip API to fetch listing information.
        :param id_: The id is on the url of any listing, it usually made with a bunt of numbers.
        :raise pydantic.error_wrappers.ValidationError: If id_ is empty or not a string.
        :return: requests.Response
        """
        IdParam(id_=id_)
        return requests.get(f"{cls.__api}/listing/{id_}")