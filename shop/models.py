from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name
