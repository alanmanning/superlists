from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
	item = request.POST.get('item_text','')
	print('POSTed item is: '+ item)
	return render(request,'home.html',{
			'new_item_text' : request.POST.get('item_text',''),
		})
