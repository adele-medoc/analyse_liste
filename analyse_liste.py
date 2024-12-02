print("donne une liste de nombres entier séparés par des virgules. Par exemple : 1,2,3,4")
liste_de_nombre = input()
liste_de_nombre = liste_de_nombre.split(",")
resultat_somme = 0
resultat_moyenne = 0
n_n_sup_moyenne = 0
nombre_pair = 0
nombre_impair = 0
print(liste_de_nombre)

for i in liste_de_nombre :
  resultat_somme = (resultat_somme + int(i))
print("Somme des nombres :" + str(resultat_somme))

resultat_moyenne = resultat_somme / len(liste_de_nombre)
print("Moyenne des nombres :" + str(resultat_moyenne))

for i in liste_de_nombre:
  if float(i) > float(resultat_moyenne):
     n_n_sup_moyenne = len(i) + 1
print("Nombre de nombres supérieurs à la moyenne :" + str(n_n_sup_moyenne))

i = 0
while i < len(liste_de_nombre):
    if (int(liste_de_nombre[i]) % 2 == 0):
        nombre_pair = nombre_pair + 1
    i = i + 1
print("Nombre de nombres pairs :" + str(nombre_pair))
