from django.shortcuts import render
from django.http import HttpResponse
from build.models import Build, BuildForm
# Create your views here.
def getRevBuild(build_title, build_cont):
	build_cont.append(Cdps_support,)
	build_title.append(Tdps_support,)
	print("first : ")
	print(build_title)


Tdps_support = "Hérault DPS/Support"
Cdps_support = """Cet archétype trés polyvalent est valable aussi bien en raid qu'en fractales haut niveaux.
Il permet d'obtenir un bon DPS, beacoup de contréle et une excellente survivabilité.
Néanmoins, si votre groupe n'a pas besoin de plus d'avantages ou de contréle, une classe de DPS pur sera plus approprié

<h1>Equipement</h1>
Toutes l'équipement en statistiques berserker
Armes : Epée/Hache () Baton
Runes : Runes de l'érudit
Cachets : Cachet d'éclair + Cachet de fermeté sur les deux sets

<h1>Compétences</h1>
Dans la majorité des cas, utilisez les légendes Brill et Jalis.
Si il faut que vous ayez accés é du debuff, utilisez Mallyx au lieu de Jalis.
Si votre groupe ne posséde aucun mesmer, vous pouvez utiliser Shiro au lieu de Jalis.

<h1>Aptitudes</h1>

<h1>Utilisation en combat</h1>

Le cycle de dps repose sur le changement de légende, disponible toutes les 10 secondes.
En effet, ce changement redonne 50 point d'énergie, ce qui permet de consommer 5pts/sec en permanance.
On garde la facette de la nature active durant tout le combat. Ensuite, cycle est donc séparé en deux phase:

Brill:
	-On active la facette de vitesse, fureur et protection
	-On décharge la facette de vitesse sur la cible
	-On continu l'auto-attaque en utilisant 'off-cd' la compétence 2 de l'épée et la facette des élements
Lorsque on redescent bas en énergie (vers 5pts), on change pour l'autre légende de faéon é ne pas tomber é court d'énergie, ce qui annulerai la facette de nature
Ensuite, selon 2nd légende:
Jalis :
	-On active Marteaux vengeur
Mallyx:
	-On active Etreindre les ténébres
Shiro:
	-On active Probabilité improbable

Puis de la méme maniére qu'avec Brill, on utilise autant que possible le 1 et le 2 de l'épée, puis on change de légende vers 5pts.
Les compétences 3, 4 et 5 n'ont aucun intéret dans l'optique d'optimiser vos dégats.
Lorsque vous utilisez les Marteaux Vengeurs de Jalis, faites trés attention : Ce sont des entités é part entiéres, qui peuvent tomber ou se casser (sur les champignons du Gardien de la Vallée par exemple...)

Lorsque vous devez controler un boss, utilisez le 5 é l'épée, changer d'arme pour le baton, executez le 5 de maniére é toucher le plus de fois possible le boss (5 coup maximum), puis:
Si le contréle n'est pas critique, finissez avec la chaine d'attaque du 2 au béton, sinon déchargez la facette (A éviter si possible)."""

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
###

def convertToHtml(s):
    html = s.replace('\n', '<br \>')
    html = html.replace('\t', '&emsp;&emsp;')
    return html

def getBuilds(prof, build_title, build_cont):
    if (prof == "revenant"):
        getRevBuild(build_title, build_cont)
        print("inter : ")
        print(build_title)
        for i in range(0, len(build_cont)):
            build_cont[i] = convertToHtml(build_cont[i])

def view_buildSelect(request):
    return render(request, 'build/buildSelect.html', {'prof' : zip(prof_name, prof_icon, prof_url)})

def view_build(request, prof):
    if prof in prof_url:
        build_title = []
        build_cont = []
        getBuilds(prof, build_title, build_cont)
        print("final : ")
        print(build_title)
        #getBuildTitle(build_list)
        #build_cont = getBuildText(build_list)
        isEmpty = bool(len(build_title)==0)
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