from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display=('name',  "age")
    fieldsets = (
        ('info', {'fields':('name', "age")}),
        ('cash', {'fields':('balance',)}),

    )
    search_fields = ('name',)
    list_filter = ('age',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display=('title','description',)
    fieldsets = (
        ('info', {'fields':('title', "description")}),
        ('characters', {'fields':('cost','size', 'age_limited')}),

    )
    search_fields = ('title',)
    list_filter = ('age_limited',)
    