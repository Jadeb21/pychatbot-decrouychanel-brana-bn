import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
def print_list(l):
    print(l)

def extraire_nom(l):
    list_nom=[]
    for i in l:
        if i[-5]<chr(90):
            list_nom.append(i[11:-5])
        else:
            list_nom.append(i[11:-4])
    for nom in list_nom :
        if list_nom.count(nom)>1:
            list_nom.remove(nom)
    list_prenom=[]
    for nom in list_nom :
        if nom == "Chirac":
            list_prenom.append("Jacques Chirac")
        elif nom == "Giscard dEstaing":
            list_prenom.append("Valéry Giscard dEstaing")
        elif nom == "Mitterrand":
            list_prenom.append("François Mitterrand")
        elif nom == "Hollande":
            list_prenom.append("François Hollande")
        elif nom == "Macron":
            list_prenom.append("Emmanuelle Macron")
        elif nom == "Sarcozy":
            list_prenom.append("Nicolas Sarcozy")
    return list_prenom

def minuscule(l):
    with open("Nomination_Chirac1.txt", "r") as f:
        for ligne in f:
            return(ligne)

def minuscule(l):

        
          # for line in list_of_files :
        #    for letter in line:
          #      letter = ord(letter)
          #  if letter > chr(97):
         #       letter = ord(letter) - 32
         #       return(letter)
         #   else:
         #       return(letter)
