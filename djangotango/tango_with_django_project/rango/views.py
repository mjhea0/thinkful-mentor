from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a")

def about(request):
    return HttpResponse("Rango says: Here is the About Page. <a href='/rango'>Back Home</a")

