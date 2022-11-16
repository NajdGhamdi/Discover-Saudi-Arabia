from django import forms

from destination.models import Destination,Event,Site









class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields="__all__"
        exclude=('slug','owner')





class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields="__all__"
        exclude=('slug',)
  


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields="__all__"
        exclude=('slug',)
  