from django.db import models

class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)    
    client_name = models.TextField()

    service_start_date = models.DateField()
    service_end_date = models.DateField()

    service_start_month = models.DateField()
    service_end_month = models.DateField()
    
    gender = models.TextField()
    marital_status = models.TextField()
    age_band = models.TextField()
    case_managers = models.TextField()
    
    client_group = models.TextField()
    client_subgroup = models.TextField()
    hcp_level_name = models.TextField()
    active_flag = models.TextField()

    state_code = models.TextField()
    area = models.TextField()

    service_start_current_fytd = models.BooleanField()
    service_end_current_fytd = models.BooleanField()

    class Meta:
        managed = False  # Don't let Django try to create or modify this
        db_table = 'clients'