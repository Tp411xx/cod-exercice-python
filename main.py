def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    print("Exercice 2 : Afficher son prénom")
    prenom = input("Entrez votre prénom : ")
    print(f"Bonjour, {prenom} !")
    
def exercice3():
    print("Afficher trois lignes")
    print(" ligne1\n ligne2\n ligne3")

def exercice4():
    print("Exercice 4 : Calculer l'âge")
    année_naissance =int(input("entrez votre année de naissance : "))
    année_actuelle = 2025
    âge = année_actuelle - année_naissance
    print(f"Vous avez {âge} ans.")
   
def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "4":
        exercice4()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
# main