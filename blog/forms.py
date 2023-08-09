from django import forms

from .models import Posts

class PostsForm(forms.ModelForm):
    """
    Form related to a Post.
    """
    class Meta:
        model = Posts
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'body': forms.Textarea(attrs={'class': 'form-control my-5'})
        }
        labels = {
            'body': 'What do you think?'
        }