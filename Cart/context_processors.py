from .models import *
from .views import *

def count(request):
    total=0
    if 'admin' in request.path:
        return {}
    else:
        try:
           c_items = Cart.objects.filter(C_id=CartId(request))
           for i in c_items:

               total+=1
        except c_items.DoesNotExist:
            total=0
    return dict(total=total)



