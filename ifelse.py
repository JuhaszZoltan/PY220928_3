kor = int(input('Hány éves vagy? '))

if kor < 18:
    print('akkor még nem mehetsz be dohiboltba')
    print('ez van')
    print('szokj le még most, te nyomi!')
else:
    print('na, mostmár IGGAZY férfi vagy!')
    print('már úgy cseszed el az életed, ahogy akarod!')

# ------------------------

jegy = int(input('milyen jegyet kaptál fizikából? '))

print('ezt úgy mondják szépen, hogy', end=' ')
if jegy == 1: print('ELÉGTELEN')
elif jegy == 2: print('ELÉGSÉGES')
elif jegy == 3: print('KÖZEPES')
elif jegy == 4: print('JÓ')
else: print('JELES')