import os
import math
import string
import sys
all_words = []
path = os.getcwd()
print(path)


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def print_list(l):
    print(l)


def extraire_nom(l):
    list_nom = []
    for i in l:
        if i[-5] <= chr(90):
            list_nom.append(i[11:-5])
        else:
            list_nom.append(i[11:-4])

    for nom in list_nom:
        if list_nom.count(nom) > 1:
            list_nom.remove(nom)

    list_prenom = []

    for nom in list_nom:

        if nom == "Chirac":
            list_prenom.append("Jacques Chirac")
        elif nom == "Giscard dEstaing":
            list_prenom.append("Valéry Giscard dEstaing")
        elif nom == "Hollande":
            list_prenom.append("François Hollande")
        elif nom == "Macron":
            list_prenom.append("Emmanuelle Macron")
        elif nom == "Mitterrand":
            list_prenom.append("François Mitterrand")
        elif nom == "Sarkozy":
            list_prenom.append("Nicolas Sarkozy")

    return list_prenom


def convert_file_lower_case(files_names, directory):
    for file_name in files_names:
        # Création chemin d'acces du fichier
        input_file_path = directory + '/' + file_name
        # Ouverture fichier
        with open(input_file_path, 'r') as content:
            # Création chemin ou sera rangé le fichier modifier
            output_file_path = "./cleaned" + '/' + file_name + "copie.txt"
            # Ouverture fichie copie
            with open(output_file_path, 'w') as copy:
                # modification des majusucles en miniscule
                line = content.readline()
                while line != '':
                    line_mod = ''
                    for car in line:
                        if car >= 'A' and car <= 'Z':
                            car = chr(ord(car) + 32)
                        line_mod += car
                    # Ligne transformer en minuscule réecrite dans la copie
                    copy.write(line_mod)
                    line = content.readline()


def replacementpunctuation(files_names):
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f1:
            content = f1.read()
            # définition des caractères de ponctuations
            punctuation_character = ',;:.?!""()[]*/'
            text_clean = ''
            # Verification des caractères un par un
            for car in content:
                if car in punctuation_character:
                    text_clean += ' '
                elif car == "'" or car == "-":
                    text_clean += ' '
                else:
                    text_clean += car
        with open(input_file_path, "w") as file_clean:
            file_clean.write(text_clean)  # Réecriture du texte sans ponctuaction dans le même fichier


def text(files_names):
    text = ''
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()
            text += content

    # Renvoyer le texte des fichiers convertis et sans ponctuation
    return text




def word_occurrences_tf(text):
    # Initialiser un dictionnaire pour stocker les occurrences de mots
    word_count = {}

    # Diviser le discours en série de mots
    words = text.split()

    # Compter la fréquence de chaque mot
    for word in words:
        # Mettre à jour le dictionnaire à chaque fréquence.
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Renvoyer le dictionnaire des occurrences de mots
    return word_count




def idf(files_names):
    occurence_word_all_files = {}
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()

            # Obtention du dictionnaire associant un mot au nombre de fois ou il apparait dans le fichier
            occurence_files = word_occurrences_tf(content)

            # Nous parcourons ensuite ce dictionnaire obtenus pour un fichier
            for (word, occurence) in occurence_files.items():
                if word in occurence_word_all_files:
                    # Si le mot existe deja dans le dictionnaire regroupant tous les mots des fichiers on rajoute +1 a son compteur
                    occurence_word_all_files[word] += 1
                # Sinon le mot n'existe pas déjà dans le dictionnaire alors on l'ajoute et on initialise son compteur a 1
                else:
                    occurence_word_all_files[word] = 1

    # Calculer les scores IDF pour chaque mot
    occurrence_idf = {}
    for (word, occurence) in occurence_word_all_files.items():
        # Associe pour chaque mot son score IDF en faisant le logarithme du nombre de fichier / le nombre de fois qu'il apparait dans un fichier
        occurrence_idf[word] = math.log((len(files_names) / (occurence) + 1))

    # Renvoyer le dictionnaire des scores IDF
    return occurrence_idf



def TD_IDF(files_names):
    tf_idf = []
    idf_scores = idf(files_names)

    tf_idf_row = []
    for word in idf_scores.keys():
        tf_idf_row.append(word)
    tf_idf.append(tf_idf_row)

    for file_name in files_names:
        input_files_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_files_path, 'r') as f:
            content = f.read()

            # Récupère dico tf associant a chaque mot du fichier le nombre de fois qu'il apparait
            tf_scores = word_occurrences_tf(content)

            tf_idf_row = []
            for word in idf_scores.keys():
                if word in tf_scores:
                    tf_score = tf_scores[word]
                else:
                    tf_score = 0
                idf_score = idf_scores[word]
                # Arrondie du resultat
                tf_idf_row.append(round(idf_score * tf_score, 2))
            tf_idf.append(tf_idf_row)

    # Renvoyer la matrice TF-IDF
    return tf_idf

