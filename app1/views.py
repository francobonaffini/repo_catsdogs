from django.shortcuts import render

def index(request):

    print('llego a la vista OK')

    return render(request, 'index.html')
