import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding = "utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

""" Language = input('what language would you like to continue in?:')
for pokemon in data:
    print (pokemon["name"][Language])
     """
Types = input ("what pokemon type are you looking for?:")
typelist=()
for pokemon in data:
    if pokemon ["type"] == Types:
      print (pokemon["name"]) 
    else:
       print ("No Pokemon found")
       break

#loop for the love of God
#then inside the loop LOOK AT THWE TYPES
#hank sit down

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

