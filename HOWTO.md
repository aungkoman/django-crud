# Django မှာ HTML View ဘယ်လိုထည့်မလဲ?

html file တစ်ခု Django မှာ ဘယ်လိုပြမလဲ?

/person-list လို့ Browser မှာ ရိုက်ထည့်လိုက်ရင် ဒီအောက်က html ပေါ်ချင်တယ်။

```html
<ul>
    <li>Person One</li>
    <li>Person Two</li>
    <li>Person Three</li>
</ul>
```

## HTML ပြဖို့ Django မှာ လုပ်ရမယ့် အဆင့် (၃) ဆင့်

ကိုယ်ပြချင်တဲ့ App Folder ထဲမှာ ```templates``` ဆိုပြီး folder အသစ်ဆောက်။

finance
    manage.py
    finance/
    familytree/
        templates/
            hello_world.html