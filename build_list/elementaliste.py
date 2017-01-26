def getEleBuild(build_title, build_cont):
	cont = [C_baton, C_fa]
	title = [T_baton, T_fa]
	for c in cont:
		build_cont.append(c)
	for t in title:
		build_title.append(t)

#item <a href="http://db.gw2.fr/item/46773">Fiole de sel</a>

T_baton = "Cataclyste DPS Bâton"
C_baton = """
Ce build permet d'obtenir le meuilleur DPS possible sur une cible à grosse zone de collision. Si vous comptez vous battre contre une cible à petite zone de collision (VG, Sabetha, ...), le build Fresh Air est plus adapté.
<h1>Equipement</h1>

Toutes l'équipement en statistiques Berserker
<ul>
	<li>Arme :<ul>
			<li>Bâton</li>
		</ul>
	<li>Runes : Rune d'érudit supérieure</li>
	<li>Cachets : Cachet de fermeté supérieur + Cachet d'exactitude supérieur</li>
</ul>

<h1>Compétences</h1>
<p></p>
<img src="http://i.imgur.com/XcSBRq4.jpg"/>

<h1>Aptitudes</h1>

<img src="http://i.imgur.com/G246KhD.jpg"/>

<h1>Utilisation en combat</h1>

<h2>Rotation :</h2>
<ul>
  <li></li>
</ul>
"""

T_fa = "Cataclyste \"Fresh Air\""
C_fa = """
<h1>Equipement</h1>

Toutes l'équipement en statistiques Berserker
<ul>
	<li>Armes :<ul>
			<li>Dague</li>
			<li>Cor de Guerre</li>
		</ul>
	<li>Runes : Runes de l'érudit</li>
	<li>Cachets : Cachet d'Air et Cachet de Fermeté</li>
</ul>

<h1>Compétences</h1>

<img src="http://i.imgur.com/thTy47d.jpg"/>

<h1>Aptitudes</h1>

<img src="http://i.imgur.com/FHSdvDI.jpg"/>

<h1>Utilisation en combat</h1>

<h2>Rotation :</h2>
<ul>
  <li></li>
</ul>
"""