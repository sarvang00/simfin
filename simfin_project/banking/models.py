from django.db import models
from django.conf import settings
from datetime import datetime

class UserData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paycheck = models.FloatField(default=700)
    rent = models.FloatField(default=600)
    creditCardBill = models.FloatField(default=0)
    phoneBill = models.FloatField(default=50)
    groceryAmount = models.FloatField(default=80)
    setRentAutoPayment = models.BooleanField(default=False)
    setPhoneAutoPayment = models.BooleanField(default=False)
    setCreditAutoPayment = models.BooleanField(default=False)
    setGroceriesPayment = models.BooleanField(default=False)
    def __str__(self):
        return self.user

class UserBankingData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chequingBalance = models.FloatField(default=2000)
    savingBalance = models.FloatField(default=8000)
    creditLimit = models.FloatField(default=1000)
    creditRating = models.IntegerField(default=670)
    day = models.IntegerField(default=1)
    to_simulate_next = models.BooleanField(default=False)
    def __str__(self):
        return self.user

class Transaction(models.Model):
    txnDate = models.DateTimeField(default=datetime.now )
    txnType = models.TextField()
    txnParticipant = models.TextField()
    txnAmount = models.FloatField(default=0)
    def __str__(self):
        return self.txnParticipant+" "+self.txnDate
