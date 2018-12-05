from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
  # return HttpResponse("Hello, World")
  context = {
    'name': 'world',
  }
  return render(request, 'myapp/index.html', context)


