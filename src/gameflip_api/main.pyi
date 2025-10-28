import datetime
import typing
from pathlib import Path
from uuid import UUID

import pyotp
import requests

from gameflip_api.enums import ShippingPaidBy, Category, Platform, UPC, ListingStatus, AcceptCurrency, Visibility
from gameflip_api.params import PriceRange, DatetimeRange, ListingSearchParams, ListingPostParams, Op


class GameflipAPI:
    __api: str
    __api_key: str
    __secret: str
    __totp: pyotp.totp.TOTP

    def __init__(self, api_key: str, secret: str) -> None:
        """
        Generates the totp to get authorization for requests.
        :param api_key: API Key is located at developer tab on your profile.
        :param secret: The secret is generated on API Key creation.
        """
        ...

    def __get_auth_header(self) -> dict: ...

    def profile(self, uuid: typing.Union[str, UUID] = 'me') -> requests.Response:
        """
        Makes a request to the gameflip API to fetch user profile information, which you can get your own information.
        :param uuid: The id is on the url of any profile, it usually starts with 'us-east' and ends with a bunt of numbers.
        To fetch data from your own profile you can set the id with 'me'.
        :raise pydantic.error_wrappers.ValidationError: If id_ is empty or not a string.
        :return: requests.Response
        """
        ...

    def wallet_history(self) -> requests.Response:
        """
        Makes a request to the gameflip API to fetch your wallet history.
        :return: requests.Response
        """
        ...

    @staticmethod
    def get_rldata_items() -> requests.Response:
        """
        Makes a request to the gameflip API to fetch Rocket League items data.
        :return: requests.Response
        """
        ...

    @classmethod
    @typing.overload
    def listing_search(cls, params: ListingSearchParams) -> requests.Response: ...

    @classmethod
    @typing.overload
    def listing_search(
        cls,
        *,
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
        """ Makes a get to /api/v1/listing

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
                Precedence is given to OR operations over AND so that a filter like tags=a,b^c^d,e will match all
                listings that have (a OR b) AND (c) AND (d OR e).
            start: Gets listing by page number

        Returns:
            requests.Response: Returns a response object
        """
        ...

    @typing.overload
    def my_listing_search(self, params: ListingSearchParams) -> requests.Response: ...

    @typing.overload
    def my_listing_search(
        self,
        *,
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
        start: typing.Optional[int] = None,
    ) -> requests.Response:
        """ Makes a get to /api/v1/listing

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
                Precedence is given to OR operations over AND so that a filter like tags=a,b^c^d,e will match all
                listings that have (a OR b) AND (c) AND (d OR e).
            start: Gets listing by page number

        Returns:
            requests.Response: Returns a response object
        """
        ...

    @classmethod
    def listing_of(cls, uuid: typing.Union[str, UUID]) -> requests.Response:
        """
        Makes a request to the gameflip API to fetch listing information.
        :param uuid: The id is on the url of any listing, it usually made with a bunt of numbers.
        :raise pydantic.error_wrappers.ValidationError: If id_ is empty or not a string.
        :return: requests.Response
        """
        ...

    def my_listing_of(self, uuid: typing.Union[str, UUID]) -> requests.Response:
        """
        Makes a request to the gameflip API to fetch listing information. Can fetch your own private listing.
        :param uuid: The id is on the url of any listing, it usually made with a bunt of numbers.
        :raise pydantic.error_wrappers.ValidationError: If id_ is empty or not a string.
        :return: requests.Response
        """
        ...

    @typing.overload
    def listing_post(self, params: ListingPostParams) -> requests.Response: ...

    @typing.overload
    def listing_post(
        self,
        *,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        price: typing.Optional[int] = None,
        category: typing.Optional[Category] = None,
        upc: typing.Optional[UPC] = None,
        accept_currency: AcceptCurrency = AcceptCurrency.USD,
        digital: bool = False,
        visibility: Visibility = Visibility.PUBLIC
    ) -> requests.Response:
        """
        Makes a post to /api/v1/listing to create a new listing
        :param name: Name of listing
        :param description: Description of listing
        :param price: Price of listing
        :param category: Category of listing
        :param upc: UPC of listing
        :param accept_currency: Accept currency of the listing
        :param digital: Specifies if it's a digital listing
        :param visibility: Visibility of listing
        :raise pydantic.error_wrappers.ValidationError: If some parameter is not correct type or price is invalid
        :return: requests.Response
        """
        ...

    def listing_delete(self, uuid: typing.Union[str, UUID]) -> requests.Response:
        """
        Makes a request to the gameflip API to delete a listing
        :param uuid: The id of the listing
        :return: requests.Response
        """
        ...

    def listing_patch(self, uuid: typing.Union[str, UUID], ops: typing.List[typing.Union[Op, typing.Dict]]) -> requests.Response:
        """
        Makes a request to the gameflip API to update a listing
        :param uuid: The id of the listing
        :param ops: Operations to apply
        :return: requests.Response
        """
        ...

    def post_photo(self, listing_uuid: typing.Union[str, UUID], photo: typing.Union[str, Path], display_order: int):
        """
        Makes a serie of requests to update a listing photo
        :param listing_uuid: The id of the listing
        :param photo: Url or Path for the photo
        :param display_order: Display order of the photo
        :raise TypeError: photo is not a string or a Path
        :raise HTTPError: some request goes wrong
        :raise FileNotFoundError: photo path not found or don't exist
        :return: None
        """
        ...