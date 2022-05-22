from django.shortcuts import render
from . forms import tableauxForm
from . import models
from django.http import HttpResponseRedirect

def ajout(request):
     if request.method == "POST":
          form = tableauxForm(request)
          if form.is_valid():
               tableaux = form.save()
               return render(request,"R209app/affiche.html",{"tableaux" : tableaux})

          else:
               return render(request,"R209app/ajout.html",{"form": form})
     else:
          form = tableauxForm()
          id = ""
          return render(request,"R209app/ajout.html",{"form" : form, "id" : id})

def index(request):
     liste = list(models.tableaux.objects.all())
     return render(request, 'R209app/index.html', {"liste": liste})

def traitement(request):
     lform = tableauxForm(request.POST)
     if lform.is_valid():
          tableaux = lform.save()
          return render(request, "R209app/affiche.html", {"tableaux" : tableaux})
     else:
          return render(request,"R209app/ajout.html",{"form": lform})

def affiche(request, id):
     tableaux = models.tableaux.objects.get(pk = id)
     return render(request,"R209app/affiche.html",{"tableaux": tableaux})

def update(request, id):
     tableaux = models.tableaux.objects.get(pk = id)
     form = tableauxForm(tableaux.dico())
     return render(request, "R209app/ajout.html",{"form": form, "id": id})

def updatetraitement(request, id):
     lform = tableauxForm(request.POST)
     if lform.is_valid():
          tableaux = lform.save(commit = False)
          tableaux.id = id
          tableaux.save()
          return render(request, "R209app/affiche.html", {"tableaux": tableaux})
     else:
          return render(request, "R209app/ajout.html", {"form": lform, "id": id})

def delete(request, id):
     tableaux = models.tableaux.objects.get(pk=id)
     tableaux.delete()
     return render(request, "R209app/affiche.html", {"tableaux": tableaux})
