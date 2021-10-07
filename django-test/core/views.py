from django.shortcuts import render

# Create your views here.
def index(req):
    context = {
        'subtitle': 'Programação web com Django Framework'
    }
    return render(req, 'index.html', context)

def contact(req):
    return render(req, 'contact.html')

