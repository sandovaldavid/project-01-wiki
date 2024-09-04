from django.http import Http404
from django.shortcuts import render

from . import util


def index(request):
    query = request.GET.get('q')
    if query:
        content = util.get_entry(query)
        if content:
            return render(request, "encyclopedia/entry.html", {
                "title": query.upper(),
                "content": content
            })
        else:
            entries = [entry for entry in util.list_entries() if query.lower() in entry.lower()]
            if entries:
                return render(request, "encyclopedia/search.html", {
                    "title": "Search",
                    "content": entries,
                    "query": query
                })
            else:
                return render(request, "encyclopedia/404.html", status=404)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content:
        return render(request, "encyclopedia/entry.html", {
            "title": title.upper(),
            "content": content
        })
    return render(request, "encyclopedia/404.html", status=404)

def page_no_found(request, exception):
    return render(request, 'encyclopedia/404.html', status=404)