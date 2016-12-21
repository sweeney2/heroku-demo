from django.shortcuts import render


def index(request):
    context = {}  # nothing dynamic to render for now
    return render(request, 'hello/index.html', context)

