from django.db import models
from django.core.exceptions import ValidationError
import random
import string

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField()
    address = models.TextField()  
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
                return self.name    

    def save(self, *args, **kwargs):
                if not self.vendor_code:
                     self.vendor_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                super().save(*args, **kwargs)      
    
    def clean(self):
        if Vendor.objects.filter(vendor_code=self.po_number).exists():
            raise ValidationError("Purchase order number must be unique.")

class PurchaseOrder(models.Model):

    PURCHASE_STATUS = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    QUALITY_RATING_CHOICES = [
        (1.0, "1 - Poor"),
        (2.0, "2 - Below Average"),
        (3.0, "3 - Average"),
        (4.0, "4 - Good"),
        (5.0, "5 - Excellent"),
    ]
 
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=PURCHASE_STATUS, default='Pending')
    quality_rating = models.FloatField(choices=QUALITY_RATING_CHOICES, null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number
    
    def save(self, *args, **kwargs):
        if not self.po_number:
            self.po_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        super().save(*args, **kwargs)

    def clean(self):
        if PurchaseOrder.objects.filter(po_number=self.po_number).exists():
            raise ValidationError("Purchase order number must be unique.")
        if self.delivery_date <= self.order_date:
            raise ValidationError("Delivery date must be after order date.")       

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"




