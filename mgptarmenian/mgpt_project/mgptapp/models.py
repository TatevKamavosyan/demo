from django.db import models

# Create your models here.
# mgptapp/mgpt_model.py




class Text(models.Model):
    input_text = models.TextField()
    generated_text = models.TextField(blank=True, null=True)
    is_match = models.BooleanField(default=False)

    def __str__(self):
        return self.input_text[:50]
