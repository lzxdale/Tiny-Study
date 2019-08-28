from django.db import models
from django.utils.timezone import now
import pandas as pd
import os
import requests

class ProxyIPTable(models.Model):
    ip = models.CharField(max_length=64)
    port = models.CharField(max_length=8)
    valid = models.BooleanField(default=True) #bool value
    create_time = models.DateTimeField(default=now) #now function should not have (), or it will just call function and return value
    other = models.CharField(max_length=256) #other info

    @classmethod
    def extract_ip(cls):
        os.chdir('C:\\Users\\81065\\git\\Free_Proxy_Pool\\proxy_crawl')
        path = 'Python C:\\Users\\81065\\git\\Free_Proxy_Pool\\proxy_crawl\\Proxy_get.py'
        os.system(path)
        data = pd.read_csv('C:\\Users\\81065\\git\\Free_Proxy_Pool\\proxy_crawl\\proxy_file.csv')
        for i in range(len(data)):
            item = data.loc[i]
            print(item['ip'])
            table = ProxyIPTable(ip=item['ip'],port=item['port'], other=[item['country']+item['anonymity']])
            table.save()
        return True

    def __str__(self):
        return "[{}] | IP:{} | port:{} | Other:{} | DateTime:{}".format(self.valid, self.ip,self.port,self.other, self.create_time)

    def check_ip_valid(self):
        pass
    @classmethod
    def class_check_ip_valid(cls, ipjob):
        proxies = {'http':"http//{}:{}".format(ipjob.ip, ipjob.port), 'https':"https//{}:{}".format(ipjob.ip, ipjob.port)}
        url ='http://www.spbeen.com/tool/request_info/'
        try:
            resp = requests.get(url,proxies=proxies, timeout=3)
            if ipjob.other not in resp.text:
                ipjob.valid = False
                ipjob.save()
                pass
        except:
            ipjob.valid = False
            ipjob.save()


    def export_proxy(self):
        pass