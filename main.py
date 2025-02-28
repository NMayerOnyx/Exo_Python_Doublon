import os
import time
import hashlib
import shutil

'''-----------------Code de nicolas----------------------'''

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

        
def checkRepoDel (repertoire1, repertoire2) :
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
                                print("SUPPRESSION DU FICHIER : ", fichier2.nom)
                                os.remove(fichier2.cheminfichier)
            else:
                print(fichier1.nom, "et", fichier2.nom, "sont différents.")
            print("===---------------===")

            '''idem du checkup précédent, sans anti répétition car les fichiers de deux dossiers différents ne peuvent pas se rescanner entre eux'''



def checkRepoCopy (repertoire1, repertoire2) :
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
                if fichier1.nom == fichier2.nom:
                    if fichier1.date < fichier2.nom:
                        shutil.copy2(fichier2.cheminfichier, fichier1.cheminfichier)
                        print("Copie de : ", fichier2.nom+fichier2.extension)
                        print("Copie effectuée dans ",fichier1.cheminfichier)
                else:
                    shutil.copy2(fichier2.cheminfichier, repertoire1+"\\"+fichier2.nom+fichier2.extension)
                    print("Copie de : ", fichier2.nom+fichier2.extension)
                    print("Copie effectuée dans ",repertoire1+"\\"+fichier2.nom+fichier2.extension)
            print("===---------------===")

            '''idem du checkup précédent, sans anti répétition car les fichiers de deux dossiers différents ne peuvent pas se rescanner entre eux'''
    

def checkTailleTotale (repertoire1) :
    filelist1 = []
    tailleTotale = 0
    totalTexte = 0
    totalImage = 0
    totalVideo = 0
    totalAudio = 0
    totalAutres = 0
    for racine, repertoires, fichiers in os.walk(repertoire1):
        for fichier in fichiers:
            filelist1.append(os.path.join(racine, fichier))
    print("====LISTE DES FICHIERS 1====")
    print(filelist1)
    for i in range(len(filelist1)) : 
        print("+++================================+++")
        print("fichier testé :", i)
        fichier1 = File(filelist1[i])
        print("+++================================+++")
        fichier1.taille = os.path.getsize(filelist1[i])
        if fichier1.extension == ".txt" or fichier1.extension == ".doc" or fichier1.extension == ".docx" or fichier1.extension == ".odt" or fichier1.extension == ".csv" or fichier1.extension == ".xls" or fichier1.extension == ".tppt" or fichier1.extension == ".odp" :
            totalTexte =+ fichier1.taille
            tailleTotale = tailleTotale + fichier1.taille
        if fichier1.extension == ".jpg" or fichier1.extension == ".png" or fichier1.extension == ".bmp" or fichier1.extension == ".gif" or fichier1.extension == ".svg" :
            totalImage =+ fichier1.taille
            tailleTotale = tailleTotale + fichier1.taille
        if fichier1.extension == ".mp4" or fichier1.extension == ".avi" or fichier1.extension == ".mov" or fichier1.extension == ".mpeg" or fichier1.extension == ".wmv" :
            totalVideo =+ fichier1.taille
            tailleTotale = tailleTotale + fichier1.taille
        if fichier1.extension == ".mp3" or fichier1.extension == ".mp2" or fichier1.extension == ".wav" or fichier1.extension == ".bwf" :
            totalAudio =+ fichier1.taille
            tailleTotale = tailleTotale + fichier1.taille
        else:
            totalAutres = fichier1.taille
            tailleTotale = tailleTotale + fichier1.taille
    print("Taille totale de tous les fichiers : ", tailleTotale, "octets")
    print("Taille totale des fichiers TEXTE : ", totalTexte, "octets")
    print("Taille totale des fichiers IMAGE : ", totalImage, "octets")
    print("Taille totale des fichiers VIDEO : ", totalVideo, "octets")
    print("Taille totale des fichiers AUDIO : ", totalAudio, "octets")
    print("Taille totale des fichiers AUTRE : ", totalAutres, "octets")

