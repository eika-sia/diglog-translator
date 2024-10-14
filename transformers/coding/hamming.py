from itertools import count
from math import ceil
from math import log2
import re

from transformers.numberSystems.dec import codeDec, decodeDec


def codeHamming(h, p):
    # p == 1: parni paritet
    h = str(h).replace(" ", "")

    # cn zastitni bitovi
    cn = 1
    while 2**cn < len(h) + cn + 1:
        cn += 1

    # matrice gdje elemnti correspondaju d => data, neki broj i-ti security bit
    solC = []
    sol = []

    tempD = 0
    tempS = 1
    for i in range(len(h)+cn):
        # bit manipulation to check if i = 2^k or 0
        if (((i+1) & (i) == 0) and i+1 != 0):
            solC.append(tempS)
            tempS += 1
            sol.append(0)
        else:
            solC.append("d")
            sol.append(h[tempD])
            tempD += 1

    mainIndex = 0
    while mainIndex < ceil(log2(len(sol))):
        # index security bita
        aI = 2**mainIndex-1
        nI = aI+1

        counter = 0
        while nI < len(sol):

            if int((decodeDec(nI+1))[-solC[aI]]) == 1 and int(sol[nI]) == 1:

                counter += 1
            nI += 1

        if p == 1 and counter % 2 == 1:
            sol[aI] = 1
        elif p == 0 and counter % 2 == 0:
            sol[aI] = 1

        mainIndex += 1
    for i in range(len(sol)):
        sol[i] = str(sol[i])
    return ("".join(sol))


def decodeHamming(h):
    h = str(h).replace(" ", "")
    sR = []
    dR = ""

    i = 0
    while i < len(h):
        if (((i+1) & (i) == 0) and i+1 != 0):
            sR.append(h[i])
        else:
            dR += str(h[i])
        i += 1

    return dR, sR


def syndromeHammning(h, p):
    # p = 1 => parni paritet
    h = str(h).replace(" ", "")
    dR, sR = decodeHamming(h)
    dE, sE = decodeHamming(codeHamming(dR, p))

    syn = []

    for i in range(len(sR)):
        syn.append(str(int(sR[i]) ^ int(sE[i])))
    syn = codeDec((''.join(syn))[::-1])
    return syn


def fixHamming(h, p):
    h = str(h).replace(" ", "")
    i = syndromeHammning(h, p)-1
    h = list(h)
    
    if (i >= len(h)):
        return "vise pogresaka, sindrom izvan dometa"
    
    if h[i] == "1":
        h[i] = "0"
    else:
        h[i] = "1"

    return "".join(h)
