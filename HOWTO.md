# Django မှာ HTML View ဘယ်လိုထည့်မလဲ?

html file တစ်ခု Django မှာ ဘယ်လိုပြမလဲ?

/person-list လို့ Browser မှာ ရိုက်ထည့်လိုက်ရင် ဒီအောက်က html ပေါ်ချင်တယ်။

```html
<h2>Person List</h2>
<ul>
    <li>Person One</li>
    <li>Person Two</li>
    <li>Person Three</li>
</ul>
```

## HTML ပြဖို့ Django မှာ လုပ်ရမယ့် အဆင့် (၃) ဆင့်

### ကိုယ်ပြချင်တဲ့ App Folder ထဲမှာ ```templates``` ဆိုပြီး folder အသစ်ဆောက်။



finance
    manage.py
    finance/
    familytree/
        templates/
            hello_world.html


### View မှာ Method တစ်ခုရေး

```python
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the money app -> index method")

def helloWorld(request):
    return render(request, 'hello_world.html')
```

### Url မှာ အခုကြေညာထားတဲ့ views ထဲက method ကို ခေါ်

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("person-list/", views.helloWorld, name="person-list"),
]
```


## HTML file မှာ Python Data တွေ ဘယ်လိုထည့်မလဲ?


```python
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the money app -> index method")

def helloWorld(request):
    # html ဘက်ကို ထည့်ပေးချင်တဲ့ data
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    # ဖိုင်နာမည်နောက်မှာ Set တစ်ခု အနေနဲ့ ထည့်ပေး
    return render(request, 'hello_world.html', {'person_list': person_list, 'title' : 'Person List' } )
```

html ဖိုင်ဘက်မှာကျတော့ ဒီလိုပြန်ယူမယ်။
```html
<h2>{{ title }} </h2>
<ul>
    <!-- python ဘက်က pass ပေးလိုက်တဲ့ SET ထဲက person_list ကို ယူမယ်။​ သူက String List ဆိုတော့ Loop ပတ်မယ် -->
    {% for person in person_list %}
            <li>{{ person }}</li>
    {% endfor %}
</ul>
```


Person Select All လုပ်ပြီး ထည့်ပေးမယ်။
