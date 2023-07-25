# Data Passing

Django မှာ တစ်နေရာကနေ တစ်နေရာ Data တွေ Pass လုပ်ရတာရှိတယ်။
တစ်နေရာက တစ်နေရာဆိုတာ

views.py ကနေ HTML Template ကို data ထည့်ပေးလိုက်တာမျိုး။
urls.py ကနေ views.py ကို data ထည့်ပေးတာမျိုး။

```py
def index(request):
    # ဒီ variable (3) ခုကို person_detail.html ဆိုတဲ့ ဖိုင်ကို ထည့်ပေးလိုက်မယ်။
    name = "Cisco"
    gender = "Male"
    age = 43
    # render method က parameter (3) ခု လက်ခံတယ်။
    """
        1. request
        2. html template file name
        3. dictionary
    """
    return render(
        request, 
        'person_detail.html', 
        { "name" : name, "gender" : gender, "age" : age }
    )
```

ဒါဆို ```person_detail.html``` က ဘယ်လို ဒီ variable တွေကို access လုပ်မလဲ?

```html
<h2> {{ name }} </h2>
<p> I am {{ age }} years old {{ gender }} </p>
```

View ဘက်က ထည့်ပေးလိုက်တဲ့ Dictionary ရဲ့ key တွေကို access လုပ်ချင်ရင် ```{{ }}``` တွန့်ကွင်း (၂)​ခုကြားမှာ ထည့်ရေးရတယ်။