from transformers.numberSystems.dec import codeDec, decodeDec


def codeAiken(h):
    """_summary_

    Args:
        h (int, string): decimal number

    Returns:
        sol (str): aiken coded integer with spaces each 4 digits
    """
    h = str(h)
    sol = ""

    for i in h:
        t = i
        if int(i) > 4:
            t = int(i) + 6
        t = str(decodeDec(t))
        while len(t) < 4:
            t = "0" + t
        sol += t + " "
    return sol


def decodeAiken(h):
    """_summary_

    Args:
        h (string,int): Aiken coded number (with or without spaces)

    Returns:
        sol (int): Aiken decoded number
    """
    h = str(h).replace(" ", "")
    n = (len(h)-1)//4*4+4

    sol = ""

    for i in range(0, n, 4):
        part = h[-(i+4):-(i+1)]+h[-(i+1)]
        partV = 0
        for i in range(len(part)):
            if i % 2 == 0:
                partV += 2 * int(part[i])
            elif i == 1:
                partV += 4 * int(part[1])
            else:
                partV += int(part[i])
        sol = str(partV) + sol

    return int(sol)
