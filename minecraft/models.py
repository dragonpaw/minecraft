from django.db import models
from django.utils.translation import ugettext as _
from collections import defaultdict
from decimal import Decimal
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    name = models.CharField('Name', max_length=80, unique=True)
    ingredients = models.ManyToManyField('self', through='Ingredient', symmetrical=False)
    slug = models.SlugField(max_length=80)
    batch_size = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name

    def get_absolute_url(self):         
        return reverse('item_detail', args=[self.slug])

    def recurse_raw_materials(self):
        if self.ingredients.count() == 0:
            return ({self: 1}, {})
        else:
            mats = defaultdict(int)
            inter = defaultdict(int)
            inter[self] += 1
            for i in Ingredient.objects.filter(makes=self):
                # Zero mats don't recurse, as they are not consumed.
                if i.quantity == 0:
                    inter[i.item] += 0 # Just verifies it exists.
                else:
                    sub_mats, sub_inter = i.item.recurse_raw_materials()
                    for m in sub_mats:
                        mats[m] += sub_mats[m] * Decimal(i.quantity) / Decimal(self.batch_size)
                    for m in sub_inter:
                        inter[m] += sub_inter[m] * Decimal(i.quantity) / Decimal(self.batch_size)
            return (mats, inter)
    
    def raw_materials(self):
        '''Recursively figure out everything needed. 
        
        Then, for clarity, remove self.'''
        mats, inter = self.recurse_raw_materials()
        # If a complex material, I got used up, so I'm in the intermeditary
        if self in inter:
            del(inter[self])
        # But if just gathered, I'm in the raw.
        elif self in mats:
            del(mats[self])
        return mats, inter

class Ingredient(models.Model):
    makes = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.DecimalField(_('Quantity'), max_digits=5, decimal_places=2, default=1)
    item = models.ForeignKey('Item', related_name='makes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')
        ordering = ('makes', 'item',)

    def __str__(self):
        return u"{0}x {1}".format(self.quantity, self.item.name)

    def quantity_each(self):
        return Decimal(self.quantity) / Decimal(self.makes.batch_size)
