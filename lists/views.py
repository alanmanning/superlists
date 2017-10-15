from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        print('Got a post request')
        new_item_text = request.POST['item_text']
        print('Got item text: '+new_item_text)
        item = Item()
        print('Made new item object')
        item.text = new_item_text
        print('set item text')
        item.save()
        print('Saved item in db')
        # Item.objects.create(text=new_item_text)
        # print('Made a new item and saved it in db')
        return redirect('/')

    items = Item.objects.all()
    print(items)
    return render(request,'home.html',{'list_items' : items})
