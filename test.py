import os

import pytest
from pydantic import ValidationError
from dotenv import load_dotenv
from gameflip_api import GameflipAPI


load_dotenv()


def test_listings_success():
    assert GameflipAPI.listings().status_code == 200


def test_my_profile_success():
    api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
    assert api.profile().status_code == 200


def test_any_profile_success():
    api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
    assert api.profile('us-east-1:dc501f75-302c-4419-8ece-57974d688e6f').status_code == 200


def test_empty_profile_id_error():
    with pytest.raises(ValidationError):
        api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
        api.profile("")


def test_wrong_type_profile_id_error():
    with pytest.raises(ValidationError):
        api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
        api.profile(0)


def test_empty_listing_id_error():
    with pytest.raises(ValidationError):
        api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
        api.listing("")


def test_wrong_type_listing_id_error():
    with pytest.raises(ValidationError):
        api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
        api.listing(0)


def test_any_listing_success():
    assert GameflipAPI.listing("44e45372-b6f1-4400-af78-419c29243d6c").status_code == 200


if __name__ == '__main__':
    pytest.main([__file__])