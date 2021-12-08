from django import forms

from .models import Entry, Topic    #create form for topic where user can add topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']     #don't have to show all fields from topic model
        labels = {'text':''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
    