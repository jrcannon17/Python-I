##5.23
#make variables that indicate the hours that are overtime vs regular pay hours

def pay(wage,hours):
  overtime=hours-40
  pay=wage*40
  if hours>40 and hours<=60:
#we can rewrite overtime_pay since it only runs for each if/elif condition,
#adding the increased overtime pay(over 60 hours)
      overtime_pay=((wage*40)+(overtime*wage)*(1.5))
      return overtime_pay
  elif hours>60:
      overtime=hours-60
      overtime_pay= ((wage*40) + ((20*wage)*(1.5))+((overtime*wage)*2))
      return overtime_pay
  else:
        return (wage*hours)
#it is possible to eliminate the float portion, however, realistically, change would
#theoritically be included, so we leave it as is.  

        
print(pay(10,35))
print(pay(10,45))
print(pay(10,61))


##5.33
#How many times can n be halved using integer division before reaching 1?
def mystery(n):
#we set a while loop to continously run the n variable
# for each time the variable can be divided by 2, adding it to the count
    count=0
    while n>1:
        n=n//2
        count=count+1
    return count
print(mystery(4))
##
####5.39
#Write function exclamation that takes as input a string and returns it with this modification:
#Every vowel is replaced by four consecutive copies of itself and an exclamation mark is added at the end.

def exclamation(string):
    vowel='aeiou'
    newstring=""
# we set a for loop to search for the vowels, and then set a condition as follows
    for i in string:
        if i.lower() in vowel:
            newstring+=i*4
        else:
            newstring+=i
# we need the else. W/o it, non vowels would be missed entirely in our newstring
    return newstring+"!"
print(exclamation('hello'))
         
##        

        

##5.43
#Implement function evenrow() that takes a two-dimensional
# list of integers and re- turns True if each row of the table sums up to an even number and False otherwise

def evenrow(n):
#since N is a list, we can run a for loop successfully and sum them individually
#to meet our condition below. Mod is used to determine if these sumes are even or not
#returning True, or otherwise False if anything else 
    for num in n:
        if sum(num)% 2==0:
            return True
        
    return False
print(evenrow([[1,3],[2,4],[0,6]]))


