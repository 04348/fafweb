from django.shortcuts import render
from django.http import HttpResponse
from build.models import Build, BuildForm
# Create your views here.

#Builds code
prof_url = ["elementaliste", "envouteur", "necroment", "rodeur", "ingenieur", "voleur", "guerrier", "gardien", "revenant"]
prof_name = ["Elementaliste",
             "Envouteur",
             "Nécroment",
             "Rôdeur",
             "Ingénieur",
             "Voleur",
             "Guerrier",
             "Gardien",
             "Revenant",
            ]
prof_icon = ["http://i.imgur.com/q6yX4m7.png", #elem
             "http://i.imgur.com/IHSueKO.png", #envout
             "http://i.imgur.com/paUelND.png", #necro
             "http://i.imgur.com/K4F4tgF.png", #rodeur
             "http://i.imgur.com/vWzclx5.png", #ingé
             "http://i.imgur.com/UYyvbjD.png", #voleur
             "http://i.imgur.com/er2FpQf.png", #war
             "http://i.imgur.com/XMJBCS1.png", #guard
             "http://i.imgur.com/vo2IGDk.png", #rev
            ]

builds_rev = [
    "Herault_DPS-Support.txt",
]
###

def convertToHtml(s):
    html = s.replace('\n', '<br \>')
    html = html.replace('\t', '&emsp;&emsp;')
    return html

def getBuilds(prof):
    builds = []
    if (prof == "revenant"):
        builds = builds_rev
    return builds

def getBuildTitle(files):
    texts = []
    for file in files:
        s = file.replace('.txt', '')
        s = s.replace('_', '&nbsp;')
        texts.append(s)
    return texts

def getBuildText(files):
    texts = []
    for file in files:
        f = open("build/builds/"+file, 'r')
        s = convertToHtml(f.read())    
        texts.append(s)
    return texts

def view_buildSelect(request):
    return render(request, 'build/buildSelect.html', {'prof' : zip(prof_name, prof_icon, prof_url)})

def view_build(request, prof):
    if prof in prof_url:
        build_list = getBuilds(prof)
        build_title = getBuildTitle(build_list)
        build_cont = getBuildText(build_list)
        isEmpty = bool(len(build_list)==0)
        return render(request, 'build/build.html', {'builds': zip(build_title, build_cont), 'titles':build_title, 'isEmpty':isEmpty})
    raise Http404

"""
def view_build(request, prof):
    if prof in prof_url:
        build_list = Build.objects.all()
        build_title = []
        build_cont = []
        for build in build_list:
            if (build.prof == prof):
                build_title.append(build.titre)
                build_cont.append(build.contenu)
        isEmpty = bool(len(build_title)==0)
        return render(request, 'build/build.html', {'builds': zip(build_title, build_cont), 'titles':build_title, 'isEmpty':isEmpty})
    raise Http404
"""

def view_buildCreate(request):
    form = BuildForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'build/buildCreate.html', locals())