import os
#defining the migration function
def dbimport(user, passwd, database , backup):
	os.system('mysql -u%s --password=%s %s < %s' % (user, passwd, database , backup))

#gather info
print("Welcome to Mahi's MYSQL database import system!\n")
print('In order for the tool to function correctly, you should place an .sql file in your site\'s root folder.')
print('Please provide me with the following database info')
user = input('MySQL Username: \n')
database = input('Database Name:\n')
passwd = input('MySQL User Password: \n')
backup = input('SQL FileName:\n')

#take time
print('Thanks, we will now start the file import process, it may take a while..')

dbimport(user, passwd, database , backup)

#profit
print('Done! The file was imported in your %s database. Thanks!' % database)
quit()
