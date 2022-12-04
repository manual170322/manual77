from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput, NumberInput, CheckboxInput
from .models import Category, Teststask, Question, Decision
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# При разработке приложения, использующего базу данных, чаще всего необходимо работать с формами, которые аналогичны моделям.
# В этом случае явное определение полей формы будет дублировать код, так как все поля уже описаны в модели.
# По этой причине Django предоставляет вспомогательный класс, который позволит вам создать класс Form по имеющейся модели
# атрибут fields - указание списка используемых полей, при fields = '__all__' - все поля
# атрибут widgets для указания собственный виджет для поля. Его значением должен быть словарь, ключами которого являются имена полей, а значениями — классы или экземпляры виджетов.
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title',]
        widgets = {
            'title': TextInput(attrs={"size":"50"}),            
        }        

class TeststaskForm(forms.ModelForm):
    class Meta:
        model = Teststask
        fields = ['category', 'title', 'details', 'minutes', 'limit']
        widgets = {
            'category': forms.Select(attrs={'class': 'chosen'}),
            'title': TextInput(attrs={"size":"50"}),
            'details': Textarea(attrs={'cols': 50, 'rows': 5}),            
            'minutes': NumberInput(attrs={"size":"10", "min":1}),
            'limit': NumberInput(attrs={"size":"10", "min":10, "max":100}),            
        }
        labels = {
            'category': _('category'),            
        }
    # Метод-валидатор для поля minutes
    def clean_quantity(self):
        data = self.cleaned_data['minutes']
        # Проверка больше нуля
        if data <= 0:
            raise forms.ValidationError(_('Quantity must be greater than zero'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data
    # Метод-валидатор для поля limit
    def clean_quantity(self):
        data = self.cleaned_data['limit']
        # Проверка больше нуля и меньше или равно 100
        if data <= 0 and data >= 100:
            raise forms.ValidationError(_('Must be greater than 0 but less than 100'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'photo', 'reply1', 'ok1', 'reply2', 'ok2', 'reply3', 'ok3', 'reply4', 'ok4', 'reply5', 'ok5']
        widgets = {
            'question': Textarea(attrs={'cols': 60, 'rows': 6}),
            'reply1': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok1' : CheckboxInput(),
            'reply2': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok2' : CheckboxInput(),
            'reply3': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok3' : CheckboxInput(),
            'reply4': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok4' : CheckboxInput(),
            'reply5': Textarea(attrs={'cols': 50, 'rows': 5}),
            'ok5' : CheckboxInput(),
        }
        labels = {
            'teststask': _('teststask'),            
        }
    # Валидатор несокльих полей
    def clean(self):
        cleaned_data = super().clean()
        cc_reply1 = cleaned_data.get("reply1")
        cc_reply2 = cleaned_data.get("reply2")
        cc_reply3 = cleaned_data.get("reply3")
        cc_reply4 = cleaned_data.get("reply4")
        cc_reply5 = cleaned_data.get("reply5")
        cc_ok1 = cleaned_data.get("ok1")
        cc_ok2 = cleaned_data.get("ok2")
        cc_ok3 = cleaned_data.get("ok3")
        cc_ok4 = cleaned_data.get("ok4")
        cc_ok5 = cleaned_data.get("ok5")
        # Должен быть хотя бы один правильный ответ
        if cc_ok1 == False and cc_ok2 == False and cc_ok3 == False and cc_ok4 == False and cc_ok5 == False:
            raise forms.ValidationError(_('At least one correct answer must be marked'))
        # Должен быть хотя бы два ответа
        x=0
        if cc_reply1 is not None:
            if len(cc_reply1)>0:
                x=x+1
        if cc_reply2 is not None:
            if len(cc_reply2)>0:
                x=x+1
        if cc_reply3 is not None:
            if len(cc_reply3)>0:
                x=x+1
        if cc_reply4 is not None:
            if len(cc_reply4)>0:
                x=x+1
        if cc_reply5 is not None:
            if len(cc_reply5)>0:
                x=x+1
        if x<2:
            raise forms.ValidationError(_('There must be at least two answers'))

class DecisionForm(forms.ModelForm):
    class Meta:
        model = Decision
        fields = ['user', 'title', 'solution', 'rating']
        widgets = {
            'user': forms.Select(attrs={'class': 'chosen', "disabled": "true"}),
            'title': TextInput(attrs={"size":"100", "readonly": "readonly"}),
            'solution': Textarea(attrs={'cols': 60, 'rows': 6, "readonly": "readonly"}),
            'rating': Textarea(attrs={'cols': 50, 'rows': 5}),
        }
# Метод-валидатор для поля limit
    def title_quantity(self):
        data = self.cleaned_data['title']
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data
    
# Форма регистрации
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
