from django.shortcuts import render
from .formularios import ConsultaForm
from .models import Consulta
from .formulas import DetectarTexto
# Create your views here.
def InicioView(r):
    datos = {
        'form':ConsultaForm()
    }
    if r.method == 'POST':
        form = ConsultaForm(r.POST, r.FILES)
        if form.is_valid():
            doc = form.cleaned_data['img']
            c   = Consulta.objects.create(img=doc)
            c.save()
            texto = DetectarTexto(c.img)
            c.txt = texto
            c.save()
            datos.update(
                {
                    'respuesta': texto,
                    'img':c.img
                }
            )
            
            return render(r, 'respuesta.html', datos)
        
    return render(r, 'inicio.html', datos)

