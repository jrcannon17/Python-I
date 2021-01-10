##6.20
phonebook={'Smith, Jane':'123-45-67','Doe, John':'987-65-43',
           'Baker, David':'587-89-01'}
#make generic dictionary
def reverse(dictionary):
#like what we do with list, set a new empty dictionary
    answer={}
    for item in dictionary:
        answer[dictionary[item]]=item
#swapping item as key for value 
        
    return(answer)

print(reverse(phonebook))

#6.22
    
def mirror(string):
#make what you believe to be mirror image of words
#attach an empty string, reply
#if char in dictionary, take these and print their value from the key map
    reply=""
    mirror_word={"b":"d","d":"b","i":"i","m":"m","o":"o","p":"q",
             "q":"p","v":"v","w":"w","x":"x"}
    for char in string:
        if char in mirror_word:
            reply+=mirror_word[char]
        else:
            reply= 'Invalid'
            break
    return reply
#we put break below it, if not, it will still take in the char that are still in the dictionary
print(mirror('pop'))
print(mirror('bed'))
    
    
####6.23
##
def scaryDict(file):
#to get rid of punctuations, just make a list alphabet to refer back to if and only
#in that string
    wordlist=[]
    scary = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
#we need word list and also new dictionary for the list to go into    
    filename=open(file,'r')
    content=filename.readlines()
    filename.close()
#we strip of white space and split by " "
#we make all words found automatically lower to grab every word

    for line in content:
        for word in line.strip().split(" "):
            new_word = ""
            for letter in word.lower():
                if letter in alpha:
                    new_word += letter

            if len(word) > 2:
                wordlist.append(new_word)

#now if my new words are in the word list, we want my word list to
#append to the new scary dictionary
    for word in wordlist:
        if word not in scary:
            scary[word] = True
#organize it with sorted and '\n'
    file = open("dictionary.txt", "w")
    for word in sorted(scary.keys()):
        file.write(word + "\n")
    file.close()
            

scaryDict('frankenstein.txt')
#the new txt will be located wherever the location of this file will be!   

####6.24
##make a list, dictionary and name count = to 1, given the name inputted is the first
#if name is not empty, append it
def names():
    names_list =[]
    names_counter = {}
    name = 1
    while name != '':
        name = input('Enter next name: ')
        if name != '':
            names_list.append(name)
#the name counter adds the same names together, else, it just stores it as one        
    for item in names_list:
        if item in names_counter:
            names_counter[item]+=1
        else:
            names_counter[item]=1
   
#in our dictionary, we make something that will be able to get grammer right based on number
            
    for key in names_counter.keys():
        if names_counter[key] ==1:
            print('There is', names_counter[key],'student named',key)
        else:
            print('There are', names_counter[key],'students named',key)
names()

  
######6.28

japanese = {'goodnight':'oyasumi','goodmorning':'ohayo','retard':'baka'}
#make a dictionary for the function
#we simply print the translation by recalling the key in the string, if it matches
def translate(dictionary):
    
    
    string = input('Please enter a word:')

    if string in dictionary.keys():
        print(dictionary[string])
    else:
        print('_ _ _ _')

translate(japanese)

    
 
##        
######6.31
'''A'''
import random
#we need the random tool from math to do this
#make two dice with their possibility rolls
#add these, randomized, together in a variable
#set a count for the games played
def crapsa():
    dice1= [1,2,3,4,5,6]
    dice2= [1,2,3,4,5,6]
    roll= random.choice(dice1)+random.choice(dice2)
    count=0
#describe the rules of craps with while loop
    while count ==0:
        if roll==7 or roll ==11:
            count += 1
            return 1
        elif roll == 2 or roll == 3 or roll == 12:
            count+=1

            return 0

        roll = random.choice(dice1)+ random.choice(dice2)
print(crapsa())

'''B'''
def craps(x):
#same as above
#no while loop needed
#note that roll= random.choice(dice1)+random.choice(dice2) could be used globally to recognize
#itself throughout the for loop, while loop, and code. Not sure if you wanted this or not  
    dice1= [1,2,3,4,5,6]
    dice2= [1,2,3,4,5,6]
    roll= random.choice(dice1)+ random.choice(dice2)
    total=0
    win= 0

    for i in range(x):

        if roll==7 or roll== 11:

            total+=1
            win +=1

            roll= random.choice(dice1) + random.choice(dice2)
        elif roll==2 or roll==3 or roll == 12:

            total+=1
            roll= random.choice(dice1)+random.choice(dice2)

        else:
            total+=1
            roll= random.choice(dice1)+random.choice(dice2)

    print(win/total)
#we take the range of times played, and then the rules of craps and make a precentage won
    
inputcrap= eval(input("How many times would you like to play?"))
craps(inputcrap)

