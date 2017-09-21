from django.contrib import admin
from .forms import QuoteForm, ContactForm
from .models import Quote, Contact


# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'departure_location', 'destination_location', 'vehicle_make', 'vehicle_model', 'vehicle_condition', 'estimated_shipping_date', 'quote_estimate', 'timestamp']
	form = QuoteForm

admin.site.register(Quote, QuoteAdmin)


class ContactAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'first_name', 'last_name', 'message', 'timestamp']
	form = ContactForm

admin.site.register(Contact, ContactAdmin)