def TD_IDF_min(td_idf):
    td_idf_min = []
    min = 0
    # Cherche les mots avec un IDF de 0
    for i in range(len(td_idf)):
        for j in range(len(td_idf[i])):
            if td_idf[i][j] == min:
                td_idf_min.append(td_idf[0][j])
                # Renvoyer la liste de mots
    td_idf_moins = set(td_idf_min)
    return td_idf_moins

def TD_IDF_max(idf):
    td_idf_max = []
    max = 0
    # Cherche l'IDF le plus élevé
    for val in idf.values() :
        #for j in range(len(idf)):
        if val > max:
            max = val


    # Cherche les mots ayant le plus grand IDF
    for i in idf.keys():
        if idf[i] == max:
            td_idf_max.append(i)
    # Renvoyer la liste de mots
    td_idf_plus = set(td_idf_max)
    return td_idf_plus


def repet_chirac(td_idf):
    most_rep =[]
    max1 = max2 = 0
    with open('./cleaned/Nomination_Chirac1.txtcopie.txt', 'r') as ch1:
        with open('./cleaned/Nomination_Chirac2.txtcopie.txt', 'r') as ch2 :
            chirac1 = ch1.read()
            chirac2 = ch2.read()

            # Chercher le Tf le plus élevé
            tf_1 = word_occurrences_tf(chirac1)
            tf_2 = word_occurrences_tf(chirac2)

            for val in tf_1.values():
                if val > max1:
                    max1 = val
            for val in tf_2.values():
                if val > max2:
                    max2 = val
            if max1 >= max2 :
                max = max1
            else:
                max = max2

            # Recherche des mots les plus fréquents
            for i in tf_1.keys():
                for j in tf_1.values():
                    if j == max:
                        most_rep.append(i)

            for i in tf_2.keys():
                for j in tf_2.values():
                    if j == max:
                        most_rep.append(i)
            non_important = list(TD_IDF_min(td_idf))

            most_repet = set(most_rep) - set(non_important)
            # Renvoyer la liste de mots
            return most_repet



def mot_Nation(files_names, idf):
    occurrences_nation = {}
    for file_name in files_names:
        input_files_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_files_path, 'r') as fn:
            content = fn.read()
            terme = "Nation"
            occurrences = word_occurrences_tf(content)
            for (terme, occurrence) in occurrences.items():
                if terme in occurrences_nation:
                    occurrences_nation
    #return count_occurrences


def mot_Climat(directory, files_names):
    os.chdir(directory)
    president = []
    file_names = os.listdir("C:/Users/maely/PycharmProjects/ProjetJadeMaelysChatBot/speeches")
    # Il faut changer l'acces au dessus pour que la fonction fonctionne
    word_count = []
    for i in range(len(file_names)):
        count = 0
        with open(file_names[i], "r") as file:
            for line in file:
                words = line.split(" ")
                for word in words:
                    if word == "climat" or word == "écologie":
                        president.append(file_names[i])
                    else:
                        count += 1
            word_count.append(count)
    lowest_count = min(word_count)
    lowest_president = ''
    for i in range(len(word_count)):
        if word_count[i] <= lowest_count:
            lowest_president = president[i]
    parts = lowest_president.split("_")
    president_name = ''
    for part in parts:
        if part != "Cleaned" and part != "Nomination" and part != "txt":
            president_name = part.replace(".txt", "")
            break
    print(f"Le premier président à parler de climat est : {president_name}")
    return president_name



def menu():
    print("\nMenu:")
    print("1. Poser une question")
    print("2. Quitter")

def fonctionnalite1():
    print("Vous venez de taper 1.")
    return True
def affichage():
    choix = input("Comment puis-je vous aider ? Taper 1 si vous avez une question sinon taper 2 : ")
    if choix == "1":
        fonctionnalite1()
    elif choix == "2":
        print("Au revoir!")
    else:
        print("Option non disponible.")
    return
def question():
    question = str(input("Posez votre question : "))
    return question
def tokenization_question(question):
    word_question = []
    question = str(question)
    # application des meme modification du texte sur la question

    content_lowercase = question.lower()

    punctuation_character = ',;:.?!""()[]*/'
    question_clean = ''

    for car in content_lowercase:
        if car in punctuation_character:
            question_clean += ' '
        elif car == "'" or car == "-":
            question_clean += ' '
        else:
            question_clean += car

    # Divise la question en mot
    content = question_clean.split()
    for word in content:
        word_question.append(word)
    return word_question

def word_presence(files_names, word_question):
    word_file = set()
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()
            speech = content.split()
            for word in speech:
                word_file.add(word)
    commun_terms = set(word_question) & word_file
    return commun_terms
