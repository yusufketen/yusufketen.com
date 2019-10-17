from django.shortcuts import render,HttpResponse


def home_view(request): # request can be changed for my opinion but this name is common in django
    if request.user.is_authenticated:
        context = {
            'name': 'Yusuf',
        }
    else:
        context = {
            'name': 'Guest',
        }
    return render(request, 'home.html', context)
