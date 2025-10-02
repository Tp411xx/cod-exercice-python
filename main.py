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

def exercice5():
    print("exercice 5 : Addition simple")
    nombre1 = float(input("entrez votre nombre 1 :"))
    nombre2 = float(input("entrez votre nombre 2 :"))
    somme = nombre1 + nombre2
    print (f"La somme de {nombre1} et {nombre2} est {somme}")

def exercice6():
    print("exercice 6 :Soustraction simple")
    nombre1 = float(input("entrez votre nombre 1 :"))
    nombre2 = float(input("entrez votre nombre 2 :"))
    somme = nombre1 - nombre2
    print (f"La somme de {nombre1} et {nombre2} est {somme}")

def exercice7():
    print("exercice 7 : Multiplication simple")
    nombre1 = float(input("entrez votre nombre 1 :"))
    nombre2 = float(input("entrez votre nombre 2 :"))
    somme = nombre1 * nombre2
    print (f"La somme de {nombre1} et {nombre2} est {somme}")

def exercice8():
    print("exercice 8 : divison simple")
    
    while  nombre1 == 0:
     nombre1 = int(input("Le nombre ne peut pas être 0, réessaie : "))

    while  nombre2 == 0:
        nombre2 = int(input("Le nombre ne peut pas être 0, réessaie : "))

    somme = nombre1 / nombre2
    print (f"La somme de {nombre1} et {nombre2} est {somme}")

def exercice9():
    print ("exercice 9 : Carré d'un nombre")
    nombre = int(input("entrez un nombre :"))
    carré = nombre ** 2
    print (f"Le carré de {nombre} est {carré}")

def exercice10():
    print("exercice 10 : Double d'un nombre")
    nombre = int(input("entrez un nombre :"))
    double = nombre * 2
    print (f"Le double de {nombre} est {double}")

def exercice11():
    print ("exercice 11 : Demi d'un nombre")
    nombre = float(input("entrez un nombre :"))
    demi = nombre / 2
    print (f"Le demi de {nombre} est {demi}")

def exercice12():
    print("exercice 12 : Afficher 5 fois")
    message = (input("entrez un message :"))
    for i in range(5):
        print(message)
        
def exercice13():
    print("exercice 13 : Compter jusqu'à 5")
    for i in range(1, 6):
        print(i)

def exercice14():
    print("exercice 14 : Table de 2")
    for i in range(1, 6):
        resultat = 2 * i
        print(f"2 x {i} = {resultat}")





def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "14":
        exercice14()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
# main