import random

#Start of small mad lib maker
#a= input("Start collecting user data")
VERBS = ["Zonked","Wasted","Bonked","Booped"]
ADJ=["Good","Big"]
zooBase = [
    "Today, my ", "[adjective]", " friend and I decided to visit the ", "[adjective]", " ", "[place]", ". ",
    "When we got there, the ", "[adjective]", " gatekeeper greeted us with a\n ", "[color]", " ", "[adjective]", " ", "[noun]", ". ",
    "We bought some ", "[adjective]", " ", "[plural noun]", " and headed inside. ",
    "The first thing we saw was a ", "[adjective]", " ", "[animal]\n", " ", "[verb ending in -ing]", " in its cage. ",
    "It made a ", "[adjective]", " sound that made us ", "[verb]", " with laughter.\n ",
    "Next, we went to see the ", "[color]", " ", "[adjective]", " ", "[plural animal]", ". ",
    "They were ", "[verb ending in -ing]", " around and playing with a ", "[color]", " ", "[adjective]", " ", "[noun]", ". ",
    "We took\n some ", "[adjective]", " ", "[color]", " pictures with them.\n ",
    "Then, we decided to have lunch at the ", "[adjective]", " ", "[place]", " café. ",
    "I ordered a ", "[adjective]", " ", "[color]", " ", "[food]", " and my friend got\n a ", "[color]", " ", "[adjective]", " ", "[food]", ". ",
    "It tasted ", "[adjective]", ", but we didn't mind. ",
    "After lunch, we watched a ", "[color]", " ", "[adjective]", " show featuring a\n ", "[adjective]", " ", "[animal]", " that could ", "[verb]", ". ",
    "It was amazing! We also saw a ", "[adjective]", " ", "[animal]", " ", "[verb ending in -ing]", " a ", "[color]", " ", "[adjective]", " ", "[noun]", " in the water. ",
    "Before we left, we bought some ", "[adjective]", " ", "[plural noun]", " from the\n gift shop. ",
    "It was a ", "[adjective]", " ", "[color]", " day at the zoo, and we\n can't wait to go back!","~~"
]
Replace=[]
ReplaceCheck=[]
Story=[]
Filter=[]
#Story=zooBase
print("Thank you for trying out madLibs. I hope you enjoy the goofy short story.")
print("Please enter a number for the story you would like.1. A story about a trip to the zoo")
selection = input()

#https://realpython.com/python-enumerate/
#check for invalid input/ ensure input is an int
try:
    selection=int(selection)
except ValueError:
    print("Non valid input")
if selection == 1 :
    Story=zooBase

#Check for the values to replace/ populate replace index list
for index,x in enumerate (Story):
    if "[" in x:
        Replace.append(index)

#Auto replace half ish of the words to speed up the pocess of filling out
for x in Replace:
    if x % 2 == 1:
        if "ad" in Story[x]:
            ReplaceCheck.append(x)
            Story[x] = ADJ[random.randint(0, len(ADJ) - 1)]
        if "ver" in Story[x]:
            ReplaceCheck.append(x)
            Story[x] = VERBS[random.randint(0, len(VERBS) - 1)]

#Test to make sure index is being stored correctly uncomment if issues encoutnered
for x in Replace:
    print(x)


for x in Replace:
    if x in ReplaceCheck:
        print("")
    else:
        Filter.append(x)
print("Test list")
for x in Filter:
    print(x)
for x in Replace:
    print(x)

#Test values
print("test")
print(len(Filter))
print(len(Replace))
###################
for x in Filter:
    print(Story[x])
    Story[x]=input("Enter the word you would like:")


#Print the final story
for x in Story:
    print(x, end="")

