from django import forms
from postsapp.models import Publication


class PubCreateForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'text', 'img']

    # def __init__(self, user, *args, **kwargs):
    #     self.user = user
    #     super(PubCreateForm, self).__init__(*args, **kwargs)
