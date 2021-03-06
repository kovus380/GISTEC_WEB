from django.forms import ModelForm

from projectapp.models import Project

app_name='projectapp'

class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description']