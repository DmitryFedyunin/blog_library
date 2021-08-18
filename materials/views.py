from django.shortcuts import render, redirect
from .forms import MaterialsForm

def create(request):
    err = ''
    if request.method == 'POST':
        form = MaterialsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            err = 'Заполнение не верно'

    form = MaterialsForm()
    data = {
        'form': form,
        'err' : err
    }
    return render(request,'materials/create-material.html', data)

def view(request):

    return render(request, 'materials/view-material.html')