from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# Create forms here.

class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = get_user_model()

    # Creating label for fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        