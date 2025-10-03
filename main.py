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
    nombre1 = float(input("entrez votre nombre 1 :"))
    nombre2 = float(input("entrez votre nombre 2 :"))
    if nombre2 == 0:
        print("Erreur : Division par zéro impossible.")
        return
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

def exercice15():
    print("exercice15 : Périmètre du carré")
    côté= float(input("entrez la longueur d'un côté du carré :"))
    périmètre = 4 * côté
    print (f"Le périmètre du carré est {périmètre}")

def exercice16():
    print("exercice 16 : Aire du carré")
    côté= float(input("entrez la longueur d'un côté du carré :"))
    aire = côté ** 2
    print (f"L'aire du carré est {aire}")


def exercice17():
    print("exercice17 : Conversion euros → dollars")
    euros = float(input("entrez un montant en euros :"))
    print (f"{euros} euros = {euros * 1.1} dollars")

def exercice18():
    print ("exercice18 : Conversion minutes → secondes")
    minutes = float(input("entrez un nombre de minutes :"))
    secondes = minutes * 60
    print (f"{minutes} minutes = {secondes} secondes")

def exercice19():
    print("exercice19 : Prix TTC")
    prix_ht = int(input("entrez le prix hors taxe :"))
    tva = prix_ht * 0.2
    prix_ttc = prix_ht + tva
    print (f"Le prix TTC est de {prix_ttc} euros")

def exercice20():
    print("exercice20 :  Message personnalisé")
    nom = input("entrez votre nom :")
    âge = input("entrez votre âge :")
    print (f"{nom} {âge} ans.") 

def exercice21():
    print("exercice21 :  Test positif/négatif")
    nombre = input("entrez un nombre :")
    if nombre > 0:
        print("Le nombre est positif.")
    elif nombre < 0:
        print("Le nombre est négatif.")
    else:
        print("Le nombre est zéro.")

def exercice22():
    print("exercice22 :  majeur/mineur")
    input("entrez un nombre :")
    if nombre >= 18:
        print("Majeur.")
    else:
        print("Mineur.")


def exercice23():
    print("exercice23 : note validé")
    input("entrez un nombre :")
    if nombre >= 10:
        print("validé.")
    else:
            print("refusé.")



def exercice24():
    print("exercice24 : le plus grand")
    numero1 = input("entrez un nombre1 :")
    numero2 = input("entrez un nombre2 :")
    if nombre1 < nombre2:
        print(f"{nombre2} est le plus grand.")
    elif nombre1 > nombre2:
        print(f"{nombre1} est le plus grand.")
    else:
        print(f"{nombre2} et {nombre1} sont égaux.")
            

def exercice25():
    print("exercice25 : ordre croissant ")
    numero1 = input("entrez un nombre1 :")
    numero2 = input("entrez un nombre2 :")
    if nombre1 < nombre2:
        print(f"{nombre1} et {nombre2} sont croissants.")
    else: 
        print(f"{nombre1} et {nombre2} ne sont pas croissants.")
          
def exercice26():
    print("exercice26 : Divisible par 5")
    numero = input("entrez un nombre :")
    if nombre % 5 == 0:
        print(f"{nombre} est divisible par 5.")
    else: 
        print(f"{nombre} n'est pas divisible par 5.")

def exercice27():
    print("exercice27 : categorie d'âge")
    nombre = int(input("entrez un nombre :"))
    if nombre < 12 :
        print(f"{nombre} enfant")
    elif 12 < nombre < 17 :
        print(f"{nombre} adolescent")
    else:
        print(f"{nombre} adulte.") 


def exercice28():
    print("exercice28 : Température de l'eau")
    nombre = int(input("entrez un nombre :"))
    if nombre < 0 :
        print(f"{nombre} solide")
    elif 0 < nombre < 100 :
        print(f"{nombre} liquide")
    else:
        print(f"{nombre} gaz.") 

def exercice29():
    print("exercice29 : Mention au bac")
    nombre = int(input("entrez un nombre :"))
    if nombre < 8 :
        print(f"{nombre} raté")
    elif 8 < nombre <11 :
        print(f"{nombre} rattrapage")
    elif 11 < nombre < 14 :
        print(f"{nombre} passable ")
    elif 14 < nombre < 16 :
        print(f"{nombre} bien")
    else:
        print(f"{nombre} très bien.") 


def exercice30():
    print("exercice30 : Compter de 1 à N")
    nombre = int(input("entrez un nombre :"))
    for i in range(1, nombre + 1):
        print(i)



def exercice31():
    print("exercice31 : Compter de N a 0")
    nombre = int(input("entrez un nombre :"))
    for i in range(nombre , -1, - 1):
        print(i)

