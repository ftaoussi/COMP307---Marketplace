from django.test import TestCase
from account.models import User

class UserModelTests(TestCase):

	def test_was_user_created(self):
		first_user = User.objects.create_user('johndoe', 'johndoe@gmail.com', 'johnpassword')
		self.assertIs(User.objects.filter(username='johndoe').exists(), True)

	def test_user_email_initialized(self): 
		first_user = User.objects.create_user('johndoe', 'johndoe@gmail.com', 'johnpassword')
		self.assertIs(first_user.email == 'johndoe@gmail.com', True)

	def test_user_password_initialized(self): 
		first_user = User.objects.create_user('johndoe', 'johndoe@gmail.com', 'johnpassword')
		self.assertIs(first_user.password is None, False)