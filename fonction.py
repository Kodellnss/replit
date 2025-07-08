fichier = open("ultima_verba.txt", "r")
contenu = fichier.read()
print(contenu)
fichier.close()

fichier = open('ultima_verba.txt', 'w')
fichier.write("yo")
fichier.close()

fichier = open('ultima_verba.txt', 'w')
fichier.write("Le lion ne s’associe pas avec le cafard")
fichier.close()

fichier = open('ultima_verba.txt', 'a')
contenu = fichier.write("\nVictor Hugo, Jersey, 2 décembre 1852\n")
fichier.close()




def hello_there() :
  print("Hello there!")  
hello_there()

def print_bonjour(prenom_a_inserer) : 
  return(f"Bonjour {prenom_a_inserer} !")
moi = input("Quel est ton prénom ? ")
print_bonjour(moi)

def create_greeting(name) :
  return f"Hello, {name} !"
info = input("Enter your name: ")
print(create_greeting(info))

def jesus(pain : int ,chiffre_multiplicateur : int) -> int : 
  return pain * chiffre_multiplicateur
p = int(input("nombre de pain : "))
x = int(input("multiplicateur : "))
print(jesus(p,x))

def multiply(x,y) : 
  return x * y
print(multiply(2,3))

def divede_et_impera(a : int | float ,c : int | float) -> int | float : 
  return a / c
print(divede_et_impera(4,3))