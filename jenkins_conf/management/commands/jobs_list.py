from django.core.management import BaseCommand
from jenkinsapi.jenkins import Jenkins
from jenkins_conf.models import JobDetail
from test.settings import JENKINS_URL
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            jenkins_obj = Jenkins(JENKINS_URL)
            keys_list = jenkins_obj.keys()
            job_object_list = []
            for key in keys_list:
                try:
                    last_build = jenkins_obj[key].get_last_build()
                    job_name = last_build.name
                    build_data = last_build._data
                    time_stamp = build_data.get('timestamp')
                    status = build_data.get('result')
                    job_id = build_data.get('id')
                    job_object_list.append(JobDetail(job_id=job_id, job_name=job_name, status=status,
                                                     execution_time=get_date_time(time_stamp/1000)))\
                        if not JobDetail.check_job_already_exists(job_id=job_id, job_name=job_name) else None
                except Exception as e:
                    pass
            job_object_list = filter(None, job_object_list)
            if job_object_list:
                JobDetail.bulk_insert_job_detail(job_object_list)
        except Exception as e:
            pass

def get_date_time(long_value):
    return datetime.fromtimestamp(long_value).strftime('%Y-%m-%d %H:%M:%S')