from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_page(request:HttpRequest):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text']) # TODO
    new_item_text = request.POST.get('item_text', '')

    # return render(request, 'lists/home.html')
    return render(request, 'lists/home.html', {
        'new_item_text': new_item_text,
    })