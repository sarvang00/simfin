from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from banking.models import UserBankingData, UserData

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login')
def index(request):
    userData = UserData.objects.filter(user=request.user.id).first()
    userBankingData = UserBankingData.objects.filter(user=request.user.id).first()

    totalBalance = userBankingData.chequingBalance+userBankingData.savingBalance
    
    context = {
        'userData': userData,
        'userBankingData': userBankingData,
        'totalBalance': totalBalance
    }
    return render(request, 'banking/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login')
def changeSimulationState(request):
    userData = UserData.objects.filter(user=request.user.id).first()
    userBankingData = UserBankingData.objects.filter(user=request.user.id).first()

    userBankingData.to_simulate_next = not(userBankingData.to_simulate_next)
    userBankingData.save()

    totalBalance = userBankingData.chequingBalance+userBankingData.savingBalance
    
    context = {
        'userData': userData,
        'userBankingData': userBankingData,
        'totalBalance': totalBalance
    }
    return render(request, 'banking/dashboard.html', context)

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login')
def getUpdatedData(request):
    userData = UserData.objects.filter(user=request.user.id).first()
    userBankingData = UserBankingData.objects.filter(user=request.user.id).first()

    userBankingData.day +=1

    if (userBankingData.day%30 == 1 or userBankingData.day%30 == 15):
        userBankingData.chequingBalance += userData.paycheck
    
    if (userBankingData.day%30 == 1):
        userBankingData.savingBalance *= 1.01
        userBankingData.chequingBalance -= userData.rent

    if (userBankingData.day%30 == 10):
        userBankingData.chequingBalance -= userData.creditCardBill
    
    if (userBankingData.day%30 == 16):
        userBankingData.chequingBalance -= userData.phoneBill
    
    if (userBankingData.day%30 == 1 or userBankingData.day%30 == 11 or userBankingData.day%30 == 21):
        userBankingData.chequingBalance -= userData.groceryAmount

    userBankingData.save()

    totalBalance = userBankingData.chequingBalance+userBankingData.savingBalance
    
    context = {
        'userData': json.dumps(model_to_dict(userData)),
        'userBankingData': json.dumps(model_to_dict(userBankingData)),
        'totalBalance': totalBalance
    }
    return JsonResponse(context)