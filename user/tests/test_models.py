from django.core.exceptions import ValidationError
from django.test import TestCase

from user.models import User

from product.models import Product


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        
        cls.user_data={
        "username": "ale",
        "password": "abcd",
        "first_name": "alexandre",
        "last_name": "alves",
        "is_seller": True,
        }
        
        cls.user_duplicated_data= {
            "username": "ale", 
            "password": "abcd", 
            "first_name": "alexandre", 
            "last_name": "alves", 
            "is_seller": True, 
                            }
        cls.ale_user= User.objects.create_user(**cls.user_data)
    
         
    def test_max_lenght(self):
         """Verifica se o tamanho maximo de username,firts_name e last_name está funcionando corretamente """
         result_max_length_first_name= User._meta.get_field("first_name").max_length
         result_max_length_last_name= User._meta.get_field("last_name").max_length
         msg="verifique se a propriedade `max_length` de foi definida como o esperado "
         expected_max_length=50 
         self.assertEqual(expected_max_length,result_max_length_first_name,msg)
         self.assertEqual(expected_max_length,result_max_length_last_name,msg)     
         
    def test_if_duplicated_username_User_can_be_created(self):
        """Verifica se o pode criar dois users com o mesmo username"""
        duplicated_user= User(**self.user_duplicated_data)
        
        expected_message='User with this Username already exists.'
      
        with self.assertRaisesMessage(ValidationError,expected_message): 
            duplicated_user.full_clean()     
            
class UserRelationshipTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_data={
        "username": "Marcinho",
        "password": "abcd",
        "first_name": "Marcio",
        "last_name": "Silva",
        "is_seller": True,
        }
        
        cls.product1 ={
        "description": "Smartband XYZ 3.0",
        "price": 100.99,
        "quantity": 15
        }
        
        cls.product2 ={
        "description": "Tv Sansung",
        "price": 500.99,
        "quantity": 2
        }
        
        cls.product3 ={
        "description": "Smart Watch",
        "price": 200.99,
        "quantity": 7
        }
        
        cls.marcio_user= User.objects.create_user(**cls.user_data)
        
        cls.product1_created= Product.objects.create(**cls.product1, seller=cls.marcio_user)
        cls.product2_created= Product.objects.create(**cls.product2, seller=cls.marcio_user)
        cls.product3_created= Product.objects.create(**cls.product3, seller=cls.marcio_user)
    
    def test_one_to_many_relashionship_with_Products(self):   
            """Verifica se a quantidade de produtos para o usuario está correta  """
            
            expected_products_quantity= 3 
            msg=f"verifique se os produtos estão sendo associados corretamente aos usuários "
            result_products_quantity=  self.marcio_user.products.count()
            self.assertEqual(expected_products_quantity,result_products_quantity,msg)     
            
            