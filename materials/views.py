from django.shortcuts import render, redirect
from .forms import MaterialsForm
from .models import Materials
from django.views.generic import DetailView, UpdateView, DeleteView




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

class MaterialView(DetailView):
    model = Materials
    template_name = 'materials/view-material.html'
    context_object_name = 'material'

class MaterialUpdate(UpdateView):
    model = Materials
    template_name = 'materials/create-material.html'

    form_class = MaterialsForm

class MaterialDelete(DeleteView):
    model = Materials
    template_name = 'materials/delete-material.html'
    success_url = '/'

def view(request):
    return render(request, 'materials/view-material.html')
