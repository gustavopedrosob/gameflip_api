import requests
import pyotp

from gameflip_api.params import GameflipAPIParams, IdParam, ListingPostParams


class GameflipAPI:
    __api = 'https://production-gameflip.fingershock.com/api/v1'

    def __init__(self, api_key, secret):
        GameflipAPIParams(api_key=api_key, secret=secret)
        self.__api_key = api_key
        self.__secret = secret
        self.__totp = pyotp.TOTP(secret)

    def __get_auth_header(self):
        return {"Authorization": f"GFAPI {self.__api_key}:{self.__totp.now()}"}

    def profile(self, id_ = 'me'):
        IdParam(id_=id_)
        return requests.get(f"{self.__api}/account/{id_}/profile", headers=self.__get_auth_header())

    def wallet_history(self):
        return requests.get(f"{self.__api}/account/me/wallet_history", headers=self.__get_auth_header())

    @staticmethod
    def get_rldata_items():
        return requests.get("https://gameflip.com/api/gameitem/inventory/812872018935")

    @classmethod
    def listing_search(
            cls,
            params = None,
            **kwargs
    ):
        if params is None:
            params = ListingPostParams(**kwargs)
        return requests.get(f"{cls.__api}/listing", params.model_dump(exclude_none=True))

    def my_listing_search(
            self,
            params = None,
            **kwargs
    ):
        if params is None:
            params = ListingPostParams(**kwargs)
        return requests.get(f"{self.__api}/listing", params.model_dump(exclude_none=True),
                            headers=self.__get_auth_header())

    @classmethod
    def listing_of(cls, id_):
        IdParam(id_=id_)
        return requests.get(f"{cls.__api}/listing/{id_}")

    def my_listing_of(self, id_):
        IdParam(id_=id_)
        return requests.get(f"{self.__api}/listing/{id_}", headers=self.__get_auth_header())

    def listing_post(
            self,
            params = None,
            **kwargs
    ):
        if params is None:
            params = ListingPostParams(**kwargs)
        return requests.post(
            f"{self.__api}/listing",
            params.model_dump(exclude_none=True),
            headers=self.__get_auth_header()
        )
