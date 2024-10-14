"""
- Binary as a basis for the main system, main converts everything between binary and selected.
- Every base converter module has two main functions:
    1. code: binary -> coded (into base) {code$base$}
    2. decode: coded (base) -> binary {decode$base$}

- Every coding module has two main functions:
    1. code: decimal -> coded (into code) {code$code$}
    2. decode: coded (code) -> decimal {decode$code$}

- Modular form simplifies each individual coder/decoder 
- Chosen input form goes to binary, output gets translated

- each imported module gets sent into a list of dictionaries with following entries:
coder$base/code$ = {
    name: (string),
    code: (function),
    decode: (function),
    valid: (string) [string of valid characters]
}

Hamming kod je poseban!!
code -> u hamming code
decode -> vraca data i security bits
syndrome -> racuna sindrom sa danim paritetom
fix -> pomocu sindroma pokusava popravit error
"""

from main_b import mainB
from main_h import mainH
from main_k import mainK


c0 = 0
while c0 == 0:
    print("Dobrodosli u univerzalni translator, ako zelite koristit translator izmedu brojevnik baza molimo upisite B, za kodove molimo upisite K i za hammingov kod H: ")
    c0 = input()
    if ((c0 != "K") and (c0 != "B") and (c0 != "H")):
        c0 = 0
        print("Nije validan unos molim probati ponovo")

if c0 == "B":
    mainB()
elif c0 == "K":
    mainK()
else:
    mainH()
