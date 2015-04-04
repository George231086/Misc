'''

Small script to brute force the translation ciphered password. 

'''

cipher='OMQEMDUEQMEK'
possiblePassword=''

for i in range(1,26):
    for char in cipher:
	    possiblePassword+=chr(ord(char)+i-int((ord(char)+i-1)/90)*26)
    
    print possiblePassword
    possiblePassword=''	

  
