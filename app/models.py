# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Jobseeker(models.Model):
    jobseeker_name= models.CharField(max_length=200)
    jobseeker_phone=  models.CharField(max_length=200)
    jobseeker_email= models.CharField(max_length= 200)
    jobseeker_dob= models.DateField("date of birth")
    jobseeker_f_name= models.CharField(max_length=200)
    jobseeker_gender=  models.CharField(max_length=200)
    jobseeker_language= models.CharField(max_length=200)
    jobseeker_jobrole=  models.CharField(max_length=200)
    jobseeker_experience=  models.CharField(max_length=200)
    jobseeker_current_state=  models.CharField(max_length=200)
    jobseeker_current_city=  models.CharField(max_length=200)
    jobseeker_per_state=  models.CharField(max_length=200)
    jobseeker_per_city=  models.CharField(max_length=200)
    job_title=  models.CharField(max_length=200)
    jobseeker_company_name=  models.CharField(max_length=200)
    jobseeker_company_address=  models.CharField(max_length=200)
    job_from = models.DateField("from")
    job_to= models.DateField("to")
    job_description=  models.CharField(max_length=200)
    jobseeker_handicapped=  models.CharField(max_length=200)
    jobseeker_passport=  models.CharField(max_length=200)
    jobseeker_education=  models.CharField(max_length=200)
    jobseeker_current_salary=  models.CharField(max_length=200)
    jobseeker_active=  models.CharField(max_length=200)
    joseeker_mitra_id= models.CharField(max_length=200)
    jobseeker_password= models.CharField(max_length=200)
    def __str__(self):
        return self.jobseeker_name


class Job(models.Model):
    job_title=  models.CharField(max_length=200)
    job_category=  models.CharField(max_length=200)
    employer_name=  models.CharField(max_length=200)
    job_contact= models.CharField(max_length=10)
    job_date= models.DateField("job creation_date")
    job_location_city=  models.CharField(max_length=200)
    job_location_state=  models.CharField(max_length=200)
    job_last_date= models.DateField('last date to apply')
    job_gender=  models.CharField(max_length=200)
    job_education=  models.CharField(max_length=200)
    job_salary=  models.CharField(max_length=200)
    job_skills=  models.CharField(max_length=200)
    job_calls= models.IntegerField()
    job_whatsapp= models.IntegerField( )
    job_active=  models.CharField(max_length=200)
    job_description = models.CharField(max_length=300)

    def __str__(self):
        return self.job_title

    def recent_jobs(self):
        return job_date >= timezone.now()- datetime.timedelta(days=1)    


class Skills(models.Model):
    skill_english= models.CharField(max_length=200)
    skill_hindi= models.CharField(max_length= 200)

    def __str__(self):
        return self.skill_english

class JobCategory(models.Model):
    job_category= models.CharField(max_length=200)
    members= models.ManyToManyField(Skills, related_name='job_group')    
    def __str__(self):
        return self.job_category


         