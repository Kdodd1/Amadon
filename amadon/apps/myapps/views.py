from django.shortcuts import render, HttpResponse, redirect
from .models import Item 

def index(request):
	try:
		request.session['items']
	except KeyError as e:
		print(e)
		request.session['items'] = 0

	try:
		request.session['total']
	except KeyError as e:
		print(e)
		request.session['total'] = 0
	

	request.session['spent'] = 0

	content= {
		"items": Item.objects.all()
	}
	print(request.session['spent'])
	return render(request, "myapps/index.html", content)

def buy(request):
	print(request.POST)
	item = Item.objects.get(id = request.POST['product_id'])
	request.session['spent'] +=(item.price * int(request.POST['quantity']))
	request.session['total'] +=(item.price * int(request.POST['quantity']))
	request.session['items'] += int(request.POST['quantity'])

	return redirect("/amadon/checkout")

def checkout(request):

	return render(request, "myapps/checkout.html")
