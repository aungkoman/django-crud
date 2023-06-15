# Django CRUD Module

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