def exercice32():
    print("exercice32 : Somme de 1 à N")
    nombre = int(input("entrez un nombre :"))
    somme = 0
    for i in range(1, nombre + 1):
        somme += i
    print(f"La somme de 1 à {nombre} est {somme}")

def exercice33():
    print("exercice33 :Table de multiplication")
    nombre = int(input("entrez un nombre : "))
    for i in range(1.11):
        resultat = nombre * i
        print(f"{nombre} x {i} = {resultat}")


def exercice34():
    print("exercice34 : Nombres pairs jusqu'à N")
    numero = input("entrez un nombre :")
    if nombre % 2 == 0:
        print(f"{nombre} est pair.")
    else:
        print(f"{nombre} n'est pas paire.")


def exercice35():
    print("exercice35 : Carrés parfaits jusqu'à N")
    nombre = int(input("entrez un nombre."))
    for i in range(1,nombre + 1):
        carré = i ** 2
        if carré <= nombre:
            print(f"Le carré de {i} est {carré}")

def exercice36():
    print("exercice 36 : Compter jusqu'à N")
    nombre = int(input("entrez un nombre :"))
    mot = input("entrez un mot :")
    for i in range(nombre +1):
        if i <= nombre:
            print(f"{mot}")

def exercice37():
    print("exercice 37 : pyramide d'étoiles")
    print(" * \n ** \n *** \n **** \n *****")


def exercice38():    
    print("exercice 38 : calculatrice simple")
    nombre1 = float(input("entrez votre nombre 1 :"))
    opérateur = input("entrez un opérateur (+, -, *, /) :")
    nombre2 = float(input("entrez votre nombre 2 :"))
    if opérateur == "+":
        résultat = nombre1 + nombre2
        print (f"La somme de {nombre1} et {nombre2} est {résultat}")
    elif opérateur == "-":
        résultat = nombre1 - nombre2
        print (f"La soustraction de {nombre1} et {nombre2} est {résultat}")
    elif opérateur == "*":
        résultat = nombre1 * nombre2
        print (f"La multiplication de {nombre1} et {nombre2} est {résultat}")
    elif opérateur == "/":
        if nombre2 == 0:
            print("Erreur : Division par zéro impossible.")
            return
        résultat = nombre1 / nombre2
        print (f"La division de {nombre1} et {nombre2} est {résultat}")
    else:
        print("Opérateur non reconnu.")
        return


def exercice39():
    print("exercice 39 : . Deviner pair/impair")
    import random
    secret = random.randint(1, 100)
    pari = input("Pariez sur 'pair' ou 'impair' :").lower()
    if (secret % 2 == 0 and pari == "pair") or (secret % 2 != 0 and pari == "impair"):
        print(f"Félicitations ! Le nombre était {secret}, vous avez gagné.")
    else:
        print(f"Dommage ! Le nombre était {secret}, vous avez perdu.")


def exercice40():
    print("exercice40 : Validation de mot de passe")
    mot_de_passe = input("entrez un mot de passe :")
    if len(mot_de_passe) < 6:
        print("Le mot de passe doit contenir au moins 6 caractères.")
        return   
    elif not any(char.isdigit() for char in mot_de_passe):
        print("Le mot de passe doit contenir au moins un chiffre.")
        return
    elif not any(char.isupper() for char in mot_de_passe):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        return
    else:
        print("Mot de passe validé.")


def exercice41():
    print("exercice41 : Moyenne de 5 notes")
    nombre_note = int(input("entrez le nombre de notes :"))
    total = 0
    for i in range(1, nombre_note + 1):
        note = int(input(f"entrez la note {i} :"))
        total += note
    moyenne = total / nombre_note
    print(f"La moyenne est de {moyenne}")


def exercice42():
    print("exercice42 : Min et max de 5 nombres")
    
    while True:  # boucle infinie, on sort avec break
        choix = input("Tapez q pour arrêter ou appuyez sur Entrée pour continuer : ")
        if choix.lower() == "q":  # .lower() gère q ou Q
            break
        
        nombre_note = 5
        minimum = None
        maximum = None
        
        for i in range(1, nombre_note + 1):
            note = int(input(f"Entrez la note {i} : "))
            
            if minimum is None or note < minimum:
                minimum = note
            if maximum is None or note > maximum:
                maximum = note
        
        print(f"Le minimum est {minimum} et le maximum est {maximum}")

def exercice43():
    print("exercice43 : Compteur de voyelles (simple)")
    texte = input("entrez un texte :").lower()
    voyelles = "aeiouy"
    compteur = 0
    for char in texte:
        if char in voyelles:
            compteur += 1
    print(f"Le texte contient {compteur} voyelles.")






def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "43":
        exercice43()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
# main