#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:19:23 2021

@author: mathiasvalderhaug
"""

class Que():
    def __init__(self, que, ans, alt):
        self.question = que
        self.answer = ans
        self.alternative = alt
        
    def __str__(self):
        tekst = self.question + "\n"
        for alternativnummer, alternativsvar, in enumerate(self.alternative):
            tekst += f"{alternativnummer+1}: {alternativsvar} \n"
        return tekst
    def sjekk_svar (self, sjekk: int):
        return sjekk == self.answer
    
quiz = []

quiz.append(Que("Hva er hovedstaden i Norge?", 2, ["Bergen", "Oslo", "Trondheim", "Ålesund"]))
quiz.append(Que("Hvor ligger England", 3, ["Ålesund", "Asia", "Europa", "Afrika"]))

for spm in quiz:
    print(spm)
    
    valg = int(input("Skriv svaret: "))
    
    if spm.sjekk_svar(valg):
        print("Riktig! "+ "\n")
        
    else:
        print("Beklager feil" + "\n")


