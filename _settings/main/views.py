from django.shortcuts import render


def index(request):
    data = {
        'title': 'new title',
        'data': ['some', 'text', 'for', 'example'],
        'data2': {
            'name': 'andrey',
            'age': 23,
            'bio': 'somebio',
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
