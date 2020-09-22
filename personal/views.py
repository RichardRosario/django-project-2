from django.shortcuts import render

# home view


def home_screen_view(request):
    return render(request, 'base.html', {})
