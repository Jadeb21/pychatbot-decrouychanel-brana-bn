
from Fonction import *
import math
import os
import string
import sys

directory = "./speeches"
extention = "txt"
l=list_of_files(directory, extention)
print_list(l)
list_nom = extraire_nom(l)
print(list_nom)


convert_file_lower_case(l,directory)


text = text(l)

tf = word_occurrences_tf(text)
idf=idf(l)
TD_IDF(l)
td_idf=TD_IDF(l)
#print(td_idf)

# Chercher les mots avec l'IDF le moins élever
td_idf_min = TD_IDF_min(td_idf)
#print(td_idf_min)

# Chercher les mots avec l'IDF le plus élevé
td_idf_max = TD_IDF_max(idf)
print(td_idf_max)

repet_chirac = repet_chirac(td_idf)
print(repet_chirac)

mot_Nation(l, idf)

menu()
affichage()
fonctionalite1 = fonctionnalite1()
if fonctionalite1 == True :
    question = question()

tk = tokenization_question(question)
print(tk)
w = word_presence(l, question)
print (w)

tf_idf_q = TF_IDF_question(tf, idf, l, question)
question_vector(tk, l)

relevancy(tf_idf_q, l)

speeches_eq(path)

response(question)

conveniency(question)

#final_answer(question, phrase)
mot_Climat(directory, l)

