from typing import Any
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class UserCreateForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any):
        super(UserCreationForm,self).__init__(*args,**kwargs)

        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text=None
            self.fields[fieldname].widget.attrs.update({"class":"form-control"})

class PassChangeForm(PasswordChangeForm):
    def __init__(self, *args: Any, **kwargs: Any):
        super(PasswordChangeForm,self).__init__(*args,**kwargs)

        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text=None
            self.fields[fieldname].widget.attrs.update({"class":"form-control"})