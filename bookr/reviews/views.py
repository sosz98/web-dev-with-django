from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})


def book_search(request):
    search = request.GET.get("search") or "..."
    return render(request, "search.html", {"search": search})
