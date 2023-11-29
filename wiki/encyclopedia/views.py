from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import random

from markdown2 import markdown
from . import util



def index(request):
   
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        
    })
def entry(request, title):
    entry = util.get_entry(title=title)
    entry_converted = markdown(entry)
    return render(request, "encyclopedia/title.html",{
        "entry": entry_converted,
        "title":f"{title}",
        "notFound":entry == None
    })


def randomEntry(request):
    entries = util.list_entries()
    entryName = random.choice(entries)
    entry = util.get_entry(title=entryName)
    entry_converted = markdown(entry)
    return render(request, "encyclopedia/random.html",{
        "entry": entry_converted,
        "title":f"{entryName}",

    })

def search(request):
    
    if request.method == "POST":
        query = request.POST.get("q")  
        entries = util.list_entries()  
        if  query.lower() in  map(str.lower, entries):
            return HttpResponseRedirect(reverse("wiki:entry", args=[query]))  
        else: 
            result = util.find_query(query=query) 
        return render(request, "encyclopedia/search.html", {
        "title": query,
        "found": result,
             
            })
    
def new(request) :
    return render(request, "encyclopedia/new.html", {

    })

def addNew(request) : 
    if request.method == "POST":
        newEntry_title = request.POST.get("newTitle")
        newEntry_content = request.POST.get("newContent")
        if util.save_entry(newEntry_title, newEntry_content) :
            return HttpResponseRedirect(reverse("wiki:entry", args=[newEntry_title]))
        else :
            return render(request, "encyclopedia/new.html", {
                "oldTitle" : newEntry_title,
                "oldContent" : newEntry_content,
                "entryExists" : True
            })

def edit(request) :
     if request.method == "POST":
        originalTitle = request.POST.get("originalTitle")
        originalContent = request.POST.get("originalContent")
        return render(request, "encyclopedia/edit.html",{
        "originalTitle" : originalTitle ,
        "originalContent" : originalContent

        })       
def saveEdit(request):
    if request.method == "POST" :
       originalTitle = request.POST.get("originalTitle")
       newTitle = request.POST.get("newTitle")
       newContent = request.POST.get("newContent")
       util.save_edit(originalTitle, newTitle, newContent)
       return  HttpResponseRedirect(reverse("wiki:entry", args=[newTitle]))
    else :
        return render(request, "encyclopedia/edit.html",{

            })

    
    


