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
list_ap = [ "[&BA8CAAA=], [&BKYBAAA=], [&BEwDAAA=], [&BIcHAAA=], [&BNIEAAA=], [&BIMCAAA=]",
			"[&BIMBAAA=], [&BBkAAAA=], [&BEgAAAA=], [&BH8HAAA=], [&BKgCAAA=], [&BGQCAAA=]",
			"[&BPEBAAA=], [&BKYAAAA=], [&BMIBAAA=], [&BH4HAAA=], [&BP0CAAA=], [&BDgDAAA=]",
			"[&BOcBAAA=], [&BIMAAAA=], [&BF0AAAA=], [&BKsHAAA=], [&BO4CAAA=], [&BF0GAAA=]",
			"[&BNMAAAA=], [&BNUGAAA=], [&BMwCAAA=], [&BJQHAAA=], [&BJsCAAA=], [&BHsBAAA=]",
			"[&BBABAAA=], [&BJIBAAA=], [&BLkCAAA=], [&BH8HAAA=], [&BBEDAAA=], [&BEICAAA=]",
			"[&BCECAAA=], [&BC0AAAA=], [&BDoBAAA=], [&BIkHAAA=], [&BO4CAAA=], [&BIUCAAA=]", ]


fract_mode = ["Quotidiennes JcE", "Quotidiennes JcJ", "Quotidiennes McM", "Quotidiennes Fractales", "Quotidiennes Spéciales", "Err. : No section"]

def home(request):
	return render(request, 'home.html')

def infos(request):
	#daily achiv
	dailies = []
	dailyjs = getJSON(API_DAILY)
	index = 0
	for mode in dailyjs:
		mode_daily = []
		for daily in dailyjs[mode]:
			cur_daily = []
			cur_daily.append(daily['id'])
			cur_daily.append(daily['level']['min'])
			cur_daily.append(daily['level']['max'])
			cur_daily.append(bool('PathOfFire' in daily['required_access']))
			mode_daily.append(cur_daily)
		dailies.append([ fract_mode[index], mode_daily])
		index = index+1
	return render(request, 'infos.html', {'dailies':dailies, 'pact':list_ap[datetime.datetime.today().weekday()]})

def timer(request):
	return render(request, 'timer.html')

def redir(request, url):
	return redirect(url)

def getJSON(url):
	req = Request(url)
	req.add_header("Accept-Language", "fr-FR")
	responce = urlopen(req)
	return json.load(responce)