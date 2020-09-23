from django.shortcuts import render

# home view


def home_screen_view(request):
    context = {}
    context['some_string'] = 'This is some string passed from the views'

    list_of_values = []
    list_of_values.append('entry1')
    list_of_values.append('entry2')
    list_of_values.append('entry3')
    list_of_values.append('entry4')
    context['list_of_values'] = list_of_values

    return render(request, 'personal/home.html', context)
