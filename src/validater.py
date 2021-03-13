#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime

def verifier_date(var):
    """
    Verifying whether the date is not in the past.
    """
    if(var != None):
        date_time = datetime.datetime.strptime(var, '%Y-%m-%d').date()
        if(date_time<datetime.date.today()):
            return -1
        else:
            return var
    else:
        return -1

def verifier_str(var):
    """
    Verifying whether the string variables are less than 100 char
    and prevents it from having strict numeric name.
    """
    if((var != None) & (type(var)==str ) & (len(var)<=100) & (len(var)>0)):
        try:
            var = int(var)
            return -1
        except:
            return var
    else:
        return -1

def verifier_int(var):
    """
    Verifies whether the given var is of type int.
    """
    if(var != None):
        try:
            var = int(var)
            if(var>=0):
                return var
            else:
                return -1
        except:
            return -1
    else:
        return -1

def verifier_list(var=[]):
    """
    Verifies the var is of list type with length <=10.
    And checks if each component in the list is of str type and 
    has less than 100 characters.
    """
    if(len(var)>10):
        return -1
    else:
        try:
            for ele in var:
                if(verifier_str(ele) == -1):
                    return -1
            return var
        except:
            return -1

def get_meta(request,audiofiletype,id1=False):
    """
    Making sure all the arguments for each Audiofiletype are processed 
    appropriately according to their metadata.
    
    Here variable 'id1' is used to determine whether to check for variable
    'id' and add it to the database subsequently.
        - By default its set to 'False' and the function returns a dictionary
    along with the parameter 'id'. Hence making it suitable for "CREATING Document".
        - If it's set to 'True' then the function returns a dictionary without 
    the 'id'. Hence making it suitable for "UPDATING Document".
    
    """
    if(audiofiletype.lower()=='song'):
        meta = {
                'name_of_the_song':verifier_str(request.args.get('name')),
                'Duration_in_seconds':verifier_int(request.args.get('duration')),
                'uploaded_time':verifier_date(request.args.get('uptime'))
                }
        if(id1):
            return meta
        else:
            meta.update({'_id':verifier_int(request.args.get('id'))})
            return meta
    elif(audiofiletype.lower()=='podcast'):
        meta = {
                'name_of_the_podcast':verifier_str(request.args.get('name')),
                'Duration_in_seconds':verifier_int(request.args.get('duration')),
                'uploaded_time':verifier_date(request.args.get('uptime')),
                'host':verifier_str(request.args.get('host')),
                'participants':verifier_list(request.args.getlist('participants')),
                }
        if(id1):
            return meta
        else:
            meta.update({'_id':verifier_int(request.args.get('id'))})
            return meta
    elif(audiofiletype.lower()=='audiobook'):
        meta = {
                'title_of_the_audiobook':verifier_str(request.args.get('name')),
                'Duration_in_seconds':verifier_int(request.args.get('duration')),
                'uploaded_time':verifier_date(request.args.get('uptime')),
                'author_of_title':verifier_str(request.args.get('author')),
                'narrator':verifier_str(request.args.get('narrator'))
                }
        if(id1):
            return meta
        else:
            meta.update({'_id':verifier_int(request.args.get('id'))})
            return meta
    else:
        return -1


# In[ ]:




