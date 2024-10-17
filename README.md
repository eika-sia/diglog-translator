## Translator razlicitih brojevnih sustava i kodova

Ovaj projekt napravljen je za predmet diglog (0036568580). Projekt se koristi pokretanjem datoteke main.py i prolazenjem kroz dialog koji je uprogramiran.

## Napomene

### Programi su segmentirani na sljedeci nacin:

### 1. root

Folder sadrzi dva programa i dva foldera:
- main.py -> glavni program i odabir te preusmjeravanje u iduce opcije
- valid.py -> sadrzi redizajnirani input za sigurno unosenje podataka

#### 2. main_e folder

Folder sadrzi dodatne opcije dialoga izabrane u main.py
- main_b.py -> odabir opcija za brojevne sustave
- main_h.py -> odabir opcija za Hammingov kod
- main_k.py -> odabir opcija za ostale kodove (bcd, xs3, aiken)

#### 3. transformers - numberSystems

Folder sadrzi programe sortirane po brojevnim sustavima koji kodiraju u i iz binarnog sustava
- dec.py -> dekadski sustav
- hex.py -> heksadekadski sustav
- oct.py -> oktalni sustav

#### 4. transformers - coding

Folder sadrzi programe sortirane po tipu koda koji se kodiraju u i iz dekadskog (bcd, xs3, aiken) ili binarnog (hamming)
- aiken.py -> aikenov kod
- bcd.py -> bcd kod
- gray.py -> grayev kod
- hamming.py -> hammingov kod
- partitet.py -> zastita 1D partitetom (nije koristen u main fileovima igdje)
- xs3.py -> xs3 kod

### Koristenje

Preporuceno koristenje je kroz main file ali s obzirom na segmentaciju i malo medusobne ovisnosti svaki od individualnih fileova moguce je uzeti i prenamjeniti za vlastite potrebe te svaki individualni file iz main_e foldera moze se koristiti individualno.

### Ocekivanje kod ocjenjivanja

Prilikom zadavanja zadatka bilo je zadano odraditi samo jedan zadatak tako da u tu svrhu predajem svoj kalkulator Hammingovih kodova. Ostatak programa predajem kao extra za jedan centralizirani sustav u slucaju da bude objavljen kako bi bio prakticniji za koristenje.

### TO-DO

Ovo su potencijalni dodatci programu:

- graficko sucelje za lakse koristenje (tkinter)
- pretvarac proizvoljnih baza (do neke razine 10 (znamenke) + 26 slova -> 36 maks baza sa konvencijonalno jednostavnim razumjevanjem vrijednosti)