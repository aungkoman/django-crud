from django.shortcuts import render
from django.http import HttpResponse

# import models
from familytree.models import Person

def index(request):
    return HttpResponse("Hello, world. You're at the family tree app -> index method")

def helloWorld(request):
    # html ဘက်ကို ထည့်ပေးချင်တဲ့ data
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    person_obj_list = Person.objects.all()
    # ဖိုင်နာမည်နောက်မှာ Set တစ်ခု အနေနဲ့ ထည့်ပေး
    return render(request, 'hello_world.html', {'person_list': person_list, 'title' : 'Person List', 'person_obj_list' : person_obj_list } )

def personDetail(request, person_id = 0):
    person = Person.objects.get(pk=person_id)

    return render(request, 'person_detail.html', { 'person_id' : person_id, 'person' : person})