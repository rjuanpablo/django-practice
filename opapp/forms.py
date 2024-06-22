from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task title", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter task title'}))
    description = forms.CharField(label="Task description", widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project name", max_length=100)