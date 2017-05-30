from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'ids': [1,2,3,4]
    }
    return render(request, 'app1/index.html', context)
