from django.db import models

# Create your models here.
ESTIMATED_SHIPPING = (
        ('ASAP', 'ASAP'),
        ('Within 2 Weeks', 'Within 2 Weeks'),
        ('Within 30 Days', 'Within 30 Days'),
        ('Not Sure', 'Not Sure'),
    )

CONDITION = (
        ("Runs", "Runs"),
        ("Doesn't run", "Doesn't run"),
    )

class Quote(models.Model):
	departure_location = models.CharField(max_length=100, blank=False, null=False)
	destination_location = models.CharField(max_length=100, blank=False, null=False)
	vehicle_make = models.CharField(max_length=100, blank=False, null=False)
	vehicle_model = models.CharField(max_length=100, blank=False, null=False)
	vehicle_condition = models.CharField(max_length=20, choices=CONDITION, null=True)
	email = models.EmailField()
	estimated_shipping_date = models.CharField(max_length=100, choices=ESTIMATED_SHIPPING)
	quote_estimate = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __unicode__(self):
		return self.email


class Contact(models.Model):
	first_name = models.CharField(max_length=100, blank=False, null=False)
	last_name = models.CharField(max_length=100, blank=False, null=False)
	email = models.CharField(max_length=100, blank=False, null=False)
	message = models.CharField(max_length=100, blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __unicode__(self):
		return self.email










