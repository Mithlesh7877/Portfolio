from django.db import models

# create models
# add blog app
# create migrate
# migrate
# add admin
class Blog(models.Model):
    blogtitle=models.CharField(max_length=200)
    publishdate=models.DateTimeField()
    body=models.CharField(max_length=300)
    image=image=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.blogtitle