from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm
from django.views.generic import DeleteView,DetailView,UpdateView

def category_view(request):
    category = Category.objects.all()
    return render(request, 'categorylist/list-category.html', {'category': category})

def create_category(request):
    err = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category')
        else:
            err = 'Заполнение не верно'

    form = CategoryForm()
    data = {
        'form': form,
        'err': err
    }
    return render(request, 'categorylist/create-category.html', data)

class CategoryViews(DetailView):
    model = Category
    template_name = 'categorylist/list-category.html'
    context_object_name = 'category'

class CategoryDelete(DeleteView):
    model = Category
    template_name =  'categorylist/delete-category.html'
    success_url = '/category'

class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'categorylist/create-category.html'
    form_class = CategoryForm