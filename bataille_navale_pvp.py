#Bibliothèque requis
from termcolor import colored
import csv
# TEST

#Initialisation des variables pour les scores
shootP1 = 0
shootP2 = 0
missP1 = 0
missP2 = 0
P1 = input("Quel est le nom du joueur 1 ?")
P2 = input("Quel est le nom du joueur 2 ?")
tr = False
tab=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
deb=0
fin=len(tab)-1


with open("scores.txt", "r") as scoreFile:
    scoreFileReader = csv.reader(scoreFile)
    scoreList = []
    for row in scoreFileReader :
        if len(row) != 0 :
            scoreList = scoreList + [row]
    scoreFile.close()

#Déclaration des deux dictionnaires de position
tabP1 = {
        "A1" : ["*", 1, 1],
        "A2" : ["*", 1, 2],
        "A3" : ["*", 1, 3],
        "A4" : ["*", 1, 4],
        "A5" : ["*", 1, 5],
        "A6" : ["*", 1, 6],
        "A7" : ["*", 1, 7],
        "A8" : ["*", 1, 8],
        "A9" : ["*", 1, 9],
        "A10" : ["*", 1, 10],
        "B1" : ["*", 2, 1],
        "B2" : ["*", 2, 2],
        "B3" : ["*", 2, 3],
        "B4" : ["*", 2, 4],
        "B5" : ["*", 2, 5],
        "B6" : ["*", 2, 6],
        "B7" : ["*", 2, 7],
        "B8" : ["*", 2, 8],
        "B9" : ["*", 2, 9],
        "B10" : ["*", 2, 10],
        "C1" : ["*", 3, 1],
        "C2" : ["*", 3, 2],
        "C3" : ["*", 3, 3],
        "C4" : ["*", 3, 4],
        "C5" : ["*", 3, 5],
        "C6" : ["*", 3, 6],
        "C7" : ["*", 3, 7],
        "C8" : ["*", 3, 8],
        "C9" : ["*", 3, 9],
        "C10" : ["*", 3, 10],
        "D1" : ["*", 4, 1],
        "D2" : ["*", 4, 2],
        "D3" : ["*", 4, 3],
        "D4" : ["*", 4, 4],
        "D5" : ["*", 4, 5],
        "D6" : ["*", 4, 6],
        "D7" : ["*", 4, 7],
        "D8" : ["*", 4, 8],
        "D9" : ["*", 4, 9],
        "D10" : ["*", 4, 10],
        "E1" : ["*", 5, 1],
        "E2" : ["*", 5, 2],
        "E3" : ["*", 5, 3],
        "E4" : ["*", 5, 4],
        "E5" : ["*", 5, 5],
        "E6" : ["*", 5, 6],
        "E7" : ["*", 5, 7],
        "E8" : ["*", 5, 8],
        "E9" : ["*", 5, 9],
        "E10" : ["*", 5, 10],
        "F1" : ["*", 6, 1],
        "F2" : ["*", 6, 2],
        "F3" : ["*", 6, 3],
        "F4" : ["*", 6, 4],
        "F5" : ["*", 6, 5],
        "F6" : ["*", 6, 6],
        "F7" : ["*", 6, 7],
        "F8" : ["*", 6, 8],
        "F9" : ["*", 6, 9],
        "F10" : ["*", 6, 10],
        "G1" : ["*", 7, 1],
        "G2" : ["*", 7, 2],
        "G3" : ["*", 7, 3],
        "G4" : ["*", 7, 4],
        "G5" : ["*", 7, 5],
        "G6" : ["*", 7, 6],
        "G7" : ["*", 7, 7],
        "G8" : ["*", 7, 8],
        "G9" : ["*", 7, 9],
        "G10" : ["*", 7, 10],
        "H1" : ["*", 8, 1],
        "H2" : ["*", 8, 2],
        "H3" : ["*", 8, 3],
        "H4" : ["*", 8, 4],
        "H5" : ["*", 8, 5],
        "H6" : ["*", 8, 6],
        "H7" : ["*", 8, 7],
        "H8" : ["*", 8, 8],
        "H9" : ["*", 8, 9],
        "H10" : ["*", 8, 10],
        "I1" : ["*", 9, 1],
        "I2" : ["*", 9, 2],
        "I3" : ["*", 9, 3],
        "I4" : ["*", 9, 4],
        "I5" : ["*", 9, 5],
        "I6" : ["*", 9, 6],
        "I7" : ["*", 9, 7],
        "I8" : ["*", 9, 8],
        "I9" : ["*", 9, 9],
        "I10" : ["*", 9, 10],
        "J1" : ["*", 10, 1],
        "J2" : ["*", 10, 2],
        "J3" : ["*", 10, 3],
        "J4" : ["*", 10, 4],
        "J5" : ["*", 10, 5],
        "J6" : ["*", 10, 6],
        "J7" : ["*", 10, 7],
        "J8" : ["*", 10, 8],
        "J9" : ["*", 10, 9],
        "J10" : ["*", 10, 10]}

