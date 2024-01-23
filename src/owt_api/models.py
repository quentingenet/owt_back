from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class WeightRecord(models.Model):
    weight_record_date = models.DateTimeField(auto_now_add=True)
    weight_value = models.DecimalField(max_digits=4, decimal_places=1)
    body_water = models.DecimalField(max_digits=4, decimal_places=1)
    fat_mass = models.DecimalField(max_digits=4, decimal_places=1)
    bone_mass = models.DecimalField(max_digits=4, decimal_places=1)
    muscular_mass = models.DecimalField(max_digits=4, decimal_places=1)
    id_bmi = models.ForeignKey('BodyMassIndex', on_delete=models.CASCADE)
    id_person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.weight_value)


class BodyMassIndex(models.Model):
    bmi = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return str(self.bmi)


class InitialData(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'
        NEUTRAL = 'N'

    body_size = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(250)])
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)
    initial_weight = models.DecimalField(max_digits=4, decimal_places=1)
    goal_weight = models.DecimalField(max_digits=4, decimal_places=1)
    is_european_unit_measure = models.BooleanField(default=True)
    register_user_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.register_user_date)


class Person(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_initial_data = models.OneToOneField(InitialData, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_user)
