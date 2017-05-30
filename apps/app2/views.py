from django.shortcuts import render, redirect, reverse

# Create your views here.
def index(request, schmoo):
    print id
    return render(request, 'app2/index.html')

def post_test(request):
    print "here"
    return redirect(reverse('app1:index'))
