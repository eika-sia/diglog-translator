
def codePartitet(h, p):
    # p == 1 => parni
    h = str(h).replace(" ", "")
    c = 0
    for i in h:
        if i == "1":
            c += 1

    if p == 1 and c % 2 == 1:
        h = "1"+h
    elif p == 0 and c % 2 == 0:
        h = "1"+h
    else:
        h = "0" + h

    return h

def decodePartitet(h, p):
    h = str(h).replace(" ", "")
    hA = codePartitet(h[1:], p)
    if h == hA:
        return h[1:]
    else:
        return "Postoji pogreska u podatcima"