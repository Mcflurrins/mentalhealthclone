from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306171713',
        'name': 'Flori Andrea Ng',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)