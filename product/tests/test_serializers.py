import pytest

pytestmark = pytest.mark.django_db

from product.factories import ProductFactory, CategoryFactory
from product.serializers import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    category = CategoryFactory(title="Ficção")
    product = ProductFactory(title="Dom Casmurro", price=50, category=[category])
    serializer = ProductSerializer(product)

    assert serializer.data['title'] == "Dom Casmurro"
    assert serializer.data['price'] == 50