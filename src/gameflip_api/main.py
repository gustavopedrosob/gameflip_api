from pathlib import Path

import requests
import pyotp

from gameflip_api.enums import ListingOps, ListingPhotoStatus
from gameflip_api.params import GameflipAPIParams, IdParam, ListingPostParams, Op
import validators


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
    def listing_search(cls, params = None, **kwargs):
        if params is None:
            params = ListingPostParams(**kwargs)
        return requests.get(f"{cls.__api}/listing", params.model_dump(exclude_none=True))

    def my_listing_search(self, params = None, **kwargs):
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

    def listing_post(self, params = None, **kwargs):
        if params is None:
            params = ListingPostParams(**kwargs)
        return requests.post(
            f"{self.__api}/listing",
            params.model_dump(exclude_none=True),
            headers=self.__get_auth_header()
        )

    def listing_delete(self, id_):
        IdParam(id_=id_)
        return requests.delete(f"{self.__api}/listing/{id_}", headers=self.__get_auth_header())

    def listing_patch(self, id_, ops):
        IdParam(id_=id_)
        ops_objects = map(lambda op: op if isinstance(op, Op) else Op(**op), ops)
        ops_json = list(map(lambda op: op.model_dump(mode="json"), ops_objects))
        headers = {"Content-Type": "application/json-patch+json"}
        headers.update(self.__get_auth_header())
        return requests.patch(f"{self.__api}/listing/{id_}", json=ops_json, headers=headers)

    def post_photo(self, listing_id, photo, display_order):
        if not (isinstance(photo, Path) or isinstance(photo, str)):
            raise TypeError("Photo must be of type Path or str.")

        if isinstance(photo, str) and validators.url(photo):
            photo_request = requests.get(photo)
            photo_request.raise_for_status()
            photo_data = photo_request.content
            mime_type = photo_request.headers.get("Content-Type", "application/octet-stream")
        else:
            if isinstance(photo, Path):
                photo_path = photo
            else:
                photo_path = Path(photo)
            if not photo_path.exists() or not photo_path.is_file():
                raise FileNotFoundError(f"File not found: {photo}")
            photo_data = open(photo_path, "rb")
            mime_type = photo_path.suffix[1:]

        post_photo_request = requests.post(f"{self.__api}/listing/{listing_id}/photo", headers=self.__get_auth_header())
        post_photo_request.raise_for_status()
        post_photo_data = post_photo_request.json()['data']
        upload_photo_url = post_photo_data['upload_url']
        photo_id = post_photo_data['id']

        put_photo_headers = {'Content-Type': f'image/{mime_type}'}
        put_photo_request = requests.put(upload_photo_url, headers=put_photo_headers, data=photo_data)
        put_photo_request.raise_for_status()

        ops = [Op(op=ListingOps.REPLACE, path=f'/photo/{photo_id}/status', value=ListingPhotoStatus.ACTIVE)]

        if display_order >= 0:
            ops.append(Op(op=ListingOps.REPLACE, path=f'/photo/{photo_id}/display_order', value=display_order))
        else:
            ops.append(Op(op=ListingOps.REPLACE, path=f'/cover_photo', value=photo_id))

        listing_patch_request = self.listing_patch(listing_id, ops)
        listing_patch_request.raise_for_status()
