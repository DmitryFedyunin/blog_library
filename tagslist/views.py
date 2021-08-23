from django.shortcuts import render, redirect
from .forms import TagsForm
from .models import Tags
from django.views.generic import DetailView, UpdateView, DeleteView

def tags_view(request):
    tags = Tags.objects.all()
    return render(request, 'tagslist/list-tag.html', {'tags': tags})

def create_tags(request):
    err = ''
    if request.method == 'POST':
        form = TagsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tags')
        else:
            err = 'Заполнение не верно'

    form = TagsForm()
    data = {
        'form': form,
        'err': err
    }
    return render(request,'tagslist/create-tag.html', data)

class TagsView(DetailView):
    model = Tags
    template_name = 'tagslist/list-tag.html'
    context_object_name = 'tags'

class TagsDelete(DeleteView):
    model = Tags
    template_name = 'tagslist/delete-tags.html'
    success_url = '/tags'

class TagsUpdate(UpdateView):
    model = Tags
    template_name = 'tagslist/create-tag.html'
    form_class = TagsForm