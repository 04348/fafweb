from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from celery.task import periodic_task
from urllib.request import Request, urlopen
from celery.schedules import crontab
from threading import Timer
from celery import task
import json
# Create your views here.

API_DAILY = 'https://api.guildwars2.com/v2/achievements/daily'
API_ACHIV = 'https://api.guildwars2.com/v2/achievements/'
DAILY_REFRESH_RATE = 7200
DAILY_PVE = []
DAILY_PVP = []
DAILY_WVW = []
DAILY_SPE = []

def home(request):
    return render(request, 'home.html')

def infos(request):
    return render(request, 'infos.html', {'pve':DAILY_PVE, 'pvp':DAILY_PVP, 'wvw':DAILY_WVW, 'spe':DAILY_SPE,})

def redir(request, url):
    return redirect(url)

def refreshDaily():
    print("Updating Dailies...")
    global DAILY_PVE
    global DAILY_PVP
    global DAILY_WVW
    global DAILY_SPE
    dailyjs = getJSON(API_DAILY)
    DAILY_PVE = getDaily(dailyjs, 'pve')
    DAILY_PVP = getDaily(dailyjs, 'pvp')
    DAILY_WVW = getDaily(dailyjs, 'wvw')
    DAILY_SPE = getDaily(dailyjs, 'special')
    timer = Timer(DAILY_REFRESH_RATE, refreshDaily)
    timer.start()
    print("Dailies updated ! Next update in " + str(DAILY_REFRESH_RATE) + "seconds")

def getJSON(url):
    req = Request(url)
    req.add_header("Accept-Language", "fr-FR")
    responce = urlopen(req)
    return json.load(responce)

def getDaily(dailyjs, mode):
    # daily : {name, com, lmin, lmax, xpac}
    dlist = []
    for daily in dailyjs[mode]:
        try:
            achiv = getJSON(API_ACHIV + str(daily['id']))
            dlist.append([
                achiv['name'],
                achiv['requirement'],
                daily['level']['min'],
                daily['level']['max'],
                bool('HeartOfThorns' in daily['required_access']),
            ])
        except:
            print("Error while parsing daily API")
    return dlist

refreshDaily()