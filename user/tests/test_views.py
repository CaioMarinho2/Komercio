from user.models import User
from rest_framework.test import APITestCase


class UserViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        
        cls.user_adm_data = {
         "username": "chan",
         "password": "abcd",
         "first_name": "chrystian",
         "last_name": "rodolfo",
         "is_seller": False,
         "is_superuser": True
         }
        
        cls.user_seller_data = {
         "username": "mark",
         "password": "abcd",
         "first_name": "Mark",
         "last_name": "Douglas",
         "is_seller": True,
         "is_superuser": False
         }
        
        cls.user_not_seller_data = {
         "username": "andy",
         "password": "abcd",
         "first_name": "Andreson",
         "last_name": "Junior",
         "is_seller": False,
         "is_superuser": False
         }  
        
        cls.user_seller_login_data={
            "username": "mark",
            "password": "abcd",
        }
        
        cls.user_not_seller_login_data={
            "username": "andy",
            "password": "abcd",
        }
        
    def user_seller_account_create(self):
        """Verifica se a criação de um usuário vendedor está funcionando """
        response= self.client.post("/api/accounts/",self.user_seller_data,format='json')
        expected_status=201
        
        self.assertEqual(expected_status,response.status_code)  
        self.assertEqual(response.data["is_seller"],True)
        
    def user_not_seller_account_create(self):
        """Verifica se a criação de um usuário vendedor está funcionando """
        response= self.client.post("/api/accounts/",self.user_not_seller_data,format='json')
        expected_status=201
        
        self.assertEqual(expected_status,response.status_code)  
        self.assertEqual(response.data["is_seller"],False)
    
    
    def wrong_keys_create(self):
        """Verifica se a criação de um usuário vendedor está funcionando """
        response= self.client.post("/api/accounts/",{},format='json')
        expected_status=400
        
        self.assertEqual(expected_status,response.status_code)
        
    def user_seller_account_login(self):
        """Verifica se o login de um usuário vendedor está funcionando """
        response= self.client.post("/api/login/",self.user_seller_login_data,format='json')
        expected_status=200
        
        self.assertEqual(expected_status,response.status_code)  
        self.assertIn("token",response.data)
        
    def user_not_seller_account_login(self):
        """Verifica se o login de um usuário vendedor está funcionando """
        response= self.client.post("/api/login/",self.user_not_seller_login_data,format='json')
        expected_status=200
        
        self.assertEqual(expected_status,response.status_code)  
        self.assertIn("token",response.data)     
        
    def update_another_account(self):
        ...
        
    def admin_desactivate_account(self):
        ...
        
    def update_activate_account(self):
        ...
    
    def list_users(self):
        response =self.client.get("/api/accounts/")
        expected_status=200
        
        self.assertEqual(expected_status,response.status_code)  
        
        
                        
               
         
         