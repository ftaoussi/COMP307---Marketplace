from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from product_listing.models import Order
import datetime

# Create your views here.
def index(request):
	context={}
	if (user.is_authenticated()):
		carts = Cart.objects.filter(user=request.user)
		if carts is not None: 
			cart = carts.first()
			context['cart'] = cart
			context['items'] = Item.objects.filter(cart=cart)
		else:
			cart = Cart(user=request.user)
			cart.save()
			context['cart'] = cart
		return reverse(request, 'cart.html', context)
	else:
		return redirect('login.html')


def viewCart(request): 
	context={}
	user = request.user
	cart = Cart.objects.get(user=user)
	context['cart'] = cart
	context['items'] = Item.objects.get(cart=cart)
	return render(request, "cart.html", context)

def modifyCart(request, action, product_id, option):
	context = {}
	if request.user.is_authenticated:
		userCart = Cart.objects.filter(user=request.user)
		if userCart is None:
			cart=Cart(user=request.user)
			cart.save()
		if (action=='add'):
			add_to_cart(request, product_id, option)
		else if (action=='remove'):
			remove_from_cart(request, product_id, option)
		else if (action=='clear'):
			clear_cart(request)
		else:
			return HttpResponse("Error")
		context={}
		user = request.user
		context['cart'] = userCart
		context['items'] = Item.objects.filter(cart=userCart)
	else:
		return reverse(request, 'login.html', context)
	return redirect(request.path_info, context)

def add_to_cart(request, product_id, quantity):
	product = Product.objects.get(id=product_id)
	this_user = request.user
	user_carts = Cart.objects.filter(user=user)
	if user_carts is None:
		user_cart = user_carts.first()
		user_cart = Cart(user=this_user)
		user_cart.save()
	item = Item(
		product=product
		cart=user_cart
		quantity= quantity
		unit_price= product.price_current
	)
	item.save()

def remove_from_cart(request, product_id, quantity):
	cart = Cart.objects.get(user=request.user)
	items = Item.objects.filter(product=product_id, cart=cart)
	if items is not None:
		item = items.first()
		if (item.quantity > quantity):
			item.quantity = item.quantity-quantity
		else:
			item.delete()

def clear_cart(request):
	cart = Cart.objects.get(user=request.user)
	cart.delete()


def checkout(request):
	context={}
	if (!request.user.is_authenticated()):
		return reverse(request, 'login.html',context)
	cart = Cart.objects.get(user=request.user)
	user = request.user
	baskets = []
	if method=='POST':
		form = forms.ShippingForm(request.POST)
		if form.is_valid():
			try:
				shipaddr = form.cleaned_data['street_address']+", "+form.cleaned_data['postcode']
				for item in cart.item.set_all():
					total = 0
					for basket in baskets:
						if (basket.seller != item.seller):
							total += 1
						else:
							thisBasket = basket
					if (total = baskets.size()):
						thisBasket = Basket(
							seller = item.seller
							buyer = user
							time = datetime.datetime.now()
							shipping_to = shipaddr
						)
						thisBasket.save()
						baskets.append(thisBasket)
						
					orderItem = OrderItem(
						product_string = item.__str__()
						unit_price = item.price
						product = item
						buyer = user
						seller = item.seller
						basket = thisBasket
						quantity = item.quantity
						shipping_to = shipaddr
					)
					orderItem.save()
					product = item.product
					product.stock -= item.quantity
	else:
		context['form'] = forms.ShippingForm
		return reverse(request, 'checkout.html', context)
	return reverse(request, 'checkoutsuccess.html', context)

