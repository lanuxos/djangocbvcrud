from django import forms
from .models import Post
 
 
# creating a form
class PostForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Post
 
        # specify fields to be used
        fields = [
            "title",
            "detail",
        ]

	
# creating a form
class InputForm(forms.Form):
    
    isHuman = forms.BooleanField()
    username = forms.CharField(max_length = 255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput())
    genders = (
        ('m', 'male'),
        ('f', 'female'),
        ('o', 'other'),
    )
    gender = forms.ChoiceField(choices=genders)
    publicGenders = (
        ('y', 'yes'),
        ('n', 'no'),
    )
    publicGender = forms.TypedChoiceField(choices=publicGenders)
    dateOfBirth = forms.DateField()
    registerTimeStamp = forms.DateTimeField()
    salary = forms.DecimalField()
    ageRange = forms.DurationField()
    email = forms.EmailField()
    upload = forms.FileField()
    uploadPath = forms.FilePathField(path='app/')
    weight = forms.FloatField()
    profile = forms.ImageField()
    children = forms.IntegerField()
    ip = forms.GenericIPAddressField()
    skills = (
        ('com', 'computer'),
        ('dri', 'driving'),
        ('lan', 'languages'),
    )
    skill = forms.MultipleChoiceField(choices=skills)
    languages = (
        ('eng', 'english'),
        ('chi', 'chinese'),
        ('vtn', 'vietnamese'),
    )
    language = forms.TypedMultipleChoiceField(choices=languages)
    married = forms.NullBooleanField()
    humanTest = forms.RegexField(regex="i'm human")
    slug = forms.SlugField()
    workingHour = forms.TimeField()
    url = forms.URLField()
    uuid = forms.UUIDField()
