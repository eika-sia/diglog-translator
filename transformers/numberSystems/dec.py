def codeDec(h):
    """_summary_

    Args:
        h (string, int): string with possible spaces or number in binary

    Returns:
        h (int): decimal value of binary input
    """
    h = str(h).replace(" ", "")
    sol = 0
    c = len(h)-1

    for i in h:
        sol += int(i)*2**c
        c -= 1

    return sol


def decodeDec(h):
    """_summary_

    Args:
        h (int, string): decimal number

    Returns:
        sol (string): binary number without spaces
    """
    h = int(h)
    sol = ""
    while h > 0:
        sol += str(h % 2)
        h = h//2

    return sol[::-1]
