from transformers.numberSystems.dec import codeDec, decodeDec


def codeBCD(h):
    """_summary_

    Args:
        h (int, string): decimal number

    Returns:
        sol (str): BCD coded integer with spaces each 4 digits
    """
    h = str(h)
    sol = ""
    
    for i in h:
        t = str(decodeDec(i))
        while len(t) < 4:
            t = "0" + t
        sol+= t + " "
    return sol

def decodeBCD(h):
    """_summary_

    Args:
        h (string,int): BCD coded number (with or without spaces)

    Returns:
        sol (int): BCD decoded number
    """
    h = str(h).replace(" ", "")
    n = (len(h)-1)//4*4+4

    sol = ""

    for i in range(0, n, 4):
        part = h[-(i+4):-(i+1)]+h[-(i+1)]
        sol = str(codeDec(part)) + sol
        
    return int(sol)