import random

#liste vuote + partite giocate, riempiremo le liste nel corso del programma
player_one = []
player_two = []
games = 1


def total(): #Calcolare il punteggio
	totale = player_one_gioca + player_two_gioca
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
	

	#Funzione per numeri giocati e dichiarati
	print("Dichiari: ")
	player_one_grida = input()
	print("Giochi: ")
	player_one_gioca = input()
	#int(player_one_grida)
	#int(player_one_gioca)
	player_two_grida = random.randint(0, 10)
    

	if player_two_grida <= 5:
		player_two_gioca = random.randint(0, player_two_grida)
	if player_two_grida > 5:
		player_two_gioca = random.randint(player_two_grida - 5, 5)

	#print("Giocatore uno grida: ")
	#print(player_one_grida)
	#print("E gioca: ")
	#print(player_one_gioca)
	print("Giocatore due grida: ")
	print(player_two_grida)
	print("E gioca: ")
	print(player_two_gioca)
	
	#Funzione per calcolare il totale
	total()

	score = player_one_gioca + player_two_gioca
	if score == player_one_grida:
		print('Giocatore 1 vince')
	elif score == player_two_grida:
		print('Giocatore 2 vince')
	else:
		print('non vince nessuno')
	
	games += 1

#stampiamo le liste per controllare che il cecck sia stato fatto correttamente + il numero di partite necessarie + exit dal programma
print(player_one)
print(player_two)

print("Partite totali: " + str(games-1))
exit()



	
	
	
	

