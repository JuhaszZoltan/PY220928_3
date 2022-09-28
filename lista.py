#                     0         1         2        3         4        5         6
nevek:list[str] = ['Bianka', 'Renáta', 'Rita', 'Zsuzsa', 'Zsuzsa', 'Emese', 'Veronika']

print(nevek)
print(f'lista hossza: {len(nevek)}')

if input('szeretnél új nevet hozzáadni? ') == 'igen':
    uj_nev:str = input('írd be az új nevet: ')
    nevek.append(uj_nev)

print('A lista elemei:')
for nev in nevek:
    print(f'\t{nev}')