# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:04:24 2019

@author: 33762
"""

#==============================ETAPE==============================
class etape:
    """
    -numero
    -date au plus tot
    -date au plus tard
    -liste de tâches
    """
    
    def __init__(self,numero,date_plus_tard,date_plus_tot,taches=[]):
        """
        constructeur de la classe etape
        """
        self.numero = numero
        self.date_plus_tard = date_plus_tard
        self.date_plus_tot = date_plus_tot
        self.taches = taches
    
    def  __str__(self):
        return self.numero
       
    def get_au_plus_tot(self):
        return self.date_plus_tot
    
    def get_au_plus_tard(self):
        return self.date_plus_tard
    
    def get_number(self):
        return self.numero
    
    def get_next_steps(self):
        res = []
        for tache in self.taches:
            res.append(tache.etape_suivante)
        return res
    
    def get_previous_steps(self,noeudAChercher):
        res = []
        liste_noeuds = self.parcourir()
        for noeud in liste_noeuds:
            if noeudAChercher in noeud.get_next_steps():
                res.append(noeud)
        return res
    
    
    def parcourir(self, liste_passage = [], liste_noeuds = []):
        liste_noeuds = [self]
        for etape in self.get_next_steps():
            if not etape in liste_passage:
                liste_passage.append(etape)
                liste_noeuds += etape.parcourir(liste_passage)
        return liste_noeuds
    
   
#==============================TACHE==============================  
class tache:
    """
    -nom 
    -duree
    -etape precedente
    -etape suivante
    """
    
    def __init__(self,nom,duree,etape_suivante=None,etape_precedente=None):
        """
        constructeur de la classe tache
        """
        self.nom = nom
        self.duree = duree
        self.etape_precedente = etape_precedente
        self.etape_suivante = etape_suivante
        
    def __str__(self):
        return self.nom

    def set_etape_pre(self,etape_pre):
        self.etape_precedente = etape_pre
        
    def get_name(self):
        return self.nom
    
    def get_duration(self):
        return self.duree
    
    def get_begin_step(self):
        return self.etape_precedente
    
    def get_end_step(self):
        return self.etape_suivante
    

#==============================MAIN==============================
def critique(pert,chemin=[]):
        chemin.append(pert)
        for etape in pert.get_next_steps():
            if not etape == None:
                if etape.get_au_plus_tard() == etape.get_au_plus_tot():
                    return critique(etape,chemin)
        if pert.get_next_steps() == []:
            return chemin  
        
#==============================TESTS==============================
        
etape8 = etape('8',220,220) 
tacheH = tache('H',10,etape8)
etape7 = etape('7',210,210,[tacheH]) 
tacheG = tache('G',60,etape7)
tacheT = tache('T',0,etape7)
tacheT2 = tache('T',0,etape7)     
etape5 = etape('5',50,210,[tacheT2]) 
etape6 = etape('6',150,150,[tacheG])    
etape3 = etape('3',150,210,[tacheT])   
tacheE = tache('E',10,etape5)
tacheF = tache('F',30,etape6)
tacheC = tache('C',30,etape3)
etape4 = etape('4',40,200,[tacheE])
etape2 = etape('2',120,120,[tacheC,tacheF])
tacheD = tache('D',10,etape4)
tacheB = tache('B',90,etape2)
etape1 = etape('1',30,30,[tacheB,tacheD])
tacheA = tache('A',30,etape1)
etape0 = etape('0',0,0,[tacheA])


tacheA.set_etape_pre(etape0)
tacheB.set_etape_pre(etape1)
tacheC.set_etape_pre(etape2)
tacheD.set_etape_pre(etape1)
tacheE.set_etape_pre(etape4)
tacheG.set_etape_pre(etape6)
tacheH.set_etape_pre(etape7)
tacheT.set_etape_pre(etape3)
tacheT2.set_etape_pre(etape5)


print(critique(etape0))