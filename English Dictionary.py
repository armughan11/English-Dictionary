import mysql.connector
from difflib import get_close_matches
con = mysql.connector.connect(
    user = "root",
    
    host = "127.0.0.1",
    database = "dictionary"
        
        
        )

cursor = con.cursor()
word = input("Enter a word: ")
word = word.title()


query = cursor.execute("SELECT word, definition FROM entries ")
result =cursor.fetchall()
dict1 = {}
for lol in result:
    dict1[lol[0]]=lol[1]
    
if word in dict1:
    print(dict1[word])
elif len(get_close_matches(word,dict1.keys())) > 0:
    print("Did you mean %s press y or n" % get_close_matches(word,dict1.keys())[0] )
    choice = input()
    if(choice=='y'):
        print(dict1[get_close_matches(word,dict1.keys())[0]])
    else:
        print("The word does not exist")

        
else:
    print("The word does not exist")


    
    

