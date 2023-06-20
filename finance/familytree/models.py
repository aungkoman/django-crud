from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    dob = models.DateField(null=True,blank=True)
    dod = models.DateField(null=True,blank=True)
    note = models.CharField(max_length=200, null=True,blank=True)
    parent_marriage = models.ForeignKey('Married', on_delete=models.SET_NULL, null=True,blank=True, related_name='children')

    def __str__(self):
        return self.name


class Married(models.Model):
    person_one = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='marriages_as_person_one')
    person_two = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='marriages_as_person_two')
    married_date = models.DateField(null=True,blank=True)
    divorced_date = models.DateField(null=True,blank=True)
    note = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.person_one.name + " & " + self.person_two.name
