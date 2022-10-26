from rest_framework.test import APITestCase
from user.models import User
from product.models import Product

class ProductViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ...