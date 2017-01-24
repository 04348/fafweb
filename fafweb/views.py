from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from celery.task import periodic_task
from urllib.request import Request, urlopen
from celery.schedules import crontab
from threading import Timer
from celery import task
import datetime
import json
# Create your views here.

API_DAILY = 'https://api.guildwars2.com/v2/achievements/daily'
API_ACHIV = 'https://api.guildwars2.com/v2/achievements/'
DAILY_REFRESH_RATE = 7200
DAILY_PVE = []
DAILY_PVP = []
DAILY_WVW = []
DAILY_SPE = []
list_ap = [ "[&BA8CAAA=], [&BKYBAAA=], [&BEwDAAA=], [&BIcHAAA=], [&BNIEAAA=], [&BIMCAAA=]",
            "[&BIMBAAA=], [&BBkAAAA=], [&BEgAAAA=], [&BH8HAAA=], [&BKgCAAA=], [&BGQCAAA=]",
            "[&BPEBAAA=], [&BKYAAAA=], [&BMIBAAA=], [&BH4HAAA=], [&BP0CAAA=], [&BDgDAAA=]",
            "[&BOcBAAA=], [&BIMAAAA=], [&BF0AAAA=], [&BKsHAAA=], [&BO4CAAA=], [&BF0GAAA=]",
            "[&BNMAAAA=], [&BNUGAAA=], [&BMwCAAA=], [&BJQHAAA=], [&BJsCAAA=], [&BHsBAAA=]",
            "[&BBABAAA=], [&BJIBAAA=], [&BLkCAAA=], [&BH8HAAA=], [&BBEDAAA=], [&BEICAAA=]",
            "[&BCECAAA=], [&BC0AAAA=], [&BDoBAAA=], [&BIkHAAA=], [&BO4CAAA=], [&BIUCAAA=]", ]

fract_daily = [ 
    [ ["Fractale Volcanique", "Fractale du Marais", "Fractale des Étherlame "],
    ["Fractale d'Aveugleneige", "Réacteur de Thaumanova", "Ruines Aquatiques"],
    ["Fractale de l'Océan Solide", "Complexe Souterrain", "Champs de bataille urbain"],
    ["Fractale des Étherlame ", "Fractale du Chaos", "Fractale des Cauchemars"],
    ["Fractale du Flanc de Falaise", "Boss de la Fusion", "Capitaine Mai Trin"],
    ["Fractale du Marais", "Fractale de l'Océan Solide", "Fractale non classée"],
    ["Fractale des Cauchemars", "Fractale d'Aveugleneige", "Fractale Volcanique"], ],
    #"impair
    [ ["Fractale des Étherlame ", "Fractale non classée", "Réacteur de Thaumanova"],
    ["Fractale du Flanc de Falaise", "Champs de bataille urbain", "Fractale du Chaos"],
    ["Complexe Souterrain", "Fractale Volcanique", "Capitaine Mai Trin"],
    ["Fractale d'Aveugleneige", "Fractale de l'Océan Solide", "Fractale des Cauchemars"],
    ["Fractale du Chaos", "Fractale non classée", "Champs de bataille urbain"],
    ["Fractale du Flanc de Falaise", "Fournaise de la Fusion", "Fractale du Marais"],
    ["Complexe Souterrain", "Réacteur de Thaumanova", "Boss de la Fusion"], ]
]

def home(request):
    return render(request, 'home.html')

def infos(request):
    today = datetime.datetime.today()
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    fracsToday = fract_daily[(today.isocalendar()[1])%2][today.weekday()]
    fracsTomo = fract_daily[(tomorrow.isocalendar()[1])%2][tomorrow.weekday()]
    print(fracsToday)
    return render(request, 'infos.html', {'pve':DAILY_PVE, 'pvp':DAILY_PVP, 'wvw':DAILY_WVW, 'spe':DAILY_SPE,
     'pact':list_ap[datetime.datetime.today().weekday()], 'fracstoday':fracsToday, 'fracstomo':fracsTomo})

def timer(request):
    return render(request, 'timer.html')

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