'''-----------------Code de thomas----------------------'''


import datetime

class File2:
    """Classe représentant un fichier."""
    
    def __init__(self, chemin_fichier: str):
        """Initialisation avec nom, chemin, extension, taille et date de modification."""
        self.cheminfichier = chemin_fichier
        if not os.path.isfile(chemin_fichier):
            raise FileNotFoundError(f"Erreur : Le fichier '{chemin_fichier}' n'existe pas.")

        self.nom, self.extension = os.path.splitext(os.path.basename(chemin_fichier))
        self.taille = os.path.getsize(chemin_fichier)
        self.date = datetime.datetime.fromtimestamp(os.path.getmtime(chemin_fichier))

    @staticmethod
    def get_folder_size(chemin_dossier: str) -> int:
        """Calcule et retourne la taille totale d'un dossier en octets."""
        if not os.path.isdir(chemin_dossier):
            raise FileNotFoundError(f"Erreur : Le dossier '{chemin_dossier}' n'existe pas.")

        return sum(
            os.path.getsize(os.path.join(dossier_racine, fichier))
            for dossier_racine, _, fichiers in os.walk(chemin_dossier)
            for fichier in fichiers
        )

    @staticmethod
    def check_taille_totale(repertoire: str):
        """Analyse la taille des fichiers d'un dossier et les classe par type."""
        if not os.path.isdir(repertoire):
            raise FileNotFoundError(f"Erreur : Le dossier '{repertoire}' n'existe pas.")

        extensions = {
            "texte": [".txt", ".doc", ".docx", ".odt", ".csv", ".xls", ".ppt", ".odp"],
            "image": [".jpg", ".png", ".bmp", ".gif", ".svg"],
            "video": [".mp4", ".avi", ".mov", ".mpeg", ".wmv"],
            "audio": [".mp3", ".mp2", ".wav", ".bwf"],
        }

        total_sizes = {key: 0 for key in extensions}
        total_sizes["autres"] = 0
        total_general = 0

        for racine, _, fichiers in os.walk(repertoire):
            for fichier in fichiers:
                chemin_fichier = os.path.join(racine, fichier)
                extension = os.path.splitext(fichier)[1]
                taille = os.path.getsize(chemin_fichier)

                total_general += taille
                for category, ext_list in extensions.items():
                    if extension in ext_list:
                        total_sizes[category] += taille
                        break
                else:
                    total_sizes["autres"] += taille

        print("Taille totale de tous les fichiers :", total_general, "octets")
        for category, taille in total_sizes.items():
            print(f"Taille totale des fichiers {category.upper()} : {taille} octets")

    @staticmethod
    def calculate_md5(chemin_fichier: str) -> str:
        """Calcule le hash MD5 d'un fichier."""
        if not os.path.isfile(chemin_fichier):
            return "Fichier introuvable"

        hasher = hashlib.md5()
        with open(chemin_fichier, "rb") as fichier:
            for chunk in iter(lambda: fichier.read(4096), b""):
                hasher.update(chunk)

        return hasher.hexdigest()

# Exemple d'utilisation
try:
    fichiertest = File2("C:\\Users\\thomas\\OneDrive\\Documents\\Bureau\\Repositories\\Fichier_Doublon\\Exo_Python_Doublon\\main.py")

    print(f"Nom du fichier : {fichiertest.nom}")
    print(f"Extension : {fichiertest.extension}")
    print(f"Taille : {fichiertest.taille} octets")
    print(f"Dernière modification : {fichiertest.date}")

    print("Hash MD5 :", File2.calculate_md5(fichiertest.cheminfichier))
except FileNotFoundError as e:
    print(e)


'''------------------------Zone de TEST------------------------'''

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

checkTailleTotale("C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier_test")


"""checkRepoCopy ("C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier1copyme","C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier2copyme")"""
"""checkRepoDel ("C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier1delme","C:\\Users\\Nicolas\\Desktop\\repo MNS\\python_exo_doublons\\dossier2delme")"""