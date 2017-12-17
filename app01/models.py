from django.db import models

# Create your models here.
class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    # author=models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish_date=models.DateField()
    publish=models.ForeignKey('Publish',related_name='booklist')
    authorlist=models.ManyToManyField('Author',related_name='booklist')



    def __str__(self):

        return self.title

class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()

    def __str__(self):

        return self.name


class Publish(models.Model):
    name=models.CharField(max_length=32)
    addr=models.CharField(max_length=32)


    def __str__(self):

        return self.name
