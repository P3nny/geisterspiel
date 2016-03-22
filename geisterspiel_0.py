from random import randint

print('Geisterspiel')
du_bist_mutig = True

while du_bist_mutig:
    geistertuer = randint(1, 3)
    print('Vor Dir sind drei Tueren.')
    print('Hinter einer ist ein Geist.')
    print('Welche Tuer oeffnest Du?')
    tuer = input('1, 2 oder 3?')
    tuer_nummer = int(tuer)
    if tuer_nummer == geistertuer:
    print('GEIST!')
    du_bist_mutig = False
    else:
    print('Kein Geist!')
    print('Du bist ein Zimmer weiter.')
print('Schnell weg!')

