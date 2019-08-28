# from website https://github.com/jarekwg/django-apscheduler/blob/master/examples/example_apscheduler/example_apscheduler/jobs.py
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job


scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


from proxyip.models import ProxyIPTable
from concurrent import futures

@register_job(scheduler, "interval", seconds=300, replace_existing=True)
def test_job():
    pass
    ProxyIPTable.extract_ip()

@register_job(scheduler, "interval", seconds=10, replace_existing=True)
def test_job():
    ipjobs = ProxyIPTable.objects.filter(valid=True)
    num = ipjobs.count()
    if num > 20:
        num = 20
    with futures.ThreadPoolExecutor(num) as executor: #open ten threads
        executor.map(ProxyIPTable.class_check_ip_valid, ipjobs)



register_events(scheduler)
scheduler.start()
print("Scheduler started!")