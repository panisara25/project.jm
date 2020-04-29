from django.forms import ModelForm 
from .models import *
from django import forms


class PostForm(forms.ModelForm):
    
    class Meta:
        model = PostJob
        fields = ('title','description','type_job',
                  'location','salary','gender','vacancy','benifit')
        
class ApplicationForm(forms.ModelForm):
    resume = forms.FileField(label='Resume',required=False, \
                                    error_messages ={'invalid': "PDF files only"},\
                                    widget=forms.FileInput)

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
    
    class Meta :
        model = Application
        fields = ('description', 'resume')
        

        

