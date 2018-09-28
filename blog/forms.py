from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':''}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':''}))

    class Meta:
        model = Post
        fields = ('title', 'text',)

