from django.http import HttpResponse
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template import Template, Context
from django.views.generic.simple import direct_to_template

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'user_permissions')

def index(request):
    u = User.objects.get(pk=1)
    return direct_to_template(request, 'index.html', {'form': UserForm(instance=u)})
