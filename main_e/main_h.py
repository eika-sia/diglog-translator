
from transformers.coding.hamming import codeHamming, decodeHamming, fixHamming, syndromeHammning
from valid import safeInput

def mainH():
    c1 = int(safeInput("Dobrodosli u Hamming kod kalkulator, za kodiranje podataka upisite 1, za ekstrakciju podataka upisite 2, za sindrom i popravljanje koda upisite 3 ", "123"))
            
    if c1 == 1:
        l = safeInput("Molim vas upisite podatke koje zelite kodirati (binarni broj, moze sadrzavati razmake, za ostale brojeve pokrenite kalkulator baza prvo): ", "01 ")
        p = safeInput("Molimo upisite paritet koji zelite koristiti (1 za parni, 0 za neparni): ", "01")
        
        print("Rezultat:", codeHamming(l, p))
    elif c1 == 2:
        l = safeInput("Molim vas upisite podatke koje zelite ekstraktirati (binarni broj, moze sadrzavati razmake): ", "01 ")
        dR, sR = decodeHamming(l)
            
        print("Podatci:", dR)
        print("Sigurnosni bitovi (od najmanjeg):", sR)
    else:
        l = safeInput("Molim vas upisite podatke za koje zelite provjeriti sindrom i probati popraviti (provjera do dvije greske i popravak jedne) (binarni broj, moze sadrzavati razmake): ", "01 ")
        p = safeInput("Molimo upisite paritet koji zelite koristiti (1 za parni, 0 za neparni): ", "01")
        
        s = syndromeHammning(l, p)
        if s == 0:
            print("Kod je ispravan! (ili je li?)")
        else:
            print("Kod ima gresku")
            print("Sindrom:", s)
            print("Pokusaj popravljanja:")
            print(fixHamming(l, p))