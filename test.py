import os

import pytest

from gameflip_api import GameflipAPI


def test_listings_success():
    assert GameflipAPI.listings().status_code == 200


def test_my_profile_success():
    api = GameflipAPI(os.getenv('key_api'), os.getenv('secret'))
    assert api.profile().status_code == 200


def test_any_profile_success():
    api = GameflipAPI(os.getenv('key_api'), os.getenv('secret'))
    assert api.profile('us-east-1:dc501f75-302c-4419-8ece-57974d688e6f').status_code == 200


def test_any_listing_success():
    assert GameflipAPI.listing("44e45372-b6f1-4400-af78-419c29243d6c").status_code == 200


if __name__ == '__main__':
    pytest.main([__file__])