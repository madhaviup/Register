from django import forms


class MyForm(forms.Form):
    firstname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Firstname', 'maxlength': '100'}
        ),
    )
    lastname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Lastname', 'maxlength': '100'}
        ),
    )
    phonenumber = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Phonenumber', 'maxlength': '100'}
        ),
    )
    address1 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Address1', 'maxlength': '100'}
        ),
    )
    address2 = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Address2', 'maxlength': '100'}
        ),
    )
    city = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'City', 'maxlength': '100'}
        ),
    )
    zipcode = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Zipcode', 'maxlength': '100'}
        ),
    )
    file = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Upload file', 'maxlength': '100'}
        )
    )



