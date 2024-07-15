from uuid import UUID
from pydantic import ValidationError
import pytest

from store.schemas.product import ProductIn
from tests.schemas.factories import product_data


def test_schemas_validated():
    data = product_data()

    product = ProductIn(**data)
    # equivalente = ProductIn.model_validate(data) teste
    assert product.name == "Iphone 14 pro Max"
    assert isinstance(product.id, UUID)


def test_schemas_return_raises():
    data = {"name": "Iphone 14 pro Max", "quantity": 18, "price": 5000}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14 pro Max", "quantity": 18, "price": 5000},
        "url": "https://errors.pydantic.dev/2.8/v/missing",
    }
