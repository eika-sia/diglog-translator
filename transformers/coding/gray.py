
def createGray(k, sol=[]):
    """_summary_

    Args:
        k (int): min length needed

    Returns:
        sol: generated gray kod of length needed
    """
    kN = k
    while not (((kN+1) & (kN) == 0) and kN+1 != 0):
        kN += 1
    kN += 1

    if kN <= 2:
        return ["0", "1"]
    else:
        lS = len(sol)
        if (((lS+1) & (lS) == 0) and lS+1 != 0) or lS == 0:
            sol = ["0", "1"]

        if lS*2 != kN:
            sol = createGray(kN//2-1, sol)

        solT = sol+sol[::-1]

        for i in range(len(solT)//2):
            print(solT[i], solT[-i-1])
            solT[i] = "0"+solT[i]
            solT[-i-1] = "1" + solT[-i-1]

    return solT


def checkGray(h):
    h = h.split(" ")
    i = 0
    while i < len(h)-1:
        xOr = ""
        for j in range(len(h[i])):
            xOr += str(int(h[i][j]) ^ int(h[i+1][j]))
            
        if xOr.count("1") > 1:
            return "Nije validan Grayev kod"
        
        i+=1
    return "Validan Grayev kod"