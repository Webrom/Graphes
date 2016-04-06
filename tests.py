from Graphes import Graphes
import math

class tests:

    def __init__(self):
        pass

    def testsUnitaires(self):
        self.toExecute = Graphes()
        print("**********************************************************************")
        print("Tests Unitaires\n")
        print("Utilisation de la matrice suivante :")
        self.m = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,math.inf]]
        for x in range(0,len(self.m)):
            print(str(self.m[x]))
        print("____________________________________________________")
        print("Test de la fonction isAnArc :")
        print("Pour M[0,1]="+str(self.m[0][1])+" (devrait renvoyer true) : "+str(self.toExecute.isAnArc(self.m,0,1)))
        print("Pour M[3,3]="+str(self.m[3][3])+" (devrait renvoyer false) : "+str(self.toExecute.isAnArc(self.m,3,3)))
        print("Pour M[0,0]="+str(self.m[0][0])+" (devrait renvoyer false) : "+str(self.toExecute.isAnArc(self.m,0,0)))
        print("____________________________________________________")
        print("Test de la fonction addInMatrice :")
        print("Pour M[0,1]="+str(self.m[0][1])+" nous lui demandons de remplacer la valeur actuelle par la valeur M[0,0]")
        self.toExecute.addInMatrice(self.m,0,1,0)
        print("Résultat M[0,1]="+str(self.m[0][1]))
        print("____________________________________________________")
        print("Test de la fonction addAnArc :")
        print("Pour M[0,0]="+str(self.m[0][0])+" nous allons lui demander d'ajouter un arc")
        self.toExecute.addAnArc(self.m,0,0)
        print("Résultat M[0,0]="+str(self.m[0][0]))
        print("____________________________________________________")
        print("Test de la fonction chooseBest, pour cela nous utilisons le tableau de distance suivant :")
        self.d = [0, 2, 4, 4, 8, 7, math.inf]
        print(str(self.d))
        print("et nous considerons que les sommets non utilisés sont les suivants :")
        self.n = [3, 4, 5, 6]
        print(str(self.n))
        print("Nous éxécutons la fonction. Logiquement elle devrait nous renvoyer le sommet 3. Résultat : "+str(self.toExecute.chooseBest(self.d,self.n)))
        print("____________________________________________________")
        print("Test de la fonction getSuccesseurs, pour cela nous utilisons la matrice suivante :")
        self.m2 = [[0,2,5,4,math.inf,math.inf,math.inf],[2,0,2,math.inf,7,math.inf,math.inf],[5,2,0,1,4,3,math.inf],[4,math.inf,1,0,math.inf,4,math.inf],[math.inf,7,4,math.inf,0,1,5],[math.inf,math.inf,3,4,1,0,7],[math.inf,math.inf,math.inf,math.inf,5,7,0]]
        for x in range(0,len(self.m2)):
            print(str(self.m2[x]))
        print("Nous souhaitons obtenir les successeurs de 0 (logiquement 1,2,3) :")
        print("Résultat : "+str(self.toExecute.getSuccesseurs(self.m2,0)))


    def testWarshall(self,list):
        print("**********************************************************************")
        print("WARSHALL\n")
        print("Matrice initiale : \n")
        for x in range(0,len(list)):
            print(str(list[x]))
        self.toExecute = Graphes()
        self.result = self.toExecute.warshall(list)
        print("Après Warshall : \n")
        for x in range(0,len(self.result)):
            print(str(self.result[x]))
        print("\n")

    def testRoutage(self,list):
        print("**********************************************************************")
        print("ROUTAGE\n")
        print("Matrice initiale : \n")
        for x in range(0,len(list)):
            print(str(list[x]))
        self.toExecute = Graphes()
        self.result = self.toExecute.fermetureTransitiveRoutage(list)
        print("Après Warshall : \n")
        for x in range(0,len(self.result)):
            print(str(self.result[x]))
        print("\n")

    def testDijkstra(self,matrice,start):
        print("**********************************************************************")
        print("Dijkstra\n")
        print("Point de départ : "+str(start))
        print("Matrice initiale : \n")
        for x in range(0,len(matrice)):
            print(str(matrice[x]))
        self.toExecute = Graphes()
        self.result = self.toExecute.dijkstra(matrice,start)
        print("____________________________RESULTAT_________________________________")
        print("Distance à partir du sommet "+str(start)+" pour aller aux sommets :")
        for x in range(len(self.result[0])):
            print(str(x)+" --> "+str(self.result[0][x]))
        print("Chemin le plus court en partant du sommet "+str(start)+"  :")
        for x in range(len(self.result[1])):
            print(str(x)+" --> "+self.printChemin(self.result[1],x)+" "+str(x))

    def printChemin(self,tab,x):
        if tab[x]!=x:
            return self.printChemin(tab,tab[x])+" "+str(tab[x])
        else:
            return " "
