import base64
import paramiko
import sys

hostname = sys.argv[1]
port = sys.argv[2] 
username = sys.argv[3]
password = sys.argv[4]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(hostname, username = username, password = password, port = port)
stdin, stdout, stderr = client.exec_command('cd /var/www/html \n pwd')
print(stdout.readlines())
stdin, stdout, stderr = client.exec_command('cd /var/www/html \n ls \n rm phpMyAdmin-4.8.5-all-languages.zip \n')
print(stdout.readlines())
    
client.close()