import random

def jeu_du_pendu():
    """
    Fonction principale pour jouer au jeu du Pendu.
    Le joueur doit deviner les lettres d'un mot avant que toutes les tentatives soient épuisées.
    """
    print("Bienvenue au jeu du Pendu!")
    print("Devinez le mot, une lettre à la fois.")
    
    # Liste de mots possibles
    mots = ["python", "programmation", "ordinateur", "jeu", "pendu", "algorithmique"]
    # Choisir un mot aléatoire dans la liste
    mot_secret = random.choice(mots)
    # Créer une représentation du mot caché avec des underscores
    mot_cache = ["_"] * len(mot_secret)
    # Définir le nombre maximal de tentatives
    tentatives_restantes = 6
    lettres_devinees = set()
    
    while tentatives_restantes > 0:
        print("\nMot à deviner: " + " ".join(mot_cache))
        print(f"Tentatives restantes: {tentatives_restantes}")
        print(f"Lettres devinées: {', '.join(sorted(lettres_devinees))}")
        
        # Demander une lettre au joueur
        lettre = input("Proposez une lettre: ").lower()
        
        # Vérifier la validité de l'entrée
        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue
        if lettre in lettres_devinees:
            print("Vous avez déjà proposé cette lettre.")
            continue
        
        # Ajouter la lettre aux lettres devinées
        lettres_devinees.add(lettre)
        
        # Vérifier si la lettre est dans le mot secret
        if lettre in mot_secret:
            print(f"Bonne réponse! La lettre '{lettre}' est dans le mot.")
            # Révéler la lettre dans le mot caché
            for i, l in enumerate(mot_secret):
                if l == lettre:
                    mot_cache[i] = lettre
        else:
            print(f"Mauvaise réponse! La lettre '{lettre}' n'est pas dans le mot.")
            tentatives_restantes -= 1
        
        # Vérifier si le joueur a deviné tout le mot
        if "_" not in mot_cache:
            print("\nFélicitations! Vous avez trouvé le mot:", mot_secret)
            break
    else:
        # Le joueur a utilisé toutes ses tentatives
        print("\nDommage! Vous avez perdu. Le mot était:", mot_secret)

def main():
    """
    Point d'entrée du programme.
    Lance le jeu du Pendu.
    """
    jeu_du_pendu()

# Appeler la fonction main si le script est exécuté directement
if __name__ == "__main__":
    main()
