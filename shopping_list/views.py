from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ShoppingList

from .forms import ShoppingForm

def index(request):
	list = ShoppingList.objects.order_by("id")

	form = ShoppingForm()

	context ={"list":list, "form": form}
	
	return render (request, "shopping_list/index.html", context)

@require_POST
def addItem(request):
	form = ShoppingForm(request.POST)

	if form.is_valid():
		new_item = ShoppingList(text = request.POST['text'])
		new_item.save()

	return (redirect('index'))

def completeItem(request, item_id):
	item = ShoppingList.objects.get(pk=item_id)
	item.complete = True
	item.save()

	return (redirect('index'))


def deleteItem(request, item_id):
	item = ShoppingList.objects.get(pk=item_id)
	item.delete()
	return redirect('index')

def deleteAll(request):
	ShoppingList.objects.all().delete()
	return redirect('index')