def getNecBuild(build_title, build_cont):
	cont = [C_condi,]
	title = [T_condi,]
	for c in cont:
		build_cont.append(c)
	for t in title:
		build_title.append(t)


T_condi = "Faucheur condition"
C_condi = """
<h1>Equipement</h1>

Toutes l'équipement en statistiques vipérin, sauf Amulette et les 2 Anneaux en Sinistre
<ul>
	<li>Armes :<ul>
			<li>Sceptre/Dague</li>
			<li>Cor de Guerre</li>
		</ul>
	<li>Runes : Runes d'épines</li>
	<li>Cachets : Cachet d'Agonie et Cachet de Terre (ou Géomancie)</li>
</ul>

<h1>Compétences</h1>

<img src="http://i.imgur.com/U9g9gn4.jpg"/>

<h1>Aptitudes</h1>

<img src="http://i.imgur.com/aLOXbCN.jpg"/>

<h1>Utilisation en combat</h1>

<h2>Rotation :</h2>
<ul>
  <li></li>
</ul>
"""