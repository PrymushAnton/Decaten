from django import forms

class UserInfoForm(forms.Form):
    name = forms.CharField(
        label="Ім&#x27;я:",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'required': 'required'
        })
    )
    surename = forms.CharField(
        label="Фамілія",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'surname',
            'required': 'required'
        })
    )
    number = forms.CharField(
        label="Номер телефону",
        max_length=10,
        min_length=8,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'number',
            'required': 'required'
        })
    )

    terms_conditions = forms.BooleanField(
        label='"Згоджуюсь та надаю особисту інформацію"',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'invalidCheck',
            'required': 'required'
        })
    )

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if not number.isdigit():
            raise forms.ValidationError("Номер телефону повинен містити тільки цифри.")
        if len(number) < 8 or len(number) > 10:
            raise forms.ValidationError("Номер телефону повинен містити від 8 до 10 цифр.")
        return number
    
    



class PostInfoForm(forms.Form):
    post_choices = [
        ('NP', 'Нова пошта'),
        ('UP', 'Укр пошта')
    ]
    sending_option_choices = [
        ('NP-home', 'У відділення'),
        ('NP_box', 'Поштомат')
    ]

    post = forms.ChoiceField(
        label="Оберіть пошту для відпрвки",
        choices=post_choices,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'post_select',
            'required': 'required'
        })
    )

    sending_option = forms.ChoiceField(
        label="Оберіть Варіант отримання",
        choices=sending_option_choices,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'sending_option',
            'required': 'required'
        })
    )

    address = forms.CharField(
        label="Адреса проживання (обов'язково вкажіть область та місто)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'address',
            'required': 'required'
        })
    )

    post_index = forms.CharField(
        label="Індекс пошти",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'post_index',
            'required': 'required'
        })
    )

    terms_conditions = forms.BooleanField(
        label='"Я згоджуюсь з умовамі відправки."',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'postCheck',
            'required': 'required'
        })
    )