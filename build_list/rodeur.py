def getRodBuild(build_title, build_cont):
	cont = [C_dcondi, C_rcondi, C_heal]
	title = [T_dcondi, T_rcondi, T_heal]
	for c in cont:
		build_cont.append(c)
	for t in title:
		build_title.append(t)


T_heal = "Druide Heal"
C_heal = """
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

T_dcondi = "Druide Altération/Support"
C_dcondi = """
Ce build est adapté pour les raids et fractales HL, il propose des dégats par altération très correct en plus de pouvoir apporter du soin et du boost de dommage au groupe.
Si votre groupe possède déjà un druide ou à besoin de plus de dégats par altération, vous pouvez facilement changez vos aptitudes pour le build Rôdeur Altération.

<h1>Equipement</h1>

Toutes l'équipement en statistiques vipérin
<ul>
	<li>Armes :<ul>
			<li>Hache/Torche</li>
			<li>Arc court</li>
		</ul>
	<li>Runes : 4 runes du Cauchemard + 2 runes du Trappeur</li>
	<li>Cachets : Cachet de Terre sur les deux armes, et si vous êtes au corps à corps, cachets de Géomancie, d'explosion sinon.</li>
</ul>

<h1>Compétences</h1>

<img src="http://i.imgur.com/2sv8Qvz.png"/>

Vous pouvez remplacer l'esprit du soleil par la glyphe des marées pour avoir accès à du contrôle de zone (Pour les Fureteurs du Gardien de la vallée par exemple), et Utiliser la compétence Enchevêtrement (ulti) pour avoir accès à plus d'immobilisation (Fureteur, esprit de Gorseval ou warg de l'escorte par exemple).

<h1>Aptitudes</h1>

<img src="http://i.imgur.com/7jORhqn.jpg"/>

<h1>Utilisation en combat</h1>

Commencez le combat avec l'arc court, et placez vos esprit juste avant d'engager le combat si possible (puis réinvoquez-les dès que possible durant tout le combat).
<h2>Rotation :</h2>
<ul>
  <li>1. Début de combat : Arc court :<ul>
		<li>Salve de Poison</li>
		<li>Changez d'arme pour activer l'aptitude Visée rapide</li>
  </ul>
  
  <li>2. Phase Hache torche :<ul>
		<li>Lancer Feu de joie pour utiliser la Visée rapide</li>
		<li>Utilisez les compétences Lames multiples, Jet de torche et Morsure de l'hiver</li>
		<li>Lancer un deuxième Feu de joie</li>
		<li>Utilisez les compétences Lames multiples, Jet de torche et Morsure de l'hiver</li>
		<li>Lorsque le rechargement de Feu de joie est à 10-12 secondes, changez d'arme</li>
  </ul>
  <li>3. Phase Arc court :<ul>
		<li>Salve de Poison pour utiliser la Visée rapide</li>
		<li>Utilisez Tir invalidant autant que possible</li>
		<li>Changez d'arme dès que possible et reprenez au 2.</li>
  </ul>
  <li>Si vous devez soigner :<ul>
		<li>Utilisez l'Avatar Célèste, ce qui enclanche Visée rapide</li>
		<li>Marée rajeunissante pour utiliser la visée rapide</li>
		<li>Impact lunaire</li>
		<li>Marée rajeunissante</li>
		<li>Impact lunaire</li>
		<li>Quittez l'avatar célèste</li>
    </ul>
</ul>
"""

T_rcondi = "Rôdeur Altération"
C_rcondi = """
Ce build est adapté pour les raids et fractales HL, il donne un des meilleur DPS du jeu, par altération. Si votre groupe a besoin d'un peu plus de support vous pouvez changez vos aptitudes pour passer Druide Condition.

<h1>Equipement</h1>

Toutes l'équipement en statistiques vipérin
<ul>
	<li>Armes :<ul>
			<li>Hache/Torche</li>
			<li>Arc court</li>
		</ul>
	<li>Runes : 4 runes du Cauchemard + 2 runes du Trappeur</li>
	<li>Cachets : Cachet de Terre sur les deux armes, et si vous êtes au corps à corps, cachets de Géomancie, d'explosion sinon.</li>
</ul>

<h1>Compétences</h1>

<img src="http://i.imgur.com/sqor6a1.png"/>

Vous pouvez remplacer l'esprit du soleil par la glyphe des marées pour avoir accès à du contrôle de zone (Pour les Fureteurs du Gardien de la vallée par exemple), et Utiliser la compétence Enchevêtrement (ulti) pour avoir accès à plus d'immobilisation (Fureteur, esprit de Gorseval ou warg de l'escorte par exemple).

<h1>Aptitudes</h1>

<img src="http://i.imgur.com/ylrFd4n.png"/>

<h1>Utilisation en combat</h1>

Commencez le combat avec l'arc court, et placez vos esprit juste avant d'engager le combat si possible (puis réinvoquez-les dès que possible durant tout le combat).
<h2>Rotation :</h2>
<ul>
  <li>1. Début de combat : Arc court :<ul>
		<li>Salve de Poison</li>
		<li>Changez d'arme pour activer l'aptitude Visée rapide</li>
  </ul>
  
  <li>2. Phase Hache torche :<ul>
		<li>Lancer Feu de joie pour utiliser la Visée rapide</li>
		<li>Utilisez les compétences Lames multiples, Jet de torche et Morsure de l'hiver</li>
		<li>Lancer un deuxième Feu de joie</li>
		<li>Utilisez les compétences Lames multiples, Jet de torche et Morsure de l'hiver</li>
		<li>Lorsque le rechargement de Feu de joie est à 10-12 secondes, changez d'arme</li>
  </ul>
  <li>3. Phase Arc court :<ul>
		<li>Salve de Poison pour utiliser la Visée rapide</li>
		<li>Utilisez Tir invalidant autant que possible</li>
		<li>Changez d'arme dès que possible et reprenez au 2.</li>
  </ul>
</ul>
"""