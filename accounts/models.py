from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.


class Guest(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phoneNumber = PhoneNumberField(unique=True)

    def __str__(self):
        return str(self.user)

    def __init__(self, *args: any, **kwargs: any) -> None:
        self._numOfBooking = 0
        self._numOfDays = 0
        self._numOfLastBookingDays = 0
        self._currentRoom = 0
        super().__init__(*args, **kwargs)
    
    @property
    def numOfBooking(self):
        return self._numOfBooking

    @numOfBooking.setter    
    def numOfBooking(self, value):
        self._x = value

    @property
    def numOfDays(self):
        return self._numOfDays
    
    @numOfDays.setter
    def numOfDays(self, value):
        self._numOfDays = value

    @property
    def numOfLastBookingDays(self):
        return self._numOfLastBookingDays
        
    @numOfLastBookingDays.setter
    def numOfLastBookingDays(self, value):
        self._numOfLastBookingDays = value

    @property
    def currentRoom(self):
        return self._currentRoom

    @currentRoom.setter
    def currentRoom(self, value):
        self._currentRoom = value


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phoneNumber = PhoneNumberField(unique=True)
    salary = models.FloatField()

    def __str__(self):
        return str(self.user)


class Task(models.Model):
    employee = models.ForeignKey(
        Employee,   null=True, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    description = models.TextField()

    def str(self):
        return str(self.employee)
