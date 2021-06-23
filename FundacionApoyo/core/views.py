from django.shortcuts import redirect, render
from .models import Personas
from .forms import PersonaForm

# llamada al fichero
def index(request):
    return render(request, "core/index.html")

    # llamada al fichero
def about(request):
    return render(request, "core/about.html")

    # llamada al fichero
def blog(request):
    blog = Personas.objects.all()
    return render(request, "core/blog.html",{'blog':blog})

    # llamada al fichero
def donacion(request):
    return render(request, "core/donacion.html")

    # llamada al fichero
def visit_us(request):
    return render(request, "core/visit_us.html")

    # llamada al fichero
def nueva_ficha(request):
    return render(request, "core/nueva_ficha.html")

    # CRUD
    
# agregar
def agregar(request):
    datos = {'form':PersonaForm()}
    if request.method == 'POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return redirect('blog')
    else:
        formulario = PersonaForm()
    return render(request, 'core/nueva_ficha.html', datos)

# eliminar
def eliminar(request, persona_id):
    persona = Personas.objects.get(id=persona_id)
    persona.delete()
    return redirect('blog')
    
# editar
def editar(request, persona_id):
    persona = Personas.objects.get(id=persona_id)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid:
            form.save()
            return redirect('blog')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'core/nueva_ficha.html',{'form':form})