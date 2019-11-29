# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 13:29:18 2019

@author: Masson Enzo
"""

class Node : #Classe Noeud 
    """
    Node class that represent nodes in rooted tree
    A node is composed of:
    - A label or list of labels of any type
    - A list of nodes, its children
    """
    
    def __init__(self, labels, children=[ ]): 
        """
        Constructeur de la classe Node
        """
        self.labels = labels
        self.children = children
    
    def content(self):
        """
        content(Node)->{Label:Any,Childrens:List[Node]}
        
        primitive qui retourne ce que contient un noeud (label et children)
        """
        return {'Label':self.labels,'Childrens':self.children} #dictionnaire qui contient label et childrens
    
    def get_Childrens(self):
         """
         get_Childrens(Node)->List[Node]
         
         méthode qui retourne la list des enfants d'un noeud
         """
         return self.content()['Childrens']
     
    def descending(self,descendance):
        """
        display_width(Node,List[Any])->List[Node]
        
        méthode qui retourne la descendance d'un noeud
        """
        for children in self.get_Childrens(): #pour chaque enfant du noeud
            descendance.append(children.labels) #on ajoute le nom de l'enfant a la list de descendance
            children.descending(descendance)  #on rappel la méthode avec l'enfant 
        return descendance #on retourne la liste de descendance
    
    def is_leaf(self):
        """
        is_leaf(Node)->Boolean
        
        retourne True si le noeud est une feuille et false sinon 
        """
        return len(self.children)==0 #si le noeud n'a pas d'enfant
        
    def degreNode(self):
        """
        degreNode(Node)->Int
        
        retourne le nombre d'enfants d'un noeud
        """
        return len(self.get_Childrens())
        
class Rtree(Node): #Class Rtree
    """
    A rooted tree is represented by its root node
    """
    
    def __init__(self, labels, children = []):
        """
        Constructeur de la classe Rtree
        """
        super().__init__(labels, children)
        
    def root(self):
        """
        root(Rtree)->Node
        
        primitive qui retourne le noeud racine d'un arbre 
        """
        return self
        
    def sub_tree(self): 
        """
        sub_tree(Rtree)->List[Rtree]
        
        primitive qui retourne la list des sous-arbres d'un arbre 
        """
        return self.children
    
    def display_depth(self,list_noeuds=[]):
        """
        display_depth(Rtree,List[Any])->List[Any]
        
        primitive qui affiche les étiquettes de l’arborescence avec un parcours en profondeur 
        """
        list_noeuds.append(self.labels)
        for i in range(len(self.children)): #pour chaque enfant 
                self.children[i].display_depth(list_noeuds)  #on rappel la fonction display_depth
        return list_noeuds

    def display_width(self,list_noeuds=[]):
        """
        display_width(Rtree,List[Any])->List[Any]
        
        primitive qui affiche les étiquettes de l’arborescence avec un parcours en largeur 
        """
        for i in range(len(self.children)):
            list_noeuds.append(self.children[i].labels)
        for i in range(len(self.children)):
            self.children[i].display_width(list_noeuds)
        return [self.labels]+list_noeuds
            
    def get_Father(self,tree):
        """
        get_Father(Rtree,Rtree)
        
        méthode qui retourne le père d'un Rtree dans un arbre donné en paramètre
        """
        for noeud in (tree.sub_tree()+[tree]):
            if self in noeud.get_Childrens():
                return noeud 
             
    def ascending(self,tree,peres):
        """
        ascending(Rtree,Rtree,List[Node])
        
        méthode qui retourne l'ascendance d'un Rtree dans un arbre 
        """
        if self.get_Father(tree) != None :  #si le noeud a un père
            peres.append(self.get_Father(tree))
            self.get_Father(tree).ascending(tree,peres)
        return peres
    
    def degreArbre(self, max_deg = 0):
        """
        degreeT(Rtree)-> Int 
        
        Méthode qui retourne le degre d'un arbre
        """
        if not len(self.children) == 0:
            for child in self.children:
                max_deg = child.degreeT(max_deg)
        if len(self.children) > max_deg: #si le noeud à plus d'enfant que le maximum detecté
            max_deg = len(self.children) #le maximum est mise à jour
        return max_deg
    
    
    def width(self,tree,max_width=0):
        """
        width(Rtree,Rtree) -> Int
        
        Méthode qui retourne la largeur d'un arbre
        """
        for noeud in (self.sub_tree()):
            if len(noeud.get_Childrens()) > max_width:
                max_width=len(noeud.get_Childrens())
            noeud.width(tree,max_width)
        return max_width
    
    
    def depth(self,deg=0):
        """
        depth(Rtree)->Int
        
        méthode qui retourne la profondeur d'un arbre 
        """
        for children in self.get_Childrens():
            deg=deg+1
            children.depth(deg)
        return deg

 
            
node3=Rtree('m')
node2=Rtree('a')
node4=Rtree('3')
node5=Rtree('3')
node6=Rtree('9')
node1=Rtree('2',[node4,node5,node6])
node0=Rtree('z',[node1,node2,node3])


print(node0.width(node0))