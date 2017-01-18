def getRevBuild(build_title, build_cont):
	cont = [C_dps_support, ]
	title = [T_dps_support, ]
	for c in cont:
		build_cont.append(c)
	for t in title:
		build_title.append(t)

#Titre : <h1>titre</h1>
#Image : <img src="url" />
#Liste : <ul>
#  			<li></li>
#  			<li>
#    			<ul>
#					<li></li>
#					<li></li>
#				</ul>
#			</li>
#			<li>/li>
#			</ul>

T_dps_support = "Hérault DPS/Support"
C_dps_support = """
Cet archétype très polyvalent est valable aussi bien en raid qu'en fractales haut niveaux. Il permet d'obtenir un bon DPS, beacoup de contrôle et une excellente survivabilité.
Néanmoins, si votre groupe n'a pas besoin de plus d'avantages ou de contréle, une classe de DPS comme l'élémentaliste ou le voleur sera plus approprié.

<h1>Equipement</h1>

Toutes l'équipement en statistiques berserker
<ul>
	<li>Armes :<ul>
			<li>Epée/Hache </li>
			<li>Baton</li>
		</ul>
	<li>Runes : Runes de l'érudit</li>
	<li>Cachets : Cachet d'éclair + Cachet de fermeté sur les deux sets</li>
</ul>
<h1>Compétences</h1>
Dans la majorité des cas, utilisez les légendes Brill et Jalis.
Si il faut que vous ayez accès à du debuff, utilisez Mallyx au lieu de Jalis.
Si votre groupe ne possède aucun mesmer, vous pouvez utiliser Shiro au lieu de Jalis.

<img src="http://i.imgur.com/7mE2Vbo.png"/>

<h1>Aptitudes</h1>

<img src="http://i.imgur.com/Qa137HJ.jpg"/>
Dévastation 2-3-1, Invocation 2-1-1, Hérault 2-2-1
<h1>Utilisation en combat</h1>

Le cycle de dps repose sur le changement de légende, disponible toutes les 10 secondes. En effet, ce changement redonne 50 point d'énergie, ce qui permet de consommer 5pts/sec en permanance.

<h2>Rotation :</h2>
<ul>
  <li>Activez la Facette de la nature et gardez-la active pendant tout la durée du combat (à moins que vous n'utilisiez Shiro)</li>
  <li>Brill :<ul>
		<li>Activer Facette des éléments, Facette de l'ombre et Facette du Chaos</li>
		<li>Décharger la Facette des éléments (Vous pouvez attendre un peu si la cible est en mouvement)</li>
		<li>Lancez autant que possible le 2 à l'épée (Frappe chirurgicale)</li>
		<li>Continuez avec l'auto attaque et le 2 jusqu'a arriver à moins de 5 points d'énergie et changez de légende</li>
    </ul>
  </li>
  <li>Jalis<ul>
		<li>Activez les Marteaux Vengeurs</li>
		<li>Continuez avec l'auto attaque et le 2 jusqu'a arriver à moins de 5 points d'énergie et changez de légende</li>
    </ul>
  </li>
  <li>Mallyx<ul>
		<li>Activez Succomber aux ténèbres</li>
		<li>Continuez avec l'auto attaque et le 2 jusqu'a arriver à moins de 5 points d'énergie et changez de légende</li>
    </ul>
  </li>
  <li>Jalis<ul>
		<li>Activez Probabilités improbables</li>
		<li>Continuez avec l'auto attaque jusqu'à arriver à moins de 5 points d'énergie et changez de légende</li>
    </ul>
  </li>
</ul>

Les compétences 3, 4 et 5 n'ont aucun intéret dans l'optique d'optimiser vos dégats.
Lorsque vous utilisez les Marteaux Vengeurs de Jalis, faites très attention : ils peuvent tomber ou se casser (sur les champignons du Gardien de la Vallée par exemple...)


Lorsque vous devez contrôler un boss, utilisez le 5 à l'épée, changez d'arme pour le baton, executez le 5 après avoir un peu reculé de manière à toucher le plus de fois possible le boss (jusqu'a 5 coup), puis si le contréle n'est pas critique, finissez avec la chaine d'attaque du 2 au bâton, sinon déchargez la Facette du Chaos (A éviter si possible).
"""
