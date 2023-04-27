from django.db import models

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    image_url = models.ImageField(upload_to='images/', null=True, blank=True)
    # serial_number = models.CharField(max_length=100)
    # purchase_date = models.DateField()

    # date the record was created and recorded
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name