from django.shortcuts import render

# llamada al fichero
def index(request):
    return render(request, "core/index.html")

    # llamada al fichero
def about(request):
    return render(request, "core/about.html")

    # llamada al fichero
def blog(request):
    return render(request, "core/blog.html")

    # llamada al fichero
def contact(request):
    return render(request, "core/contact.html")

    # llamada al fichero
def services(request):
    return render(request, "core/services.html")

    # llamada al fichero
def visit_us(request):
    return render(request, "core/visit_us.html")