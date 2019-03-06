from django.db import models

class category(models.Model):
	customer_id = models.CharField(max_length = 250)
	name = models.CharField(max_length = 250)
	description = models.CharField(max_length = 250)

	def __str__(self):
		return self.name


class seller(models.Model):
	
	customer_id = models.CharField(max_length = 250)
	name = models.CharField(max_length = 250)
	mobile_no = models.IntegerField()
	e_mail = models.CharField(max_length = 250)
	state = models.CharField(max_length = 250)
	lga = models.CharField(max_length = 250)
	bio = models.CharField(max_length = 250)
	status = models.CharField(max_length = 250)

	def __str__(self):
		return self.name

class product(models.Model) :
	customer_id = models.CharField(max_length = 250)
	name = models.CharField(max_length = 250)
	description = models.CharField(max_length = 250)

	def __str__(self):
		return self.description

class order(models.Model):
	customer_id = models.CharField(max_length = 250)
	order_id = models.IntegerField()
	qty = models.CharField(max_length = 250)
	amount = models.CharField(max_length = 250)
	description = models.CharField(max_length = 250, default='description')
	name = models.CharField(max_length = 250, default='PRODUCT')

	def __str__(self):
		return self.name + '-' + self.description