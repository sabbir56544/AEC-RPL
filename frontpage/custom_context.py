from .models import Category


def mycontext(request):
    categories = Category.objects.all()
    return {'categories': categories}

