#coding and decoding of given msg

import string
import random
print("1 for coding , and 0 for decoding ")
choice=int(input("press between 1 and 0: "))
word=input("Enter your msg:\n")
def codeing():
    char=3
    
    if choice==1:
     if len(word)>=3:
      #   r1="dhx"
      #   r2="kwq"
        ran=''.join((random.choice(string.ascii_lowercase)) for i in range(char))
        ran2=''.join((random.choice(string.ascii_lowercase+string.digits)) for i in range(char))
        words=str(ran)+word[1:]+word[0]+str(ran2)
        print(words)
     else:
        reverse=word[::-1]   
        print(reverse)

codeing()
 

def decoding():
    if choice==0:
     if len(word)>=3:
        
        words=word[3:-3]
        v=words[-1]+words[:-1]

        print(v)
     else:
        reverse=word[::-1]   
        print(reverse)

decoding()
# tefehanjpd
    



    
    






