from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html", {
        "active_sidebar": "homepage"
    })

def aba1(request):
    return render(request, "aba1.html", {
        "active_sidebar": "convergencia-iniciativas"
    })

def aba2(request):
    return render(request, "aba2.html", {
        "active_sidebar": "difusao-cientifica"
    })

def aba3(request):
    return render(request, "aba3.html", {
        "active_sidebar": "contribuicoes"
    })

def aba4(request):
    return render(request, "aba4.html", {
        "active_sidebar": "midia-externa"
    })

