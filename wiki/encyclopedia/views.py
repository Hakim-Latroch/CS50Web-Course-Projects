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
        return render(request, "encyclopedia/title.html", {
        "title": query,
        "found": result,

        
            })
    


