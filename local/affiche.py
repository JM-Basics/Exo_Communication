import ledArduino
import dicoMatrice2D

print("quelle lettre afficher ?")
lettre = input(">>> ")
matrice = dicoMatrice2D.dico2D[lettre]

for ligne in matrice:
    print(ligne)
    
ledArduino.ledMatrice(matrice)


