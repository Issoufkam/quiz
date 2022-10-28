from funct import Question


list_question = [
    "Qu’est-ce que le cloud computing ?\n (a) La sauvegarde des fichiers stockés sur les ordinateurs de bureau et les appareils mobiles pour éviter la perte de données\n (b) Le déploiement d’applications connectées à une infrastructure sur site\n (c) L’exécution de code sans avoir besoin de gérer ou de mettre en service des serveurs\n (d) La mise à disposition de ressources informatiques et d’applications à la demande via Internet, avec une tarification à l’utilisation",
    "Quel autre nom peut-on donner au déploiement sur site ?\(a) Déploiement de cloud privé\n(b) Application basée sur le cloud\n(c) Déploiement hybride\n(d) AWS Cloud",
    "Dans quelle mesure la mise à l’échelle du cloud computing vous aide-t-elle à réduire vos coûts ?\n(a) Dans quelle mesure la mise à l’échelle du cloud computing vous aide-t-elle à réduire vos coûts ?\n(b) L’utilisation agrégée du cloud par un grand nombre de clients se traduit par une baisse des prix à l’utilisation.\n(c) L’accès à des services à la demande permet d’éviter une capacité excédentaire ou limitée.\n(d) Vous pouvez rapidement déployer des applications auprès des clients et leur fournir une faible latence.",
    "Vous souhaitez utiliser une instance Amazon EC2 pour une charge de travail de traitement par lots. Quel serait le meilleur type d’instance Amazon EC2 à utiliser ?\n(a) À usage général\n(b) Optimisée en mémoire\n(c) Optimisée pour le calcul\n(d) Optimisée pour le stockage",
    "Quelles sont les options de durée de contrat pour les instances réservées Amazon EC2 ? (Sélectionnez-en DEUX.)\n(a) 1 an\(b) 2 ans\(c) 3 ans\(d) 4 ans\n(e) 5 ans"
]

questions_reponse = [
    Question(list_question[0], 'd'),
    Question(list_question[1], 'a'),
    Question(list_question[2], 'b'),
    Question(list_question[3], 'c'),
    Question(list_question[4], 'c'),
]


def test(questions):
    name = input("Entrez votre nom: ")
    score=0
    for question in questions:
        print(question.question)
        reponse = input('Votre reponse: ')
        if reponse == question.reponse:
            score+=2
    print(f"{name} votre score est {score}/{len(questions)}")