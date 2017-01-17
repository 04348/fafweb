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

Toutes l'équipement en statistiques 
<ul>
	<li>Armes :<ul>
			<li></li>
			<li></li>
		</ul>
	<li>Runes : </li>
	<li>Cachets : </li>
</ul>

<h1>Compétences</h1>

<img src=""/>

<h1>Aptitudes</h1>

<img src=""/>

<h1>Utilisation en combat</h1>

<h2>Rotation :</h2>
<ul>
  <li></li>
</ul>
"""

T_tank = "Chronomancien Tank"
C_tank = """
<h1>Equipement</h1>

Toutes l'équipement en statistiques 
<ul>
	<li>Armes :<ul>
			<li></li>
			<li></li>
		</ul>
	<li>Runes : </li>
	<li>Cachets : </li>
</ul>

<h1>Compétences</h1>

<img src=""/>

<h1>Aptitudes</h1>

<img src=""/>

<h1>Utilisation en combat</h1>

<h2>Rotation :</h2>
<ul>
  <li></li>
</ul>
"""