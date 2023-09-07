from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'amount': 3,
        'description': 'Tugas Kuliah'
    }

    return render(request, "main.html", context)
