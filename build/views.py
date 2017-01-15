from django.shortcuts import render
from django.http import HttpResponse
from build.models import Build, BuildForm
from build_list.revenant import getRevBuild

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

def convertToHtml(s):
    html = s.replace('\n', '<br \>')
    html = html.replace('\t', '&emsp;&emsp;')
    return html

def getBuilds(prof, build_title, build_cont):
    if (prof == "revenant"):
        getRevBuild(build_title, build_cont)

    for i in range(0, len(build_cont)):
        build_cont[i] = convertToHtml(build_cont[i])

def view_buildSelect(request):
    return render(request, 'build/buildSelect.html', {'prof' : zip(prof_name, prof_icon, prof_url)})

def view_build_n(request, prof, n):
    if prof in prof_url:
        build_title = []
        build_cont = []
        getBuilds(prof, build_title, build_cont)
        isEmpty = bool(len(build_title)==0)
        try:
            n = int(n)
        except:
            raise Http404
        if (n > 0 and n <= len(build_title)):
            buildNum = n
        else:
            buildNum = 0
        return render(request, 'build/build.html', {'prof':prof ,'builds': zip(build_title, build_cont), 'titles':build_title, 'isEmpty':isEmpty, 'buildNum':buildNum})
    raise Http404

def view_build(request, prof):
    return view_build_n(request, prof, 1)

#Old version, using DB (canceled du to 20 simultaneous connection max on psotgre)
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