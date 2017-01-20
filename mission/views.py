from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
m_url = ["rando", "prime", "defi", "puzzle", "course"]

m_name = ["Randonnés", "Primes", "Défis", "Puzzles", "Courses"]

m_icon = ["http://i.imgur.com/UyqQ3Z5.png",
		  "http://i.imgur.com/A51dpIP.png",
		  "http://i.imgur.com/LhkhmhT.png",
		  "http://i.imgur.com/4lC2KDK.png",
		  "http://i.imgur.com/NZSTAXy.png",]

def view_missionSelect(request):
	return render(request, 'mission/missionSelect.html', {'missions': zip(m_name, m_url, m_icon)})

def view_mission(request, mission):
	if mission in m_url:
		if (mission == "course"):
			list_mission = list_course
			tp_mission = tp_course
			name = m_name[4]
		elif (mission == "defi"):
			list_mission = list_defi
			tp_mission = tp_defi
			name = m_name[2]
		elif (mission == "prime"):
			list_mission = list_prime
			tp_mission = tp_prime
			name = m_name[1]
		elif (mission == "puzzle"):
			list_mission = list_puzzle
			tp_mission = tp_puzzle
			name = m_name[3]
		else:
			list_mission = list_rando
			tp_mission = tp_rando
			name = m_name[0]
		return render(request, 'mission/mission.html', {'mission': zip(list_mission, tp_mission), 'm_name':name})
	raise Http404

list_puzzle = [
	["Laboratoire de proxémie", "Terres sauvages de Brisban", ["http://i.imgur.com/zpGFPYz.jpg"], ],
	["Domaine de Langmar", "Plaines d’Ashford", ["http://i.imgur.com/z5JGizB.jpg"], ],
	["Cache d’Angvar", "Congères d’Antreneige", ["http://i.imgur.com/6BdaLZC.jpg"], ],
]

tp_puzzle = [
	"[&BPkGAAA=]", #Laboratoire de proxémie
	"[&BPgGAAA=]", #Domaine de Langmar
	"[&BP8GAAA=]", #Cache d’Angvar
]

list_defi = [
	["Brise-attaque des eaux du Tourment", "Steppes de la Strie Flamboyante", ["http://i.imgur.com/6RXIhCt.jpg"], ],
	["Stigmatisation et mise à mort", "Champs de Ruines", ["http://i.imgur.com/4YbgoyP.jpg"], ],
	["De gros problèmes", "Mont Maelstrom", ["http://i.imgur.com/Iy4lLT7.jpg"], ],
	["Sauvetage de ravitaillement", "Marais de Fer", ["http://i.imgur.com/41zkUP7.jpg"], ],
	["Défendez la sentinelle de la brèche", "Chutes de la Canopée", ["http://i.imgur.com/UZK47Fk.jpg"], ],
	["Lancer de crabe à Sud-Soleil", "Crique de Sud-Soleil", ["http://i.imgur.com/uFWjmys.jpg"], ],
]

tp_defi = [
	"[&BPsBAAA=]", #Brise-attaque des eaux du Tourment
	"[&BEsBAAA=]", #Stigmatisation et mise à mort
	"[&BNICAAA=]", #De gros problèmes
	"[&BOoBAAA=]", #Sauvetage de ravitaillement
	"[&BEYEAAA=]", #Défendez la sentinelle de la brèche
	"[&BNAGAAA=]", #Lancer de crabe à Sud-Soleil
]

list_course = [
	["Foulée de l'Ourse", "Passage de Lornar", ["http://i.imgur.com/0ETDu4t.jpg"], ],
	["Poulet en fuite", "Champs de Ruines", ["http://i.imgur.com/8NjwfW3.jpg"], ],
	["Fugue du crabe", "Crique du Sud Soleil", ["http://i.imgur.com/G80N0HD.jpg"], ],
	["Terrier du Dévoreur", "Plateau de Diessa", ["http://i.imgur.com/gcyLGct.jpg"], ],
	["Fuite du loup fantôme", "Hinterlands Harathis", ["http://i.imgur.com/PIMk8LP.jpg"], ],
	["Course arachnide", "Falaises de Hantedraguerre", ["http://i.imgur.com/S8wNxbk.jpg"], ],
	["Pagaie quaggan", "Détroit des gorges glacées", ["http://i.imgur.com/u7TtGJq.jpg"], ],
]

tp_course = [
	"[&BOkAAAA=]", #Foulée de l'Ourse
	"[&BEwBAAA=]", #Poulet en fuite
	"[&BNAGAAA=]", #Fugue du crabe
	"[&BMkDAAA=]", #Terrier du Dévoreur
	"[&BKUAAAA=]", #Fuite du loup fantôme
	"[&BF0CAAA=]", #Course arachnide
	"[&BIACAAA=]", #Pagaie quaggan
]

list_prime = [
	["\"Adjointe\" Brooke", "Congères Antreneige ", ["http://i.imgur.com/EhzO7wG.jpg?1"],],
	["André \"Sauvage\" Douest", "Crique de sud-soleil ", ["http://i.imgur.com/yyEujzb.jpg?1"],],
	["Bwiki le Rat de bibiliothèque", "Passage de Lornar ", ["http://i.imgur.com/u4FOC4Y.jpg"],],
	["Brekkabek le Skritt", "Hinterlands Harathis ", ["http://i.imgur.com/lqk8y44.jpg"],],
	["Chaman Arderus Montée", "Flambecoeur ", ["http://i.imgur.com/NdlIw51.jpg"],],
	["Croisée Michèle", "Marais de Lumillule ", ["http://i.imgur.com/1RRKliB.jpg"],],
	["Félix Colairik", "Plateau diessa ", ["http://i.imgur.com/07Fkog2.jpg?1"],],
	["Komali Micui", "Mont Maelstrom ", ["http://i.imgur.com/KXX9kiI.jpg"],],
	["Mayana Imposant", "Marais de Lumillule  ", ["http://i.imgur.com/HqLRN8S.jpg"],],
	["Poobadoo", "Colline de Kessex ", ["http://i.imgur.com/i8lKkFh.jpg"],],
	["Prisonnier 1411", "Marais de fer ", ["http://i.imgur.com/SVwrG6C.jpg"],],
	["6-RUS", "Chutes de la Canopée ", ["http://i.imgur.com/JbfvXpE.jpg"],],
	["Sotzz le voyou", "Champs Gendarran ", ["http://i.imgur.com/ceg8i4R.jpg?1"],],
	["Tarban le Diplomate", "Terres sauvages de Brisban ", ["http://i.imgur.com/PEqLFe1.jpg"],],
	["Teesa la Louche", "Détroit des gorge glacées ", ["http://i.imgur.com/m0YWBFr.jpg"],],
	["Trekksa la Rusée", "Steppes Stries Flamboyantes ", ["http://i.imgur.com/kqpufgM.jpg"],],
	["Trillia Mylieu", "Champs de ruines ", ["http://i.imgur.com/6q821J8.jpg"],],
	["Yanonka, la palefrenière de rats", "Champs de ruines ", ["http://i.imgur.com/9SFufAk.jpg"],],
]

tp_prime = [
	"", #"Adjointe" Brooke
	"", #André \"Sauvage\" Douest
	"", #Bwiki le Rat de bibiliothèque
	"", #Brekkabek le Skritt
	"", #Chaman Arderus Montée", "Flambecoeur
	"", #Croisée Michèle", "Marais de Lumillule
	"", #Félix Colairik", "Plateau diessa
	"", #Komali Micui", "Mont Maelstrom
	"", #Mayana Imposant", "Marais de Lumillule
	"", #Poobadoo", "Colline de Kessex
	"", #Prisonnier 1411", "Marais de fer
	"", #6-RUS", "Chutes de la Canopée
	"", #Sotzz le voyou", "Champs Gendarran
	"", #Tarban le Diplomate", "Terres sauvages de Brisban
	"", #Teesa la Louche", "Détroit des gorge glacées
	"", #Trekksa la Rusée", "Steppes Stries Flamboyantes
	"", #Trillia Mylieu", "Champs de ruines
	"", #Yanonka, la palefrenière de rats
]

