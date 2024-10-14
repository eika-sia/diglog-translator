from transformers.coding.aiken import codeAiken, decodeAiken
from transformers.coding.bcd import codeBCD, decodeBCD
from transformers.coding.xs3 import codeXS3, decodeXS3


def mainK():
    coderAiken = {
        "name": "aiken",
        "code": codeAiken,
        "decode": decodeAiken
    }
    coderBCD = {
        "name": "BCD",
        "code": codeBCD,
        "decode": decodeBCD
    }
    coderXS3 = {
        "name": "XS3",
        "code": codeXS3,
        "decode": decodeXS3
    }
    coders = [coderAiken, coderBCD, coderXS3]

    v_d = "0123456789"
    v_k = "01 "
    c0 = 0
    while c0 == 0:
        print("Dobrodosli u translator kodova, zelite li prevesti nesto u kod (K) ili prevesti nesto iz koda (D): ")
        c0 = input()
        if ((c0 != "K") and (c0 != "D")):
            c0 = 0
            print("Nije validan unos molim probati ponovo")

    if c0 == "K":
        ci = 0
        while ci == 0:
            print(
                "Dobrodosli u translator u kodove, za pocetak upisite kod za input (aiken, BCD, XS3): ")
            bi = input()
            for i in coders:
                if i["name"] == bi:
                    ci = i
            if ci == 0:
                print("Nije validan unos molim probati ponovo")

        v = False
        while not v:
            print("Sada vas broj za input: ")
            l = input()
            v = True
            for i in l:
                if not (i in v_d):
                    v = False
            if not v:
                print("Nije validan unos molim probati ponovo")

        print(ci["code"](l))
    else:
        ci = 0
        while ci == 0:
            print("Dobrodosli u translator iz kodova, za pocetak upisite kod kojim ste kodirali (aiken, BCD, XS3): ")
            bi = input()
            for i in coders:
                if i["name"] == bi:
                    ci = i
            if ci == 0:
                print("Nije validan unos molim probati ponovo")

        v = False
        while not v:
            print(
                "Sada vas broj za input (binarni input smije sadrzavati proizvoljne razmake): ")
            l = input()
            v = True
            for i in l:
                if not (i in v_k):
                    v = False
            if not v:
                print("Nije validan unos molim probati ponovo")

        print(ci["decode"](l))
