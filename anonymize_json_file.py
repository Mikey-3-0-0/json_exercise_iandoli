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
    window = tk.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()   # this supress the tk window

    file_path = filedialog.askopenfilename(parent=window,
                                  initialdir="",
                                  title="Select A File",
                                  filetypes = (("All files", "*"), ("Text files", "*.txt")))
    #file_path = filedialog.askopenfilename()
    return file_path

#FUNCTION THAT RETURNS A DICTIONARY THAT ASSOCIATE NAMES AND ID NUMBERS
def link(usernames_list,start_from=0):
    i=0
    link_dict={} #i start an empty dict to save each name and its corresponding ID number
    while i<len(usernames_list):
        link_dict[usernames_list[i]]=str(i+start_from).zfill(10) #i put as key the name and as value the ID number
        i+=1
    return link_dict

#FUNCTION TO DE-ANONYMIZE
def deanon(explicit_list,associations):
    for i in range(0,len(explicit_list)):
        for k in associations.keys():
            if explicit_list[i][1]==associations[k]:
                explicit_list[i][1]=k
    
#FUNCTION TO ANONYMIZE A SECOND LOG FILE
def second_file(previous_user, previous_associations):
    second_file=input('If you want to anonymize a second file press 1, otherwise press 0\n')
    if second_file=='1':
        print('Choose the file to anonymize from the window opened\n')
        #import file
        file=open(filepath())
        explicit_list2=load(file) 
        file.close()
        #initialization
        i=1
        k=0
        #user list extraction
        user2=[] 
        user2.append(explicit_list2[0][1]) 
        while i<len(explicit_list2):
            found=False 
            while k<len(user2):
                if explicit_list2[i][1]==user2[k]:
                    found=True 
                    break 
                else: 
                    k+=1
            if not found: 
                user2.append(explicit_list2[i][1]) 
            i+=1 
            k=0 
        #searching new users not existing in the first user list
        new_user=[]
        for i in range(0,len(user2)):
            already_existing=False
            for k in range (0,len(user)):
                if user[k]==user2[i]:
                    already_existing=True
                    break
                else:
                    k+=1
            if not already_existing:
                new_user.append(user2[i])
            i+=1
        #creating a second association dictionary for the new users
        associations_new=link(new_user,len(user))
        associations.update(associations_new)
        #SUBSTITUTION OF NAMES WITH ID NUMBERS
        i=0
        k=0
        while i<len(explicit_list2):
            explicit_list2[i][1]=associations[explicit_list2[i][1]]
            i+=1

        #ELIMINATION OF THE "INVOLVED USER" COLUMN
        i=0
        while i<len(explicit_list2):
            del explicit_list2[i][2]
            i+=1
        exist_second=True
    else:
        print('ok, you anonymized only one list')
        exist_second=False
        explicit_list2=[]
    return [explicit_list2,exist_second]


#IMPORT THE EXPLICIT FILE
from json import load
print('Choose the file to anonymize from the window opened\n')
file=open(filepath())
explicit_list=load(file) #explicit_list is the list with the name still on it
file.close()

#INITIALIZING SOME VALUES
i=1
k=0

#EXTRACION OF ALL LOGGED NAMES (NOT REPEATED)
user=[] #create an empty list for the names of people who logged
user.append(explicit_list[0][1]) #the first user on the explicit list is for sure the first who logged
#so he automatically goes in the user list, as he surely never logged before and has not 
#already a number assigned
while i<len(explicit_list):
    found=False #found is a boolean that indicates if the user as already logged before
    while k<len(user):
        if explicit_list[i][1]==user[k]: #if i find a name that has altready logged
            found=True #i put found equale true
            break #and i stop the cicle because it means i don't have to add it
        else: #if the name is not the one altready saved in user
            k+=1 #i keep searching in user list
    if not found: #if the isn't among the ones already in user list
        user.append(explicit_list[i][1]) #i add it
    i+=1 #i go on with the explicit list
    k=0 #and i start again with the user list

#SUBSTITUTION OF NAMES WITH ID NUMBERS
i=0
k=0
associations=link(user)
while i<len(explicit_list):
    explicit_list[i][1]=associations[explicit_list[i][1]]
    i+=1

#ELIMINATION OF THE "INVOLVED USER" COLUMN
i=0
while i<len(explicit_list):
    del explicit_list[i][2]
    i+=1

#ANONIMIZATION OF A SECOND LOG FILE
second_file_return=second_file(user, associations)
second_file_anonymized=second_file_return[0]
exist_second=second_file_return[1]


#DE-ANONYMIZATION
procede_de_anon = input('If you want to de-anonymize one list again, press 1, otherwise press 0\n')
if procede_de_anon=='1':
    if exist_second==True:
        which_list=input('press 1 if you wanto to de-anonymize the first file, 2 for the second one\n')
        if which_list=='1':
            deanon(explicit_list,associations)
        elif which_list=='2':
            deanon(second_file_anonymized,associations)
        else:
            print('you press a wrong number')
        print('the list is NOT anonymized anymore')
    else:
        deanon(explicit_list,associations)
else:
    print('the list is still anonymized')







    
    
    
    
    
    
    
    
    
    
    
    
    
    
