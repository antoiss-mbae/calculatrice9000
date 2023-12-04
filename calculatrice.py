def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Erreur : Division par zéro n'est pas autorisée.")
    return a / b

def afficher_historique(historique):
    print("Historique des calculs :")
    for calcul in historique:
        print(calcul)

def calculatrice():
    historique = []  # Liste pour stocker les calculs effectués

    while True:
        try:
            # Saisie des nombres et de l'opération
            saisie = input("Entrez le premier nombre (ou 'q' pour quitter) : ")
            if saisie.lower() == 'q':
                break  # Quitter la boucle si l'utilisateur entre 'q'

            nombre1 = float(saisie)
            nombre2 = float(input("Entrez le deuxième nombre : "))
            operation = input("Entrez l'opération (+, -, *, /) : ")

            # Vérification de l'opération et exécution
            if operation == '+':
                resultat = addition(nombre1, nombre2)
            elif operation == '-':
                resultat = soustraction(nombre1, nombre2)
            elif operation == '*':
                resultat = multiplication(nombre1, nombre2)
            elif operation == '/':
                resultat = division(nombre1, nombre2)
            else:
                raise ValueError("Erreur : Opération non valide.")

            # Ajout du calcul à l'historique
            calcul = f"{nombre1} {operation} {nombre2} = {resultat}"
            historique.append(calcul)

            # Affichage du résultat
            print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat}")

        except ValueError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")

    # Afficher l'historique à la sortie
    afficher_historique(historique)

# Exemple d'utilisation de la calculatrice avec historique
calculatrice()
