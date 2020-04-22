from django.test import TestCase
from account.models import User
from product_listing.models import Product, Category, Subcategory, Neighborhood
from django.utils import timezone

class ProductModelTests(TestCase):

	def test_was_product_created(self):
		category = Category(name="clothing")
		category.save()

		subcategory = Subcategory(name="hoodies")
		subcategory.parent_category = category
		subcategory.save()

		neighborhood = Neighborhood(name="downtown")
		neighborhood.save()

		user = User.objects.create_user('johndoe', 'johndoe@gmail.com', 'johnpassword')

		first_product = Product(
			name = "Lit T-Shirt",
			seller = user,
			price_current = 12,
			price_initial = 12,
			category = category,
			subcategory = subcategory,
			location = neighborhood,
			time = timezone.now(),
			description = "it's a lit t-shirt",
			stock = 2,
			size = 'M'
			)
		first_product.save()
		self.assertIs(Product.objects.filter(name="Lit T-Shirt").exists(), True)