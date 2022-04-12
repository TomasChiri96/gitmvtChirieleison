from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from mvt1.models import familiar, mascota
# Create your views here.


def familia(request):
    padre = familiar(nombre= 'Hugo', apellido = 'Chiri', edad = 50, fecha_nacimiento="1992/12/12")
    padre.save()
    documento = f"Mi papa se llama {padre.nombre} Apellido{padre.apellido} y tiene {padre.edad} Ya que nacio el dia {padre.fecha_nacimiento}"
  

    return HttpResponse(documento)

def familia1(request):
     madre = familiar(nombre= 'Laura', apellido = 'Correa', edad = 55, fecha_nacimiento="1992/12/12")
     madre.save()
     documento1 = f"Mi madre se llama: {madre.nombre}, Apellido:{madre.apellido} Y tiene {madre.edad} Ya que nacio el dia {madre.fecha_nacimiento}"

     return HttpResponse(documento1)

def familia2(request):
    hermana = familiar(nombre= 'Thais', apellido = 'Chiri', edad = 20, fecha_nacimiento='2000/05/12')
    hermana.save()
    documento2 = f"Mi sister es {hermana.nombre}, Apellido:{hermana.apellido} y tiene {hermana.edad} Ya que nacio el dia {hermana.fecha_nacimiento}"

    return HttpResponse(documento2)

def perro1(request):

    iris = mascota(raza='labrador', nombre='Iris')
    iris.save()
    info1 = f"Tenemos a {iris.nombre} que es un perro {iris.raza}"

    return HttpResponse(info1)

def perro2(request):

    choco = mascota(raza='Ladrador', nombre='chocolate')
    choco.save()
    info2 = f"Tenemos a {choco.nombre} que es un perro {choco.raza}"

    return HttpResponse(info2)

def plantilla_madre(request):
    
    nom = 'Laura'
    ape = 'Correa'

    diccionario = {"nombre":nom, "apellido":ape}
    mihtml = open('C:\\Users\\tomas\\Desktop\\mvt_chirieleison\\mvt\\mvt\\plantillas\\template1.html')
    plantilla = Template(mihtml.read())

    mihtml.close()
    micontexto = Context(diccionario)
    documento = plantilla.render(micontexto)

    return HttpResponse(documento)


def plantilla_padre(request):
    nom = 'Hugo'
    ape = 'Chiri'

    diccionario = {"nombre":nom, "apellido":ape}
    mihtml = open('C:\\Users\\tomas\\Desktop\\mvt_chirieleison\\mvt\\mvt\\plantillas\\template2.html')
    plantilla = Template(mihtml.read())

    mihtml.close()
    micontexto = Context(diccionario)
    documento = plantilla.render(micontexto)

    return HttpResponse(documento)

def plantilla_sister(request):
    nom = 'Thais'
    ape = 'Chiri'

    diccionario = {"nombre":nom, "apellido":ape}
    mihtml = open('C:\\Users\\tomas\\Desktop\\mvt_chirieleison\\mvt\\mvt\\plantillas\\template3.html')
    plantilla = Template(mihtml.read())

    mihtml.close()
    micontexto = Context(diccionario)
    documento = plantilla.render(micontexto)

    return HttpResponse(documento)






