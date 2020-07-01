def decrypt(string_to_decrypt):
	decrypted_string = ''
	for i in string_to_decrypt:
		if i.isnumeric() == True:
			i = str(chr(ord(i) - 1))
			decrypted_string += i
		else:
			i = chr(ord(i) - 3)
			decrypted_string += i

	return decrypted_string

f = open('encrypted.txt', 'r')
content = f.read()
f2 = open('encrypted-backup.txt', 'a+')
f.close()

print('Creating backup file')
f2.write(content)

print('Encrypting original')

new_content = decrypt(content)
f = open('encrypted.txt', 'w')
f.write(new_content)

print('All Done!')
