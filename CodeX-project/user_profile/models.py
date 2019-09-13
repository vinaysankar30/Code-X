from django.db import models

class users(models.Model):
    email = models.EmailField(max_length=20, null=False)
    password = models.TextField(max_length=20, null=False)
    disp_name = models.TextField(max_length=15, null=False)
class posts(models.Model):
    title = models.TextField(max_length=20,null=False)
    pdf_file = models.FileField(upload_to='files/')