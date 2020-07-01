def encrypt(string_to_encrypt):
	encrypted_word = ''
	for i in string_to_encrypt:
		if i.isnumeric() == True:
			i = str(chr(ord(i) + 1))
			encrypted_word += i
		else:
			i = chr(ord(i) + 3)
			encrypted_word += i

	return encrypted_word

f = open('encrypted.txt', 'r')
content = f.read()
f2 = open('encrypted-backup.txt', 'a+')
f.close()

print('Creating backup file')
f2.write(content)

print('Encrypting original')

new_content = encrypt(content)
f = open('encrypted.txt', 'w')
f.write(new_content)

print('All Done!')





#word = input('Give me a sentence to encrypt:\n')
#print(encrypt(word))