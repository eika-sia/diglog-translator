from transformers.coding.aiken import codeAiken, decodeAiken
from transformers.coding.bcd import codeBCD, decodeBCD
from transformers.coding.gray import checkGray, createGray
from transformers.coding.partitet import codePartitet
from transformers.coding.xs3 import codeXS3, decodeXS3
from valid import safeInput


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
    coderGray = {
        "name": "gray",
        "code": createGray,
        "decode": checkGray
    }
    coders = [coderAiken, coderBCD, coderXS3, coderGray]

    v_d = "0123456789"
    c0 = safeInput("Dobrodosli u translator kodova, zelite li prevesti nesto u kod (K), prevesti nesto iz koda (D) ili kalkulator Grayevog koda (G): ", "KDG")

    if c0 == "G":
        c1 = safeInput("Dobrodosli u kalkulator grayevog koda, za stvaranje novog grayevog koda unesite (K), za provjeru unesite (C): ", "KC")
        
        if c1 == "K":
            k = safeInput("Molimo unesite potrebnu duljinu koda", v_d)
            print(coderGray["code"](k, []))
        else:
            h = safeInput("Molimo unesite grayev kod koji treba provjeriti (staviti razmak izmedu svakog clana): ", "01 ")
            print(coderGray["decode"](h))
    
    elif c0 == "K":
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

        l = safeInput("Sada vas broj za input: ", v_d)

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

        l = safeInput("Sada vas broj za input (binarni input smije sadrzavati proizvoljne razmake): ", "01 ")

        print(ci["decode"](l))
