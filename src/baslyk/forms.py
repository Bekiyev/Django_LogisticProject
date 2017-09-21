from django import forms
from .models import Quote, Contact


class QuoteForm(forms.ModelForm):
	class Meta:
		model = Quote
		fields = ['departure_location', 'destination_location', 'vehicle_make', 'vehicle_model', 'vehicle_condition', 'estimated_shipping_date','email']
		
		widgets={
        "departure_location":forms.TextInput(attrs={'value':'Houston','id':'txtSource','class':'txtPlaces', 'name':'departure_location', 'placeholder':'Zip or city'}),

        "destination_location":forms.TextInput(attrs={'value':'Dallas','id':'txtDestination','class':'txtPlaces', 'name':'destination_location', 'placeholder':'Zip or city'}),

        "vehicle_make":forms.TextInput(attrs={'value':'BMW','id':'make-input', 'name':'vehicle_make'}),

        "vehicle_model":forms.TextInput(attrs={'value':'530i','id':'model-input', 'name':'vehicle_model'}),
        "email":forms.TextInput(attrs={'value':'bekiyev@gmail.com', 'id':'email-input', 'name':'email'}),
                  }  

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['email', 'first_name', 'last_name', 'message']