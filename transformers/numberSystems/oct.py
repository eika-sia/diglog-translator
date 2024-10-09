from transformers.numberSystems.dec import decodeDec


ALPHABET_O = [("0", "000"), ("1", "001"), ("2", "010"), ("3", "011"),
              ("4", "100"), ("5", "101"), ("6", "110"), ("7", "111")]


def codeOct(h):
    """_summary_

    Args:
        h (string,int): string with spaces or int, both binary

    Returns:
        sol (string): oct code in string type
    """
    h = str(h).replace(" ", "")
    n = (len(h)-1)//3*3+3

    sol = ""

    for i in range(0, n, 3):
        part = h[-(i+3):-(i+1)]+h[-(i+1)]
        partV = 0
        c = len(part)-1

        for j in part:
            partV += int(j)*2**c
            c -= 1

        sol = str(partV) + sol
    return sol


def decodeOct(h):
    """_summary_

    Args:
        h (string): oct code

    Returns:
        sol: binary code
    """
    sol = ""

    for i in h:
        t = str(decodeDec(i))
        while len(t) < 3:
            t = "0"+t
        sol += t + " "

    return sol
