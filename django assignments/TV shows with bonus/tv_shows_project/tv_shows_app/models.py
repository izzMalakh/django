from email.policy import default
from django.db import models
from datetime import date
today = date.today()



class ShowManager(models.Manager):
    def show_form_validator(self, requestData):
        errors = {}
        if len(requestData['titleshow']) < 2:
            errors['title'] = 'Show title should be at least 2 characters'

        if len(requestData['network']) < 3:
            errors['network'] = 'Show network should be at least 3 characters'

        if len(requestData['des']) < 10:
            errors['description'] = 'Description should be at least 10 charachters'

        # BONUS(1):
        #--------------------------------------------------------
        if requestData['date'] > str(today):
            errors['release_date'] = 'Date should be in the past'
        if len(requestData['date']) == 0:
            errors['release_date'] = 'Date is empty!'
        #--------------------------------------------------------

        # BONUS(2):
        #----------------------------------------------------------------
        if Show.objects.filter(title__contains=requestData['titleshow']):
            errors['title'] = 'Show title should be unique!'
        #----------------------------------------------------------------
        
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="Nothing")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
