from django.db import models

# Create your models here.


class About(models.Model):
    photo = models.ImageField(upload_to='photo/', verbose_name="Rasmi")
    name = models.CharField(max_length=150, verbose_name="Ismi")
    degree = models.CharField(max_length=255, verbose_name="Darajasi")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Telefon raqam")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Men haqimda"
        verbose_name_plural = "Men haqimda"



class Service(models.Model):
    logo_teg = models.TextField(verbose_name="Hizmat ko'rsatish turi logosi")
    title = models.CharField(max_length=255, verbose_name="Hizmat ko'rsatish nomi")
    content = models.TextField(verbose_name="Hizmat ko'rsatish tavsifi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xizmat ko'rsatish turi"
        verbose_name_plural = "Xizmat ko'rsatish turlari"