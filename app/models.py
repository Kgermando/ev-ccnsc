from django.db import models

# Create your models here.
class Home(models.Model):
    home_title = models.CharField(max_length=50)
    home_contenu = models.CharField(max_length=200)
    actu_image = models.ImageField(upload_to='img_img/')
    created = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('actualite:actualite-view-detail', args=[str(self.id)])

    def __str__(self):
        return self.home_title

# Contact Form
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
