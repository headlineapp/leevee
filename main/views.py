from django.shortcuts import render

def show_homepage(request):
    return render(request, 'index.html')

def show_dashboard(request):
    return render(request, 'dashboard.0.html')

def show_inbox(request):
    return render(request, 'inbox.html')