from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    sort = request.GET.get('sort')
    print(sort)
    if sort == 'name':
        sort_param = 'name'
    elif sort == 'min_price':
        sort_param = 'price'
    elif sort == 'max_price':
        sort_param = '-price'
    else:
        sort_param = 'id'
    template = 'catalog.html'
    # phones_list = []
    # for phone in Phone.objects.all():
    #     print(f'{phone.id}:{phone.name}-{phone.price}')
    #     phones_list.append({'name': phone.name, 'price': phone.price, 'image': phone.image})
    context = {'phones_list': Phone.objects.all().order_by(sort_param)}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print(slug)
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
