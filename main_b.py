from transformers.numberSystems.dec import codeDec, decodeDec
from transformers.numberSystems.hex import codeHex, decodeHex
from transformers.numberSystems.oct import codeOct, decodeOct


def mainB():
    coderBin = {
        "name": "bin",
        "code": lambda x: x,
        "decode": lambda x: x,
        "valid": "01 "
    }
    coderDec = {
        "name": "dec",
        "code": codeDec,
        "decode": decodeDec,
        "valid": "0123456789"
    }
    coderHex = {
        "name": "hex",
        "code": codeHex,
        "decode": decodeHex,
        "valid": "0123456789ABCDEF"
    }
    coderOct = {
        "name": "oct",
        "code": codeOct,
        "decode": decodeOct,
        "valid": "01234567"
    }

    coders = [coderBin, coderDec, coderHex, coderOct]

    ci = 0
    while ci == 0:
        print("Dobrodosli u translator baza, za pocetak upisite bazu broja za input (bin, dec, oct, hex): ")
        bi = input()
        for i in coders:
            if i["name"] == bi:
                ci = i
        if ci == 0:
            print("Nije validan unos molim probati ponovo")

    v = False
    while not v:
        print("Sada vas broj za input (za hex koristiti sva velika slova, binarni inputi mogu sadrzavati proizvoljne razmake): ")
        l = input()
        v = True
        for i in l:
            if not (i in ci["valid"]):
                v = False
        if not v:
            print("Nije validan unos molim probati ponovo")

    co = 0
    while co == 0:
        print("Hvala puno! Sada koja je zeljena baza za output (bin, dec, oct, hex): ")
        bo = input()
        for i in coders:
            if i["name"] == bo:
                co = i
        if co == 0:
            print("Nije validan unos molim probati ponovo")

    print(co["code"](ci["decode"](l)))