tabP2 = {
        "A1" : ["*", 1, 1],
        "A2" : ["*", 1, 2],
        "A3" : ["*", 1, 3],
        "A4" : ["*", 1, 4],
        "A5" : ["*", 1, 5],
        "A6" : ["*", 1, 6],
        "A7" : ["*", 1, 7],
        "A8" : ["*", 1, 8],
        "A9" : ["*", 1, 9],
        "A10" : ["*", 1, 10],
        "B1" : ["*", 2, 1],
        "B2" : ["*", 2, 2],
        "B3" : ["*", 2, 3],
        "B4" : ["*", 2, 4],
        "B5" : ["*", 2, 5],
        "B6" : ["*", 2, 6],
        "B7" : ["*", 2, 7],
        "B8" : ["*", 2, 8],
        "B9" : ["*", 2, 9],
        "B10" : ["*", 2, 10],
        "C1" : ["*", 3, 1],
        "C2" : ["*", 3, 2],
        "C3" : ["*", 3, 3],
        "C4" : ["*", 3, 4],
        "C5" : ["*", 3, 5],
        "C6" : ["*", 3, 6],
        "C7" : ["*", 3, 7],
        "C8" : ["*", 3, 8],
        "C9" : ["*", 3, 9],
        "C10" : ["*", 3, 10],
        "D1" : ["*", 4, 1],
        "D2" : ["*", 4, 2],
        "D3" : ["*", 4, 3],
        "D4" : ["*", 4, 4],
        "D5" : ["*", 4, 5],
        "D6" : ["*", 4, 6],
        "D7" : ["*", 4, 7],
        "D8" : ["*", 4, 8],
        "D9" : ["*", 4, 9],
        "D10" : ["*", 4, 10],
        "E1" : ["*", 5, 1],
        "E2" : ["*", 5, 2],
        "E3" : ["*", 5, 3],
        "E4" : ["*", 5, 4],
        "E5" : ["*", 5, 5],
        "E6" : ["*", 5, 6],
        "E7" : ["*", 5, 7],
        "E8" : ["*", 5, 8],
        "E9" : ["*", 5, 9],
        "E10" : ["*", 5, 10],
        "F1" : ["*", 6, 1],
        "F2" : ["*", 6, 2],
        "F3" : ["*", 6, 3],
        "F4" : ["*", 6, 4],
        "F5" : ["*", 6, 5],
        "F6" : ["*", 6, 6],
        "F7" : ["*", 6, 7],
        "F8" : ["*", 6, 8],
        "F9" : ["*", 6, 9],
        "F10" : ["*", 6, 10],
        "G1" : ["*", 7, 1],
        "G2" : ["*", 7, 2],
        "G3" : ["*", 7, 3],
        "G4" : ["*", 7, 4],
        "G5" : ["*", 7, 5],
        "G6" : ["*", 7, 6],
        "G7" : ["*", 7, 7],
        "G8" : ["*", 7, 8],
        "G9" : ["*", 7, 9],
        "G10" : ["*", 7, 10],
        "H1" : ["*", 8, 1],
        "H2" : ["*", 8, 2],
        "H3" : ["*", 8, 3],
        "H4" : ["*", 8, 4],
        "H5" : ["*", 8, 5],
        "H6" : ["*", 8, 6],
        "H7" : ["*", 8, 7],
        "H8" : ["*", 8, 8],
        "H9" : ["*", 8, 9],
        "H10" : ["*", 8, 10],
        "I1" : ["*", 9, 1],
        "I2" : ["*", 9, 2],
        "I3" : ["*", 9, 3],
        "I4" : ["*", 9, 4],
        "I5" : ["*", 9, 5],
        "I6" : ["*", 9, 6],
        "I7" : ["*", 9, 7],
        "I8" : ["*", 9, 8],
        "I9" : ["*", 9, 9],
        "I10" : ["*", 9, 10],
        "J1" : ["*", 10, 1],
        "J2" : ["*", 10, 2],
        "J3" : ["*", 10, 3],
        "J4" : ["*", 10, 4],
        "J5" : ["*", 10, 5],
        "J6" : ["*", 10, 6],
        "J7" : ["*", 10, 7],
        "J8" : ["*", 10, 8],
        "J9" : ["*", 10, 9],
        "J10" : ["*", 10, 10]}

#Fonctions

