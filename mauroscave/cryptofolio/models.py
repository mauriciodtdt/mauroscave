from django.db import models

class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    api_key = models.CharField(max_length=64)
    api_secret = models.CharField(max_length=64)


class Balance(models.Model):
    timestamp = CustomDateTimeField(auto_now_add=True)
    usdt_balance = models.FloatField()
    aud_balance = models.FloatField()
    btc_balance = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    