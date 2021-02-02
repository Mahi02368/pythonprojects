import os

#defining the migration function
def migration(user, password, host):
	os.system('wget -brc -o transfer_log.log --ftp-user="%s" --ftp-password=%s ftp://%s' % (user, password, host))

#gather info
print('Welcome to ''I Ceci'' migration system!\nIn order to achieve the best possible result, you should also place a database backup in your domain\'s public folder.')
print('The FTP account you are going to use should lead directly to your site root folder, in order to avoid downloading unnecessary files which could take more space then needed.\nTo start, please give us the following information:')
user = input('FTP Username: \n')
passwd = input('FTP Password: \n')
#port = input('Port: (if not provided, leave blank and we will use port 21 by default):\n')
host = input('FTP Host: (preferably an IP or servername):\n')

#take time
print('Thanks, we will now start the file migration process, it may take a while..')
#if port != '21':
#	migration(user, passwd, 21, host)
#else:
#	migration(user, passwd, port, host)
migration(user, passwd, host)

#profit
print('Done! you can import your database or run the database-import.py file. Thanks!')
quit()




