from random import randint

print('Geisterspiel\n')
du_bist_mutig = True
score = 0

while du_bist_mutig:
	geistertuer = randint(1, 3)
	print('Vor Dir sind drei Tueren.')
	print('Hinter einer ist ein Geist.')
	print('Welche Tuer oeffnest Du?\n')
	tuer = input('1, 2 oder 3?\n')
	tuer_nummer = int(tuer)
	if tuer_nummer == geistertuer:
		print('\n GEIST!')
		du_bist_mutig = False
	else:
		print('\n Kein Geist! \n')
		print('Du bist ein Zimmer weiter.')
		score = score +1
print('\n Schnell weg!')
print('\n Spiel vorbei. Deine Punkte:', score, '\n')

