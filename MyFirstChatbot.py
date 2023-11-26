import os
from Fonction import *

directory = "./speeches"
extention = "txt"
l=list_of_files(directory, extention)
print_list(l)
list_nom = extraire_nom(l)
print(list_nom)


convert_file_lower_case(l,directory)
replacementpunctuation(l)

word_occurrences_tf(text)
idf(files_names)
TD_IDF(l)