import os
from Fonction import *

directory = "./speeches"
extension = "txt"
l=list_of_files(directory, extension)
print_list(l)
list_nom = extraire_nom(l)
print(list_nom)
letter=minuscule(l)
print(letter)