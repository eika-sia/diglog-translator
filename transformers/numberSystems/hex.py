from transformers.numberSystems.dec import decodeDec

ALPHABET = [(10, "A"), (11, "B"), (12, "C"), (13, "D"), (14, "E"), (15, "F")]


def codeHex(h):
    """_summary_

    Args:
        h (string,int): string with spaces or int, both binary

    Returns:
        sol (string): hex code in string type
    """
    h = str(h).replace(" ", "")
    n = (len(h)-1)//4*4+4

    sol = ""

    for i in range(0, n, 4):
        part = h[-(i+4):-(i+1)]+h[-(i+1)]
        partV = 0
        c = len(part)-1

        for j in part:
            partV += int(j)*2**c
            c -= 1
        if partV >= 10:
            for x in ALPHABET:
                if x[0] == partV:
                    sol = x[1] + sol
        else:
            sol = str(partV) + sol
    return sol


def decodeHex(h):
    sol = ""
    for i in h:
        t = i
        if t in "ABCDE":
            for j in ALPHABET:
                if i == j[1]:
                    t = j[0]
        t = str(decodeDec(t))
        while len(t) < 4:
            t = "0"+t
        sol += t + " "
    return sol