list_rando = [
	["Alcôve de Courtilleracine" ,"Le Bosquet, Point de passage : portail asura",
		["http://image.noelshack.com/fichiers/2013/16/1366476839-gardenroot-alcove-le-bosquet-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476829-gardenroot-alcove-le-bosquet-1.jpg" ] ],
	["Alimentation en eau d’Orvanic" ,"Marais de la Lumillule, Point de passage du goulet de l'océan",
		["http://image.noelshack.com/fichiers/2013/16/1366537156-orvanic-sourcewaters-lumillule-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366537169-organic-sourcewaters-lumillule-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366537196-organic-sourcewaters-lumillule-3.jpg" ] ],
	["Antre cachécailleux ","Plaine d'Ashford, Point de passage de Féritas",
		["http://image.noelshack.com/fichiers/2013/19/1368291278-skalestash-hideway-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368291284-skalestash-hideway-2.jpg" ] ],
	["Antre de Hurleneige" ,"Contreforts d'Antreneige, Point de passage de la terrasse du faucon des neiges",
		["http://image.noelshack.com/fichiers/2013/16/1366547289-snowhowl-den-congeres-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366547301-snowhowl-den-congeres-2.jpg" ] ],
	["Autel d’Inondesel" ,"Marais de la Lumillule, Point de passage d'Inondesel",
		["http://image.noelshack.com/fichiers/2013/16/1366544859-saltflood-altar-lumillule-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366544874-saltflood-altar-lumillule-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366544882-saltflood-altar-lumillule-3.jpg", "http://image.noelshack.com/fichiers/2013/16/1366544890-saltflood-altar-lumillule-4.jpg" ] ],
	["Aveuglement de l'Erudit" ,"Falaise de Hantedraguerre, Point de passage de Steelbrachen",
		["http://image.noelshack.com/fichiers/2013/16/1366545043-scholar-s-blind-hantedraguerre-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545055-scholar-s-blind-hantedraguerre-2.jpg" ] ],
	["Balcon des délices" ,"Saut de Malchor, Point de passage de Pagga", ["http://image.noelshack.com/fichiers/2013/16/1366454028-delight-s-balcony-malchor-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366454038-delight-s-balcony-malchor-2.jpg", 								 "http://image.noelshack.com/fichiers/2013/16/1366454049-delight-s-balcony-malchor-3.jpg" ] ],
	["Banc de Varech de Malméduse" ,"Congères d'Antreneige, Point de Passage de l'Exil ou de Vaselac",
		["http://image.noelshack.com/fichiers/2013/14/1365369175-badjelly-kelpbed-congeres-d-entreneige.jpg", "http://image.noelshack.com/fichiers/2014/23/1402058594-banc-de-varech-malmeduse04.jpg" ] ],
	["Barrière de Bercebruyère" ,"Forêt de Caledon, Point de passage de la Spirale",
		["http://image.noelshack.com/fichiers/2013/16/1366371370-briarthorn-barrier-foret-de-caledon-passage-de-la-spirale.jpg", "http://image.noelshack.com/fichiers/2014/23/1402058836-barriere-de-bercebruyere04.jpg" ] ],
	["Bassin de la Sentinelle" ,"Marais de fer, Point de passage du campement du Guet du stigmate",
		["http://image.noelshack.com/fichiers/2013/16/1366545283-sentinel-sink-marais-de-fer-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545296-sentinel-sink-marais-de-fer-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545305-sentinel-sink-marais-de-fer-3.jpg" ] ],
	["Belvédère goutedo " ,"Passage de Lornar, Point de passage de la complainte",
		["http://image.noelshack.com/fichiers/2013/21/1369238775-steamscrap-overlook-1.jpg", "http://image.noelshack.com/fichiers/2013/21/1369238779-steamscrap-overlook-2.jpg" ] ],
	["Bistrot rouport " ,"Citadelle noire, Point de passage du Terrain de rassemblement",
		["http://image.noelshack.com/fichiers/2013/19/1368289391-wheelport-pub-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368289397-wheelport-pub-2.jpg", "http://image.noelshack.com/fichiers/2013/19/1368289402-wheelport-pub-3.jpg" ] ],
	["Bivouac du Lys" ,"Province de Métrica, Point de passage de la vieille fonderie de golems",
		["http://image.noelshack.com/fichiers/2013/16/1366478370-lily-s-bivvy-flambecoeur-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366478380-lily-s-bivvy-flambecoeur-2.jpg" ] ],
	["Bord de Valaigu" ,"Steppes de la Strie flamboyante, Point de passage du Fort de crête fendue",
		["http://image.noelshack.com/fichiers/2013/16/1366545353-sharkhallow-s-edge-strie-flamboyante-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545368-sharkhallow-s-edge-strie-flamboyante-2.jpg" ] ],
	["Bosquet de Tarstar" ,"Montée de Flambecoeur, Point de passage de l'Apostat",
		["http://image.noelshack.com/fichiers/2013/16/1366551837-tarstar-copse-flambecoeur-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366551848-tarstar-copse-flambecoeur-2.jpg" ] ],
	["Boucherie piègécayeux " ,"Marais de fer, Point de passage du village d'Attrapécaille",
		["http://image.noelshack.com/fichiers/2013/19/1368361357-skalecatch-butcher-shop-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368361361-skalecatch-butcher-shop-2.jpg" ] ],
	["Cache à miel de Boisecoeur" ,"Vallée de la Reine, Point de passage de Phinney",
		["http://image.noelshack.com/fichiers/2013/16/1366477565-heartwood-honey-cache-vallee-de-la-reine.jpg" ] ],
	[" Cache de l’Ours des cavernes" ,"Congères d'Antreneige, Point de passage du faucheur",
		["http://image.noelshack.com/fichiers/2014/23/1402061466-cache-de-lours-des-cavernes03.jpg", "http://image.noelshack.com/fichiers/2014/23/1402061468-cache-de-lours-des-cavernes04.jpg" ] ],
	["Cache du fugitif" ,"Rivage maudit, Point de passage du pénitent",
		["http://image.noelshack.com/fichiers/2013/16/1366376430-cache-of-the-pursued-rivage-maudit-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366376472-cache-of-the-pursued-rivage-maudit-2.jpg" ] ],
	["Caisse du marchand" ,"Hoelbrak, Point de passage de Peeta",
		["http://image.noelshack.com/fichiers/2013/16/1366552486-trader-s-tash-hoelbrak-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366552491-trader-s-tash-hoelbrak-2.jpg" ] ],
	["Camp principal du gardien" ,"Hinterlands Arathis, Point de passage de Grey Gritta",
		["http://image.noelshack.com/fichiers/2013/16/1366477436-guardian-overwatch-hinterlands-arathis-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477426-guardian-overwatch-hinterlands-arathis-1.jpg" ] ],
	["Canyons de Gallow" ,"Terres sauvages de Brisban, Point de passage des prés de potence",
		["http://image.noelshack.com/minis/2013/16/1366471806-161731canyonsdegallow.png", "http://image.noelshack.com/fichiers/2013/16/1366476748-gallow-canyons-brisban-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476781-gallow-canyons-brisban-2.jpg" ] ],
	["Carré de chou du bandit" ,"Hinterlands Arathis, Point de passage de Démétra",
		["http://image.noelshack.com/fichiers/2013/14/1365368045-bandit-s-cabbage-patch-hinterlands-harathis.jpg" ] ],
	["Cavité de la cathédrale" ,"Saut de Malchor, Point de passage de Wren",
		["http://image.noelshack.com/fichiers/2014/23/1402062970-cavite-de-la-cathedrale03.jpg", "http://image.noelshack.com/fichiers/2013/16/1366378509-cathedral-s-cavity-saut-de-malchior-2.jpg" ] ],
	["Cavité du Contremaître" ,"Falaises Hantedraguerre, Point de passage de Dociu",
		["http://image.noelshack.com/fichiers/2013/16/1366476270-foreman-s-recess-hantedraguerre-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476287-foreman-s-recess-hantedraguerre-2.jpg", "http://image.noelshack.com/fichiers/2014/23/1402063192-cavite-du-contremaitre04.jpg" ] ],
	["Cellier de la Garde du Lion" ,"Contreforts du voyageur, Point de passage du Refuge de Doubléperon",
		["http://image.noelshack.com/fichiers/2013/16/1366478424-lionguard-larder-contreforts-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366478435-lionguard-larder-contreforts-2.jpg" ] ],
	["Cellier du Lion Noir" ,"Le Bosquet, étage intermédiaire/inférieur, à l'hôtel des ventes",
		["http://image.noelshack.com/fichiers/2013/14/1365371640-black-lionroot-cellar-le-bosquet-passage-du-speculateur.jpg", "http://image.noelshack.com/fichiers/2014/23/1402063725-cellier-du-lion-noir04.jpg" ] ],
	["Champ de force de la cinquième brasse" ,"Détroit de la dévastation, Point de passage Fort Trinité",
		["http://image.noelshack.com/fichiers/2013/16/1366455696-fathom-five-forcefiels-devastation-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366455706-fathom-five-forcefield-devastation-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366455714-fathom-five-forcefield-devastation-3.jpg" ] ],
	["Champ de Montesauvage" ,"Côte de la marée sanglante, Point de passage de Remanda",
		["http://image.noelshack.com/fichiers/2013/16/1366539410-risewild-green-maree-sanglante-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366539423-risewild-green-maree-sanglante-2.jpg" ] ],
	["Châtiment de Bluup " ,"Rata Sum, Point de passage de Recherche (niveau inférieur)",
		["http://image.noelshack.com/fichiers/2013/19/1368287221-bluup-s-comeuppance-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368287324-bluup-s-comeuppance-2.jpg", "http://image.noelshack.com/fichiers/2013/19/1368287357-blupp-s-comeuppance-3.jpg", "http://image.noelshack.com/fichiers/2013/19/1368287382-bluup-s-comeuppance-4.jpg", "http://image.noelshack.com/fichiers/2013/19/1368287403-bluup-s-comeuppance-5.jpg" ] ],
	["Chute d’East End" ,"Terres sauvages de Brisban, Point de passage de East End",
		["http://image.noelshack.com/fichiers/2013/16/1366455454-east-end-falls-terres-sauvages-de-brisbane.jpg", "http://image.noelshack.com/fichiers/2014/23/1402064429-chutes-deast-end04.jpg" ] ],
	["Chutes de Gerbécaille " ,"Chutes de la Canopée, Point de passage d'Okaniroo (en général contesté), Point de passage de l'anneau",
		["http://image.noelshack.com/fichiers/2013/16/1366545583-skalesplash-fall-canopee-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545599-skalesplash-fall-canopee-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545624-skalesplash-fall-canopee-3.jpg" ] ],
	["Chutes de la Génitrice" ,"Détroit des Gorges glacées, Point de passage de la Courbe du Yak",
		["http://image.noelshack.com/fichiers/2013/16/1366372147-broodmother-falls-gorges-glacees-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366372172-broodmother-falls-gorges-glacees-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366372195-broodmother-falls-gorges-glacees-3.jpg" ] ],
	["Cisaillement interdit" ,"Saut de Malchor, Point de passage des murmures",
		["http://image.noelshack.com/fichiers/2013/16/1366476189-forbidden-shear-malchor-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476208-forbidden-shear-malchor-2.jpg" ] ],
	["Coeur du flacon du fondateur" ,"Champs de ruine, Point de passage de la Crécerelle",
		["http://image.noelshack.com/fichiers/2013/16/1366476418-founder-s-flagon-hearth-champs-de-ruines-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476463-founder-s-flagon-hearth-champs-de-ruines-2.jpg" ] ],
	["Coffre-fort de Kevach" ,"Contreforts du voyageur, Point de passage de la cave de Lostvyrm",
		["http://image.noelshack.com/fichiers/2013/21/1369238218-kevach-s-strongroom-1.jpg", "http://image.noelshack.com/fichiers/2013/21/1369238224-kevach-s-strongroom-2.jpg", "http://image.noelshack.com/fichiers/2013/21/1369238228-kevach-s-strongroom-3.jpg" ] ],
	["Coin d'Anya" ,"Plateau de Diessa, Ville de Nolan dans le renfoncement près du panorama", 
		["http://image.noelshack.com/minis/2013/14/1365360835-gw2-anyas-patch-guild-trek.png","http://image.noelshack.com/fichiers/2014/23/1402065254-coin-danya03.jpg" ] ],
	["Coin de Castavall" ,"Côte de la marée sanglante, Point de passage de Castavall",
		["http://image.noelshack.com/fichiers/2013/16/1366378112-castavall-corner-maree-sanglante-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366378137-castavall-corner-maree-sanglante-2.jpg" ] ],
	["Coin du Magièdre" ,"Province de Métrica, Point de passage de la Cour métrique",
		["http://image.noelshack.com/fichiers/2013/16/1366478528-magihedron-corner-rata-sum-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366478539-magihedron-corner-rata-sum-2.jpg" ] ],
	["Col des Frères" ,"Hoelbrack, Pavillon de la panthère des neiges",
		["http://image.noelshack.com/fichiers/2013/16/1366373443-brother-s-notch-veines-du-dragon-hoelbrach.jpg" ] ],
	["Col du Coeur criant" ,"Montée de Flambecoeur, Point de passage de l'Apostat",
		["http://image.noelshack.com/fichiers/2013/16/1366477506-heart-speaks-notch-flambecoeur-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477519-heart-speaks-notch-flambecoeur-2.jpg" ] ],
	["Console de commande principale LIN39 " ,"Province de Métrica, Point de passage Muridienne",
		["http://image.noelshack.com/fichiers/2013/19/1368293149-master-control-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368293155-master-control-2.jpg" ] ],
	["Contrepoids d’Osenfold" ,"Contreforts du voyageur, Point de passage d'Osenfold",
		["http://image.noelshack.com/fichiers/2013/16/1366537350-osenfold-counterweights-contreforts-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366537365-osenfold-counterweights-contreforts-2.jpg" ] ],
	["Côte de Couvedrake" ,"Plateau de Diessa, Point de passage Lac Brèchezeaux",
		["http://image.noelshack.com/fichiers/2013/16/1366454368-drakehatch-shore-lac-brechezeaux-plateau-de-diessa.jpg" ] ],
	["Côte de Tagotl " ,"Collines de Kesse, Point de passage de Viathan",
		["http://image.noelshack.com/fichiers/2013/16/1366551574-tagotl-shore-kessex-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366551588-tagotl-shore-kessex-2.jpg" ] ],
	["Cour des Chutes brisées" ,"Citadelle Noire, Point de passage Ruines de Rin",
		["http://image.noelshack.com/fichiers/2013/16/1366372422-broken-falls-courtyard-ruines-de-rin-citadelle-noire.jpg" ] ],
	["Cour des Chutes de la Biche" ,"Plaines d'Ashford, Point de passage de la Cité d'Ascalon",
		["http://image.noelshack.com/fichiers/2013/16/1366454245-doefalls-plaines-d-ashford.jpg" ] ],
	["Crevasse du Gibier" ,"Passage le Lornar, Point de passage de la maison de Vanjir",
		["http://image.noelshack.com/fichiers/2013/16/1366553483-venison-hollow-lornar-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366553493-venison-hollow-lornar-2.jpg" ] ],
	["Crique d’Isenfall" ,"Congères d'Antreneige, Point de passage d'Isenfall",
		["http://image.noelshack.com/fichiers/2013/19/1368367128-isenfall-wash-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368367134-isenfall-wash-2.jpg" ] ],
	["Crique de Trouvécaille" ,"Montée de Flambecoeur, Point de passage du poste de commandement de Tuyère",
		["http://image.noelshack.com/fichiers/2013/16/1366545509-skalefound-cove-flambecoeur-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545516-skalefound-cove-flambecoeur-2.jpg", "http://image.noelshack.com/fichiers/2014/23/1402067247-gw521.jpg" ] ],
	["Débarras d’Ulta" ,"Terres sauvages de Brisban, Point de passage de la Métamagique d' Ulta",
		["http://image.noelshack.com/fichiers/2013/16/1366552883-ulta-scraproom-brisban-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366552891-ulta-scraproom-brisban-2.jpg" ] ],
	["Dents de la corruption" ,"Détroit des gorges glacées, Point de passage de Drakkar",
		["http://image.noelshack.com/fichiers/2013/16/1366381538-corruption-s-teeth-gorges-glacees-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366381561-corruption-s-teeth-gorges-glacees-2.jpg" ] ],
	["Désir de Pochtecatl" ,"Côte de la Marée sanglante, Point de passage de Jelako",
		["http://image.noelshack.com/fichiers/2013/19/1368306852-pochtecatl-s-desire-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368306859-pochtecatl-s-desire-2.jpg" ] ],
	["Déversoir de Thaumanova" ,"Province de Métrica, Point de passage muridienne",
		["http://image.noelshack.com/fichiers/2013/16/1366551951-thaumanova-spillway-metrica-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366551962-thaumanova-spillway-metrica-2.jpg" ] ],
	["Distillerie de la Chouette cachée" ,"Congères d'Antreneige, Point de passage du Hibou",
		["http://image.noelshack.com/fichiers/2013/16/1366477672-hidden-owl-distillery-congeres-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477686-hidden-owl-distillery-congeres-2.jpg" ] ],
	["Dortoir du hall de Skibo " ,"Rata Sum, Point de passage auxiliaire",
		["http://image.noelshack.com/fichiers/2013/19/1368347709-skibo-hall-dormitory-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368347715-skibo-hall-dormitory-2.jpg", "http://image.noelshack.com/fichiers/2013/19/1368347718-skibo-hall-dormitory-3.jpg" ] ],
	["Échafaudage autoporteur" ,"Citadelle noire, Point de passage des Ruines de Rin",
		["http://image.noelshack.com/fichiers/2013/16/1366476584-freestand-scaffold-citadelle-noire.jpg" ] ],
	["Emplacement hanté" ,"Saut de Malchor, Point de passage des lumières",
		["http://image.noelshack.com/fichiers/2013/16/1366547831-spectrehaunt-socket-malchor-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366547840-spectrehaunt-socket-malchor-2.jpg" ] ],
	["Emprise agitée" ,"Mont Maelström, Point de passage du site du vieux traîneau",
		["http://image.noelshack.com/fichiers/2013/16/1366539142-restless-footings-maelstrom-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366539153-restless-footings-maelstrom-2.jpg" ] ],
	["Ermitage abandonné" ,"Steppes de la Strie flamboyante, Point de passage de la pierre gardienne",
		["http://image.noelshack.com/fichiers/2013/16/1366553362-vacant-hermitage-strie-flamboyante-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366553374-vancant-hermitage-strie-flamboyante2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366553379-vacant-hermitage-strie-flamboyante-3.jpg" ] ],
	["Escarpement du pêcheur" ,"Province de Métrica, Point de passage de la vieille fonderie de golems",
		["http://image.noelshack.com/fichiers/2013/16/1366475937-fisher-s-crag-province-de-metrica.jpg", "http://image.noelshack.com/fichiers/2014/23/1402072631-escarpement-du-pecheur04.jpg" ] ],
	["Etreinte de l’hymne" ,"Rivage maudit, Point de passage du rocher de l'épave", ["http://image.noelshack.com/minis/2013/19/1368200260-gw2-anthems-hold-guild-trek.png", "http://image.noelshack.com/fichiers/2013/19/1368374457-anthem-s-hold-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368374462-anthem-s-hold-2.jpg" ] ],
	["Excavation profanée" ,"Colline de Kesse, Point de passage de Sombreplaie",
		["http://image.noelshack.com/fichiers/2013/16/1366453991-defiled-delve-collines-de-kesse.jpg" ] ],
	["Faille de Pouacregriffe" ,"Marais de fer, Point de passage du lac Pourprenage",
		["http://image.noelshack.com/fichiers/2013/16/1366454154-dirtclaw-cleft-marais-de-fer-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366454164-dirtclaw-cleft-marais-de-fer-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366454177-dirtclaw-cleft-marais-de-fer-3.jpg" ] ],
	["Fière tanière du jaguar" ,"Province de Métrica, Point de passage d'Artegon",
		["http://image.noelshack.com/fichiers/2013/16/1366477957-jaguar-pride-den-metrica-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477964-jaguar-pride-den-metrica-2.jpg" ] ],
	["Folie de Widd" ,"Forêt de Calédon, Point de passage de Mabon",
		["http://image.noelshack.com/fichiers/2013/19/1368308040-widd-s-folly-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368308054-widd-s-folly-2.jpg" ] ],
	["Fontaine de Verdance" ,"Rivage maudit, Point de passage de Verdance",
		["http://image.noelshack.com/fichiers/2013/16/1366553572-verdance-front-rivage-maudit-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366553578-verdance-front-rivage-maudit-2.jpg" ] ],
	["Fontaine des racines cachées" ,"Le Bosquet, Point de passage du spéculateur",
		["http://image.noelshack.com/fichiers/2013/14/1365366867-backroot-fountain-le-bosquet.jpg" ] ],
	["Forage du nid de skelk" ,"Détroit des gorges glacées, Point de passage du bourbier de la mélancolie",
		["http://image.noelshack.com/fichiers/2013/16/1366545780-skelkness-borehole-gorges-glacees-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545793-skelknest-borehole-gorges-glacees-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545799-skelkness-borehole-gorges-glacees-3.jpg", "http://image.noelshack.com/fichiers/2013/16/1366546286-skelknest-borehole-gorges-glacees-4.jpg" ] ],
	["Fosse de la guivre des glaces" ,"Détroit des gorges glacées, Point de passage de Dimotiki", 
		["http://image.noelshack.com/fichiers/2013/16/1366477737-icewurm-trench-gorges-glacees-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477753-icewurm-trench-gorges-glacees-2.jpg" ] ],
	["Fosse de Piègetroll" ,"Passage de Lornar, Point de passage du Prieuré de Durmand",
		["http://image.noelshack.com/fichiers/2013/16/1366552628-trolltrap-pit-lornar-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366552638-trolltrap-pit-lornar-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366552646-trolltrap-pit-lornar-3.jpg" ] ],
	["Fouilles de Stigmafrappe" ,"Champs de ruines, Point de passage de Tenaebron",
		["http://image.noelshack.com/fichiers/2013/15/1365425010-brandstrike-dig-champs-de-ruines.jpg" ] ],
	["Fouilleur de fumier" ,"Falaises de Hantedraguerre, Point de passage Steelbrachen",
		["http://image.noelshack.com/fichiers/2013/16/1366476057-forager-s-midden-falaises-de-hantedraguerres-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476077-forager-s-midden-falaises-de-hantedraguerres-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476155-forager-s-midden-falaises-de-hanedraguerres-3.jpg" ] ],
	["Foyer de Kari" ,"Collines de Kesse, Point de passage Canyon de Cereboth",
		["http://image.noelshack.com/fichiers/2013/16/1366478050-kari-s-hot-spot-kessex-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366478062-kari-s-hot-spot-kessex-2.jpg" ] ],
	["Frayère des drakes des récifs" ,"Crique de Sud Soleil, Point de passage de l'Îlot de perle ou directement par le bateau", ["http://image.noelshack.com/fichiers/2013/21/1369222030-reef-drake-den-1.jpg", "http://image.noelshack.com/fichiers/2013/21/1369222037-reef-drake-den-2.jpg", "http://image.noelshack.com/fichiers/2013/21/1369222041-reef-drake-den-3.jpg" ] ],
	["Fuite de Toxal" ,"Terres sauvages de Brisban, Point de passage de Mirkrise",
		["http://image.noelshack.com/fichiers/2013/19/1368310554-toxal-spill-brisban-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368310563-toxal-spill-brisban-2.jpg" ] ],
	["Galerie du limon sanglant" ,"Côte de la marée sanglante, Point de passage lugubre",
		["http://image.noelshack.com/fichiers/2013/15/1365424972-blood-oooze-galery-maree-sanglante.jpg" ] ],
	["Geôle de Provatum" ,"Montée de Flambecoeur, Point de passage du gardien",
		["http://image.noelshack.com/fichiers/2013/16/1366538211-provatum-carcer-flambecoeur-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366538229-provatum-carcer-flambecoeur-2.jpg" ] ],
	["Gouffre de Whitland" ,"Mont Maelström, Point de passage du site du vieux traîneau",
		["http://image.noelshack.com/fichiers/2013/16/1366554016-whitland-sinkhole-maestrom-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366554026-whitland-sinkhole-maestrom-2.jpg" ] ],
	["Grenier effondré" ,"Marais de la Lumillule, Point de passage de la Maison de Frimo",
		["http://image.noelshack.com/fichiers/2013/16/1366545408-shattered-loft-lumillule-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545418-shattered-loft-lumillule-2.jpg" ] ],
	["Griffure de l’éclat céleste" ,"Hinterlands Arathis, Point de passage de Grey Gritta",
		["http://image.noelshack.com/fichiers/2013/16/1366545915-skyshrine-scratch-hinterlands-arathis-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545929-skyshrine-scratch-hinterlands-arathis-2.jpg" ] ],
	["Griffure invisible" ,"Forêt de Caledon, Point de passage de Mabon",
		["http://image.noelshack.com/fichiers/2013/16/1366553011-unseen-scratch-caledon-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366553017-unseen-scratch-caledon-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366553026-unseen-scratch-caledon-3.jpg" ] ],
	["Grotte d’Eaudefonte" ,"Chutes de la Canopée, Point de passage de banc d'écaille.",
		["http://image.noelshack.com/fichiers/2013/16/1366478575-meltwater-cave-canopee-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366536136-meltwater-cave-canopee-2.jpg" ] ],
	["Grotte de Gorgetoile" ,"Steppes de la Strie flamboyante, Point de passage du Glaive",
		["http://image.noelshack.com/fichiers/2013/16/1366377215-canyonweb-cave-strie-flamboyante-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366377245-canyonweb-cave-strie-flamboyante-2.jpg" ] ],
	["Grotte de Lawen" ,"Champs de Gendarran, Point de passage du premier refuge",
		["http://image.noelshack.com/fichiers/2013/16/1366478261-lawen-grotto-gendarran-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366478269-lawen-grotto-gendarran-2.jpg" ] ],
	["Grotte Oubliée" ,"Steppes de la Strie flamboyante, Point de passage Terra Carorunda",
		["http://image.noelshack.com/fichiers/2013/16/1366476350-forgotten-grotto-strie-flamboyante-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476372-forgotten-grotto-strie-flamboyante-2.jpg" ] ],
	["Gué kraalétroi" ,"Champs de ruines, Point de passage de la route de l'ogre",
		["http://image.noelshack.com/fichiers/2013/19/1368359063-narrowkraal-crossing-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368359068-narrowkraal-crossing-2.jpg" ] ],
	["Guet de la bagarre de barils" ,"Hoelbrak, Point de passage la boussole du Héro",
		["http://image.noelshack.com/fichiers/2013/16/1366478108-kegbrawl-watch-hoelbrak.jpg" ] ],
	["Guet réverbérant" ,"Contreforts du voyageur, Point de passage d'Ecorchenuit",
		["http://image.noelshack.com/fichiers/2013/16/1366539259-reverberant-s-watch-contreforts-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366539273-reverberant-s-watch-contreforts-2.jpg" ] ],
	["Guivre des sables maraudeuse" ,"Crique de Sud Soleil, Point de passage de l'Avant poste de Kiel", ["http://image.noelshack.com/minis/2013/21/1369222707-gw2-sandwurm-prowl-guild-trek.png", "http://image.noelshack.com/fichiers/2013/21/1369222629-sandwurm-prowl-1.jpg", "http://image.noelshack.com/fichiers/2013/21/1369222635-sandwurm-prowl-2.jpg" ] ],
	["Hall de Guilde du Destin" ,"Vallée de la Reine, Point de passage de Shaemoor",
		["http://image.noelshack.com/fichiers/2013/16/1366454107-destiny-s-guildhall-vallee-de-la-reine-village-de-shaemoor.jpg" ] ],
	["Halte de Coupegorge" ,"Champs de Gendarran, Point de passage de Brigantine",
		["http://image.noelshack.com/fichiers/2013/16/1366453884-cutthroat-s-rest-champs-de-gendarran.jpg" ] ],
	["Halte de Soren Draa" ,"Province de Métrica, Point de passage de Soren Draa",
		["http://image.noelshack.com/fichiers/2013/16/1366547573-soren-draa-rest-shop-metrica-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366547580-soren-draa-rest-shop-metrica-2.jpg" ] ],
	["Impasse du Gladiver" ,"Rivage maudit, Point de passage R & D",
		["http://image.noelshack.com/fichiers/2013/16/1366554377-winterknell-impasse-rivage-maudit-2.jpg" ] ],
	["Jardin de Fortepatte" ,"Plateau de Diessa, Point de passage de Nageling",
		["http://image.noelshack.com/fichiers/2013/16/1366550077-strongpaw-s-garden-plateau-de-diessa.jpg" ] ],
	["Klub des Karkas" ,"Crique de Sud Soleil, Point de passage de l'Îlot de perle", ["http://image.noelshack.com/minis/2013/21/1369221297-gw2-the-karka-club-guild-trek.png", "http://image.noelshack.com/fichiers/2013/21/1369221408-the-karka-club-1.jpg", "http://image.noelshack.com/fichiers/2013/21/1369221423-the-karka-club-2.jpg" ] ],
	["L’impasse du peuple" ,"Détroit des gorges glacées, Point de passage de Grosnev",
		["http://image.noelshack.com/fichiers/2013/24/1370856564-impasse-du-peuple-5.jpg", "http://image.noelshack.com/fichiers/2013/24/1370856668-impasse-du-peuple-4.jpg", "http://image.noelshack.com/fichiers/2013/24/1370856851-impasse-du-peuple-3.jpg", "http://image.noelshack.com/fichiers/2013/24/1370857071-impasse-du-peuple-2.jpg" ] ],
	["Laboratoire de la taverne de Turai" ,"Promontoire divin, Point de passage Place de Balthazar",
		["http://image.noelshack.com/fichiers/2013/16/1366552769-turai-tavern-promontoire-divin-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366552776-turai-tavern-promontoire-divin-2.jpg" ] ],
	["La sellette de Kaldar" ,"Hoelbrak, Point de passage du Poste de garde de l'est",
		["http://image.noelshack.com/fichiers/2013/19/1368290182-kaldar-s-hot-seat-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368290187-kaldar-s-hot-seat-2.jpg" ] ],
	["Le devoir de Morndottir" ,"Hoelbrack, Point de passage du rocher de l'abri",
		["http://image.noelshack.com/fichiers/2013/16/1366477391-grimdottir-s-duty-hoelbrak.jpg" ] ],
	["Le magasin des ouvriers" ,"Falaises de Hantedraguerre, Point de passage de la route grise",
		["http://image.noelshack.com/fichiers/2013/16/1366552274-the-worker-s-stores-hantedraguerre-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366552284-the-worker-s-stores-hantedraguerre-2.jpg" ] ],
	["Les Marches du Talus" ,"Chutes de la Canopée, Point de passage de Talus",
		["http://image.noelshack.com/fichiers/2013/16/1366551693-talus-steps-canopee-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366551703-talus-steps-canopee-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366551712-talus-steps-canopee-3.jpg" ] ],
	["Marches vaporeuses" ,"Crique de Sud Soleil, Point de passage du Point du Lion", ["http://image.noelshack.com/fichiers/2013/21/1369224336-steamy-steps-1.jpg", "http://image.noelshack.com/fichiers/2013/21/1369224339-steamy-steps-2.jpg", "http://image.noelshack.com/fichiers/2013/21/1369224343-steamy-steps-3.jpg" ] ],
	["Mirador Beetlestone" ,"Vallée de la Reine, Point de passage de Beetletun",
		["http://image.noelshack.com/fichiers/2013/19/1368304250-beetlestone-mirador-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368304256-beetlestone-mirador-2.jpg" ] ],
	["Monument à l’Ancien" ,"Crique de Sud soleil, Point de passage du Refuge d'Owain", ["http://image.noelshack.com/minis/2013/21/1369225830-gw2-monument-to-the-ancient-one-guild-trek.png", "http://image.noelshack.com/fichiers/2013/21/1369225756-monument-to-the-ancient-one-1.jpg", "http://image.noelshack.com/fichiers/2013/21/1369225759-monument-to-the-ancient-one-2.jpg" ] ],
	["Motte de Lamenoire" ,"Plateau de Diessa, Point de passage Temple de la fontaine de Rhand",
		["http://image.noelshack.com/fichiers/2013/14/1365370434-blackblade-butte-fontaine-de-rand-plateau-de-diessa.jpg" ] ],
	["Mouillage de Covington" ,"Côte de la marée sanglante, Point de passage de la mouette rieuse",
		["http://image.noelshack.com/fichiers/2013/16/1366453785-covington-s-stowage-maree-sanglante-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366381922-covington-s-stawage-maree-sanglante-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366453819-covington-s-stowage-maree-sanglante-3.jpg" ] ],
	["Mouillage du Capitaine" ,"Saut de Malchor, Point de passage des lumières",
		["http://image.noelshack.com/fichiers/2013/16/1366377636-captain-s-berth-malchor-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366377661-captain-s-berth-malchor-2.jpg" ] ],
	["Mur d’enceinte de Claypool" ,"Vallée de la Reine, Village de Claypool",
		["http://image.noelshack.com/fichiers/2013/16/1366381520-claypool-bailey-village-de-claypool.jpg" ] ],
	["Nid d’araignée cavernicole" ,"Passage de Lornar, Point de passage de l'enclave du Pinacle",
		["http://image.noelshack.com/fichiers/2013/16/1366381474-cave-spider-nidus-lornar-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366381489-cave-spider-nidus-lornar-2.jpg" ] ],
	["Nid de raptor" ,"Marais de fer, Point de passage de la Ville de l'étoile de Caninecol",
		["http://image.noelshack.com/fichiers/2013/19/1368365759-raptor-s-aerie-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368365765-raptor-s-aerie-2.jpg" ] ],
	["Objets trouvés de l’Autorité du Port" ,"Rata Sum, Point de passage du port",
		["http://image.noelshack.com/fichiers/2013/16/1366537832-port-authority-lost-and-found-rata-sum-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366537852-port-authority-lost-and-found-rata-sum-2.jpg" ] ],
	["Œil du Scorpion des mers" ,"Rivage maudit, Point de passage de la Crête indiscrète",
		["http://image.noelshack.com/fichiers/2013/16/1366545226-sea-scorpion-s-eye-rivage-maudit-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545239-sea-scorpion-s-eye-rivage-maudit-2.jpg" ] ],
	["Œuvre d’Heidi" ,"Hinterland Arathis, Point de passage du Plateau du Séraphin",
		["http://image.noelshack.com/fichiers/2013/19/1368285358-heidi-s-showpiece-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368285381-heidi-s-showpiece-2.jpg", "http://image.noelshack.com/fichiers/2013/19/1368285402-heidi-s-showpiece-3.jpg" ] ],
	["Paddock du moa vert" ,"Forêt de Caledon, Point de passage du Refuge de Caledon",
		["http://image.noelshack.com/fichiers/2013/16/1366477309-green-moa-paddock-caledon-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477320-green-moa-paddock-caledon-2.jpg" ] ],
	["Palan charmine" ,"Montée de Flambecoeur, Point de passage du cochon de fer",
		["http://image.noelshack.com/fichiers/2013/19/1368363526-orecart-hoist-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368363532-orecart-hoist-2.jpg" ] ],
	["Panorama de Phasmatis" ,"Plaines d'Ashford, Point de passage du chantier naval de Dockfer",
		["http://image.noelshack.com/fichiers/2013/16/1366537674-phasmatis-prospect-ashford-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366537687-phasmatis-prspect-ashford-2.jpg" ] ],
	["Parapet des constellations" ,"Le Bosquet, Point de passage du quartier populaire supérieur",
		["http://image.noelshack.com/fichiers/2013/16/1366381529-constellation-parpet-refuge-des-constellations-le-bosquet.jpg", "http://image.noelshack.com/fichiers/2013/20/1368983471-constellation-parapet-1.jpg", "http://image.noelshack.com/fichiers/2013/20/1368983479-constellation-parapet-2.jpg" ] ],
	["Pas de Tir de Mina" ,"Promontoire divin, Point de passage des communes",
		["http://image.noelshack.com/fichiers/2013/16/1366535010-mina-s-target-shoot-promontoire-divin-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366535054-mina-s-target-shoot-promontoire-divin-2.jpg" ] ],
	["Pavillon de Grenth" ,"Promontoire divin, Point de passage Place de Grenth",
		["http://image.noelshack.com/fichiers/2013/16/1366477356-grenth-s-pavillion-promontoire-divin.jpg" ] ],
	["Pavillon du seigneur" ,"Collines de Kesse, Point de passage du Seigneur",
		["http://image.noelshack.com/fichiers/2013/16/1366537510-overlord-lodge-kesse-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366537523-overlord-lodge-kesse-2.jpg" ] ],
	["Perchoir d’œil-de-faucon" ,"Chutes de la Canopée, Point de passage du serpent",
		["http://image.noelshack.com/fichiers/2013/20/1368983026-hawkeye-perch-1.jpg", "http://image.noelshack.com/fichiers/2013/20/1368983034-hawkeye-perch-2.jpg" ] ],
	["Perchoir de l’Ermite" ,"Champs de ruine, Point de passage du campement de Rosco",
		["http://image.noelshack.com/fichiers/2013/16/1366477604-hermit-s-roost-champs-de-ruine-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477620-hermit-s-roost-champs-de-ruine-2.jpg" ] ],
	["Perchoir de Raptor" ,"Champs de Gendarran, Point de passage d'Aveugleneige",
		["http://image.noelshack.com/fichiers/2013/16/1366538714-raptor-s-perch-gendarran-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366538723-raptor-s-perch-gendarran-2.jpg" ] ],
	["Perchoir Tubavapeur" ,"Crique de Sud Soleil, Point de passage de l'Îlot de perle", ["http://image.noelshack.com/minis/2013/21/1369223784-gw2-steampipe-perch-guild-trek-3.png", "http://image.noelshack.com/fichiers/2013/21/1369223805-steampipe-perch-1.jpg", "http://image.noelshack.com/fichiers/2013/21/1369223815-steampipe-perch-2.jpg", "http://image.noelshack.com/fichiers/2013/21/1369223816-steampipe-perch-3.jpg" ] ],
	["Pergola d’Aubeluit" ,"Le Bosquet, Point de passage de Ronan, niveau inférieur",
		["http://image.noelshack.com/fichiers/2013/16/1366453953-dawngleam-pergola-le-bosquet-passage-de-ronan.jpg" ] ],
	["Pic du Béliervédère" ,"Falaises Hantedraguerre, Point de passage de l'avalanche",
		["http://image.noelshack.com/fichiers/2013/16/1366538406-ramview-peak-hantedraguerre-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366538421-ramview-peak-hantedraguerre-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366538429-ramview-peak-hantedraguerre-3.jpg" ] ],
	["Place engloutie" ,"Détroit de la dévastation, Point de passage de Pic du signal",
		["http://image.noelshack.com/fichiers/2013/20/1368982467-drowned-plaza-1.jpg" ] ],
	["Plage nécrolithe" ,"Forêt de Calédon, Point de passage de Calédon",
		["http://image.noelshack.com/fichiers/2013/19/1368288536-necrolith-landing-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368288541-necrolith-landing-2.jpg" ] ],
	["Planche à dessin de Tekki" ,"Terres sauvages de Brisban, Point de passage de la métamagique d'Ulta",
		["http://image.noelshack.com/fichiers/2013/19/1368295404-tekki-s-drawing-board-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368295409-tekki-s-drawing-board-2.jpg" ] ],
	["Plateau de Krallcamden" ,"Plaines d'Ashford, Point de passage Forêt de Cadem",
		["http://image.noelshack.com/fichiers/2013/16/1366376879-cademkral-plaines-d-ashford.jpg" ] ],
	["Plongeur focebourbié" ,"   ",
		["http://image.noelshack.com/fichiers/2014/23/1402242568-plongeur-facebourbie03.jpg", "http://image.noelshack.com/fichiers/2014/23/1402242571-plongeur-focebourbie04.jpg" ] ],
	["Poche de diablotin de feu" ,"Mont Maelström, Point de passage de Maelström",
		["http://image.noelshack.com/fichiers/2013/16/1366455814-fire-imp-pocket-maelstrom-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366455826-fire-imp-pocket-maelstr-m-2.jpg" ] ],
	["Point de vue d’Isgarren" ,"Collines de Kessex, Point de passage de Sombreplaie",
		["http://image.noelshack.com/fichiers/2013/19/1368305146-isgarren-viewpoint-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368305152-isgarren-viewpoint-2.jpg" ] ],
	["Point de vue de Dockfer" ,"Plaines d'Ashford, Point de passage du chantier naval de Dockfer",
		["http://image.noelshack.com/fichiers/2013/16/1366477902-irondock-viewpoint-ashford-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477914-irondock-viewpoint-ashford-2.jpg" ] ],
	["Point de vue de Gnashar" ,"Terres sauvages de Brisban, Point de passage de Wendom",
		["http://image.noelshack.com/fichiers/2013/16/1366476883-gnashar-s-viewpoint-brisban-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477147-gnashar-s-viewpoint-brisban-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477237-gnashar-s-viewpoint-brisban-3.jpg" ] ],
	["Point de vue de Rurik" ,"Promontoire divin, Point de passage de Rurikton",
		["http://image.noelshack.com/fichiers/2013/16/1366539528-rurik-view-promontoire-divin-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366539537-rurik-view-promontoire-divin-2.jpg" ] ],
	["Pont du Guet-du-feu" ,"Marais de fer, Point de passage du campement du guet-du-feu",
		["http://image.noelshack.com/fichiers/2013/16/1366459483-firewatch-flybridge-marais-de-fer-1.jpg", "http://image.noelshack.com/fichiers/2013/22/1370192244-firewatch-flybridge-marais-de-fer-2.jpg" ] ],
	["Porche de Fawcett" ,"Hinterlands Arathis, Point de passage du plateau du Séraphin ou d'Arca",
		["http://image.noelshack.com/fichiers/2013/16/1366455774-fawcett-s-porch-hinterlands-arathis.jpg", "http://image.noelshack.com/fichiers/2013/21/1369252146-porche-de-fawcett-4.jpg", "http://image.noelshack.com/fichiers/2013/21/1369252143-porche-de-fawcet-3.jpg" ] ],
	["Port extérieur du Vizir" ,"Détroit de la dévastation, Point de passage du poste isolé",
		["http://image.noelshack.com/fichiers/2013/16/1366553668-vizier-s-anteport-devastation-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366553676-vizier-s-anteport-devastation-2.jpg" ] ],
	["Porte de Droknah" ,"Monts Maelström, Point de passage du site du vieux traîneau",
		["http://image.noelshack.com/fichiers/2013/16/1366454410-droknah-s-gate-maestrom-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366454428-droknah-s-gate-maestrom-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366454446-droknah-s-gate-maestrom-3.jpg" ] ],
	["Porte de Wikk" ,"Chutes de la Canopée, Point de passage du Tutorat de Valance",
		["http://image.noelshack.com/fichiers/2013/16/1366554109-wikk-s-gate-canopee-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366554118-wikk-s-gate-canopee-2.jpg" ] ],
	["Portique de Rata Pten" ,"Mont Maelström, Point de passage de Criterion",
		["http://image.noelshack.com/fichiers/2013/16/1366538826-rata-pten-mortico-maelstrom-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366538835-rata-pten-mortico-maelstrom-2.jpg" ] ],
	["Poste de vigie de Décimus" ,"Plaines d'Ashford, Point de passage du portail de Vir",
		["http://image.noelshack.com/fichiers/2013/16/1366553901-watchpoint-decimus-ashford-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366553908-watchpoint-decimus-ashford-2.jpg" ] ],
	["Préfecture de Lychcroft" ,"Collines de Kesse, Point de passage du site d'Ombrecoeur",
		["http://image.noelshack.com/fichiers/2013/16/1366478476-lychcroft-wardenship-kesse-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366478485-lychcroft-wardenship-kesse-2.jpg" ] ],
	["Prison de Taupvlaquie" ,"Contreforts du voyageur, Point de passage d'Halvaunt",
		["http://image.noelshack.com/fichiers/2013/16/1366536951-moleberia-prison-contreforts-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366536964-moleberia-prison-contreforts-2.jpg" ] ],
	["Promontoire de Portmatt" ,"Côte de la marée sanglante, Point de passage des lamentations",
		["http://image.noelshack.com/fichiers/2013/16/1366538033-portmatt-s-promontory-maree-sanglante-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366538062-portmat-s-promontory-maree-sanglante-2.jpg" ] ],
	["Quai de Lestepied" ,"Détroit de la dévastation, Point de passage de Tonnecaboche",
		["http://image.noelshack.com/fichiers/2013/16/1366478325-lightfoot-dock-devastation-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366478332-lightfoot-dock-devastation-2.jpg" ] ],
	["Recoin du Corbeau" ,"Hoelbrak, Point de passage du corbeau",
		["http://image.noelshack.com/fichiers/2013/16/1366538949-raven-nook-hoelbrak.jpg" ] ],
	["Recoin du Scriptorium" ,"Citadelle noire, Point de passage du factorium",
		["http://image.noelshack.com/fichiers/2013/16/1366545168-scriptorium-nook-citadelle-noire.jpg" ] ],
	["Recoin lapidaire de Flakk" ,"Rata Sum, Syndicat de la dynamique, Point de passage de la comptabilité",
		["http://image.noelshack.com/fichiers/2013/16/1366475985-flakk-s-lapidary-nook-rata-sum.jpg" ] ],
	["Refuge d’Antreneige" ,"Congères d'Antreneige, Point de passage de la congère",
		["http://image.noelshack.com/fichiers/2013/16/1366547164-snowden-safehouse-congeres-1.jpg", "http://image.noelshack.com/fichiers/2013/22/1370193293-snowden-safehouse-congeres-2.jpg" ] ],
	["Refuge de siamouth" ,"Marais de la Lumillule, Point de passage du ciel lugubre",
		["http://image.noelshack.com/fichiers/2013/16/1366545460-siamoth-refuge-lumillule-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545472-siamoth-refuge-lumillule-2.jpg" ] ],
	["Refuge du Stentor" ,"Détroit de la dévastation, Point de passage du Pic de signal",
		["http://image.noelshack.com/fichiers/2013/16/1366548087-stentor-shelter-devastation-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366548101-stentor-shelter-devastation-2.jpg" ] ],
	["Refuge percebul" ,"Steppes de la Strie flamboyante, Point de passage de l'Oeil d'acier",
		["http://image.noelshack.com/fichiers/2013/19/1368360377-burstbubble-blind-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368360383-burstbubble-blind-2.jpg" ] ],
	["Repaire de l’Arctodus" ,"Contrefort du Voyageur, Point de passage de la Colonie de Vendrake",
		["http://image.noelshack.com/fichiers/2013/14/1365366301-arctodus-haunt-riviere-froidfrill-contrefort-du-voyageur.jpg" ] ],
	["Repaire de l’Autel du Ruisseau" ,"Vallée de la Reine, Point de passage de l'autel du ruisseau",
		["http://image.noelshack.com/fichiers/2013/14/1365365927-altar-brook-vallee-de-l-autel-du-ruisseau-vallee-de-la-reine.jpg" ] ],
	["Repaire de Soufflettin" ,"Passage de Lornar, Point de passage du gouffre du démon",
		["http://image.noelshack.com/fichiers/2013/16/1366455618-ettinbreath-lair-lornar-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366455644-ettinbreath-lair-lornar-2.jpg" ] ],
	["Repli stratégique" ,"Rivage maudit, Point de passage du rocher de l'épave",
		["http://image.noelshack.com/fichiers/2013/16/1366551471-tactical-retreat-rivage-maudit-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366551479-tactical-retreat-rivage-maudit-2.jpg" ] ],
	["Retraite Gelée" ,"Chutes de la Canopée, Point de passage de Feuilleblanche",
		["http://image.noelshack.com/fichiers/2013/16/1366476625-frozen-antrum-canopee-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476645-frozen-antrum-canopee-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366476679-frozen-antrum-canopee-3.jpg" ] ],
	["Rotonde de Soggorsort" ,"Forêt de Caledon, Point de passage du Hameau d'Annwen",
		["http://image.noelshack.com/fichiers/2013/16/1366547429-soggorsort-rotunda-caledon-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366547439-soggorsort-rotunda-caledon-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366547447-soggorsort-rotunda-caledon-3.jpg" ] ],
	["Ruelle du vadrouilleur de l’est" ,"Promontoire divin, Place de Dwayna, quartier populaire Est",
		["http://image.noelshack.com/fichiers/2013/16/1366455493-eastlurk-alley-quartier-populaire-est-le-promontoire-divin.jpg" ] ],
	["Salon d’Esparvent" ,"Citadelle noire, Point de passage de l'Imperator",
		["http://image.noelshack.com/fichiers/2013/16/1366547698-sparwind-s-lounge-citadelle-noire.jpg" ] ],
	["Salon de Wrelk" ,"Champs de Gendarran, Point de passage d'Almuten",
	["http://image.noelshack.com/fichiers/2013/19/1368283728-wrelk-s-salon-1.jpg", "http://image.noelshack.com/minis/2013/19/1368283752-wrelk-s-salon-2.png", ] ],
	["Sanctuaire hanté par un diablotin" ,"Forêt de Caledon, Point de passage du marais de Wychmire",
		["http://image.noelshack.com/fichiers/2013/16/1366477850-imphant-hallow-caledon-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477863-imphant-hallow-caledon-2.jpg" ] ],
	["Sanctuaire piersacrée" ,"Plateau de Diessa, Point de passage du Sanctuaire",
		["http://image.noelshack.com/fichiers/2013/19/1368292027-holystone-sanctum-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368292035-holystaone-sanctum-2.jpg" ] ],
	["Saut de Drakefaille" ,"Champs de ruine, Point de passage du Guet de Mordrage",
		["http://image.noelshack.com/fichiers/2013/16/1366454282-drakecleft-sheff-champs-de-ruines.jpg" ] ],
	["Saut de la conceptualisation" ,"Rata Sum, Point de passage de l'Incubateur",
		["http://image.noelshack.com/fichiers/2013/16/1366477795-ideation-leap-rata-sum-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366477808-ideation-leap-rata-sum-2.jpg" ] ],
	["Saut de Mistriven" ,"Passage de Lornar, Point de passage de Mistriven",
		["http://image.noelshack.com/fichiers/2013/16/1366535100-mistriven-shelf-lornar-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366535113-mistriven-shelf-lornar-2.jpg" ] ],
	["Sépulcre azumière" ,"Détroit de la dévastation, Point de passage de Xenarius",
		["http://image.noelshack.com/fichiers/2013/19/1368377319-sepulchre-skylight-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368377324-sepuchre-skylight-2.jpg" ] ],
	["Sépulcre ravagé" ,"Plateau de Diessa, Point de passage Landes ravagées",
		["http://image.noelshack.com/fichiers/2013/14/1365371410-blasted-sepulchtre-landes-ravagees-plateau-de-diessa.jpg" ] ],
	["Seuil d’Usharr" ,"Marais de la Lumillule, Point de passage de la tête du crapaud",
		["http://image.noelshack.com/fichiers/2013/19/1368307713-usharr-s-threshold-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368307718-usharr-s-threshold-2.jpg" ] ],
	["Sommet de l’Epave" ," ",
		["http://image.noelshack.com/fichiers/2013/16/1366478014-junker-s-apex-citadelle-noire.jpg" ] ],
	["Source de Brûlereinette" ,"Marais de la Lumillule, Point de passage Flamefrog",
		["http://image.noelshack.com/fichiers/2013/16/1366459341-firefrog-springs-limillule.jpg" ] ],
	["Source de Dwayna" ,"Promontoire divin, Point de passage des Communes",
		["http://image.noelshack.com/fichiers/2013/19/1368286111-dwayna-s-fount-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368286257-dwayna-s-fount-2.jpg" ] ],
	["Source des lamentations" ,"Détroit des gorges glacées, Point de passage de la Maison de Hautecieux",
		["http://image.noelshack.com/fichiers/2013/19/1368369582-source-of-lament-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368369586-source-of-lament-2.jpg" ] ],
	["Surprise d’Elise" ,"Hinterlands Arathis, Point de passage Ruines de Demetra la Sacrée",
		["http://image.noelshack.com/fichiers/2013/16/1366455532-elise-s-surprise-hinterlands-arathis.jpg" ] ],
	["Surveillant de Folleflamme" ,"Province de Métrica, Point de passage Soren Draa",
		["http://image.noelshack.com/fichiers/2013/16/1366554250-wildflame-monitor-province-metrica.jpg" ] ],
	["Terrasse de Wassa" ,"Champs de Gendarran, Point de passage du premier refuge",
		["http://image.noelshack.com/fichiers/2013/16/1366553780-wassa-s-terrace-gendarran-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366553791-wassa-s-terrace-gendarran-2.jpg" ] ],
	["Tour de guet de Mâchefléau" ,"Marais de Fer, Point de passage du Campement de Belpelisse",
		["http://image.noelshack.com/fichiers/2013/16/1366545096-scourgejaw-watchtower-marais-de-fer-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545106-scourgejaw-watchtower-marais-de-fer-2.jpg", "http://image.noelshack.com/fichiers/2013/16/1366545117-scourgejaw-watchtower-marais-de-fer-3.jpg" ] ],
	["Tour de la tribulation" ,"Falaises de Hantedraguerre, Point de passage de la tribulation",
		["http://image.noelshack.com/fichiers/2013/19/1368371671-tower-of-tribulation-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368371796-tower-of-tribulation-2.jpg" ] ],
	["Trou de tirailleur de Creusepierre" ,"Champs de Gendarran, Point de passage de Talajian",
		["http://image.noelshack.com/fichiers/2013/16/1366548216-stonebore-spiderhole-gendarran-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366548229-stonebore-spiderhole-gendarran-2.jpg" ] ],
	["Tunnel de Bandacier" ,"Steppes de la Strie flamboyante, Point de passage de Tumok",
		["http://image.noelshack.com/fichiers/2013/16/1366547970-steelband-s-tunnel-strie-flamboyante-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366547981-steelband-s-tunnel-strie-flamboyante-2.jpg" ] ],
	["Tunnel sous le lac" ,"Vallée de la Reine, Point de passage de la scierie d'Ojon",
		["http://image.noelshack.com/fichiers/2013/16/1366478193-lakebottom-underpass-vallee-de-la-reine-1.jpg", "http://image.noelshack.com/fichiers/2013/16/1366478202-lakebottom-underpass-valee-de-la-reine-2.jpg" ] ],
	["Upsilon hyperboloïde" ,"Saut de Malchor, Point de passage des crevasses oubliées",
		["http://image.noelshack.com/fichiers/2013/19/1368372980-upsilon-hyperboloid-1.jpg", "http://image.noelshack.com/fichiers/2013/19/1368372989-upsilon-hyperboloid-2.jpg" ] ],
	["Vallon de Cymbel" ,"Champs de ruine, Point de passage La route de l'ogre",
		["http://image.noelshack.com/fichiers/2013/16/1366453918-cymbel-s-glen-champs-de-ruines.jpg" ] ],
]
tp_rando = [
	"", #Alc&ocirc;ve de Courtilleracine
	"", #Alimentation en eau d&#39;Orvanic
	"[&BJcDAAA=]", #Antre cach&eacute;cailleux 
	"", #Antre de Hurleneige
	"[&BMcBAAA=]", #Autel d&#39;Inondesel
	"", #Aveuglement de l&#39;Erudit
	"", #Balcon des d&eacute;lices
	"", #Banc de Varech de Malm&eacute;duse
	"", #Barri&egrave;re de Bercebruy&egrave;re
	"", #Bassin de la sentinelle
	"[&BOoAAAA=]", #Belv&eacute;d&egrave;re goutedo 
	"[&BKUDAAA=]", #Bistrot rouport 
	"", #Bivouac du Lys
	"", #Bord de Valaigu
	"", #Bosquet de Tarstar
	"[&BOcBAAA=]", #Boucherie pi&egrave;gecayeux 
	"", #Cache &agrave; miel de Boisecoeur
	"", #Cache de l&#39;Ours des cavernes
	"", #Cache du fugitif
	"", #Réserve du marchand
	"", #Camp principal du gardien
	"", #Canyons de Gallow
	"", #Carr&eacute; de chou du bandit
	"", #Cavit&eacute; de la cath&eacute;drale
	"", #Cavit&eacute; du Contrema&icirc;tre
	"", #Cellier de la Garde du Lion
	"", #Cellier du Lion Noir
	"", #Champ de force de la cinqui&egrave;me brasse
	"", #Champ de Montesauvage
	"[&BLgEAAA=]", #Ch&acirc;timent de Bluup 
	"", #Chute d&#39;East End
	"", #Chutes de Gerb&eacute;caille
	"", #Chutes de la G&eacute;nitrice
	"", #Cisaillement interdit
	"", #Coeur du flacon du fondateur
	"[&BMEDAAA=]", #Coffre-fort de Kevach 
	"", #Coin d&#39;Anya
	"", #Coin de Castavall
	"", #Coin de Magi&egrave;dre
	"", #Col des fr&egrave;res
	"", #Col du Coeur criant
	"[&BEcAAAA=]", #Console de commande principale LIN39 
	"", #Contrepoids d&#39;Osenfold
	"", #C&ocirc;te de Couvedrake
	"", #C&ocirc;te de Togatl
	"", #Cour de Chutes bris&eacute;es
	"", #Cour des Chutes de la Biche
	"", #Crevasse du Gibier
	"[&BLgAAAA=]", #Crique d&#39;Isenfell 
	"", #Crique de Trouv&eacute;caille
	"", #D&eacute;barras d&#39;Ulta
	"", #Dents de la corruption
	"[&BK8BAAA=]", #D&eacute;sir de Pochtecatl 
	"", #D&eacute;versoir de Thaumanova
	"", #Distillerie de la Chouette cach&eacute;e
	"", #Dortoir du Hall de Skibo
	"", #&Eacute;chafaudage autoporteur
	"", #Emplacement hant&eacute;
	"", #Emprise agit&eacute;e
	"", #Ermitage abandonn&eacute;
	"", #Escarpement du p&ecirc;cheur
	"[&BOQGAAA=]", #Etreinte de l&#39;hymne 
	"", #Excavation profan&eacute;e
	"", #Faille de Pouacregriffe
	"", #Fi&egrave;re tani&egrave;re du jaguar
	"[&BDoBAAA=]", #Folie de Widd 
	"", #Fontaine de Verdance
	"", #Fontaine des racines cach&eacute;es
	"", #Forage du nid de skelk
	"", #Fosse de Pi&egrave;getroll
	"", #Fosse de la guivre des glace
	"", #Fouilles de Stigmafrappe 
	"", #Fouilleur de fumier
	"", #Foyer de Kari
	"[&BNUGAAA=]", #Fray&egrave;re des drakes des r&eacute;cifs 
	"", #Fuite de Toxal
	"", #Galerie du limon de sanglant
	"", #G&eacute;&ocirc;le de Provatum
	"", #Gouffre de Whitland
	"", #Grenier effondr&eacute;
	"", #Griffure de l&#39;&eacute;clat c&eacute;leste
	"", #Griffure invisible
	"", #Grotte d&#39;Eaudefonte
	"", #Grotte de Gorgetoile
	"", #Grotte de Lawen
	"", #Grotte Oubli&eacute;e
	"[&BE8BAAA=]", #Gu&eacute; kraal&eacute;troi 
	"", #Guet de la bagarre de barils
	"", #Guet r&eacute;verb&eacute;rant
	"[&BNUGAAA=]", #Guivre des sables maraudeuse 
	"", #Hall de Guilde du Destin
	"", #Halte de Coupegorge
	"", #Halte de Soren Draa
	"", #Impasse du Gladiver
	"", #Jardin de Fortepatte
	"", #L&#39;impasse du peuple
	"", #Laboratoire de la taverne de Turai
	"[&BI0DAAA=]", #La sellette de Kaldar 
	"", #Le devoir de Morndottir
	"", #Le magasin des ouvriers
	"", #Les Marches du Talus
	"[&BNUGAAA=]", #Les karkas associ&eacute;s 
	"[&BNIGAAA=]", #Marche vaporeuses 
	"[&BPoAAAA=]", #Mirador de Beetletun 
	"[&BNgGAAA=]", #Monument &agrave; l&#39;ancien 
	"", #Motte de Lamenoire
	"", #Mouillage de Covington
	"", #Mouillage du Capitaine
	"", #Mur d&#39;enceinte de Claypool
	"", #Nid d&#39;Araign&eacute;e cavernicole
	"", #Nid du raptor
	"", #Objets trouv&eacute;s de l&#39;Autorit&eacute; du Port
	"", #Oeil du Scorpion des mers
	"[&BKcAAAA=]", #&OElig;uvre d&#39;Heidi 
	"", #Paddock du moa vert
	"[&BBcCAAA=]", #Palan charmine 
	"", #Panorama de Phasmatis
	"", #Parapet des constellations
	"", #Pas de Tir de Mina
	"", #Pavillon de Grenth
	"", #Pavillon du Seigneur
	"[&BNUGAAA=]", #Perchoir Tubavapeur 
	"", #Perchoir de Raptor
	"", #Perchoir de l&#39;Ermite</strong>
	"[&BEUCAAA=]", #Perchoir d&#39;&oelig;il-de-faucon 
	"", #Pergola d&#39;Aubeluit
	"", #Pic du B&eacute;lierv&eacute;d&egrave;re
	"", #Place engloutie
	"[&BBIEAAA=]", #Plage n&eacute;crolithe 
	"[&BGUAAAA=]", #Planche &agrave; dessin de Tekki 
	"", #Plateau de Krallcamden
	"[&BNECAAA=]", #Plongeur facebourbi&eacute; 
	"", #Poche de diablotin de feu
	"", #Point de vue de Dockfer
	"", #Point de vue de Gnashar
	"", #Point de vue de Rurik
	"[&BBEAAAA=]", #Point de vue d&#39;isgarren 
	"", #Pont de Guet-du-feu
	"", #Porche de Fawcett
	"", #Porte de Droknah
	"", #Porte de Wikk
	"", #Port ext&eacute;rieur du Vizir
	"", #Portique de Rata Pten
	"", #Poste de vigie de D&eacute;cimus
	"", #Pr&eacute;fecture de Lychcroft
	"", #Prison de Taupvaquie
	"", #Promontoire de Portmatt
	"", #Quai de Lestepied</strong>
	"", #Recoin du Scriptorium</strong>
	"", #Recoin lapidaire de Flakk
	"", #Refuge d&#39;Antreneige
	"", #Refuge de siamouth
	"", #Refuge du Stentor
	"[&BFIDAAA=]", #Refuge percebul 
	"", #Repaire de Soufflettin
	"", #Repaire de l&#39;Arctodus
	"", #Rep&egrave;re de l&#39;Autel du Ruisseau
	"", #Repli strat&eacute;gique
	"", #Retraite Gel&eacute;e
	"", #Rotonde de Soggorsort
	"", #Ruelle du vadrouilleur de l’est
	"", #Salon d&#39;Esparvent
	"[&BJQBAAA=]", #Salon de Wrelk 
	"", #Sanctuaire hant&eacute; par un diablotin
	"[&BMUDAAA=]", #Sanctuaire piersacr&eacute;e 
	"", #Saut de Drakefaille
	"", #Saut de Mistriven</strong>
	"", #Saut de la conceptualisation
	"", #Sentinelle Engloutie / Bassin de la Sentinelle
	"[&BNIEAAA=]", #S&eacute;pulcre azumi&egrave;re 
	"", #S&eacute;pulcre ravag&eacute;
	"[&BMsBAAA=]", #Seuil d&#39;Usharr 
	"", #Sommet de l&#39;Epave
	"", #Source de Br&ucirc;lereinette
	"[&BCoDAAA=]", #Source de Dwayna 
	"[&BIECAAA=]", #Source des lamentations 
	"", #Surprise d&#39;Elise
	"", #Surveillant de Folleflamme
	"", #Terrasse de Wassa
	"", #Tour de guet de M&acirc;chefl&eacute;au
	"[&BFYCAAA=]", #Tour de la tribulation 
	"", #Trou de tirailleur de Creusepierre
	"", #Tunnel de Bandacier
	"", #Tunnel sous le lac
	"[&BKgCAAA=]", #Upsilon Hyperbolo&iuml;de 
	"[&BE8BAAA=]", #Vallon de Cymbel
]