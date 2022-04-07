from django.forms import ModelForm
from .models import BookStatus

# Create the form class.
class StatusForm(ModelForm):
    class Meta:
        model = BookStatus
        fields = ['book', 'status', 'member']
