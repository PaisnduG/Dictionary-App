import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

def querying(word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(word))
    results = cursor.fetchall() 

    if results:
        for sentence in results:
            print(sentence[1])
    else:
        return 0

all_words = []
query = cursor.execute("SELECT * FROM Dictionary")
results = cursor.fetchall()

if results:
    for word in results:
        all_words.append(word[0])

def translate(word):
    if querying(word) == 0:
        if len(get_close_matches(word, all_words, n=3, cutoff=0.7)) > 0:
            yn = input("Did you mean {} instead? Enter Y if yes, N otherwise: ".format(get_close_matches(word, all_words, n=3, cutoff=0.7)[0]))
            if yn =='Y':
                return querying(get_close_matches(word, all_words, n=3, cutoff=0.7)[0])
            elif yn =='N':
                return "No word found!"
            else:
                return "We didn't understand your query."
       
    

word = input("Enter Word: ")
 
translate(word)


