def safeInput(msg, alphabet):
    v = False
    while v == False:
        v = True
        print(msg)
        p = input()
        for i in p:
            if not (i in alphabet):
                v = False
                print("Nije validan unos, probajte ponovo")
                break
                
    return p