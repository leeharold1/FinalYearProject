from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Reservations, DeliveryOrder, CollectionOrder
from django.utils import timezone

class CreateUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'



class ReserveTableForm(forms.ModelForm):
	class Meta:
		model = Reservations
		fields = '__all__'
		widgets = {
					'date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),
					'time': forms.TimeInput(attrs={'type': 'time', 'step': 900, 'min': '18:00'}),
					'party_size': forms.NumberInput(attrs={'min': 2, 'step': 2}),
					}



class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryOrder
        fields = '__all__'

class CollectionForm(forms.ModelForm):
    class Meta:
        model = CollectionOrder
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.pickupTime = timezone.now() + timezone.timedelta(minutes=20)
        if commit:
            instance.save()
        return instance