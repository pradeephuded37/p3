from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>Welcome To The Project</marquee>")

def home(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html",context={'data':pradeep,'name':deep})

def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html",{'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':5})

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))

def vowels(request, s):
    vowels = 'aeiouAEIOU'
    vowel = 0
    consonant = 0
    for i in s:
        if i in vowels:
            o += 1
        else:
            consonant += 1
    return render(request, 'directry/vowels.html', {'string':s, 'vowel':vowel, 'consonant':consonant})


