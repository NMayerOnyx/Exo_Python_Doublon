import os
import time

class File :

    """Classe pour fichier"""

    def __init__ (self,chemin_fichier) :
        
        nom_base = os.path.basename(chemin_fichier)
        print("Nom de base:", nom_base)
        nom, extension = os.path.splitext(nom_base)
        print("Nom:", nom)
        print("Extension:", extension)

        self.nom = nom
        self.extension = extension
        self.cheminfichier = chemin_fichier
        self.taille = None
        self.premoct = None
        self.date = None
        self.signature = None

        print("Chemin: ", chemin_fichier)
        
        
        
    def fileTaille(self,chemin_fichier):
        None
    def filePrem():
        None
    def fileDate():
        None
    def fileSign():
        None

repoSlot1 = ""
repoSlot2 = ""

def loadRepo () :
    global repoSlot1
    global repoSlot2
    selectr = input("Quel emplacement de chemin? (1 ou 2)")
    if selectr != "1" and selectr != "2" :
        print("erreur, mauvaise entrée!")
    else :
        chemin = input("Entrez le chemin du répertoire : ")
        if selectr == "1" :
            repoSlot1 = chemin
        else :
            repoSlot2 = chemin

def checkRepo (repertoire) :
    filelist = []
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            filelist.append(os.path.join(racine, fichier))
    print(filelist)
    for i in range(len(filelist)) : 
        print("loop1 :", i)
        fichier1 = File(filelist[i])
        print("+++================+++")
        for f in range(len(filelist)) :
            result = False 
            if i !=f :
                print("loop2 :", f)
                fichier2 = File(filelist[f])
                if fichier1.extension == fichier2.extension:
                    fichier1.date = os.path.getmtime(filelist[i])
                    print(fichier1.date)
                    fichier2.date = os.path.getmtime(filelist[f])
                    


        

    

def lister_fichiers_recursivement(repertoire):
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            print(os.path.join(racine, fichier))
 

repoSlot1="C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier_test"

print(repoSlot1)
checkRepo(repoSlot1)

fichiertest = File("C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier_test\\nhazrek.pdf")

fichiertest.date = os.path.getmtime(fichiertest.cheminfichier)
print(fichiertest.date)