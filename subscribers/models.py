from django.db import models

class Subscribers(models.Model):

    email= models.CharField(max_length=200, blank=False, null=False)
    full_name= models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Subscribers"
        verbose_name_plural = "Subscribers"

#     def get_absolute_url(self):
#         re_detail", kwargs={"pk": self.pk})
# )
