import datetime
import os

import pytest
from pydantic import ValidationError
from dotenv import load_dotenv
from gameflip_api import GameflipAPI
from gameflip_api.params import PriceRange, Range, ListingSearchParams, DatetimeRange

load_dotenv()


def test_listings_success():
    assert GameflipAPI.listing_search().status_code == 200


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


@pytest.mark.parametrize("value", [0, 0.1, [], {}, set()])
def test_profile_id_type_error(value):
    with pytest.raises(ValidationError):
        api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
        # noinspection PyTypeChecker
        api.profile(value)


def test_empty_listing_id_error():
    with pytest.raises(ValidationError):
        api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
        api.listing_of("")


@pytest.mark.parametrize("value", [0, 0.1, [], {}, set()])
def test_listing_id_type_error(value):
    with pytest.raises(ValidationError):
        api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
        # noinspection PyTypeChecker
        api.listing_of(value)


def test_empty_api_key_error():
    with pytest.raises(ValidationError):
        GameflipAPI("", os.getenv('SECRET'))


@pytest.mark.parametrize("value", [0, 0.1, [], {}, set()])
def test_api_key_type_error(value):
    with pytest.raises(ValidationError):
        # noinspection PyTypeChecker
        GameflipAPI(value, os.getenv('SECRET'))


def test_empty_secret_error():
    with pytest.raises(ValidationError):
        GameflipAPI(os.getenv("KEY_API"), "")


@pytest.mark.parametrize("value", [0, 0.1, [], {}, set()])
def test_secret_type_error(value):
    with pytest.raises(ValidationError):
        GameflipAPI(os.getenv("KEY_API"), "")


def test_any_listing_success():
    assert GameflipAPI.listing_of("44e45372-b6f1-4400-af78-419c29243d6c").status_code == 200


def test_listings_invalid_price_range_error():
    with pytest.raises(ValidationError):
        GameflipAPI.listing_search(price=PriceRange(start=0, end=100))


@pytest.mark.parametrize(
    "start, end",
    [
        (100, 10),
        (datetime.datetime(2025, 1, 1), datetime.datetime(2024, 1, 1))
    ]
)
def test_invalid_range(start, end):
    with pytest.raises(ValidationError):
        Range(start=start, end=end)


def test_listing_formats():
    datetime_1 = datetime.datetime(2025, 1, 1)
    datetime_2 = datetime.datetime(2025, 1, 1, 12)
    datetime_range = DatetimeRange(start=datetime_1, end=datetime_2)
    expected_datetime_string = '2025-01-01T00:00:00.000Z,2025-01-01T12:00:00.000Z'
    listing_params = ListingSearchParams(price=PriceRange(start=75, end=100), created=datetime_range, updated=datetime_range, expiration=datetime_range, seller_online_until=datetime_range)
    params = listing_params.model_dump()
    assert (params['price'] == '75,100' and params['created'] == expected_datetime_string and
            params['updated'] == expected_datetime_string and params['expiration'] == expected_datetime_string and
            params['seller_online_until'] == expected_datetime_string)


def test_listing_post_success():
    api = GameflipAPI(os.getenv('KEY_API'), os.getenv('SECRET'))
    result = api.listing_post()
    assert result.status_code == 200