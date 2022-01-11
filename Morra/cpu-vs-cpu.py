import random

# liste vuote + partite giocate, riempiremo le liste nel corso del programma
player_one = []
player_two = []
player_one_l = []
player_two_l = []
games = 1


def total(string):  # Calcolare il punteggio

    if string == 'Pareggio!' or string == 'non vince nessuno':
        player_two.append("T")
        player_one.append("T")
    elif string == 'Giocatore 1 vince':
        player_one.append("V")
        player_two.append("P")
    elif string == 'Giocatore 2 vince':
        player_two.append("V")
        player_one.append("P")


def scelta_numero(giocatore):
    scelta = random.randint(0, 10)
    print('Giocatore %s sceglie: %d' % (giocatore, scelta))
    return scelta


def numero_giocato(numero, giocatore):
    if numero <= 5:
        giocata = random.randint(0, numero)
    if numero > 5:
        giocata = random.randint(numero - 5, 5)
    print('Giocatore %s gioca: %d' % (giocatore, giocata))
    return giocata


def check_win(a, b):
    score = a + b
    if score == player_one_sceglie and score == player_two_sceglie:
        return 'Pareggio!'
    elif score == player_one_sceglie:
        return 'Giocatore 1 vince'
    elif score == player_two_sceglie:
        return 'Giocatore 2 vince'

    return 'non vince nessuno'


# while loop per non dare limiti di numero di partite
while player_one.count("V") < 3 and player_two.count("V") < 3:

    print("partita n: " + str(games))

    player_one_sceglie = scelta_numero('uno')
    player_two_sceglie = scelta_numero('due')
    player_one_gioca = numero_giocato(player_one_sceglie, 'uno')
    player_two_gioca = numero_giocato(player_two_sceglie, 'due')

    result = check_win(player_one_gioca, player_two_gioca)
    print(result)

    # Funzione per calcolare il totale
    total(result)

    player_one_l.append(str(player_one_sceglie))
    player_two_l.append(str(player_two_sceglie))

    games += 1


print('Giocatore 1: '+''.join(str(list(zip(player_one, player_one_l)))))
print('Giocatore 2: '+''.join(str(list(zip(player_two, player_two_l)))))

print("Partite totali: " + str(games))
exit()
