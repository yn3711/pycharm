from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


guy = Person.objects.get(name='bob')
print(guy.age)  # output is 35
