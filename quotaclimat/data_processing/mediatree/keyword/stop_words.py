# Based on advertising
STOP_WORDS = [
    "bonus écologique"
    ,"verlaine isolation thermique"
    ,"haute isolation thermique fabriqué en france"
    ,"ou covoiturage tous les moyens sont bon"
    ,"blablacar et recevez cent euros de prime covoiturage"
    ,"conditions sébastien point fr covoiturage"
    ,"sur dacia point fr covoiturage"
    ,"dacia point fr un covoiturage"
    ,"engie peut vous aider par exemple avec des panneaux solaires"
    ,"verlaine photovoltaïques"
    ,"verlaine le climat"
    ,"photovoltaïque groupe"
    ,"groupe verlaine isolation photovoltaïques"
    ,"photovoltaïques vie"
    ,"garanti photovoltaïques"
    ,"photovoltaïque verlaine"
    ,"installation photovoltaïque de trois kilowatt"
    ,"photovoltaïque de groupe verlaine"
    ,"installation photovoltaïque de trois kilos"
    ,"installation photovoltaïque peut vous faire économiser jusqu'"
    ,"installation photovoltaïque et garantis vingt-cinq ans"
    ,"centrale photovoltaïque et pompes à chaleur groupe verlaine"
    ,"centrale photovoltaïque pompes à chaleur groupe verlaine"
    ,"climat de confiance"
    ,"panneau photovoltaïque et bornes de recharge thompson groupe verlaine"
    ,"photovoltaïque pour réduire vos factures d' électricité groupe verlaine"
    ,"centrale photovoltaïque mobile facile"
    ,"photovoltaïque groupe verlaine"
    ,"photovoltaïque de groupe verlaine"
    ,"centrale photovoltaïque a posé en toute simplicité"
    ,"centrale photovoltaïque à poser en toute simplicité"
    ,"centrale photovoltaïque de quatre cents watts"
    ,"centrale photovoltaïque produisait et consommer votre propre énergie"
    ,"verlaine isolation centrales photovoltaïques"
    ,"verlaine isolation photovoltaïque et pompe à chaleur"
    ,"verlaine isolation centrales photovoltaïques et pompes"
    ,"verlaine isolation photovoltaïque et pompes à chaleurs"
    ,"verlaine isolation photovoltaïques pompes à chaleur"
    ,"verlaine isolation photovoltaïque pompe à chaleur"
    ,"on refait son isolation change sans chauffage"
    ,"installe des panneaux photovoltaïques et des bornes de recharge"
    ,"le leader du photovoltaïque chez les particulier"
    ,"panneaux solaires pour produire votre énergie"
    ,"installateur panneaux de photovoltaïques"
    ,"installateurs de panneaux photovoltaïques"
    ,"installateur de panneaux photovoltaïques"
    ,"installateur de panneaux solaires"
    ,"installateurs de panneaux solaires"
    ,"verlaine installation de panneaux solaires"
    ,"votre expert en panneaux solaires" #  mon kits solaires point fr
    ,"le top des panneaux solaires"
    ,"panneaux solaires garantie à vie"
    ,"avec des panneaux solaires c' est jusqu' à mille cinq"
    ,"de panneaux solaires cinq mille huit"
    ,"en panneaux solaires c' est une banque décidé"
    ,"en panneaux solaires est une bande décidé"
    ,"économies d' énergie impact environnemental des vies"
    ,"économies d' énergie l' impact environnemental des vies"
    ,"ou des entreprises font des économies d' énergie ou l' impact environnemental des vies"
    ,"font des économies d' énergie ou l' impact environnemental"
    ,"pompes entretien à pour chaleur pompes et à photovoltaïque"
    ,"panneaux solaires groupe"
    ,"pour réduire votre facture d' électricité en installant des panneaux solaires"
    ,"panneaux solaires j' agis avec engie"
    ,"panneaux solaires j' agis avec kendji"
    ,"les tuiles se transforme en panneaux solaires"
    ,"en installant des panneaux solaires j' agis" 
    ,"panneaux solaires face à l' inflation" 
    ,"l'isolation le chauffage les panneaux solaires" 
    ,"installer vos panneaux solaires produire" 
    ,"la crème solaire pour les panneaux solaires" 
    ,"panneaux solaires c' est moi qui" 
    ,"panneaux solaires installation matériel démarches" 
    ,"panneaux solaires installation matérielle démarches"
    ,"la solution de panneaux solaires qui vous aide" 
    ,"installant des panneaux solaires usagés avec" 
    ,"installant des panneaux solaires usagers avec" 
    ,"vous équiper de panneaux solaires et faire des" 
    ,"panneaux solaires découvrez les offres"  
    ,"on monte les panneaux solaires que j'ai"
    ,"énergie solaire avec avicenne"
    ,"panneaux photovoltaïques garanti à vie"
    ,"on installe des panneaux photovoltaïques borne de recharge"
    ,"on installe des panneaux photovoltaïques des bornes de recharge"
    ,"le leader du photovoltaïque"
    ,"en train d"
    ,"consigne de vote"
    ,"climat de confiance"
    ,"huile de coude est aussi une énergie renouvelable"
    ,"huile de coude était aussi une énergie renouvelable"
    ,'huile de coude étaient aussi une énergie renouvelable'
    ,'huile de coude étaient aussi est aussi une énergie renouvelable '
    ,"franchisés dans les énergies renouvelable"
    ,"franchisé dans les énergies renouvelable"
    ,'énergie renouvelable stéphan'
    ,"énergie renouvelable pour moins polluer"
    ,"énergie renouvelable pour dépenser moins"
    ,"grand acheteur d' énergie renouvelable"
    ,"énergie renouvelable au monde"
    ,"par des garanties d' origine renouvelable"
    ,"énergies renouvelables groupe verlaine"
    ,"borne de recharge offert"
    ,"plus de mille bornes de recharge"
    ,"localise une borne de recharge"
    ,"edf installe votre borne de recharge"
    ,"pour faire installer ma borne de recharge"
    ,"borne de recharge partager"
    ,"localisent une borne de recharge"
    ,"bornes de recharge offert"
    ,"presque impérativement avoir une borne de recharge"
    ,"bornes de recharge et des mois de loyer"
    ,"bornes de recharge et deux"
    ,"si vous avez une borne de recharge partager"
    ,"cent pour cent électriques bornes de recharge"
    ,"votre borne de recharge que vous habitez"
    ,"borne de recharge j' ai pas hésité"
    ,"borne de recharge et deux mois"
    ,"une borne de recharge bien installé"
    ,"vous avez une borne de recharge" 
    ,"en ce moment borne de recharge"
    ,"vous offre la borne de recharge"
    ,"profiter de la borne de recharge offert"
    ,"borne de recharge est offert"
    ,"borne de recharge offerte" 
    ,"faire installer une borne de recharge" 
    ,"en copropriété une borne de recharge" 
    ,"pour les plus branchées la borne de recharge" 
    ,"leasing électrique à"
    ,"dispositif mon leasing électrique"
    ,"gouvernemental mon leasing électrique"
    ,"éligibles au leasing électrique"
    ,"éligible au leasing électrique"
    ,"ce leasing électrique ça rendait vraiment la voiture"
    ,"offre mon leasing électrique"
    ,"leasing électrique économise"
    ,"climatique c' est pour ça que je suis au crédit coopératif"
    ,"installateur de pompe à chaleur air"
    ,"pompe à chaleur atlantique"
    ,"isolation photovoltaïque et pompe à chaleur pour une réno"
    ,"centrale photovoltaïque du futur" # thompson
    ,"leader du photovoltaïque"
    ,"centrale photovoltaïque à partir"
    ,"et plus durable et avec spoticar"
    ,"l' éolien jeanjean"
    ,"rénovation énergétique point fr"
    ,"la rénovation énergétique la météo avec"
    ,"papa la rénovation énergétique"
    ,"mouvement de la rénovation énergétique"
    ,"la rénovation énergétique réussie c' est simple"
    ,"rénovation énergétique avec point p"
    ,"projets de rénovation énergétique avec"
    ,"lancé dans la rénovation énergétique de sa maison"
    ,"lance dans la rénovation énergétique de sa maison"
    ,"lancer dans la rénovation énergétique de sa maison"
    ,"rénovation énergétique rendez-vous sur"
    ,"rénovation énergétique contacté effie"
    ,"rénovation énergétique contacter effie"
    ,"rénovation énergétique contacté effie"
    ,"rénovation énergétique contactés effie"
    ,"rénovation énergétique contactés effie"
    ,"rénovation énergétique contacté efi"
    ,"rénovation énergétique groupe verlaine"
    ,"des travaux de rénovation énergétique jusqu' au"
    ,"edf c' est une rénovation énergétique"
    ,"rénovation énergétique c' était la météo avec groupe verlaine"
    ,"pour votre rénovation énergétique france renov le service public"
    ,"rendre la rénovation énergétique accessible au plus grand nombre à découvrir"
    ,"de rénovation énergétique avec castorama"
    ,"rénovation énergétique rendez vous "
    ,"pour la rénovation énergétique par contre"
    ,"experts de la rénovation énergétique il te conseille"
    ,"la rénovation énergétique il te conseille"
    ,"mon parcours rénovation diagnostic"
    ,"merlin la rénovation énergétique"
    ,"rénovation énergétique la météo avec groupe verlaine"
    ,"rénovation globale groupe verlaine"
    ,"bien démarrer votre rénovation énergétique"
    ,"en machine le gaspillage"
    ,"l' économie circulaire liddell"
    ,"l' économie circulaire carrefour"
    ,"pour l' économie circulaire bonjour"
    ,"sans ogm et cent pour cent"
    ,"nourries sans ogm"
    ,"nourries sans ogm et ogm cent"
    ,"Salon de jardin miami fabriqué avec quatre-vingts pour cent de matériaux recyclés"
    ,"l' entreprise de julie fabrique des meubles en matériaux recyclés"
    ,"jardin miami fabriqué avec quatre-vingts pour cent de matériaux recyclés"
    ,"trier ses déchets ça fait partie du jeu"
    ,"trier ses déchets même si ce n' est pas toujours évident"
    ,"voire règlement services déchets"
    ,"salon de jardin miami fabriqué avec quatre-vingts pour cent de matériaux recyclés"
    ,"l' entreprise de julie fabrique des meubles en matériaux recyclés"
    ,"jardin miami fabriqué avec quatre-vingts pour cent de matériaux recyclés"
    ,"nous-mêmes du plastique recyclé"
    ,"nous-même du plastique recyclé"
    ,"trois usines exclusivement dédiée aux recyclage"
    ,"trois usines exclusivement dédié au recyclage"
    ,"trois usines exclusivement dédiés au recyclage"
    ,"trois usines exclusivement dédiées au recyclage"
    ,"vivement dédiées au recyclage"
    ,"un gouvernement de recyclage"
    ,"trier devient plus simple"
    ,"grâce à vous qui trier vos bouteilles"
    ,"nous les recycle pour en faire de nouvelles"
    ,"cristalline est capable de recycler"
    ,"cristalline et capable de recycler"
    ,"vos bouteilles nous les recycler"
    ,"recycler des lunettes"
    ,"est capable de recycler recycler"
    ,"recycler des milliers de tonnes"
    ,"nous les recycler pour en faire"
    ,"recycler en disant on a déjà recycler"
    ,"recycler en dix ans on a déjà recycler"
    ,"recycler en dix ans on a déjà recyclé"
    ,"recycler et créer des contrats"
    ,"pour recycler votre épave"
    ,"la recycler la vieille"
    ,"ou les notices de panneaux photovoltaïques"
    ,"grâce aux dons à la réparation au recyclage"
    ,"renforcement de nos filières de recyclage"
    ,"est partout en france le recyclage de pare-brise"
    ,"est le royaume du recyclage il faut juste"
    ,"en termes de tri des déchets le recyclage ou d' énergies renouvelables"
    ,"recyclage depuis trente ans" # cristalline
    ,"cristaline l' eau préférée"
    ,"eau minérale naturelle"
    ,"packs d' eau"
    ,"d' gien eau"
    ,"est à fond sur le tri sélectif"
    ,"transition énergétique baisse de lumière"
    ,"transition énergétique co"
    ,"transition énergétique nos lumières"
    ,"transition énergétique lumière"
    ,"transition énergétique on est aux lumières"
    ,"transition énergétique ces lots lumière"
    ,"transition énergétique c' est aux lumières"
    ,"vendez votre voiture point fr"
    ,"votre voiture obtenait un prix"
    ,"recharge ma brosse à dents"
    ,"qui bossait dans l' eau" # maif
    ,"je croyais que dégât des eaux" # maif
    ,"un goût généreux et le respect de la nature sans résidu de pesticides" # tramier
    ,"écoresponsables offre valable" #aldi
    ,"écoresponsable offre valable" #aldi
    ,"vergers écoresponsables" #aldi
    ,"factures avec l' installation de panneaux solaires"
    ,"panneaux solaires et faire des économies carrefour"
    ,"garantie carrefour énergie"
    ,"économies sur votre énergie"
    ,"énergie c' est trop cher je vous réponds fait comme marc"
    ,"énergie une étude révèle que six français sur dix"
    ,"énergie choisissez edf"
    ,"énergie et notre avenir économisant"
    ,"voiture de l' année"
    ,"voiture année"
    ,"carrefour point fr les publicités de voiture"
    ,"aramisauto nos voitures"
    ,"aramis auto nos voitures"
    ,"voiture sur aramisauto"
    ,"voiture au meilleur prix"
    ,"l' univers de la voiture d' occasion"
    ,"voiture sur aramis auto"
    ,"future voiture d' occasion reconditionnée"
    ,"vous appel parce que ma voiture"
    ,"disposition une voiture le temps"
    ,"isolation par l' extérieur"
    ,"votre énergie avec l' installation de panneaux solaires"
    ,"offrez à vos clients un devis précis pour améliorer la performance énergétique"
    ,"augmenter la performance énergétique et la"
    ,"performance énergétique de votre logement groupe verlaine"
    ,"gaz très haute performance énergétique plus confortable"
    ,"pergola bioclimatique"
    ,"on imagine des murs végétalisé"
    ,"pêche durable liddell"
    ,"pêche durable littell"
    ,"pêche durable l' idéal"
    ,"maprimerénov leroy"
    ,"maprimerénov et économiser jusqu' à"
    ,"maprimerénov une offre comme ça même chez lapeyre"
    ,"aux aides maprimerénov et de faisabilité sous condition"
    ,"leroy merlin quand on refait son isolation"
    ,"météo avec parc saint-paul"
    ,"économies d' énergie l' impact environnemental des vies"
    ,"économies d' énergie impact environnemental des vies"
    ,"compliqué d' économiser de l' énergie alors engie vous aide"
    ,"pour faire des économies d' énergie juliette"
    ,"elle voudrait faire des économies de chauffage"
    ,"total énergie"
    ,"option énergies vertes"
    ,"devenir franchisés dans les énergies renouvelables"
    ,"écologiques pour remplacer votre"
    ,"accrochages c' est aussi plus écologique"
    ,"transition écologique avec le groupe tf1"
    ,"planète radio"
    ,"responsable service"
    ,"plus responsable chez électro dépôt"
    ,"haut responsable"
    ,"responsable politique"
    ,"vous êtes responsable"
    ,"responsable du"
    ,"responsables du"
    ,"la responsable"
    ,"le responsable"
    ,"les responsables"
    ,"chaque responsable"
    ,"pas responsable"
    ,"responsable de"
    ,"comme responsable"
    ,"du responsable"
    ,"verger écoresponsable"
    ,"français écoresponsable sont à"
    ,"érigés en barrage"
    ,"partie du barrage"
    ,"barrage au"
    ,"barrage et affrontement"
    ,"barrage à des"
    ,"barrage filtrant"
    ,"par terre"
    ,"pieds sur terre"
    ,"tremblement de terre"
    ,"paradis sur terre"
    ,"terre battue"
    ,"rituel de la forêt"
    ,"électrique ou hydrogène il existe"
    ,"électrique hydrogène il existe"
    ,"de l' ombre et de la lumière"
    ,"vélo pour aller chercher le pain"
    ,"camion ou du vélo"
    ,"vélo liddell"
    ,"vélo électrique de décathlon"
    ,"vélo électrique nakamura"
    ,"sofinco tu peux acheter un vélo électrique"
    ,"votre trajet à vélo un vrai"
    ,"c' est quoi un vélo électrique"
    ,"à vélo avec les forfaits kilométriques alliance"
    ,"vue sur mer"
    ,"issu de l' agriculture biologique en boutique"
    ,"agriculture biologique pour les produits de beauté"
    ,"vous aimez les voitures électriques" # renault
    ,"and roll des voitures électriques"
    ,"conduisiez une voiture électrique l' application"
    ,"engie pourquoi l' ordinaire devrait être la norme"
    ,"de plus en plus d' énergie éolien comme celui-ci" # amazon
    ,"l' eau filtrée britta"
    ,"bonne maman beaucoup de noisette huile de palme"
    ,"sans pesticides pour des recettes"
    ,"chez céréales bio"
    ,"agir pour la préserver découvrez comment" #gouv.fr
]
