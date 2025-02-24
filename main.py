import os
import time
import hashlib

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

def calculate_md5(file_path):
    '''calcule le MD5 du fichier nommé file_path'''
    with open(file_path, 'rb') as f:
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()

def octets_vers_chaine_hex(octets):
    '''converti la chaine d'octets en format hexadécimal'''
    return ''.join(f'{octet:02x}' for octet in octets)

def lister_fichiers_recursivement(repertoire):
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            print(os.path.join(racine, fichier))

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
    print("=================REPO CHEKUP START=================")
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
                    print("time1 : ", fichier1.date)
                    fichier2.date = os.path.getmtime(filelist[f])
                    print("time2 : ", fichier2.date)
                    if fichier1.date == fichier2.date :
                        fichier1.taille = os.path.getsize(filelist[i])
                        print("size1 : ", fichier1.taille)
                        fichier2.taille = os.path.getsize(filelist[f])
                        print("size1 : ", fichier2.taille)
                        if fichier1.taille == fichier2.taille :
                            with open(filelist[i], "rb") as g:
                                premiers_octets = g.read(5)
                            fichier1.premoct = octets_vers_chaine_hex(premiers_octets)
                            with open(filelist[f], "rb") as g:
                                premiers_octets = g.read(5)
                            fichier2.premoct = octets_vers_chaine_hex(premiers_octets)
                            if fichier1.premoct == fichier2.premoct : 
                                fichier1.signature = calculate_md5(fichier1.cheminfichier)
                                fichier2.signature = calculate_md5(fichier2.cheminfichier)
                                if fichier1.signature == fichier2.signature :
                                    print(fichier1.nom, "et", fichier2.nom, "sont identiques!!")
                else:
                    print(fichier1.nom, "et", fichier2.nom, "sont différents.")

                    


        

    


 

repoSlot1="C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier_test"

print(repoSlot1)
checkRepo(repoSlot1)

fichiertest = File("C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier_test\\nhazrek.pdf")

fichiertest.date = os.path.getmtime(fichiertest.cheminfichier)
fichiertest.taille = os.path.getsize(fichiertest.cheminfichier)
with open(fichiertest.cheminfichier, "rb") as f:
    premiers_octets_test = f.read(5)
chaine_hex = octets_vers_chaine_hex(premiers_octets_test)



print(fichiertest.date)
print(fichiertest.taille)
print (premiers_octets_test)
print (chaine_hex)
print('hash:', calculate_md5(fichiertest.cheminfichier))