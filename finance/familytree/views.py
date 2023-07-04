from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# import models
from familytree.models import Person,Married

def our_person_list(request):
    # get persons from database
    person_list = Person.objects.all()
    return render(request, 'our_person_list.html', { "person_list" : person_list })

def greeting(request):
    # variables
    name = "Cisco Ramon"
    gender = "male"
    # list
    marks = [55, 45, 78]
    # dictionary
    personal_file = {
        "name" : "Cisco",
        "age" : 45,
        "address" : "Mandalay"
    }
    age = 13
    return render(request, 'greeting.html', 
        {
            "name" : name, 
            "gender" : gender,
            "marks" : marks,
            "personal_file" : personal_file,
            'age' : age
        } 
    )

def myHtml(request):
    return render(request,'test.html')
    # return HttpResponse("Hello World")

# function declaration
def testFunc(request):
    return HttpResponse("Hello TEST")


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


    """
    marks = [1,2,3] # List
    print(marks[1]) # 2
    # dictionary
    person = {
        'name' : 'Mg Mg',
        'age' : 14
    }
    print(person['name']) # Mg Mg
    """