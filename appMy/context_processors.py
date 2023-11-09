from appMy.models import BasketShop

def myContext(request):
   if request.user.is_authenticated:
      basketlength = len(BasketShop.objects.filter(user=request.user))
      return {"basketlength": basketlength}
   return ""