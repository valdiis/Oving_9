#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Created on Thu Oct 21 16:19:23 2021

@author: mathiasvalderhaug



text_fila = open("sporsmaalsfil.txt", "r", encoding="UTF8")

question = []
nevner = []
svar1 = []

for lines in text_fila.readlines():
    tekst = lines.replace("[", "").replace("]", "")
    tekst = lines.split(":")
    question.append(tekst[0])
    nevner.append(tekst[1])

    svar1_rad = tekst[2].split(",")
    svar1.append(svar1_rad)
    
nevner = [i.strip(" ") for i in nevner]

class Quiz:
    # __init__() blir kalt automatisk kvar gang classen blir brukt for å lage et nytt objekt 
    def __init__(self, que, opt, ans):
        self.question = que
        self.option = opt
        self.answer = ans
        
    def __str__(self):
        #lager en god representasjon av spørsmål og alternativ
        
        #spørsmål på første linjen 
        tekst = self.question + "\n"
        
        for counter in range(len(self.option)):
            tekst += f"{counter}- {self.option[counter]} \n"
        return tekst

    def sjekk_svar (self, sjekk):
        if sjekk == self.answer:
            print("Korrekt svar: " + self.option[int(self.answer)])
        return sjekk == self.answer


    
game = []
for a in range(8):
    game.append(Quiz(question[a], svar1[a], nevner[a]))
    
score1 = 0
score2 = 0



for i in game:
    print(i)
    valg1 = input("Velg et svaralternativ for spiller 1: ")
    valg2 = input("Velg et svaralternativ for spiller 2: ")

    if i.sjekk_svar(valg1):
        print("Riktig for spiller 1\n")
        score1 += 1
    if i.sjekk_svar(valg2):
        print("Riktig for spiller 2\n")
        score2 += 1
    else:
        print("Feil svar/")

print(f"Spiller 1 fikk: {score1}")
print(f"Spiller 2 fikk: {score2}")