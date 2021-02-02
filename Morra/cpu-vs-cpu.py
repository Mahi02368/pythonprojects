import random

#liste vuote + partite giocate, riempiremo le liste nel corso del programma
player_one = []
player_two = []
player_one_l = []
player_two_l = []
games = 1


def total(a, b): #Calcolare il punteggio
	totale = a + b
	if totale == player_one_grida and totale == player_two_grida:		
		player_two.append("T")
		player_one.append("T")
	elif totale == player_one_grida:
		player_one.append("V")
		player_two.append("P")
	elif totale == player_two_grida:
		player_two.append("V")
		player_one.append("P")
	else:
		player_two.append("N")
		player_one.append("N")


#while loop per non dare limiti di numero di partite
while player_one.count("V") < 3 and player_two.count("V") < 3:
	
	print("partita n: " + str(games))
	
	player_one_grida = random.randint(0, 10)
	player_two_grida = random.randint(0, 10)
    
 	if player_one_grida <= 5:
		player_one_gioca = random.randint(0, player_one_grida)
	if player_one_grida > 5:
		player_one_gioca = random.randint(player_one_grida - 5, 5)

	if player_two_grida <= 5:
		player_two_gioca = random.randint(0, player_two_grida)
	if player_two_grida > 5:
		player_two_gioca = random.randint(player_two_grida - 5, 5)

	print("Giocatore uno grida: ")
	print(player_one_grida)
	print("E gioca: ")
	print(player_one_gioca)
	print("Giocatore due grida: ")
	print(player_two_grida)
	print("E gioca: ")
	print(player_two_gioca)
	
	#Funzione per calcolare il totale
	total(player_one_gioca, player_two_gioca)

	score = player_one_gioca + player_two_gioca
	if score == player_one_grida and score == player_two_grida:
		print('Pareggio!')
	elif score == player_one_grida:
		print('Giocatore 1 vince')
	elif score == player_two_grida:
		print('Giocatore 2 vince')
	else:
		print('non vince nessuno')

	player_one_l.append(str(player_one_grida))
	player_two_l.append(str(player_two_grida))
	
	games += 1


print('Giocatore 1: '+''.join(str(list(zip(player_one, player_one_l)))))
print('Giocatore 2: '+''.join(str(list(zip(player_two, player_two_l)))))

print("Partite totali: " + str(games))
exit()

