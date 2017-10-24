from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        item = Item()
        item.text = new_item_text
        item.save()
        # Item.objects.create(text=new_item_text)
        # print('Made a new item and saved it in db')
        return redirect('/lists/a-unique-url')

    items = Item.objects.all()
    print('Got all list items. They are:')
    print(items)
    print('About to render template')
    ret = render(request,'home.html',{'todo_items' : items})
    print('rendered template')
    return ret


def view_list(request):
    items = Item.objects.all()
    ret = render(request,'home.html',{'todo_items' : items})
    return ret
