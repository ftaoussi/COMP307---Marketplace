from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from cart.models import Cart, Item
import cart.forms
import datetime

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
		userCart = Cart.objects.filter(user=request.user)
		if userCart is None:
			this_cart=Cart(user=request.user)
			this_cart.save()
			userCart = Cart.objects.filter(user=request.user)
		if (action=='add'):
			add_to_cart(request, product_id, option)
		elif (action=='remove'):
			remove_from_cart(request, product_id, option)
		elif (action=='clear'):
			clear_cart(request)
		else:
			return HttpResponse("Error")
		context['cart'] = userCart.first()
		context['items'] = Item.objects.filter(cart=userCart)
	else:
		return reverse(request, 'account/login.html', context)
	return redirect(request.path_info, context)

def add_to_cart(request, product_id, quantity):
	product = Product.objects.get(id=product_id)
	this_user = request.user
	usercarts = Cart.objects.filter(user=user)
	usercart = user_carts.first()
	itemsMatching = Item.objects.filter(product=product, cart=user_cart, unit_price=product.unit_price)
	if itemsMatching is not None:
		item = Item(
			product=product,
			cart = usercart,
			quantity= quantity,
			unit_price= product.price_current
		)
		item.save()
	else:
		itemMatching = itemsMatching.first()
		itemMatching.quantity += quantity
	
	item = Item(
		product=product,
		cart = user_cart,
		quantity= quantity,
		unit_price= product.price_current
	)
	item.save()


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
	except Cart.DoesNotExist:
		this_cart = Cart(user=request.user)
		this_cart.save()
	user = request.user
	baskets = []
	if request.method=='POST':
		form = forms.ShippingForm(request.POST)
		if form.is_valid():
			try:
				shipaddr = form.cleaned_data['street_address']+", "+form.cleaned_data['postcode']
				for item in this_cart.item.set_all():
					total = 0
					for basket in baskets:
						if (basket.seller != item.seller):
							total += 1
						else:
							thisBasket = basket
					if (total == baskets.size()):
						thisBasket = Basket(
							seller = item.seller,
							buyer = user,
							time = datetime.datetime.now(),
							shipping_to = shipaddr
						)
						thisBasket.save()
						baskets.append(thisBasket)
						
					orderItem = OrderItem(
						product_string = item.__str__(),
						unit_price = item.price,
						product = item,
						buyer = user,
						seller = item.seller,
						basket = thisBasket,
						quantity = item.quantity,
						shipping_to = shipaddr
					)
					orderItem.save()
					product = item.product
					product.stock -= item.quantity
			except:
				return HttpResponse("Please try again")
	else:
		context['form'] = cart.forms.ShippingForm
		return render(request, 'cart/checkout.html', context)
	return HttpResponseRedirect(request, 'cart/checkoutsuccess.html', context)


def checkoutsuccess(request):
	return render(request, 'cart/checkoutsuccess.html')
