
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('pylab', 'inline')
from time import *


# In[3]:


usernames = []
passwords = []
emails = []


# In[ ]:


#-Boolean creation-#
usrn_check1 = False
pswrd_check1 = False
usrn_check2 = False
pswrd_check2 = False
fpass = False
taken1 = False
taken2 = False

#-Ask user if they are new-#
new = input("Are you a new user? (y/n) ")

#----------------------------------------------------------------------------------------------------------------#

#-If the user is new-#
if (new == "y"):
    
    #-Account Creation-#
    print("\nRegister:")
    newuser = input("Enter your username: ")
    while (new == "y"): #Password length requirement loop
        newpass = input("Enter your password: ")
        if (len(newpass) < 8): #"len" function credit to Stack Overflow - checks length of input
            print ('\033[93m' + "Password must be at least 8 characters.")
        else:
            break
    newemail = input("Enter your email address: ") 
    
    #-Check if username and email are taken-#
    for l in usernames:
        if l == newuser:
            taken1 = True
            break
        else:
            taken1 = False
            break
    for m in emails:
        if m == newemail:
            taken2 = True
            break
        else:
            taken2 = False
            break
            
    if (taken1 and taken2):
        print ('\033[93m' + "Sorry, the username and email you entered is already taken.")
    elif (taken1):
        print ('\033[93m' + "Sorry, the username you entered is already taken.")
    elif (taken2):
        print ('\033[93m' + "Sorry, the email you entered is already taken.")
    else:
        usernames.append(newuser)
        passwords.append(newpass)
        emails.append(newemail)
        
        sleep(1)
        print("\nUser account created.")
    
    #-Login Segment-#
    sleep(1)
    print("\nLogin:")
    user= input("What is your username: ")
    pw= input("What is your password: ")
    
    #-Search arrays for username and password-#
    for i in usernames:
        if i == user:
            for j in passwords:
                if j == pw:
                    usrn_check1 = True 
                    pswrd_check1 = True
                    break 

    #-Correct Login/Incorrect Login-#
    if (pswrd_check1 is True and usrn_check1 is True):
        print("Welcome. \n-Coded by Trent Bissette")
    else:
        print('\033[93m' + "Sorry that login is incorrect.")
        pwinc = input('\033[93m' + "Forgot your login info? (y/n) ")
        if (pwinc == "y"):
            fpass = True
        else:
            fpass = False 
            print('\033[93m' + "Please try again. \n-Code by Trent Bissette")
    
    #-If user forgot their login info-#
    if (fpass):
        nEmail = input("Enter your email address to recover your login info: ")
        sleep(1) 
        for k in emails:
            if k == nEmail:
                print("An email has been sent to recover your login info. \n-Code by Trent Bissette") 
                break
            else: 
                print('\033[93m' + "Please enter a valid email address. \n-Code by Trent Bissette")
                break 
                
#-----------------------------------------------------------------------------------------------------------------#
    
#-If user isn't new (Does same thing as above without account creation)-#
elif (new == "n"):
    
    #-Let user login-#
    print("\nLogin:")
    user= input("What is your username: ")
    pw= input("What is your password: ")
    
    #-Search arrays for username and password-#
    for i in usernames: 
        if i == user:
            for j in passwords: 
                if j == pw:
                    usrn_check2 = True
                    pswrd_check2 = True
                    break
                    
    #-Correct Login/Incorrect Login-#
    if (pswrd_check2 is True and usrn_check2 is True):
        print("Welcome. \n-Code by Trent Bissette")
    else:
        print('\033[93m' + "Sorry that login is incorrect.")
        pwinc = input('\033[93m' + "Forgot your login info? (y/n) ")
        if (pwinc == "y"):
            fpass = True
        else:
            fpass = False 
            print('\033[93m' + "Please try again.")
        
    #-If the user forgot their login info-#
    if (fpass): 
        nEmail = input("Enter your email address to recover your login info: ")
        sleep(1) 
        for k in emails:
            if k == nEmail:
                print("An email has been sent to recover your login info. \n-Code by TERN") 
                break
            else:
                print('\033[93m' + "Please enter a valid email address. \n-Code by TERN")
                break
                
#---------------------------------------------------------------------------------------------------------------#
                
#-Print out all arrays for troubleshooting-#
elif (new == "arrays"):
    print(usernames)
    print(passwords)
    print(emails)
                
#-If user does not say they are new or not-#
else:
    print ('\033[93m' + "Please enter y/n.")
    #--#

