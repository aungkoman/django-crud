# အခြေခံ Database Operations များ

## နမူနာ Model

model က ဒီလို ရှိတယ် ဆိုကြပါစို့
```python
from django.db import models
     
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
```

## စမ်းကြည့်ဖို့အတွက် Python Shell ကို ဝင်မယ်။

```bash
python manage.py shell
```


## Insert

Person တစ်ခု insert လုပ်ချင်ရင်

```python
from .models import Person
 
# query1
# step 1 : create new object
obj1 = Person(first_name="Aung", last_name="Man", address="Mandalay")
# step 2 : invoke save method
obj1.save()
 
# query2
# step 1 : call create method
obj2 = Person.objects.create(first_name="Aung", last_name="Man", address="Mandalay")


# access 
print(obj1.id) # auto generated number -> 1
print(obj1.name) # Aung
```

*** note **** 
Whenver a object is created django will automatically assigns a primary key “id” to the record which is used to identify the record uniquely.


## Select

```python
# select person object , it's id is 1
obj1 = Person.objects.get(id=1) 
print(obj1.name) # Aung

# update
obj1.first_name = "Aung Ko"
obj1.save()

# delete
obj1.delete()

```

## Refrences

Ref; https://medium.com/@anjaneyulubatta/django-model-crud-operations-4121dc127f53