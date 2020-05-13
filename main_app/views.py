from django.shortcuts import render

# Define the index view
def index(request):
  return render(request, 'index.html')