from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165944',
        'name': 'Ghiranza Athaya Hamid',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)