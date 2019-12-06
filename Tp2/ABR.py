# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 08:03:42 2019

@author: 33762
"""
from random import randint


#==========================Question 1=================================

class Node:
    """
    Node class that represent nodes in ABR
    A node is composed of:
    - A data (Int or List(Int))
    - A left (Node or None) the data of left is inferior of his parent's data 
    - A right (Node or None) the data of right is superior of his parent's data 
    """

#    def __init__(self, data):
#       self.data = data
#       self.left = None
#       self.right = None

    def __str__(self):
        return str(self.data)
    
#==========================Question 5=================================
    def __init__(self, data):
        """
        Constructeur de la classe Node 
        prend en paramètre soit un int soit une List de int 
        si data est une list alors l'abr créer sera équilibré
        """
       if type(data) == list: #constructeur pour une liste de int
           self.data = None
           self.left = None
           self.right = None
           listeTriee = sorted(data) #trie la liste
           self.indexMediane = int(len(listeTriee)/2) #mediane de cette liste
           if listeTriee != []:
               self.data=listeTriee[self.indexMediane]
           gauche=listeTriee[0:self.indexMediane] #ce qui est à gauche de la mediane
           droite=listeTriee[self.indexMediane+1:len(data)] #ce qui est à droite de la mediane 
           if gauche != []:
               self.left = Node(gauche) #recursif pour la partie de gauche
           if droite != []:
                self.right = Node(droite) #recursif pour la partie de droite
       elif type(data) == int: #constructeur pour un int 
            self.data = data
            self.left = None
            self.right = None
            
#==========================Question 8=================================
    def __eq__(self,other):
        """
        deux nodes sont égaux si leur data sont égales
        """
        return self.data==other.data
    
     def __lt__(self, other):
         """
         un node est inférieur à une autre si son data est inférieur à celle de l'autre
         """
         return self.data<other.data
     
        
#==========================Question 6=================================
    def add_node(self, data):
        """
        data->int
        méthode qui ajoute un noeud à un ABR 
        ATTENTION cela désequilibre l'arbre
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add_node(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add_node(data)
    
    
    def pprint(self):
        """
        méthode pour afficher du plus petit au plus grand les noeuds d'un ABR
        """
        if self.left:
            self.left.pprint()
        print(self.data)
        if self.right:
            self.right.pprint()
            
#==========================Question 7=================================            
    def equilibre(self):
        """
        méthode pour équilibrer un ABR 
        ex: à utiliser après un add_node
        """
        return Node(self.listeTriée())
        
            
#==========================Question Bonus=================================
#Retourner un liste triée comprenant tous les noeuds d'un ABR
    def listeTriée(self,res=[]):
        """
        méthode qui parcours l'arbre et qui retourne une liste triée de tous les noeuds 
        """
        if self.left:
            self.left.listeTriée()
        res.append(self.data)
        if self.right:
            self.right.listeTriée() 
        return res
            
#==========================Question 3=================================      
    def existe(self,noeudATrouver,compteur=0):
        """
        méthode qui renvoit True si l'arbre contient le noeud donné en paramètre
        false sinon 
        elle renvoie aussi le nombre d'itérations pour arriver au resultat
        """
        compteur=compteur+1;
        if self.data == noeudATrouver:
            return True,compteur 
        elif self.data>noeudATrouver:
            if self.left != None :
                return self.left.existe(noeudATrouver,compteur)
            else:
                return False,compteur
        elif self.data<noeudATrouver:
            if self.right != None :
                return self.right.existe(noeudATrouver,compteur)
            else:
                return False,compteur
         
            
def existeList(Liste,objetATrouver):
    """
    méthode qui renvoit True si une liste contient l'objet donné en paramètre
    false sinon 
    elle renvoie aussi le nombre d'itérations pour arriver au resultat
    """
    for i in range(0,len(Liste)):   
        if Liste[i]==objetATrouver:
            return True,i
    return False,len(Liste)    
    
#==========================Question 2=================================
#abr=Node(1)
#abr.add_node(2)
#abr.add_node(4)
#abr.add_node(5)
#abr.add_node(6)
#abr.add_node(7)
#abr.add_node(8)
#abr.add_node(9)


#==========================Question 4=================================
#liste = []
#for i in range(100):
#    liste.append(randint(0, 100))
#
#abrTest=Node(randint(0,100))
#for i in range(99):
#    abrTest.add_node(randint(0, 100))
#
#IntAChercher=randint(0,100)
#
#print(existeList(liste,IntAChercher))
#print(abrTest.existe(IntAChercher))
#Globalement la méthode existe trouve la réponse en beaucoup moins de coups que la méthode existeList
    

#==========================TEST=================================
abr=Node([7,2,4,1,9,6,8,5])
abr.add_node(3)
abreq=abr.equilibre()
print(abreq.right.left.left)
