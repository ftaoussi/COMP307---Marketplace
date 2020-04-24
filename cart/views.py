from django.http import HttpResponse
from django.shortcuts import redirect, reverse, render
from cart.models import Cart, Item, OrderItem, Basket
from product_listing.models import Product
import cart.forms
import datetime
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
	context={}
	total = 0
	if request.user.is_authenticated:
		carts = Cart.objects.filter(user=request.user)
		if carts is not None: 
			this_cart = carts.first()
			context['cart'] = this_cart
			context['items'] = Item.objects.filter(cart=this_cart)
		else:
			this_cart = Cart(user=request.user)
			this_cart.save()
			context['cart'] = this_cart
		for item in context['items']:
			total += item.unit_price
		context['total'] = total
		return render(request, 'cart/cart.html', context)
	else:
		return redirect('/account/login')


#def viewCart(request): 
#	context={}
#	user = request.user
#	cart = Cart.objects.get(user=user)
#	context['cart'] = cart
#	context['items'] = Item.objects.get(cart=cart)
#	return render(request, "cart.html", context)

def modifyCart(request, action, product_id, quantity):
	context = {}
	if request.user.is_authenticated:
		try:
			user_cart = Cart.objects.get(user=request.user)
		except:
			user_cart = Cart.objects.create(user=request.user)
		if (action=='add'):
			add_to_cart(request, product_id, quantity)
		elif (action=='remove'):
			remove_from_cart(request, product_id, quantity)
		elif (action=='clear'):
			clear_cart(request)
		else:
			return HttpResponse("Error")
	else:
		return reverse(request, 'account/login.html', context)
	return redirect('/')

def add_to_cart(request, product_id, quantity):
	user_cart = Cart.objects.get(user=request.user)
	product = Product.objects.get(id=product_id)
	itemsMatching = Item.objects.filter(product=product, cart=user_cart, unit_price=product.price_current)
	this_item= itemsMatching.first()
	if this_item is None:
		item = Item(
			product=product,
			cart = user_cart,
			quantity= quantity,
			unit_price= product.price_current
		)
		item.save()
	else:
		print('ok')
		new_q = this_item.quantity + quantity
		itemsMatching.update(quantity=new_q)


def remove_from_cart(request, product_id, quantity):
	this_cart = Cart.objects.get(user=request.user)
	items = Item.objects.filter(product=product_id, cart=this_cart)
	if items is not None:
		item = items.first()
		if (item.quantity > quantity):
			item.quantity = item.quantity-quantity
		else:
			item.delete()

def clear_cart(request):
	this_cart = Cart.objects.get(user=request.user)
	this_cart.delete()


def checkout(request):
	context={}
	if request.user.is_authenticated == False:
		return reverse(request, 'account/login.html',context)
	try:
		this_cart = Cart.objects.get(user=request.user)
	except:
		return redirect('/cart')
	if this_cart.item_set.all() is None:
		form = forms.ShippingForm
		msg = "Your cart is empty"
		form.add_error(None, msg)
		return render (request, 'cart/checkout.html', context)
	user = request.user
	baskets = []
	items = this_cart.item_set.all()
	if request.method=='POST':
		form = cart.forms.ShippingForm(request.POST)
		if form.is_valid():
			try:
				shipaddr = form.cleaned_data['street_address']+", "+form.cleaned_data['postcode']
				for item in items:
					total = 0
					for basket in baskets:
						if (basket.seller != item.seller):
							total += 1
						else:
							thisBasket = basket
					if (total == len(baskets)):
						thisBasket = Basket(
							seller = item.product.seller,
							buyer = user,
							time = datetime.datetime.now(),
							shipping_to = shipaddr
						)
						thisBasket.save()
						baskets.append(thisBasket)
					orderItem = OrderItem(
						product_string = item.__str__(),
						unit_price = item.unit_price,
						product = item.product,
						buyer = user,
						seller = item.product.seller,
						basket = thisBasket,
						quantity = item.quantity,
						shipping_to = shipaddr
					)
					orderItem.save()
					product = item.product
					if product.stock > item.quantity:
						product.stock -= item.quantity
					else:
						Product.objects.filter(pk=product.pk).update(stock=0)
					item.delete()
				this_cart.delete()
			except:
				print('except')
				return HttpResponse("Please try again")	
			return render(request, 'cart/checkoutsuccess.html', context)

		else:
			print('form is invalid')
			form = cart.forms.ShippingForm
			context['form'] = form
			return render (request, 'cart/checkout.html', context)
	else: 
		form = cart.forms.ShippingForm
		context['form'] = form
		return render (request, 'cart/checkout.html', context)
	

def checkoutsuccess(request):
	return render(request, 'cart/checkoutsuccess.html')
