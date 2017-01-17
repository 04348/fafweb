def getEleBuild(build_title, build_cont):
	cont = [C_baton, C_fa]
	title = [T_baton, T_fa]
	for c in cont:
		build_cont.append(c)
	for t in title:
		build_title.append(t)


T_baton = "Cataclyste DPS Bâton"
C_baton = """
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

T_fa = "Cataclyste \"Fresh Air\""
C_fa = """
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