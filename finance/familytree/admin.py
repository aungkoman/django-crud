from django.contrib import admin

from .models import Gender, Person, Married


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_marriage')

admin.site.register(Gender)
admin.site.register(Person, PersonAdmin)
admin.site.register(Married)