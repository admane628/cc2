from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from collec_management.forms import CollecForm, ElmForm
from collec_management.models import Collec, Element
# Create your views here.
def about(request):
    return render(request, 'collec_management/about.html')

@login_required
def collection(request ,id) :
    collectionInexistant= get_object_or_404(Collec , id=id, created_by=request.user)
    elements = Element.objects.filter(collection=collectionInexistant)
    return render(request ,'collec_management/collection_detail.html', {'collectionInexistant' : collectionInexistant, "elements":elements})

@login_required
def new( request ) :
 if request.method == "POST" :
    form=CollecForm(request.POST)
    if form.is_valid () :
       collec=form.save(commit = False )
       collec.created_by = request.user
       collec.save () # Sauvegarde en base de donnees
       return HttpResponseRedirect(reverse('collection' ,args=[collec.id] ))
 else :
    form = CollecForm() # Formulaire vide
 return render(request,"collec_management/formulaireNew.html" ,
               {"form" :form })

def all(request):
    collections=Collec.objects.all()
    return render(request, "collec_management/colleclist.html", {"collections":collections})

@login_required
def delete(request , collec_id) :
   collec=get_object_or_404(Collec , pk=collec_id, created_by=request.user)
   if request.method=="POST" :
      collec.delete()
      return redirect("all")

   return render (request , "collec_management/collec_delete.html",{"collec" :collec})


def check_save(form) :
   if form.is_valid() :
      collec=form.save(commit = False )
      collec.save ()
   return collec.id

@login_required
def change(request , collec_id) :
   collec = get_object_or_404(Collec , pk=collec_id, created_by=request.user)
   if request.method == "POST" :
      form =CollecForm(request.POST , instance=collec)
      collecModif_id = check_save(form)
      return redirect("collection" , id = collecModif_id)
   else :
      form =CollecForm(instance=collec)
   return render(request,
                 "collec_management/collec_modifier.html"
                 ,{"form": form})
def menu(request):
    return render(request, 'collec_management/menu.html')

@login_required
def element(request ,id) :
    elm = get_object_or_404(Element , id=id, created_by=request.user)
    return render(request ,'collec_management/element_detail.html', {'elm' : elm})

@login_required
def element_edit(request, id):
    elm = get_object_or_404(Element , pk=id, created_by=request.user)
    if request.method == "POST" :
       form =ElmForm(request.POST , instance=elm)
       elmModif_id = check_save(form)
       return redirect("element" , id = elmModif_id)
    else :
       form =ElmForm(instance=elm)
    return render(request,
                  "collec_management/element_modifier.html"
                  ,{"form": form})
