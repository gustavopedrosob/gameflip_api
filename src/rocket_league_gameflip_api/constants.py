import typing

SEVEN: typing.Literal[7] = 7
FOURTEEN: typing.Literal[14] = 14
THIRTY: typing.Literal[30] = 30
FORTY_FIVE: typing.Literal[45] = 45
NINETY: typing.Literal[90] = 90
ONE_HUNDRED_AND_EIGHTY: typing.Literal[180] = 180
EXPIRE_IN_DAYS = (SEVEN, FOURTEEN, THIRTY, FORTY_FIVE, NINETY, ONE_HUNDRED_AND_EIGHTY)

ONE: typing.Literal[1] = 1
TWO: typing.Literal[2] = 2
THREE: typing.Literal[3] = 3
SHIPPING_WITHIN_DAYS = (ONE, TWO, THREE)

DRAFT: typing.Literal["draft"] = "draft"
READY: typing.Literal["ready"] = "ready"
ON_SALE: typing.Literal["onsale"] = "onsale"
VISIBILITY = (DRAFT, READY, ON_SALE)
