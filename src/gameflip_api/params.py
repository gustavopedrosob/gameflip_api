import datetime
import typing
from uuid import UUID

from pydantic import BaseModel, Field, field_validator
from pydantic_core.core_schema import ValidationInfo

from gameflip_api.enums import Category, Platform, UPC, ShippingPaidBy, ListingStatus, AcceptCurrency, Visibility, \
    ListingOps

T = typing.TypeVar("T")

class Range(BaseModel, typing.Generic[T]):
    start: T
    end: T

    @field_validator("end", mode="after")
    @classmethod
    def check_end_after_start(cls, value: int, info: ValidationInfo) -> int:
        if "start" in info.data and value < info.data["start"]:
            raise ValueError("start must be greater or equal to end.")
        return value

    def __str__(self):
        return f"{self.start},{self.end}"


class IntRange(Range[int]):
    pass


class PriceRange(Range[int]):
    @field_validator("start", "end")
    @classmethod
    def must_be_greater_or_equal_to_75(cls, v):
        if v < 75:
            raise ValueError("start and end must be greater or equal to 75.")
        return v


class DatetimeRange(Range[datetime.datetime]):
    def __str__(self):
            return f"{self.__format_datetime(self.start)},{self.__format_datetime(self.end)}"

    @staticmethod
    def __format_datetime(datetime_: datetime.datetime):
        return datetime_.isoformat(timespec='milliseconds') + "Z"


class ListingSearchParams(BaseModel):
    term: typing.Optional[str] = None
    category: typing.Optional[Category] = None
    platform: typing.Optional[Platform] = None
    genre: typing.Optional[str] = None
    upc: typing.Optional[UPC] = None
    shipping_paid_by: typing.Optional[ShippingPaidBy] = None
    digital: typing.Optional[bool] = None
    status: typing.Optional[ListingStatus] = None
    owner: typing.Optional[str] = None
    condition: typing.Optional[str] = None
    condition_min: typing.Optional[str] = None
    price: typing.Optional[PriceRange] = None
    created: typing.Optional[DatetimeRange] = None
    updated: typing.Optional[DatetimeRange] = None
    expiration: typing.Optional[DatetimeRange] = None
    seller_online_until: typing.Optional[DatetimeRange] = None
    tags: typing.Optional[str] = None
    start: typing.Optional[int] = None

    def model_dump(self, *args, **kwargs):
        d = super().model_dump(*args, **kwargs)
        for attr in ["price", "created", "updated", "expiration", "seller_online_until"]:
            if d.get(attr) is not None:
                d[attr] = str(getattr(self, attr))
        return d


class ListingPostParams(BaseModel):
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    price: typing.Optional[int] = Field(None, gt=74, description="Price of item")
    category: typing.Optional[Category] = None
    upc: typing.Optional[UPC] = None
    accept_currency: AcceptCurrency = AcceptCurrency.USD
    digital: bool = False
    visibility: Visibility = Visibility.PUBLIC


class GameflipAPIParams(BaseModel):
    api_key: str = Field(..., min_length=1, description="API key is required.")
    secret: str = Field(..., min_length=1, description="Secret is required.")


class UUIDParam(BaseModel):
    uuid: UUID


class Op(BaseModel):
    op: ListingOps
    path: str
    value: typing.Any


class ExchangeParams(BaseModel):
    role: typing.Optional[ShippingPaidBy] = None
    id: typing.Optional[UUID] = None
    name: typing.Optional[str] = None
    buyer: typing.Optional[str] = None
    seller: typing.Optional[str] = None
    price: typing.Optional[PriceRange] = None
    risk: typing.Optional[IntRange] = None
    status: typing.Optional[ListingStatus] = None
    buyer_rated : typing.Optional[bool] = None
    seller_rated : typing.Optional[bool] = None
    start: typing.Optional[int] = None
    category: typing.Optional[Category] = None
    upc: typing.Optional[UPC] = None
    digital: typing.Optional[bool] = None
    escrow: typing.Optional[bool] = None
    settled: typing.Optional[DatetimeRange] = None
    shipped: typing.Optional[DatetimeRange] = None
    received: typing.Optional[DatetimeRange] = None
    auto_rate_after: typing.Optional[DatetimeRange] = None
    created: typing.Optional[DatetimeRange] = None
    updated: typing.Optional[DatetimeRange] = None
    version: typing.Optional[int] = None
    limit: typing.Optional[int] = None


class ExchangePostParams(BaseModel):
    listing_id: UUID
    source_id: UUID
    address_id: UUID