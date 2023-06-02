#!/usr/bin/python3

#importer bibloteker som jeg trenger i knanao oden.
import paramiko
import time

#her definerer vi variabler som bruker navn til servern vi skal koble oss til 
TARGET_IP = input("skriv in ip-en her: ")
BRUKERNAVN = "vetle"
SSH_PORT = 22
PASSORD = "changeme"
koammandoer = [
    "uptime",  # Server tid oppe
    "free -m",  # hvor mye minne som blir brukt
    "df -h",  # disk plass 
    "top -i"  # cpu prosess
]

# her setter vi opp en ssh connection 
ssh_client = paramiko.SSHClient()
#her tar vi å auto godkjenner når vi ssh'er 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


#her setter vi en while løkka slik at den 
while True:
    try:
        # her kobler vi oss til ipen og ssh porten med bruker navn og passord 
        ssh_client.connect(TARGET_IP, SSH_PORT, BRUKERNAVN, PASSORD)
        
    # denne her legger vi til i tilfelle noe går galt så ser vi hvor det skjedde 
    except paramiko.AuthenticationException:
        print("bruker navn og/eller passord er feil")
    