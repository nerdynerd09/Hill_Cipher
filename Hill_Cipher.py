import string
from numpy import *
import numpy as np

alphabets = string.ascii_letters
keyIndex=[]
wordIndex = []
arr_moduloMatrix = []

class Hill_cipher():

    def Intro(self):
        print("""                 +++++++++++++++++++++++++++++++++++++++++++++++++++
                 + ----------   WELCOME TO HILL CIPHER   ---------- + 
                 +++++++++++++++++++++++++++++++++++++++++++++++++++
                                Instagram -- @hackersarena0\n\n""")

    def key(self):
        try:
            user_input = input("Enter your key--> ")
            self.row = int(input("Enter Row--> "))
            self.column = int(input("Enter Column--> "))
        except(ValueError):
            user_input= "HILL"
            self.row = 2
            self.column = 2
        for i in user_input:
            keyIndex.append(alphabets.index(i)%26)
        try:
            self.key_matrix= matrix(array(keyIndex).reshape(self.row,self.column))
        except(ValueError):
            print("\nERROR: Make sure that product of row and column is equal to the number of alphabets of the key word.")
            exit()

    def word(self):
        userWord = input("\nEnter the word to be encrypted --> ")
        for j in userWord:
            wordIndex.append(alphabets.index(j)%26)
        self.word_matrix = matrix(array(wordIndex).reshape(self.column,int(len(wordIndex)/self.column)))

    def cipher(self):
        self.resultantMatrix = self.key_matrix * self.word_matrix
        self.modulo_resultantMatrix = self.resultantMatrix%26

        self.modulo_resultantMatrix = np.array(matrix(self.modulo_resultantMatrix))
        for i in self.modulo_resultantMatrix:
            for j in i:
                arr_moduloMatrix.append(j)

        ciphetText = [alphabets[k] for k in arr_moduloMatrix]
        print("Ciphered Text is --> ",''.join(ciphetText))


s = Hill_cipher()

try:
    s.Intro()
    s.key()
    s.word()
    s.cipher()

except (KeyboardInterrupt):
    print("\nCrtl+c detected.\nExiting.....")