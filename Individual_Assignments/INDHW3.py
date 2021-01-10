####4.16
fword=input("Enter first word:")
sword=input("Enter second word:")
tword=input("Enter third word:")

lst=[]
lst.append(fword)
lst.append(sword)
lst.append(tword)
lst2=[]
for word in lst:
    lst2.append(word)
lst.sort()
if lst==lst2:
    print(True)
#we make two list and compare them, letter by letter
#they are duplicates of each other until lst is sorted
#then compared to list 2. They are then compared, letter by letter

####4.19
first='Marlena'
last='Sigel'
middle='Mae'
#a
fstring='{}, {} {}'
#b
sstring='{}, {} {}.'
#c
tstring='{} {}. {}'
#d
dstring='{}. {}. {}'
#e
estring='{}, {}.'

print(fstring.format(last,first,middle))
print(sstring.format(last,first,middle[0]))
print(tstring.format(first,middle[0],last))
print(dstring.format(first[0],middle[0],last))
print(estring.format(last,first[0]))
##4.20
#please tell me there is another way to do this one
#I tried the \n and it worked, a little sloppy, but it worked
#each {} is a variable after .format, place accordingly as seen below

sender='tim@abc.com'
recipient='tom@xyz.org'
subject='Hello!'
print('{}{}\n{}{}\n{}{}'.format("From:", sender,"To:",recipient,"Subject:",subject))





##4.24
#probably the easiest problem given. Can also be done using .format instead
#of printing so many times. 
def cheer(x):
    print("How do you spell winner?\nI know, I know!")
    for word in x:
        print(word.upper(),end='  ')
    print('!')
    print("And that's how you spell winner!")
#I put .capitalize just to be professional. Technically, it is not needed
    print('Go',x.capitalize(),'!')

    



##4.29
def stats(filename):
   
#it is imperative to close the file and then to open again if we want to do
#something else to the file (read v readlines). This, to me, would be the easy
#way out, however, the book wants us to just use one (read or readlines)

#First, we proceed as normal: open the file, then doing what I want with the file
#In this case, I used readlines (though read is possible as well for this problem)
    infile=open(filename)
    lines=infile.readlines()
    infile.close()

    words=0
    chars=0
    for line in lines:
        line=line.strip()
        line=line.split()
        words+=(len(line))

        for word in line:
            chars+=(len(word))

       

    print('line count:',(len(lines)))
    print('word count:',words)
    print('character count:',chars)

#they want a word count AND a character count, so I will set these to 0
#as you know, with any type action taken with multiple characters,
#we are going to need a for loop...so....
#strip takes away the things we dont want in the file
#what do we want to split? The spaces
#now that we've gotten things out of the way with split and strip
#now we count the words
#within that loop, we can count the characters. Print
#it is also possible to put some of these commands, such as split in the
#print line as well. 


####4.31
#openin file, setting variable for open file
#split makes thing into a list. I want to count inside this list
#make a for loop to continue through the words.
#making a Boeelan function for this 


def duplicate(filename):
    infile=open(filename)
    content=infile.read()
    lst=content.split()        
    for words in lst:
        if lst.count(words)>1:
            return True
    return False
    infile.close()
        
#We first use split to make our file in list format
#then we find the 'words' in that list. Now, though words
#are strings (due to split), we can still use .count to
#count ALL the words, thus including the character.
#if it counts the word more then one time, then True.
#Otherwise, false