'''
def vecteur_TF_IDF():
    for word in question:
        if word in corpus_word:
            index.mot
    return'''

def TF_IDF_question(tf, idf, l, question):

    vecteur_question = []
    for mot in idf:
        if mot in question:
            tf = question.count(mot)
            tfidf = tf * idf[mot]
            vecteur_question.append(tfidf)
        else:
            vecteur_question.append(0)

    return vecteur_question



def tokenize(question):
    word_question = []
    question = str(question)
    # application des meme modification du texte sur la question

    content_lowercase = question.lower()

    punctuation_character = ',;:.?!""()[]*/'
    question_clean = ''

    for car in content_lowercase:
        if car in punctuation_character:
            question_clean += ' '
        elif car == "'" or car == "-":
            question_clean += ' '
        else:
            question_clean += car

    # Divise la question en mot
    content = question_clean.split()
    for word in content:
        word_question.append(word)
    return word_question


def question_words(tokens:list):
    meaningful_words = []  # filtering out the terms that aren't in the corpus
    for j in range(len(tokens)):
        if tokens[j] in all_words:
            meaningful_words.append(tokens[j])
    return meaningful_words


def question_vector(tokens, l):
    TF_question = {}
    for j in range(len(tokens)):
        if tokens[j] in TF_question:
            TF_question[tokens[j]] += 1
        else:
            TF_question[tokens[j]] = 1

    TF_IDF_question = {}

    for key, value in TF_question.items():
        TF_IDF_question[key] = value * idf(l)[key]
    return TF_IDF_question


def scalar(vector1, vector2):
    scalar_value = 0

    for i in range(len(vector1)):
        scalar_value += vector1[i] * vector2[i]
    return scalar_value


def norm(a):
    somme = 0
    for coordinate in a:
        somme += coordinate**2
    return math.sqrt(somme)


def similarity(v1, v2):
    result = 0
    if norm(v1) * norm(v2) != 0:
        result = scalar(v1, v2) / (norm(v1) * norm(v2))
    return result


def relevancy(question_TFIDF, filenames):
    similarities = {}
    current = os.getcwd()

    for i in range(len(os.listdir(filenames))):
        filepath = os.path.join(current, "cleaned", "Cleaned_" + os.listdir(filenames)[i])
        with open(filepath, 'r') as text:
            singleline = ""
            for line in text.readlines():
                singleline += line

            doc_token = question_vector(question_words(tokenize(singleline)))
            doc_copy = doc_token

            question_copy = question_TFIDF
            # Now we have vectors of the same size

            similarities[filepath] = similarity(list(question_copy.values()), list(doc_copy.values()))

    maximum = similarities[list(similarities.keys())[0]]
    maxkey = ""
    for key, value in similarities.items():
        if value > maximum:
            maxkey = key

    return maxkey


def speeches_eq(path):  # This will return the equivalent file in the speeches folder
    path_chain = path.split("\\")
    path_chain[-2] = "speeches"
    path_chain[-1] = path_chain[-1][8:]
    real_path = "\\".join(path_chain)
    return real_path


def response(question):
    vector = question_vector(question_words(tokenize(question)))
    keyword = list(vector)[0]

    for key, value in vector.items():
        if value > vector[keyword]:
            keyword = key

    most_relevant_doc = speeches_eq(relevancy(vector, "speeches"))

    with open(most_relevant_doc, "r") as doc:
        save_line = ""

        for linee in doc.read().split("\n"):
            if keyword in linee:
                save_line = linee

        print("question: ", question)
        print("Relevant document returned: ", most_relevant_doc)
        print("Word that is likely to be what you're looking for: ", keyword)
        print("Response generated: ", save_line)
    return save_line


def conveniency(question):
    return response(question_vector(question_words(tokenize(question))))


QUESTION_STARTERS = {
    "comment": "Après analyse, ",
    "pourquoi": "Car, ",
    "qui": "La personne responsable de cela est ",
    "combien": "Au total il y a ",
    "est-ce que": "Il est possible que ",
    "peut-on": "Oui, il est possible de ",
    "serait-il possible": "Il est envisageable de ",
    "comment faire": "Voici comment procéder : ",
    "quelle est la raison": "La raison principale est ",
    "est-ce que tu peux": "Oui, je peux ",
    "est-ce que tu sais": "Oui, je sais que ",
    "peux-tu": "Oui, je peux ",
}

reponse = "###    mettre la phrase réponse    ###"


def final_answer(question: str, solut: str):
    solut = solut.strip() + "."
    for key in QUESTION_STARTERS:
        if question.startswith(key,0,25):
            solut = solut[0].upper() + solut[1:]
            solut = QUESTION_STARTERS[key] + solut
    print(solut)


