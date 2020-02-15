from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name='sources', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} : {self.name}"

class Record(models.Model):
    user = models.ForeignKey(User, related_name='records', on_delete=models.CASCADE)
    source = models.ForeignKey(Source, related_name='records', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.id} : {self.user}"

    class Meta:
        get_latest_by = ['id']

