import os

def ifconfig():
	wlan = []
	eth = []
	os.system('ifconfig > random.log')
	with open('random.log','r') as file:
		text = file.read()
		elements = text.split()
		for word in elements:
			if 'wlan' in word:
				wlan.append(word)
			elif 'eth' in word and word[-2].isdigit():
				eth.append(word)
	print(wlan)
	print(eth)
	return 0

print(ifconfig())


