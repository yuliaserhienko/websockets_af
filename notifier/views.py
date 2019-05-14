from django.shortcuts import render


def notify(request):
    return render(request, 'main.html', {})
