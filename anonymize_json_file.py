# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 17:39:27 2024

@author: iandoli michela
"""

#IMPORT PACKAGE I NEED
import  tkinter as tk
from tkinter import filedialog #The tkinter.filedialog module provides
# classes and factory functions for creating file/directory selection windows.

#FUNCTION TO GET FILE PATH
def filepath ():
    file_path = filedialog.askopenfilename()
    return file_path

#IMPORT THE EXPLICIT FILE
from json import load
file=open(filepath())
initial=load(file) #expl is abbreviation for explicit, the list with the name still on it
file.close()

#INITIALIZING SOME VALUES
i=1
k=0

#EXTRACION OF ALL LOGGED NAMES (NOT REPEATED)
user=[] #create an empty list for the names of people who logged
user.append(initial[0][1]) #the first user on the explicit list il for sure the first who logged
#so he automatically goes in the user list, as he surely never logged before and has not 
#already a number assigned
while i<len(initial):
    found=False #found is a boolean that indicates if the user as already logged before
    while k<len(user):
        if initial[i][1]==user[k]: #if i find a name that has altready logged
            found=True #i put found equale true
            break #and i stop the cicle because it means i don't have to add it
        else: #if the name is not the one altready saved in user
            k+=1 #i keep searching in user list
    if not found: #if the isn't among the ones already in user list
        user.append(initial[i][1]) #i add it
    i+=1 #i go on with the explicit list
    k=0 #and i start again with the user list

#SAVE A DICTIONARY TO ASSOCIATE NAME AND ID NUMBER    
user_tuple=tuple(user) #i need user list as tuple to use it as keys in dictionary
'''
è inutile trasformare la lista in tupla perchè effettivamente le chiavi sono str
sarebbe stato necessario se io avessi usato le liste come chiavi, allora avrei 
dovuto trasformarle prima in tuple
'''
link={} #i start an empty dict to save each name and its corresponding ID number
while k<len(user):
    link[user_tuple[k]]=str(k).zfill(10) #i put as key the name and as value the ID number
    k+=1

#SUBSTITUTION OF NAMES WITH ID NUMBERS
i=0
k=0
while i<len(initial):
    initial[i][1]=link[initial[i][1]]
    i+=1

#ELIMINATION OF THE "INVOLVED USER" COLUMN
i=0
while i<len(initial):
    del initial[i][2]
    i+=1


