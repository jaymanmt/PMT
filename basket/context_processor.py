from .models import basketItem

def basketcount(request):
    basketcounter = basketItem.objects.filter(owner=request.user).count()
    return {
        "basketcounter":basketcounter
    }

