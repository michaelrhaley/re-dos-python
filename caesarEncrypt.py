import sys
import os
#Kudos to Al Sweigart for the shortcuts using encryption (the bulk of the logic used)
#Program in Python lang the caesar.c from pset2

MAX_KEY_SIZE = 26

def getMessage():
    print("What is your secret message?! ", end="")
    return input()
    
def getKey():
    key = 0
    while True:
        print("What will the secret key be?! (1-26): ", end="")
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
            
def getEncryption(message, key):
    translated = ""
    
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            
            if symbol.isupper():
                if num > ord("Z"):
                    num -= 26
                elif num < ord("A"):
                    num += 26
            elif symbol.islower():
                if num > ord("z"):
                    num -= 26
                elif num < ord("a"):
                    num += 26
                    
            translated += chr(num)
        else:
            translated += symbol
    return translated
    
message = getMessage()
key = getKey()

print("Your secret message encrypted is: ", end="")
print(getEncryption(message, key))
