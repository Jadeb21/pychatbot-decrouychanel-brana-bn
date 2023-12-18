import os
import math


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

def nation(files_names):
    '''for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()'''

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

def mot_Climat(files_names, idf):
    occurrences_climat = {}
    for file_name in files_names:
        input_files_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_files_path, 'r') as fn:
            content = fn.read()
            termes = "Climat", "écologie"
            occurrences = word_occurrences_tf(content)
            for (termes, occurrence) in occurrences.items():
                if termes in occurrences_climat:
                    occurrences_climat
    #return count_occurrences_climat
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
def question(fonctionnalite1):
    question = input("Posez votre question : ")
    return
def tokeniser(question):
    punctuation_character = ',;:.?!""()[]*/'
    Q_clean = ''
    question = str(question)
    # Verification des caractères un par un
    '''for car in range (len(question)):
        if punctuation_character in question:
            question() += ' '
        elif punctuation_character == "'" or punctuation_character == "-":
            Q_clean += ' '
        else:
            Q_clean += punctuation_character'''
    return (question.replace(punctuation_character, ' ')

    #caracteres_ponctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
            # Suppression de la ponctuation et conversion en minuscules
            #question = ''.join(caractere for caractere in question if caractere not in caracteres_ponctuation).lower()
    # Tokenisation en mots individuels
    #mots = question.split()

def terme_commun(question, files_names):
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f:
            content = f.read()
            questions = set(question)
            corps = set(files_names)
            terme_commun = questions.intersection(corps)
    return terme_commun

def vecteur_TF_IDF():
    return