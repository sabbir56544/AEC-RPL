from django.shortcuts import render
from .models import Category, Sub_Category, Slider, Service

from django.http.response import JsonResponse


def home(request):
    categories = Category.objects.all()
    sliders = Slider.objects.all()
    services = Service.objects.all()

    context = {
        'categories': categories,
        'sliders': sliders,
        'services': services,
    }
    return render(request, 'index.html', context)



def category(request, cat_name):
    cats = Category.objects.get(name=cat_name)
    sub = Sub_Category.objects.filter(category=cats)
    print(request.GET)
  
    context = {
        'sub': sub,
        'cat': cats,
    }

    return render(request, 'courses.html', context)


def category_detail(request, pk):
    sub = Sub_Category.objects.get(pk=pk)
    context = {
        'subs': sub
    }
    return render(request, 'courses-detaIis.html', context)



def serach_courses(request):
    if request.method == 'POST':
        search_cat = request.POST['search_category']
        serach_courses = Category.objects.filter(name__contains=search_cat)
        return render(request, 'search.html', {'serach_courses': serach_courses, 'search_categpry': search_cat})
    return render(request, 'search.html')


def autosuggest(request):
    query_original = request.GET.get('term')
    queryset = Category.objects.filter(name__icontains=query_original)
    mylist = []
    mylist += [x.name for x in queryset ]
    return JsonResponse(mylist, safe=False)    