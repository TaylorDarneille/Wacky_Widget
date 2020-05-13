from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView

# Define the index view
def index(request):
  item = Item.objects.all()
  return render(request, 'index.html')

class ItemCreate(CreateView):
  model = Item
  fields = '__all__' 
  success_url = '/' 
