import pytest

pytestmark = pytest.mark.django_db

from order.factories import OrderFactory
from product.factories import ProductFactory

@pytest.mark.django_db
def test_order_creation():
    product = ProductFactory()
    order = OrderFactory(product=[product])
    
    assert order.product.count() == 1
    assert order.user.username is not None