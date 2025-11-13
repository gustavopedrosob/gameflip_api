import re
from uuid import UUID

from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema


class AwsCognitoUUID(str):
    """
    Tipo customizado que valida strings no formato:
    <region>:<uuid>
    Exemplo: us-east-1:dc501f75-302c-4419-8ece-57974d688e6f
    """

    pattern = re.compile(
        r"^[a-z]{2}-[a-z]+-\d+:[0-9a-fA-F-]{36}$"
    )

    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type, _handler: GetCoreSchemaHandler):
        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.str_schema()
        )

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str):
            raise TypeError("valor should be string.")

        if not cls.pattern.match(value):
            raise ValueError("invalid format (expected '<region>:<uuid>')")

        # Valida se a parte após ':' é um UUID válido
        region, uuid_part = value.split(":", 1)
        try:
            UUID(uuid_part)
        except ValueError:
            raise ValueError("UUID invalid after ':'")

        return cls(value)


class Price(int):
    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type, _handler: GetCoreSchemaHandler):
        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.int_schema()
        )

    @classmethod
    def validate(cls, value):
        if not isinstance(value, int):
            raise TypeError("value should be int.")

        if value < 75:
            raise ValueError("value should be higher than 75.")

        return cls(value)