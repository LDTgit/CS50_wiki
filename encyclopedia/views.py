import random
from django.shortcuts import render, redirect
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def view_post(request, title):
    data=util.get_entry(title)
    if data is None:
        return render(request, "encyclopedia/not_found.html")
    return render(request, "encyclopedia/view_post.html", {
        "data": markdown2.markdown(data),
        "title": title
    }) 

def search(request):
    query=request.POST.get("q")
    data=util.get_entry(query)
    if data:
        return redirect("view_post", title=query)
    titles=util.list_entries()
    filtered_titles=[]
    for title in titles:
        if query.lower() in title.lower():
            filtered_titles.append(title)
    result = {
        "query": query,
        "entries": filtered_titles,
       }
    if len(filtered_titles) == 0:
        result["error_message"]= "No matches found!"
    return render(request, "encyclopedia/search_page.html", result)

def new_page(request):
    return render(request, "encyclopedia/new_page.html")

def add_page(request):
    title = request.POST.get("a")
    content = request.POST.get("b")
    if title in util.list_entries():
        return render(request, "encyclopedia/new_page.html", {
            "title":title,
            "content":content,
            "error_message": "This title already exists!"
        })
    else:
        util.save_entry(title, content)
        return redirect("view_post", title=title)

def edit_page(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "content":content
    })

def modify_page(request, title):
    content = request.POST.get("b")
    util.save_entry(title, content)
    return redirect("view_post", title=title)

def random_page(request):
    return redirect("view_post", title=random.choice(util.list_entries()))