from django.db import models
from django.utils.timezone import now

class ProxyIPTable(models.Model):
    ip = models.CharField(max_length=64)
    port = models.CharField(max_length=8)
    valid = models.BooleanField(max_length=True) #bool value
    create_time = models.DateTimeField(default=now) #now function should not have (), or it will just call function and return value
    other = models.CharField(max_length=256) #other info

    def extract_ip(self):
        pass

    def check_ip_valid(self):
        pass

    def export_proxy(self):
        pass