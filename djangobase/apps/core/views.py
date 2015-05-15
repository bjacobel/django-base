from django.shortcuts import render

def DefaultView(request):

    ctx = {}

    return render(request, 'pages/default.html', ctx)