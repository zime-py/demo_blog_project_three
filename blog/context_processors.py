from blog.models import *

def category_list(request):
    categories = Category.objects.all()
    return {'categories':categories}