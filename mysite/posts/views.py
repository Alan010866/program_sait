from django.shortcuts import render


def view_posts(request):
    return render(request, "posts/index.html")
