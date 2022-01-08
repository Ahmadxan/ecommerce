from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    made = models.CharField(max_length=255, blank=True, null=True)  # blank va null
    content = models.CharField(max_length=255, blank=True, null=True)  # blank va null
    gender = models.CharField(max_length=20, default='Male', choices=(('Male', 'Male'), ('Female', 'Female')),
                              blank=True,
                              null=True)  # blank va null

    def __str__(self):
        return self.name
