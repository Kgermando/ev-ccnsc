from django.db import models

# Create your models here.

class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    objet_name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=101)
    phone_num = models.CharField(max_length=15)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Message de ' + self.first_name + ' ' + self.last_name
