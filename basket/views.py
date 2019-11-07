from django.shortcuts import render

# Create your views here.
def showbasket(request):
    return render(request, "basket/basket.template.html")