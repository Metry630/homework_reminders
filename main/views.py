from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Oey Joshua Jodrian - PBP D',
        'amount': 3,
        'description': 'Homework Reminders'
    }

    return render(request, "main.html", context)
