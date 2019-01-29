from django.db import models

class Profile(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER)

    def __str__(self):
        return '%s %s' % (self.fname, self.lname)