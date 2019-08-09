import base64
import paramiko
import sys

def ssh_command(ssh):
    command = input("Command:")
    ssh.invoke_shell()
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read())

def ssh_connect(host, user, key):
    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=key)
        channel = ssh.invoke_shell()
        stdin = channel.makefile("wb")
        stdout = channel.makefile("rb")
        text = ''
        
        while (text != 'exit'):
            text =  input("Command:\t")
            stdin = text
            print(stdout.read())
            
    except Exception as e:
        print('Connection Failed')
        print(e)
        stdout.close()
        stdin.close()
        ssh.close()

if __name__=='__main__':
    user = 'horst'
    key = 'Jierdeliren@126'
    host = "eggplantcui.ca"
    
    
    ssh_connect(host, user, key)
    