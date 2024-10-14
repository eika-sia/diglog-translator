
from transformers.coding.hamming import codeHamming, decodeHamming, fixHamming, syndromeHammning
"""
l = "1011100101"
p = 0
print("data:", l, "\n")
print("Coding hamming")
print(codeHamming(l, p))
print("\n")

print("data extraction")
dr, sr = decodeHamming(codeHamming(l, p))
print("podatci:", dr)
print("security bitovi:", sr)
print("\n")

print("sindrom kalkulator:")
print("poruka poslana:", codeHamming(l, p))
er = list(codeHamming(l, p))
er[2] = "0"
er = "".join(er)
print("poruka primljena:", er)
print("sindrom:", syndromeHammning(er, p))
print("popravljeni kod:", fixHamming(er, p))
"""

def mainH():
    c = False
    while not c:
        print("Dobrodosli u Hamming kod kalkulator, za kodiranje podataka upisite 1, za ekstrakciju podataka upisite 2, za sindrom i popravljanje koda upisite 3 ")
        c1 = int(input())
        if c1 not in [1, 2, 3]:
            print("Nije validan izbor, probajte ponovo")
        else:
            c = True
            
    if c1 == 1:
        v = False
        while not v:
            v = True
            print("Molim vas upisite podatke koje zelite kodirati (binarni broj, moze sadrzavati razmake, za ostale brojeve pokrenite kalkulator baza prvo): ")
            l = input()
            for i in l:
                if not (i in ["0", "1", " "]):
                    v = False  
                    print("neispravan upis, molimo probajte ponovo")
        v = False
        while not v:
            v = True
            print("Molimo upisite paritet koji zelite koristiti (1 za parni, 0 za neparni): ")
            p = int(input())
            if p != 1 and p!=0:
                print("Neispravan unos probajte ponovo")
                v = False
        print("Rezultat:", codeHamming(l, p))
    elif c1 == 2:
        v = False
        while not v:
            v = True
            print("Molim vas upisite podatke koje zelite ekstraktirati (binarni broj, moze sadrzavati razmake): ")
            l = input()
            for i in l:
                if not (i in ["0", "1", " "]):
                    v = False  
                    print("neispravan upis, molimo probajte ponovo")
            dR, sR = decodeHamming(l)
            
        print("Podatci:", dR)
        print("Sigurnosni bitovi (od najmanjeg):", sR)
    else:
        v = False
        while not v:
            v = True
            print("Molim vas upisite podatke za koje zelite provjeriti sindrom i probati popraviti (provjera do dvije greske i popravak jedne) (binarni broj, moze sadrzavati razmake): ")
            l = input()
            for i in l:
                if not (i in ["0", "1", " "]):
                    v = False  
                    print("neispravan upis, molimo probajte ponovo")
        v = False
        while not v:
            v = True
            print("Molimo upisite paritet koji zelite koristiti (1 za parni, 0 za neparni): ")
            p = int(input())
            if p != 1 and p!=0:
                print("Neispravan unos probajte ponovo")
                v = False
        
        s = syndromeHammning(l, p)
        if s == 0:
            print("Kod je ispravan! (ili je li?)")
        else:
            print("Kod ima gresku")
            print("Sindrom:", s)
            print("Pokusaj popravljanja:")
            print(fixHamming(l, p))