from django.shortcuts import render

# Create your views here.

def HomeView(request):

    context = {
        'title': 'Cinema',
    }

    return render(request, 'Cinema/index.html', context)
