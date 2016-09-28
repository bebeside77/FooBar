from django.db import models


class Pair(models.Model):
    person1 = models.CharField(max_length=100),
    person2 = models.CharField(max_length=100),
    date = models.DateField

    def __str__(self):
        return '%s(%s,%s)' % (self.date, self.person1, self.person2)

