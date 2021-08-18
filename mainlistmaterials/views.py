from django.shortcuts import render
from materials.models import Materials


def index(request):
    materials = Materials.objects.all()[:10]
    return render(request,'mainlistmaterials/list-materials.html', {'materials': materials})

def about(request):
    data = {
        'welcome': 'Привеет, чего хотел?',
        'values': ['Один','Два', 'Три'],
        'obj': {
            'car': 'Hyndai',
            'engine': 1.6,
            'color': 'white'
        }
    }
    return render(request, 'mainlistmaterials/base/about.html', data)