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

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "3":
        exercice3()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
# main