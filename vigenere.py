#!/usr/bin/python
#encoding: utf8

from math import floor
import string

class vigenere():
    """This class implements Vigenère cipher. Vigenère cipher is a variant of
    Caesar cipher and thus doesn't provide real security.
    
    Note: Avoid using other than alphabets in your passkey
    
    """
    def __init__(self, text, cipher):
        #self.alphabet = string.lowercase
        self.alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
        self.text = text
        self._cipher = cipher
        self.realpass = ''
        if len(cipher) >= len(self.text):
            self.realpass = self._cipher[:len(self.text)]
            assert len(self.text) == len(self.realpass)
        else:
            full = floor(len(self.text) / float(len(self._cipher)))
            self.realpass = self._cipher * int(full)
            self.realpass += self._cipher[:(len(self.text) - \
                len(self.realpass))]

    def index(letter)
        return self.alphabet.find(letter)

    def encode(self):
        coded = []
        code = 0
        for i, j in enumerate(self.text):
            if j in self.alphabet and self.realpass[i] in self.alphabet:
                code = int(self.index(s)
        return vigenere(''.join(coded), self._cipher)

    def decode(self):
        for i, j in enumerate(cipher):
            letterindex = index(j)
            passindex = index(fullpass[i])
            plaintext += alphabet[letterindex - passindex]
