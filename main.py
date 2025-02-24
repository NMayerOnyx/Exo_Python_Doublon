class File :
    def __init__ (self, nom, extension, taille, premocts, date, signature) :
        self.nom = nom
        self.extension = extension
        self.taille = taille
        self.premoct = premocts
        self.date = date
        self.signature = None

repoSlot1 = ""
repoSlot2 = ""

def loadRepo ():
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

loadRepo()
print(repoSlot1)
loadRepo()
print(repoSlot2)

loadRepo()