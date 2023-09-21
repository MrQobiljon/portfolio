from django.db import models

# Create your models here.


class About(models.Model):
    photo = models.ImageField(upload_to='photo/', verbose_name="Rasmi")
    name = models.CharField(max_length=150, verbose_name="Ismi")
    degree = models.CharField(max_length=255, verbose_name="Darajasi")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Telefon raqam")
    address = models.TextField(verbose_name="Manzil", null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    about_me = models.TextField(verbose_name="Men haqimda", null=True, blank=True)

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



class Info(models.Model):
    completed = models.IntegerField(default=0, verbose_name="Bajarilgan ishlar")
    experience = models.IntegerField(default=0, verbose_name="Tajriba")
    client = models.IntegerField(default=0, verbose_name="Klientlar")
    award = models.IntegerField(default=0, verbose_name="Mukofotlar")

    def __str__(self):
        return f"{self.completed} ta ish barajildi"

    class Meta:
        verbose_name = "Xizmat ko'rsatish turi"
        verbose_name_plural = "Xizmat ko'rsatish turlari"


class CategoryPortfolio(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kategoriya")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Portfolio kategoriyasi"
        verbose_name_plural = "Portfolio kategoriyalari"


class Portfolio(models.Model):
    category = models.ForeignKey(CategoryPortfolio, on_delete=models.CASCADE, verbose_name="Kategoriya")
    title = models.CharField(max_length=255, verbose_name="Loyixa nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Qilingan ish"
        verbose_name_plural = "Qilingan ishlar"


class Gallery(models.Model):
    image = models.ImageField(upload_to='portfolio/', verbose_name="Rasm")
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, verbose_name="Qilingan ish")

    def __str__(self):
        return self.portfolio.title



class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kategoriya")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalari"


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Nomi")
    content = models.TextField(blank=True, null=True, verbose_name="Izohi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Saytga qo'yilgan vaqti")
