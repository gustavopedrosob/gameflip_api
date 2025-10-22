import os

import pytest

from gameflip_api import GameflipAPI


def test_listing():
    assert GameflipAPI.listing().status_code == 200


def test_my_profile():
    api = GameflipAPI(os.getenv('key_api'), os.getenv('secret'))
    assert api.profile().status_code == 200


def test_any_profile():
    api = GameflipAPI(os.getenv('key_api'), os.getenv('secret'))
    assert api.profile('us-east-1:dc501f75-302c-4419-8ece-57974d688e6f').status_code == 200


if __name__ == '__main__':
    pytest.main([__file__])