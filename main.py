import random

def deviner_nombre():
    """
    Fonction principale pour jouer au jeu Deviner le Nombre.
    L'ordinateur génère un nombre aléatoire, et le joueur doit le deviner.
    """
    print("Bienvenue au jeu Deviner le Nombre!")
    print("L'ordinateur a choisi un nombre entre 1 et 100.")
    print("Essayez de le deviner! Tapez 'quit' pour quitter le jeu.")
    
    # Générer un nombre aléatoire entre 1 et 100
    nombre_secret = random.randint(1, 100)
    tentatives = 0  # Compteur de tentatives
    
    while True:
        # Demander au joueur d'entrer un nombre
        entree = input("\nEntrez votre nombre: ")
        
        # Vérifier si le joueur veut quitter le jeu
        if entree.lower() == "quit":
            print("Merci d'avoir joué! À bientôt!")
            break
        
        # Vérifier que l'entrée est un nombre valide
        if not entree.isdigit():
            print("Veuillez entrer un nombre valide.")
            continue
        
        # Convertir l'entrée en entier
        nombre_joueur = int(entree)
        tentatives += 1
        
        # Comparer le nombre du joueur avec le nombre secret
        if nombre_joueur < nombre_secret:
            print("Trop petit! Essayez encore.")
        elif nombre_joueur > nombre_secret:
            print("Trop grand! Essayez encore.")
        else:
            print(f"Félicitations! Vous avez trouvé le nombre {nombre_secret} en {tentatives} tentatives!")
            break

def main():
    """
    Point d'entrée du programme.
    Lance le jeu Deviner le Nombre.
    """
    deviner_nombre()

# Appeler la fonction main si le script est exécuté directement
if __name__ == "__main__":
    main()
