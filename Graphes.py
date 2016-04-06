import math


class Graphes:

    def __init__(self):
        pass

    #Permet savoir si un arc est présent entre deux sommets d’un graphe
    def isAnArc(self,matrice,x,y):
        if matrice[x][y]>0 and matrice[x][y]!=math.inf:
            return True
        else:
            return False

    #Permet d'ajouter un arc
    def addAnArc(self,matrice,x,y):
        matrice[x][y]=1

    #Permet de recopier un élément dans la matrice dans un autre élément de la matrice
    def addInMatrice(self,matrice,x,y,i):
        matrice[x][y]=matrice[x][i]

    #permet d’obtenir la matrice de fermeture transitive (G+)
    def warshall(self,matrice):
        for i in range(len(matrice)):
            for x in range(len(matrice)):
                if self.isAnArc(matrice,x,i):
                    for y in range(len(matrice)):
                        if self.isAnArc(matrice,i,y):
                            self.addAnArc(matrice,x,y)
        return matrice

    #Fermeture transitive avec matrice de routage
    def fermetureTransitiveRoutage(self,matrice):
        for i in range(len(matrice)):
            for x in range(len(matrice)):
                if self.isAnArc(matrice,x,i):
                    for y in range(len(matrice)):
                        if not self.isAnArc(matrice,x,y) and self.isAnArc(matrice,i,y):
                            self.addInMatrice(matrice,x,y,i)
        return matrice

    #Permet de choisir le meilleur point
    def chooseBest(self,distance,notUseYet):
        tempDistance = math.inf
        best = math.inf
        for i in range(len(distance)):
            if distance[i]<tempDistance and notUseYet.count(i)>0:
                tempDistance=distance[i]
                best = i
        return best

    #Permet d’obtenir tous les successeurs d’un point
    def getSuccesseurs(self,matrice,x):
        self.list = []
        for i in range(len(matrice)):
            if self.isAnArc(matrice,x,i):
                self.list.append(i)
        return self.list


    def dijkstra(self,matrice,start):
        #On considère que l'utilisateur, quand il passe les numéros de sommets de départ et d'arrivé, a pris en compte que la matrice ne commence pas à 1 mais 0
        distance = [None]*len(matrice)
        distance[start] = 0
        #Tableau avec les sommets que nous n'avons pas encore utilisés
        notUseYet = []
        #Tableau pour indiquer le prédecesseur
        pred = [None]*len(matrice)
        #Le pred du point de départ est lui même
        pred[start] = start
        #Permet d'inclure tous les points sauf celui de départ dans la liste de ceux qui ne sont pas encore utilisés et de réalisé l'initialisation de l'algorithme
        for i in range(len(matrice)):
            if i != start:
                notUseYet.append(i)
                if self.isAnArc(matrice,start,i):
                    distance[i] = matrice[start][i]
                    pred[i] = start
                else:
                    distance[i] = math.inf
        #Après initialisation, déroulement de l'algorithme
        while len(notUseYet) != 0:
            #Choisi le meilleur sommet
            t = self.chooseBest(distance,notUseYet)
            #Supprime le sommet choisi de la liste des sommes non choisis
            notUseYet.remove(t)
            #Récupére tous les successeurs
            for i in self.getSuccesseurs(matrice,t):
                temp = distance[t] + matrice[t][i]
                #Si la nouvelle distance (temp) est inférieur à celle qui nous avions dans le tableau de distance, alors on remplace et le point t devient le nouveau successeur
                if temp<distance[i]:
                    distance[i] = temp
                    pred[i] = t
        return [distance,pred]

