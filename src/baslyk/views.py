from django.shortcuts import render
from .forms import QuoteForm, ContactForm

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
	title = " "
	form = QuoteForm(request.POST or None)
	context = {
		"form": form,		
	}
	if form.is_valid():
		icindekiler = form.save(commit=False)
		icindekiler.save()
		context = {
			"title": "Your cost: 980$"
			}
	return render(request, 'home.html', context)


def contact(request):
	form = ContactForm(request.POST or None)
	#context = { "form": form }	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#context = { "title": "We will get back to you shortly. Thank You" }
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_first_name = form.cleaned_data.get("first_name")
		form_last_name = form.cleaned_data.get("last_name")
		subject = 'Site Contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s, %s, %s, %s" %(form_first_name, form_last_name, form_message, form_email)
		some_html_message = "<h3>Firstname: %s</h3><h3>Lastname: %s</h3><h3>Concerns: %s</h3><h3>Contact info: %s</h3>" %(form_first_name, form_last_name, form_message, form_email)
		send_mail(subject, contact_message, form_email, to_email, html_message=some_html_message, fail_silently=False)

	context = {
		"form": form,
		}
	return render(request, 'contact.html', context)



def CostCalculate(request):
	form = QuoteForm(request.POST or None)
	context = {
		"form": form,		
	}
	if form.is_valid():
		icindekiler = form.save(commit=False)
		icindekiler.save()
	return render(request, 'cost.html', context)



def thanks(request):
	title = " hello"
	context = {
			'title': title	
	}
	
		
	return render(request, 'thanks.html', context)











		


