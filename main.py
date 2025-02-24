import os
import time
import hashlib

class File :

    """Classe pour fichier"""

    def __init__ (self,chemin_fichier) :

        """initialisation de File, avec nom, chemin et extension"""
        
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
    """liste les fichiers d'un dossier et affiche un texte (NE PRODUIS PZS UNE LISTE)"""
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            print(os.path.join(racine, fichier))

repoSlot1 = ""
repoSlot2 = ""

def loadRepo () :
    
    '''Charge un chemin de dossier dans un des deux emplacements repoSlot'''

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

    '''Compare les fichiers d'un dossier entre eux'''

    print("\n\n\n=================REPO CHEKUP START=================\n\n\n")
    filelist = []
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            filelist.append(os.path.join(racine, fichier))
        '''Crée une liste de chemins vers les fichiers du dossier, réutiliser pour somme de taille des fichiers'''

    print("====LISTE DES FICHIERS====")
    print(filelist)
    for i in range(len(filelist)) : 
        print("+++================================+++")
        print("Fichier comparant :", i)
        fichier1 = File(filelist[i])
        print("+++================================+++")
        for f in range(len(filelist)-i) :
            f = f+i
            if i != f :
                print("===---------------===")
                print("Fichier comparé :", f)
                fichier2 = File(filelist[f])
                if fichier1.extension == fichier2.extension:
                    fichier1.date = os.path.getmtime(filelist[i])
                    print("time1 : ", fichier1.date)
                    fichier2.date = os.path.getmtime(filelist[f])
                    print("time2 : ", fichier2.date)
                    if fichier1.date == fichier2.date :
                        fichier1.taille = os.path.getsize(filelist[i])
                        '''Reutiliser pour somme de taille des fichiers, OUBLIE PAS de faire et la somme de chaque type de fichier (comme dans l'énoncé) et la somme TOTALE en meme temps'''
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
                print("===---------------===")

                '''DANS L'ORDRE, vérifie si: l'extension du fichier est la meme, la date de modification du fichier est la meme, la taille du fichier est la meme, si les 5 premiers octets sont les memes, 
                si la signature hash du fichier est le meme. Si tout est oui, le fichier est identique, sinon il est différent
                
                deux fichiers déja scannés ne se rescannerons pas.'''
                    
def checkRepoTwo (repertoire1, repertoire2) :
    print("\n\n\n=================DOUBLE REPO CHEKUP START=================\n\n\n")
    filelist1 = []
    filelist2 = []
    for racine, repertoires, fichiers in os.walk(repertoire1):
        for fichier in fichiers:
            filelist1.append(os.path.join(racine, fichier))
    print("====LISTE DES FICHIERS 1====")
    print(filelist1)

    for racine, repertoires, fichiers in os.walk(repertoire2):
        for fichier in fichiers:
            filelist2.append(os.path.join(racine, fichier))
    print("====LISTE DES FICHIERS 1====")
    print(filelist2)

    for i in range(len(filelist1)) : 
        print("+++================================+++")
        print("Fichier comparant :", i)
        fichier1 = File(filelist1[i])
        print("+++================================+++")
        for f in range(len(filelist2)) :

            print("===---------------===")
            print("Fichier comparé :", f)
            fichier2 = File(filelist2[f])
            if fichier1.extension == fichier2.extension:
                fichier1.date = os.path.getmtime(filelist1[i])
                print("time1 : ", fichier1.date)
                fichier2.date = os.path.getmtime(filelist2[f])
                print("time2 : ", fichier2.date)
                if fichier1.date == fichier2.date :
                    fichier1.taille = os.path.getsize(filelist1[i])
                    print("size1 : ", fichier1.taille)
                    fichier2.taille = os.path.getsize(filelist2[f])
                    print("size1 : ", fichier2.taille)
                    if fichier1.taille == fichier2.taille :
                        with open(filelist1[i], "rb") as g:
                            premiers_octets = g.read(5)
                        fichier1.premoct = octets_vers_chaine_hex(premiers_octets)
                        with open(filelist2[f], "rb") as g:
                            premiers_octets = g.read(5)
                        fichier2.premoct = octets_vers_chaine_hex(premiers_octets)
                        if fichier1.premoct == fichier2.premoct : 
                            fichier1.signature = calculate_md5(fichier1.cheminfichier)
                            fichier2.signature = calculate_md5(fichier2.cheminfichier)
                            if fichier1.signature == fichier2.signature :
                                print(fichier1.nom, "et", fichier2.nom, "sont identiques!!")
            else:
                print(fichier1.nom, "et", fichier2.nom, "sont différents.")
            print("===---------------===")

            '''idem du checkup précédent, sans anti répétition car les fichiers de deux dossiers différents ne peuvent pas se rescanner entre eux'''

        

    


'''Zone de TEST'''

repoSlot1="C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier_test"
repoSlot2="C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier_test_2"

print(repoSlot1)
checkRepo(repoSlot1)
checkRepoTwo(repoSlot1, repoSlot2)

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