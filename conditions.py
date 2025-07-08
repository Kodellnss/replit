# def age_pair (age : int) -> str : 
#   if age % 2 == 0 :
#     return "pair"
#   else :
#     return "impair"

# age = int(input("Quel est votre age ? "))
# print(age_pair(age))

# worthy = "No"
# thanos_here = True

# if worthy == "yes !":
#     print("Thor picked up the Hammer")
# elif thanos_here == False:  # le == True est superflu ici, essayez sans pour voir ;)
#     print("Captain America picked up the Hammer")
# else:
#     print("The avenger could not lift the Hammer")

# print("fight !")

# def sncf_reduc (age : int | float) -> str : 
#   if age <= 27 : 
#     return "Carte Avantage Jeune : Vous bénéficiez d'une réduction de 30% sur vos trajets en train pour 49e par mois"
#   elif age > 27 and age < 60 :
#     return "Carte Avantage Famille : Vous bénéficiez d'une réduction de 30% sur vos trajets en train pour 49e par mois"
#   else:
#     return "Carte Avantage Senior : Vous bénéficiez d'une réduction de 30% sur vos trajets en train pour 49e par mois"

# age = int(input("Quel est votre age ? "))
# print(sncf_reduc(age))

validite = input("Votre carte est-elle valide ? (oui/non) ")
member = input("Êtes-vous membre de la SNCF ? (oui/non) ")

def syst_rduc(age: int) -> str:
    # Si l'utilisateur est membre, il a l'accès sans condition
    if member.lower() == "oui":
        return "Vous avez l'accès"

    # Sinon, on vérifie l'âge et la validité
    if age < 18:
        return "Vous n'avez pas l'accès"
    elif validite.lower() == "oui":
        return "Vous avez l'accès"
    else:
        return "Vous n'avez pas l'accès"

# On demande l'âge uniquement si la personne n'est pas membre
if member.lower() != "oui":
    age = int(input("Quel est votre âge ? "))
else:
    age = 0  # valeur neutre, non utilisée car membre

print(syst_rduc(age))


    
    