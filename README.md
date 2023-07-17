# Django CRUD Module

## News Eleven Website 

eleven ဆိုပြီး app တစ်ခု ထည့်မယ်။
model ထည့်မယ်။
admin panel မှာ model တွေထည့်မယ်။
view မှာ template တွေ render ချမယ်။
template တွေကို သက်ဆိုင်ရာ data object တွေ ထုတ်ပေးမယ်။


```bash
# create new app
python manage.py startapp newseleven
```


## Requirement

Browser မှာ /personal-file လို့ ရိုက်ထည့်လိုက်ရင်

လူတစ်ယောက်ရဲ့ ကိုယ်ရေးအချက်အလက် ပြပေးရမယ်။

HTML Heading , Table သုံးပြီး။




## Family Tree

python manage.py startapp familytree

ငွေသုံးစာရင်းကို Django နဲ့ ရေးမယ်။

## Features

- [ ] ကိုယ့်ရဲ့ လက်ကျန်ငွေ ကြည့်လို့ရမယ်။ (Balance)
- [ ] ဝင်ငွေ ထွက်ငွေ အမျိုးအစား စာရင်း (Transaction Category)
- [ ] ဝင်ငွေ ထွက်ငွေ မှတ်တမ်းများ


## Command Logs
```bash
# create project
django-admin startproject finance
# change directory to project folder
cd finance
# create app
python manage.py startapp money
```


## Steps

- [ ] Project Create လုပ်မယ်။
- [ ] Create လုပ်ထားတဲ့ Project ထဲမှာ App တစ်ခုထည့်မယ်။
- [ ] View တစ်ခုရေးမယ်။​ (Hello World)

### Hello World ရေးမယ်။

- [ ] app folder ထဲမှာ views.py ဖိုင်ကိုဖွင့်ပြီး method တစ်ခုရေး။

```python
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the money app -> index method")
```

- [ ] app folder ထဲမှာ urls.py ဖိုင် create လုပ်ပြီး url array တစ်ခုရေး။

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

BTW, ref က https://docs.djangoproject.com/en/4.2/intro/tutorial01/

- [ ] Project Folder ထဲက urls.py မှာ ကိုယ့် app ရဲ့ urls.py သွားထည့်

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("money/", include("money.urls")),
    path("admin/", admin.site.urls),
]
```

money/ နဲ့ လာရင် money folder ထဲက urls.py ကို ယူသုံးပါပေါ့။

- [ ] hello world ပေါ်လား စမ်းကြည့်ဖို့ အောက်က command run

```bash
python manage.py runserver
```

ပေါ်လာတဲ့ url ကို ဝင်ကြည့်။

http://127.0.0.1:8000/money/

/money  ထည့်ဖို့ မမေ့နဲ့။

up and running တက်လာပြီ။


## Data Structure for our Money App

Model ဘယ်(၂) ခုလိုမလဲ?

- [ ] TranscationCategory
- [ ] Transcation

### Transaction Category မှာ ဘာတွေပါမလဲ?

name ပဲ​ပါမယ်။

### Transaction မှာ ဘာပါမလဲ?

- [ ] ဝင်ငွေလား / ထွက်ငွေလား မှတ်ဖို့ bool တစ်ခု -> income | bool
- [ ] အကြောင်းအရာ -> description | String
- [ ] ငွေပမာဏ -> amount | double
- [ ] မုန့်ဖိုးရတာလား / မုန့်ဝယ်စားတာလား မှတ်ဖို့ -> TransactionCategory
- [ ] ရက်စွဲ -> created_date

ဆိုတော့က ာ App Folder ထဲက models.py ကို ပြင်မယ်။

```python


```

