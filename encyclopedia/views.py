from django.shortcuts import render
from markdown2 import Markdown
from random import choice
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def check_entry(request, name):

    if util.get_entry(name) is None:
        return render(request, "encyclopedia/error_page.html", {
            "name": name,
        })
    else:
        entry_info = util.get_entry(name)
        md = Markdown()
        page = md.convert(entry_info)
        return render(request, "encyclopedia/entry.html", {
            "name": name,
            "page_info": page,
        })

def search(request):
    query = request.GET['q'].lower()
    entries = util.list_entries()
    matches = []

    for name in entries:
        if name.lower() == query:
            return check_entry(request, name)

    for title in entries:
        if query in title.lower():
            matches.append(title)
            return render(request, "encyclopedia/search.html", {
                "matches": matches,
            })

    return render(request, "encyclopedia/error_page.html", {
        "name": query,
    })

def new_page(request):
   if request.method == 'POST':
    title = request.POST.get("title")
    content = request.POST.get("text_area")
    for name in util.list_entries():
        if name.lower() == title.lower():
            return render(request, "encyclopedia/new_page.html", {
                "message": "Title already exists.",
                })

    util.save_entry(title, content)
    entry_info = util.get_entry(title.lower())
    md = Markdown()
    page = md.convert(entry_info)
    return render(request, "encyclopedia/entry.html", {
         "name": title,
         "message": "Success! New encyclopedia entry has been added.",
         "page_info": page,
    })
   return render(request, "encyclopedia/new_page.html")

def edit_entry(request, name):
    if request.method == 'POST':
        title = request.POST.get("edit_title")
        content = request.POST.get("edit_text_area")
        util.save_entry(title, content)
        entry_info = util.get_entry(title.lower())
        md = Markdown()
        page = md.convert(entry_info)
        return render(request, "encyclopedia/entry.html", {
            "name": title,
            "message": "Success! You entry has been edited.",
            "page_info": page,
        })

    content = util.get_entry(name)
    return render(request, "encyclopedia/edit_entry.html", {
                  "name": name,
                  "text_area": content,
    })

def random_entry(request):
     result = choice(util.list_entries())
     entry_info = util.get_entry(result)
     md = Markdown()
     page = md.convert(entry_info)
     return render(request, "encyclopedia/entry.html", {
         "name": result,
         "page_info": page,
     })








