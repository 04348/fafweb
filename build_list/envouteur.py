def getEnvBuild(build_title, build_cont):
	cont = [C_dps, C_tank]
	title = [T_dps, T_tank]
	for c in cont:
		build_cont.append(c)
	for t in title:
		build_title.append(t)


T_dps = "Chronomancien DPS"
C_dps = """
<h1>Equipement</h1>

Toutes l'équipement en statistiques Berserker, Sac à dos Exotique avec un doublon de Platine
<ul>
	<li>Armes :<ul>
			<li>Epée/Bouclier</li>
			<li>Focus ou Epée(main gauche)</li>
		</ul>
	<li>Runes : Rune de Charisme</li>
	<li>Cachets : Cachet de Concentration sur l'épée(Main droite) et cachet de Fermeté pour la main gauche</li>
</ul>

<h1>Compétences</h1>

<img src="http://i.imgur.com/1pz3Im7.jpg"/>

<h1>Aptitudes</h1>

<img src="http://i.imgur.com/TjC7IRD.jpg"/>

<h1>Utilisation en combat</h1>

<h2>Rotation :</h2>
<ul>
  <li></li>
</ul>
"""

T_tank = "Chronomancien Tank"
C_tank = """
<h1>Equipement</h1>

Equipement en statistiques Berserker, Sac à dos Exotique avec un doublon de Platine
SAUF Deux choix : 1 anneau et 2 accessoires en Chevalier OU Les 6 pièces d'armure en Commandant
<ul>
	<li>Armes :<ul>
			<li>Epée/Bouclier</li>
			<li>Focus ou Epée(main gauche)</li>
		</ul>
	<li>Runes : Rune de Charisme</li>
	<li>Cachets : Cachet de Concentration sur l'épée(Main droite) et cachet de Fermeté pour la main gauche</li>
</ul>

<h1>Compétences</h1>

<img src="http://i.imgur.com/1pz3Im7.jpg"/>

<h1>Aptitudes</h1>

<img src="http://i.imgur.com/TjC7IRD.jpg"/>

<h1>Utilisation en combat</h1>

<h2>Rotation :</h2>
<ul>
  <li></li>
</ul>
"""