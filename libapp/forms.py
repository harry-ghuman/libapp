from django import forms
from libapp.models import Suggestion,Libitem,Libuser


class SuggestionForm(forms.ModelForm):
    class Meta:
        model=Suggestion
        fields = ['title','pubyr','type','cost','comments']
        widgets = {'type':forms.RadioSelect(), }
        labels = {
            'pubyr':u'Publication Year','cost':u'Estimated cost in Dollars',
        }
# from django import forms
# from libapp.models import Suggestion
#
#

# class SuggestionForm(forms.ModelForm):
#     model = Suggestion
#     title = forms.CharField(max_length=100)
#     pubyr = forms.IntegerField()
#     type = forms.ChoiceField(widget=forms.RadioSelect())
#     cost = forms.IntegerField(label='Estimated Cost in Dollars')
#     num_interested = forms.IntegerField()
#     comments = forms.CharField(widget=forms.Textarea())

class SearchlibForm(forms.ModelForm):
    class Meta:
        model = Libitem
        fields = ['title']
    title = forms.CharField(max_length=100, required=False)
    by = forms.CharField(max_length=100, required=False)


class UserForm(forms.ModelForm):
    class Meta:
        model = Libuser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput
        }
