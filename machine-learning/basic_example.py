#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 22:15:10 2020

@author: gabrielguimaraes
"""

numero = 2

print(numero)

vetor = [2,3,4]

import numpy as np

vetor = np.asarray(vetor)

print("maior valor", vetor.max())

print("posicao de maior valor", vetor.argmax())

print("valor minimo", vetor.min())

print("media", vetor.mean())

print("soma", vetor.sum())

vetor2 = numero * vetor

#generate random number

np.arange(1, 50, 3)







