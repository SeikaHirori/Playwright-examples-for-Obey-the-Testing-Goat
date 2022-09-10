from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from lists.models import Item

# Create your views here.

def home_page(request:HttpRequest):
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save() # FIXME

    new_item_text = request.POST.get('item_text', '')

    # return render(request, 'lists/home.html')
    return render(request, 'lists/home.html', {
        'new_item_text': new_item_text,
    })