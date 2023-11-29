from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    entry = util.get_entry(title=title)
    return render(request, "encyclopedia/title.html",{
        "entry": entry,
        "title":f"{title}",
        "notFound":entry == None
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
    
    


