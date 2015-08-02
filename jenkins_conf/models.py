from django.db import models


class JobDetail(models.Model):
    job_id = models.PositiveIntegerField()
    job_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    execution_time = models.DateTimeField()

    @classmethod
    def bulk_insert_job_detail(cls, list_objects):
        cls.objects.bulk_create(list_objects)

    @classmethod
    def check_job_already_exists(cls, **kwargs):
        return cls.objects.filter(**kwargs).exists()