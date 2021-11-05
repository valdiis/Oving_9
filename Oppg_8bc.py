#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:19:23 2021

@author: mathiasvalderhaug
"""

from typing import Counter


text_fila = open("spørsmaalsfil.txt", "r", encoding="UTF8" ")
question = []
nevner = []
svar1 = []

for linje in text_fila.readlines():
    tekst = linje.split(":")
    question.append(tekst[0])
    nevner.append(tekst[1])

    svar1_rad = teks[2].split(",")
    svar1.append(svar1_rad)

nevner = [i.strip(" ")] for i in nevner]

class Quiz():
    # __init__() blir kalt automatisk kvar gang classen blir brukt for å lage et nytt objekt 
    def __init__(self, que, opt, ans):
        self.question = que
        self.option = opt
        self.answer = ans
        
    def __str__(self):
        #lager en god representasjon av spørsmål og alternativ
        
        #spørsmål på første linjen 
        tekst = self.question + "\n"
        
        for counter in range(len(self.options)):
            tekst += f"{counter}- {self.options[counter]} \n"
        return tekst

    def sjekk_svar (self, sjekk):
        if sjekk == self.answer
        print("Korrekt svar: " + self.options[int(self.answer)])


    
spill = []

quiz.append(Que("Hva er hovedstaden i Norge?", 2, ["Bergen", "Oslo", "Trondheim", "Ålesund"]))
quiz.append(Que("Hvor ligger England", 3, ["Ålesund", "Asia", "Europa", "Afrika"]))

for spm in quiz:
    print(spm)
    
    valg = int(input("Skriv svaret: "))
    
    if spm.sjekk_svar(valg):
        print("Riktig! "+ "\n")
        
    else:
        print("Beklager feil" + "\n")


