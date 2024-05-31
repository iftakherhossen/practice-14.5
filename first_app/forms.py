from django import forms
from django.forms.widgets import NumberInput
import datetime

# Create your forms here.
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
]
FAVORITE_FOOD_CHOICES = [
    ('biriyani', 'Biriyani'),
    ('chicken', 'Chicken'),
    ('pizza', 'Pizza'),
]

class OrdinaryCodersForm(forms.Form):
    name = forms.CharField(max_length=50, initial='Your Name')
    email = forms.EmailField(required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    date = forms.DateField(widget=NumberInput(attrs={'type':'date'}), initial=datetime.date.today)
    value = forms.DecimalField()
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER)
    favorite_food = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_FOOD_CHOICES)
    agree = forms.BooleanField(label="Remember Me", initial=True)  
    
class GeeksForGeeksForm(forms.Form):
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField( help_text = "Enter 6 digit roll number") 
    name = forms.CharField(max_length=50, initial='Your Name')
    email = forms.EmailField(required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    password = forms.CharField(widget = forms.PasswordInput()) 
    date = forms.DateField(widget=NumberInput(attrs={'type':'date'}), initial=datetime.date.today)
    value = forms.DecimalField()
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    gender = forms.TypedChoiceField(widget=forms.RadioSelect,choices=GENDER)
    favorite_food = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_FOOD_CHOICES)
    agree = forms.BooleanField(label="Remember Me", initial=True)  
    duration = forms.DurationField()
    file = forms.FileField()
    image = forms.ImageField()
    ipAddress = forms.GenericIPAddressField()
    regex = forms.RegexField(regex="^[A-Za-z]+$")
    slug = forms.SlugField()
    time = forms.TimeField()
    url = forms.URLField()
    uuid = forms.UUIDField()