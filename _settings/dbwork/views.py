from django.shortcuts import render, redirect
from .models import news_post
from .forms import news_postForm
from django.views.generic import DetailView, UpdateView, DeleteView


class NewDelete(DeleteView):
    model = news_post  # указываем с какой моделью будем работать
    template_name = 'dbwork/delete.html'  # указываем какой шаблон будет отображать
    success_url = '/news/'


class NewUpdate(UpdateView):
    model = news_post  # указываем с какой моделью будем работать
    template_name = 'dbwork/create.html'  # указываем какой шаблон будет отображать
    form_class = news_postForm

class NewDetailed(DetailView):
    model = news_post  # указываем с какой моделью будем работать
    template_name = 'dbwork/details_view.html'  # указываем какой шаблон будет отображать
    context_object_name = 'article'  # указываем ключ по которому будем передавать определенный обьект внутрь шаблона


def news_home(request):
    news = news_post.objects.order_by('-news_date')
    return render(request, 'dbwork/news_home.html', {'news': news})


def create(request):
    error_message = ""
    if request.method == 'POST':
        form = news_post(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error_message = "Fill in the fields correctly!"

    form = news_postForm()
    data = {
        'form': form,
        'error_mess': error_message
    }
    return render(request, 'dbwork/create.html', data)
