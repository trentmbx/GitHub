
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('pylab', 'inline')
from random import *


# In[3]:


def encrypt():
    #Alphabet arraylist
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #Input for message, list form
    encI = list(input("Enter a message to encrypt: ").lower())
    #Create a random number for shift
    rNum = randint(0, 25)
    #Encrypted message
    encrypt = ""
    #Go through arraylist of input
    for i in range(len(encI)):
        for j in range(len(alpha)):
            if (alpha[j] == encI[i]):
                if ((j + rNum) > 25):
                    encrypt = encrypt + alpha[(j + rNum) - 25]
                else:
                    encrypt = encrypt + alpha[j + rNum]
    print("Your encrypted message is -" + encrypt + "-")
    print("Shifted", rNum, "times.")
    
    #Decrypt function
    def decrypt():
        #Alphabet arraylist
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        #Input for message to encrypt
        encI2 = list(input("Enter your encrypted message: ").lower())
        #Input for the shift used to encrypt
        shift = int(input("Enter your encrypted shift: "))
        #Variable for decrypted message
        decrypt = ""
    
        #Go through arraylists of input
        for k in range(len(encI2)):
            for l in range(len(alpha)):
                if (alpha[l] == encI2[k]):
                    if ((l - shift) > 25):
                        decrypt = decrypt + alpha[(l - shift) + 25]
                    else:
                        decrypt = decrypt + alpha[l - shift]
                
        print("The original message is -" + decrypt + "-")
    
    decrypt()
    
encrypt()

