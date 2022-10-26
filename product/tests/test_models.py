from django.test import TestCase
from product.models import Product
from user.models import User

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        
        cls.user_data={
        "username": "ale23",
        "password": "abcd",
        "first_name": "alexandre23",
        "last_name": "alves23",
        "is_seller": True,
        }
        
        cls.product ={
        "description": "Mouse Redragon",
        "price": 100.99,
        "quantity": 2
        }
        cls.ale23_user= User.objects.create_user(**cls.user_data)
        cls.product1_created= Product.objects.create(**cls.product, seller=cls.ale23_user)
        
    def test_max_digits_and_decimals(self):
        
        """Verifica se o tamanho maximo de digitos de um numero e os decimais estão funcionando corretamente """
        
        result_max_digits= Product._meta.get_field("price").max_digits
        result_decimal_places= Product._meta.get_field("price").decimal_places
        msg="verifique se a propriedade `max_digits` foi definida como o esperado "
        msg2="verifique se a propriedade `decimals` foi definida como o esperado "
        expected_max_digits=10
        expected_decimals=2
        
        self.assertEqual( expected_max_digits,result_max_digits,msg)
        self.assertEqual(expected_decimals,result_decimal_places,msg2)
             