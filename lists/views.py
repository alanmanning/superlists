from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']

        list_ = List.objects.create()
        item = Item(text=new_item_text, list=list_)
        item.text = new_item_text
        item.save()
        # Item.objects.create(text=new_item_text)
        # print('Made a new item and saved it in db')
        return redirect('/lists/a-unique-url')

    all_lists = List.objects.all()
    return render(request,'home.html',{'all_lists' : all_lists})
    # items = Item.objects.all()
    # ret = render(request,'home.html',{'todo_items' : items})
    # return ret


def view_list(request,list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    ret = render(request,'list.html',{'todo_items' : items})
    return ret


def new_list(request):
    ret = render(request,'new_list.html')
    return ret
