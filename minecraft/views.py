import math

from django.shortcuts import render, get_object_or_404

from . import models

def item_index(request):
    return render(request, 'items.html', {
        'items': models.Item.objects.all(),
    })

def item_detail(request, slug):
    item = get_object_or_404(models.Item, slug=slug)

    materials, intermediates = item.raw_materials()
    final_mats = [(x, materials[x]) for x in sorted(materials.keys())]
    final_int = [(x, intermediates[x]) for x in sorted(intermediates.keys())]

    return render(request, 'item_detail.html', {
        'item': item,
        'ingredients': item.ingredient_set.all(),
        'intermediates': final_int,
        'materials': final_mats,
        'uses': models.Ingredient.objects.filter(item=item),
    })