#Création des deux tableaux personnalisables pour les deux joueurs
def createBoardPlayer1():
    """
    Cette fonction permet de créer le tableau du joueur 1.
    """
    A1=["*", 1, 1]
    A2=["*", 1, 2]
    A3=["*", 1, 3]
    A4=["*", 1, 4]
    A5=["*", 1, 5]
    A6=["*", 1, 6]
    A7=["*", 1, 7]
    A8=["*", 1, 8]
    A9=["*", 1, 9]
    A10=["*", 1, 10]
    B1=["*", 2, 1]
    B2=["*", 2, 2]
    B3=["*", 2, 3]
    B4=["*", 2, 4]
    B5=["*", 2, 5]
    B6=["*", 2, 6]
    B7=["*", 2, 7]
    B8=["*", 2, 8]
    B9=["*", 2, 9]
    B10=["*", 2, 10]
    C1=["*", 3, 1]
    C2=["*", 3, 2]
    C3=["*", 3, 3]
    C4=["*", 3, 4]
    C5=["*", 3, 5]
    C6=["*", 3, 6]
    C7=["*", 3, 7]
    C8=["*", 3, 8]
    C9=["*", 3, 9]
    C10=["*", 3, 10]
    D1=["*", 4, 1]
    D2=["*", 4, 2]
    D3=["*", 4, 3]
    D4=["*", 4, 4]
    D5=["*", 4, 5]
    D6=["*", 4, 6]
    D7=["*", 4, 7]
    D8=["*", 4, 8]
    D9=["*", 4, 9]
    D10=["*", 4, 10]
    E1=["*", 5, 1]
    E2=["*", 5, 2]
    E3=["*", 5, 3]
    E4=["*", 5, 4]
    E5=["*", 5, 5]
    E6=["*", 5, 6]
    E7=["*", 5, 7]
    E8=["*", 5, 8]
    E9=["*", 5, 9]
    E10=["*", 5, 10]
    F1=["*", 6, 1]
    F2=["*", 6, 2]
    F3=["*", 6, 3]
    F4=["*", 6, 4]
    F5=["*", 6, 5]
    F6=["*", 6, 6]
    F7=["*", 6, 7]
    F8=["*", 6, 8]
    F9=["*", 6, 9]
    F10=["*", 6, 10]
    G1=["*", 7, 1]
    G2=["*", 7, 2]
    G3=["*", 7, 3]
    G4=["*", 7, 4]
    G5=["*", 7, 5]
    G6=["*", 7, 6]
    G7=["*", 7, 7]
    G8=["*", 7, 8]
    G9=["*", 7, 9]
    G10=["*", 7, 10]
    H1=["*", 8, 1]
    H2=["*", 8, 2]
    H3=["*", 8, 3]
    H4=["*", 8, 4]
    H5=["*", 8, 5]
    H6=["*", 8, 6]
    H7=["*", 8, 7]
    H8=["*", 8, 8]
    H9=["*", 8, 9]
    H10=["*", 8, 10]
    I1=["*", 9, 1]
    I2=["*", 9, 2]
    I3=["*", 9, 3]
    I4=["*", 9, 4]
    I5=["*", 9, 5]
    I6=["*", 9, 6]
    I7=["*", 9, 7]
    I8=["*", 9, 8]
    I9=["*", 9, 9]
    I10=["*", 9, 10]
    J1=["*", 10, 1]
    J2=["*", 10, 2]
    J3=["*", 10, 3]
    J4=["*", 10, 4]
    J5=["*", 10, 5]
    J6=["*", 10, 6]
    J7=["*", 10, 7]
    J8=["*", 10, 8]
    J9=["*", 10, 9]
    J10=["*", 10, 10]

    print("Table du joueur 1")
    print(" ",1,A1[0],B1[0],C1[0],D1[0],E1[0],F1[0],G1[0],H1[0],I1[0],J1[0])
    print(" ",2,A2[0],B2[0],C2[0],D2[0],E2[0],F2[0],G2[0],H2[0],I2[0],J2[0])
    print(" ",3,A3[0],B3[0],C3[0],D3[0],E3[0],F3[0],G3[0],H3[0],I3[0],J3[0])
    print(" ",4,A4[0],B4[0],C4[0],D4[0],E4[0],F4[0],G4[0],H4[0],I4[0],J4[0])
    print(" ",5,A5[0],B5[0],C5[0],D5[0],E5[0],F5[0],G5[0],H5[0],I5[0],J5[0])
    print(" ",6,A6[0],B6[0],C6[0],D6[0],E6[0],F6[0],G6[0],H6[0],I6[0],J6[0])
    print(" ",7,A7[0],B7[0],C7[0],D7[0],E7[0],F7[0],G7[0],H7[0],I7[0],J7[0])
    print(" ",8,A8[0],B8[0],C8[0],D8[0],E8[0],F8[0],G8[0],H8[0],I8[0],J8[0])
    print(" ",9,A9[0],B9[0],C9[0],D9[0],E9[0],F9[0],G9[0],H9[0],I9[0],J9[0])
    print("",10,A10[0],B10[0],C10[0],D10[0],E10[0],F10[0],G10[0],H10[0],I10[0],J10[0])
    print(" "," ","A","B","C","D","E","F","G","H","I","J")
    print("---------------------------------------")


    liste_case=["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
    liste_case_pour_ordi=liste_case
    copy_list=liste_case

    #Placement des bateaux
    porte_avion=["","","","",""]
    croiseur=["","","",""]
    contre_torpilleur=["","",""]
    sous_marin=["","",""]
    torpilleur=["",""]
    n=0
    bateau_place=0
    bateaux=["PORTE AVION","CROISEUR","CONTRE TORPILLEUR","SOUS MARIN","TORPILLEUR"]
    case=0
    print("Vous pouvez uniquement mettre les bateaux en ligne ou en colonne. Pas en diagonale. Et vous n'avez pas le droit de mettre 2 cases trop éloigné.")
    print("Voici la liste des bateaux disponibles : ")
    print(colored('PORTE AVION (5 cases), CROISEUR (4), CONTRE TORPILLEUR (3), SOUS MARIN (3), TORPILLEUR (2)', 'blue'))
    print("Un dernier conseil, restez en majuscule bloqué pour les bateaux et les cases de la forme : xy (exemple : A1)")
    while bateau_place<5:
        bateau=input('Quel bateau voulez vous placer ? ')
        if bateau not in bateaux:
            print("Vous avez déjà placé se bateau ")
            continue
        if bateau=='PORTE AVION':
            while case<5:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise")
                    continue
                porte_avion[n]=ask
                n += 1
                case += 1
            a=porte_avion[0]
            b=porte_avion[1]
            c=porte_avion[2]
            d=porte_avion[3]
            e=porte_avion[4]
            if a[0]==b[0] and a[0]==c[0] and a[0]==d[0] and a[0]==e[0]:
                print('Votre bateau a été placé')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if a[1]==b[1] and b[1]==c[1] and c[1]==d[1] and d[1]==e[1]:
                print('Votre bateau a été placé')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça')
                porte_avion=["","","","",""]
            continue
        if bateau=='CROISEUR':
            while case<4:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise ")
                    continue
                croiseur[n]=ask
                n += 1
                case += 1
            x=croiseur[0]
            y=croiseur[1]
            z=croiseur[2]
            w=croiseur[3]
            if x[0]==y[0] and y[0]==z[0] and z[0]==w[0]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if x[1]==y[1] and y[1]==z[1] and z[1]==w[1]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça ')
                croiseur=["","","",""]
            continue
        if bateau=='CONTRE TORPILLEUR':
            while case<3:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise ")
                    continue
                contre_torpilleur[n]=ask
                n += 1
                case += 1
            p=contre_torpilleur[0]
            m=contre_torpilleur[1]
            k=contre_torpilleur[2]
            if p[0]==m[0] and m[0]==k[0]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if p[1]==m[1] and m[1]==k[1]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça ')
                contre_torpilleur=["","",""]
            continue
        if bateau=='SOUS MARIN':
            while case<3:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise ")
                    continue
                sous_marin[n]=ask
                n += 1
                case += 1
            o=sous_marin[0]
            i=sous_marin[1]
            u=sous_marin[2]
            if o[0]==i[0] and i[0]==u[0]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if o[1]==i[1] and i[1]==u[1]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça')
                sous_marin=["","",""]
            continue
        if bateau=='TORPILLEUR':
            while case<2:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise ")
                    continue
                torpilleur[n]=ask
                n += 1
                case += 1
            l=torpilleur[0]
            f=torpilleur[1]
            if l[0]==f[0]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if l[1]==f[1]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça ')
                torpilleur=["",""]
            continue
    print(chr(27) + "[2J")
    return [porte_avion, croiseur, contre_torpilleur, sous_marin, torpilleur]
    
def createBoardPlayer2():
    """
    Cette fonction permet de créer le tableau du joueur 2.
    """
    A1=["*", 1, 1]
    A2=["*", 1, 2]
    A3=["*", 1, 3]
    A4=["*", 1, 4]
    A5=["*", 1, 5]
    A6=["*", 1, 6]
    A7=["*", 1, 7]
    A8=["*", 1, 8]
    A9=["*", 1, 9]
    A10=["*", 1, 10]
    B1=["*", 2, 1]
    B2=["*", 2, 2]
    B3=["*", 2, 3]
    B4=["*", 2, 4]
    B5=["*", 2, 5]
    B6=["*", 2, 6]
    B7=["*", 2, 7]
    B8=["*", 2, 8]
    B9=["*", 2, 9]
    B10=["*", 2, 10]
    C1=["*", 3, 1]
    C2=["*", 3, 2]
    C3=["*", 3, 3]
    C4=["*", 3, 4]
    C5=["*", 3, 5]
    C6=["*", 3, 6]
    C7=["*", 3, 7]
    C8=["*", 3, 8]
    C9=["*", 3, 9]
    C10=["*", 3, 10]
    D1=["*", 4, 1]
    D2=["*", 4, 2]
    D3=["*", 4, 3]
    D4=["*", 4, 4]
    D5=["*", 4, 5]
    D6=["*", 4, 6]
    D7=["*", 4, 7]
    D8=["*", 4, 8]
    D9=["*", 4, 9]
    D10=["*", 4, 10]
    E1=["*", 5, 1]
    E2=["*", 5, 2]
    E3=["*", 5, 3]
    E4=["*", 5, 4]
    E5=["*", 5, 5]
    E6=["*", 5, 6]
    E7=["*", 5, 7]
    E8=["*", 5, 8]
    E9=["*", 5, 9]
    E10=["*", 5, 10]
    F1=["*", 6, 1]
    F2=["*", 6, 2]
    F3=["*", 6, 3]
    F4=["*", 6, 4]
    F5=["*", 6, 5]
    F6=["*", 6, 6]
    F7=["*", 6, 7]
    F8=["*", 6, 8]
    F9=["*", 6, 9]
    F10=["*", 6, 10]
    G1=["*", 7, 1]
    G2=["*", 7, 2]
    G3=["*", 7, 3]
    G4=["*", 7, 4]
    G5=["*", 7, 5]
    G6=["*", 7, 6]
    G7=["*", 7, 7]
    G8=["*", 7, 8]
    G9=["*", 7, 9]
    G10=["*", 7, 10]
    H1=["*", 8, 1]
    H2=["*", 8, 2]
    H3=["*", 8, 3]
    H4=["*", 8, 4]
    H5=["*", 8, 5]
    H6=["*", 8, 6]
    H7=["*", 8, 7]
    H8=["*", 8, 8]
    H9=["*", 8, 9]
    H10=["*", 8, 10]
    I1=["*", 9, 1]
    I2=["*", 9, 2]
    I3=["*", 9, 3]
    I4=["*", 9, 4]
    I5=["*", 9, 5]
    I6=["*", 9, 6]
    I7=["*", 9, 7]
    I8=["*", 9, 8]
    I9=["*", 9, 9]
    I10=["*", 9, 10]
    J1=["*", 10, 1]
    J2=["*", 10, 2]
    J3=["*", 10, 3]
    J4=["*", 10, 4]
    J5=["*", 10, 5]
    J6=["*", 10, 6]
    J7=["*", 10, 7]
    J8=["*", 10, 8]
    J9=["*", 10, 9]
    J10=["*", 10, 10]

    print("Table du joueur 2")
    print(" ",1,A1[0],B1[0],C1[0],D1[0],E1[0],F1[0],G1[0],H1[0],I1[0],J1[0])
    print(" ",2,A2[0],B2[0],C2[0],D2[0],E2[0],F2[0],G2[0],H2[0],I2[0],J2[0])
    print(" ",3,A3[0],B3[0],C3[0],D3[0],E3[0],F3[0],G3[0],H3[0],I3[0],J3[0])
    print(" ",4,A4[0],B4[0],C4[0],D4[0],E4[0],F4[0],G4[0],H4[0],I4[0],J4[0])
    print(" ",5,A5[0],B5[0],C5[0],D5[0],E5[0],F5[0],G5[0],H5[0],I5[0],J5[0])
    print(" ",6,A6[0],B6[0],C6[0],D6[0],E6[0],F6[0],G6[0],H6[0],I6[0],J6[0])
    print(" ",7,A7[0],B7[0],C7[0],D7[0],E7[0],F7[0],G7[0],H7[0],I7[0],J7[0])
    print(" ",8,A8[0],B8[0],C8[0],D8[0],E8[0],F8[0],G8[0],H8[0],I8[0],J8[0])
    print(" ",9,A9[0],B9[0],C9[0],D9[0],E9[0],F9[0],G9[0],H9[0],I9[0],J9[0])
    print("",10,A10[0],B10[0],C10[0],D10[0],E10[0],F10[0],G10[0],H10[0],I10[0],J10[0])
    print(" "," ","A","B","C","D","E","F","G","H","I","J")
    print("---------------------------------------")


    liste_case=["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
    liste_case_pour_ordi=liste_case
    copy_list=liste_case

    #Placement des bateaux
    porte_avion=["","","","",""]
    croiseur=["","","",""]
    contre_torpilleur=["","",""]
    sous_marin=["","",""]
    #La ligne diabolique
    torpilleur=["",""]
    n=0
    bateau_place=0
    bateaux=["PORTE AVION","CROISEUR","CONTRE TORPILLEUR","SOUS MARIN","TORPILLEUR"]
    case=0
    print("Vous pouvez uniquement mettre les bateaux en ligne ou en colonne. Pas en diagonale. Et vous n'avez pas le droit de mettre 2 cases trop éloigné.")
    print("Voici la liste des bateaux disponibles : ")
    print(colored('PORTE AVION (5 cases), CROISEUR (4), CONTRE TORPILLEUR (3), SOUS MARIN (3), TORPILLEUR (2)', 'blue'))
    print("Un dernier conseil, restez en majuscule bloqué pour les bateaux et les cases de la forme : xy (exemple : A1)")
    while bateau_place<5:
        bateau=input('Quel bateau voulez vous placer ? ')
        if bateau not in bateaux:
            print("Vous avez déjà placé se bateau ")
            continue
        if bateau=='PORTE AVION':
            while case<5:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise")
                    continue
                porte_avion[n]=ask
                n += 1
                case += 1
            a=porte_avion[0]
            b=porte_avion[1]
            c=porte_avion[2]
            d=porte_avion[3]
            e=porte_avion[4]
            if a[0]==b[0] and a[0]==c[0] and a[0]==d[0] and a[0]==e[0]:
                print('Votre bateau a été placé')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if a[1]==b[1] and b[1]==c[1] and c[1]==d[1] and d[1]==e[1]:
                print('Votre bateau a été placé')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça')
                porte_avion=["","","","",""]
            continue
        if bateau=='CROISEUR':
            while case<4:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise ")
                    continue
                croiseur[n]=ask
                n += 1
                case += 1
            x=croiseur[0]
            y=croiseur[1]
            z=croiseur[2]
            w=croiseur[3]
            if x[0]==y[0] and y[0]==z[0] and z[0]==w[0]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if x[1]==y[1] and y[1]==z[1] and z[1]==w[1]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça ')
                croiseur=["","","",""]
            continue
        if bateau=='CONTRE TORPILLEUR':
            while case<3:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise ")
                    continue
                contre_torpilleur[n]=ask
                n += 1
                case += 1
            p=contre_torpilleur[0]
            m=contre_torpilleur[1]
            k=contre_torpilleur[2]
            if p[0]==m[0] and m[0]==k[0]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if p[1]==m[1] and m[1]==k[1]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça ')
                contre_torpilleur=["","",""]
            continue
        if bateau=='SOUS MARIN':
            while case<3:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise ")
                    continue
                sous_marin[n]=ask
                n += 1
                case += 1
            o=sous_marin[0]
            i=sous_marin[1]
            u=sous_marin[2]
            if o[0]==i[0] and i[0]==u[0]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if o[1]==i[1] and i[1]==u[1]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça')
                sous_marin=["","",""]
            continue
        if bateau=='TORPILLEUR':
            while case<2:
                ask=input('Quelle case voulez vous ? ')
                if ask in copy_list:
                    copy_list.remove(ask)
                else:
                    print("Cette case est déjà prise ")
                    continue
                torpilleur[n]=ask
                n += 1
                case += 1
            l=torpilleur[0]
            f=torpilleur[1]
            if l[0]==f[0]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
                continue
            if l[1]==f[1]:
                print('Votre bateau a été placé ')
                case=0
                n=0
                bateaux.remove(bateau)
                bateau_place += 1
            else:
                print('Vous ne pouvez pas mettre votre bateau comme ça ')
                torpilleur=["",""]
            continue
    print(chr(27) + "[2J")
    return [porte_avion, croiseur, contre_torpilleur, sous_marin, torpilleur]
   
#Affiche ces tableaux en question, en reprenant les variables de tabP1 et tabP2
def showBoard1() :
    """
    Cette fonction affiche le tableau du joueur, si la case contient un * on a pas encore tiré à cette case, 0 correspond à une case vide et 1 à une case avec un bateau.
    """
    print("Table du joueur 1")
    print(" ",1,tabP1["A1"][0],tabP1["B1"][0],tabP1["C1"][0],tabP1["D1"][0],tabP1["E1"][0],tabP1["F1"][0],tabP1["G1"][0],tabP1["H1"][0],tabP1["I1"][0],tabP1["J1"][0])
    print(" ",2,tabP1["A2"][0],tabP1["B2"][0],tabP1["C2"][0],tabP1["D2"][0],tabP1["E2"][0],tabP1["F2"][0],tabP1["G2"][0],tabP1["H2"][0],tabP1["I2"][0],tabP1["J2"][0])
    print(" ",3,tabP1["A3"][0],tabP1["B3"][0],tabP1["C3"][0],tabP1["D3"][0],tabP1["E3"][0],tabP1["F3"][0],tabP1["G3"][0],tabP1["H3"][0],tabP1["I3"][0],tabP1["J3"][0])
    print(" ",4,tabP1["A4"][0],tabP1["B4"][0],tabP1["C4"][0],tabP1["D4"][0],tabP1["E4"][0],tabP1["F4"][0],tabP1["G4"][0],tabP1["H4"][0],tabP1["I4"][0],tabP1["J4"][0])
    print(" ",5,tabP1["A5"][0],tabP1["B5"][0],tabP1["C5"][0],tabP1["D5"][0],tabP1["E5"][0],tabP1["F5"][0],tabP1["G5"][0],tabP1["H5"][0],tabP1["I5"][0],tabP1["J5"][0])
    print(" ",6,tabP1["A6"][0],tabP1["B6"][0],tabP1["C6"][0],tabP1["D6"][0],tabP1["E6"][0],tabP1["F6"][0],tabP1["G6"][0],tabP1["H6"][0],tabP1["I6"][0],tabP1["J6"][0])
    print(" ",7,tabP1["A7"][0],tabP1["B7"][0],tabP1["C7"][0],tabP1["D7"][0],tabP1["E7"][0],tabP1["F7"][0],tabP1["G7"][0],tabP1["H7"][0],tabP1["I7"][0],tabP1["J7"][0])
    print(" ",8,tabP1["A8"][0],tabP1["B8"][0],tabP1["C8"][0],tabP1["D8"][0],tabP1["E8"][0],tabP1["F8"][0],tabP1["G8"][0],tabP1["H8"][0],tabP1["I8"][0],tabP1["J8"][0])
    print(" ",9,tabP1["A9"][0],tabP1["B9"][0],tabP1["C9"][0],tabP1["D9"][0],tabP1["E9"][0],tabP1["F9"][0],tabP1["G9"][0],tabP1["H9"][0],tabP1["I9"][0],tabP1["J9"][0])
    print("",10,tabP1["A10"][0],tabP1["B10"][0],tabP1["C10"][0],tabP1["D10"][0],tabP1["E10"][0],tabP1["F10"][0],tabP1["G10"][0],tabP1["H10"][0],tabP1["I10"][0],tabP1["J10"][0])
    print(" "," ","A","B","C","D","E","F","G","H","I","J")
    print("---------------------------------------")
    
def showBoard2() :
    """
    Excusez moi mais là c'est du radotage ! J'ai déjà dit ce qui vous intéresse dans showBoard1 !
    """
    print("Table du joueur 2")
    print(" ",1,tabP2["A1"][0],tabP2["B1"][0],tabP2["C1"][0],tabP2["D1"][0],tabP2["E1"][0],tabP2["F1"][0],tabP2["G1"][0],tabP2["H1"][0],tabP2["I1"][0],tabP2["J1"][0])
    print(" ",2,tabP2["A2"][0],tabP2["B2"][0],tabP2["C2"][0],tabP2["D2"][0],tabP2["E2"][0],tabP2["F2"][0],tabP2["G2"][0],tabP2["H2"][0],tabP2["I2"][0],tabP2["J2"][0])
    print(" ",3,tabP2["A3"][0],tabP2["B3"][0],tabP2["C3"][0],tabP2["D3"][0],tabP2["E3"][0],tabP2["F3"][0],tabP2["G3"][0],tabP2["H3"][0],tabP2["I3"][0],tabP2["J3"][0])
    print(" ",4,tabP2["A4"][0],tabP2["B4"][0],tabP2["C4"][0],tabP2["D4"][0],tabP2["E4"][0],tabP2["F4"][0],tabP2["G4"][0],tabP2["H4"][0],tabP2["I4"][0],tabP2["J4"][0])
    print(" ",5,tabP2["A5"][0],tabP2["B5"][0],tabP2["C5"][0],tabP2["D5"][0],tabP2["E5"][0],tabP2["F5"][0],tabP2["G5"][0],tabP2["H5"][0],tabP2["I5"][0],tabP2["J5"][0])
    print(" ",6,tabP2["A6"][0],tabP2["B6"][0],tabP2["C6"][0],tabP2["D6"][0],tabP2["E6"][0],tabP2["F6"][0],tabP2["G6"][0],tabP2["H6"][0],tabP2["I6"][0],tabP2["J6"][0])
    print(" ",7,tabP2["A7"][0],tabP2["B7"][0],tabP2["C7"][0],tabP2["D7"][0],tabP2["E7"][0],tabP2["F7"][0],tabP2["G7"][0],tabP2["H7"][0],tabP2["I7"][0],tabP2["J7"][0])
    print(" ",8,tabP2["A8"][0],tabP2["B8"][0],tabP2["C8"][0],tabP2["D8"][0],tabP2["E8"][0],tabP2["F8"][0],tabP2["G8"][0],tabP2["H8"][0],tabP2["I8"][0],tabP2["J8"][0])
    print(" ",9,tabP2["A9"][0],tabP2["B9"][0],tabP2["C9"][0],tabP2["D9"][0],tabP2["E9"][0],tabP2["F9"][0],tabP2["G9"][0],tabP2["H9"][0],tabP2["I9"][0],tabP2["J9"][0])
    print("",10,tabP2["A10"][0],tabP2["B10"][0],tabP2["C10"][0],tabP2["D10"][0],tabP2["E10"][0],tabP2["F10"][0],tabP2["G10"][0],tabP2["H10"][0],tabP2["I10"][0],tabP2["J10"][0])
    print(" "," ","A","B","C","D","E","F","G","H","I","J")
    print("---------------------------------------")
     
#Permettra à chaque joueur de jouer.
def shootPlayer1():
    """
    Prenez place dans le centre tactique opérationnel Mon Commandant !
    Vous devez rentrer des commandes de la forme A1, J10... pour attaquer. 
    Soyez stratégique sinon vous perdrez du temps, voire même la guerre.
    """
    squarePlayer1 = input("Dans quel case voulez vous tirer {} ?".format(P1))
    for i in listeBateauxPlayer2:  # Trouver la case dans sunk puis la supprimer puis remplacer le * par 1.
        for j in i:
            if squarePlayer1 == j:
                i.remove(squarePlayer1)
                tabP2[squarePlayer1][0] = "1"
                global shootP1
                shootP1 = shootP1 + 1
                return 
            else:  # Remplacer par 0
                tabP2[squarePlayer1][0] = "0"
                global missP1 
                missP1 = missP1 +1
                
def shootPlayer2():
    """
    D'ici vous pourrez les bombarder Leader Suprême !
    Vous devez rentrer des commandes de la forme A1, J10... pour attaquer. 
    Soyez stratégique sinon vous perdrez du temps, voire même la guerre.
    """
    squarePlayer2 = input("Dans quel case voulez vous tirer {} ?".format(P2))
    for i in listeBateauxPlayer1:  # Trouver la case dans sunk puis la supprimer puis remplacer le * par 1.
        for j in i:
            if squarePlayer2 == j:
                i.remove(squarePlayer2)
                tabP1[squarePlayer2][0] = "1"
                global shootP2 
                shootP2 = shootP2 + 1
                return
            else : #Remplacer par 0
                tabP1[squarePlayer2][0] = "0"
                global missP2 
                missP2 = missP2 + 1
                
#Assure la rotation des joueurs et vérifie qui gagne.               
def Sunk() :
    """
    Cette fonction note la position de chaque case des bateaux, elle assure le tour par tour entre les deux adversaires et annonce le gagnant.
    """
    while listeBateauxPlayer1 != [[], [], [], [], []] and listeBateauxPlayer2 != [[], [], [], [], []] :
        print(chr(27) + "[2J") #Supprime la console
        showBoard1()
        showBoard2()
        shootPlayer1()
        shootPlayer2()
        if listeBateauxPlayer1 == [[], [], [], [], []]: #Résultat de la partie
            print(colored("Le joueur 2 a gagné !", 'red'))
        else:
            print(colored("Le joueur 1 a gagné !", 'green'))                   

#Score des différentes parties faites
def Score() :
    """
    Ce bout de code créé une ligne dans le fichier scores.txt.
    """
    with open("scores.txt", "a", newline="") as scoreFile:
        scoreFileWriter = csv.writer(scoreFile)
        scoreFileWriter.writerow([P1, "coup réussi : ", shootP1, "coup raté : ", missP1, P2, "coup réussi : ", shootP2, "coup raté : ", missP2])
        scoreFile.close()
 
#Algorithme de recherche dichotomique         
def dicho():
    """Il fallait un algorithme ¯\_(ツ)_/¯"""
    x=int(input("Quel nombre voulez vous entre 0 et 10 ? "))
    global deb
    global tr
    global fin
    while tr == False and deb <= fin :
        mil = int((deb+fin)/2)
        if tab[mil] == x:
            tr == True
            print(x, " est trouvé à l'indice ", mil)
            return
        else:
            if x > tab[mil]:
                deb=mil+1
            else:fin=mil-1
    if tr==False:
        print(x, " n'est pas trouvé dans le tableau")


# dicho()
# listeBateauxPlayer1 = createBoardPlayer1()
# listeBateauxPlayer2 = createBoardPlayer2()
listeBateauxPlayer1 = [['A1', 'B1', 'C1', 'D1', 'E1'], ['A2', 'B2', 'C2', 'D2'], ['A3', 'B3', 'C3'], ['A4', 'B4', 'C4'], ['A5', 'B5']]
listeBateauxPlayer2 = [['A1', 'B1', 'C1', 'D1', 'E1'], ['A2', 'B2', 'C2', 'D2'], ['A3', 'B3', 'C3'], ['A4', 'B4', 'C4'], ['A5', 'B5']]
assert listeBateauxPlayer1 != [[], [], [], [], []], 'Il ne peut pas avoir aucun bateau'
assert listeBateauxPlayer2 != [[], [], [], [], []], 'Il ne peut pas avoir aucun bateau'
Sunk()
Score()
