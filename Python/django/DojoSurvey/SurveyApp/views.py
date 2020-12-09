from django.shortcuts import render, redirect
from time import strftime


def index(request):
    return render(request, "index.html")


def submission(request):
    print(request.POST)
    request.session['cookult'] = request.POST
    return redirect('/result')
    # return render(request, "result.html", context)


def result(request):
    return render(request, 'result.html')
