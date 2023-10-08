from django.shortcuts import render

def blog(request):
    return render(request, 'blog-detail.html')

def blog_detail(request):
    return render(request, 'blog-list-left-sidebar.html')
