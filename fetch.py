#!/usr/bin/python3

#importer bibloteker som jeg trenger i knanao oden.
import paramiko
import time
import getpass

#her definerer vi variabler som bruker navn til servern vi skal koble oss til 
TARGET_IP = input("skriv in ip-en her: ")
BRUKERNAVN = input("skriv inn brukernav: ")
SSH_PORT = 22
PASSORD = getpass.getpass("skriv inn passord: ")


# her setter vi opp en ssh connection 
ssh_client = paramiko.SSHClient()
#her tar vi å auto godkjenner når vi ssh'er 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


#her setter vi en while løkka slik at den 
while True:
    try:
        # her kobler vi oss til ipen og ssh porten med bruker navn og passord 
        ssh_client.connect(TARGET_IP, SSH_PORT, BRUKERNAVN, PASSORD)
        
        koammandoer = [
            "uptime",  # Server tid oppe
            "free -h",  # hvor mye minne som blir brukt
            "df -h",  # disk plass 
            "top -b -n 1 | head -n 20"  # cpu prosess
        ]

        for kommando in koammandoer:
            #her bruker vi kommandoene vi har skrevet
            stdin, stdout, stderr = ssh_client.exec_command(kommando)
            #dekrypterer det vi har fått ut fra kommandoen 
            uttak = stdout.read().decode().strip()
            #printer kommadoen som blir brukt
            print(f"kommandoen: {kommando}\n")
            #printer outpout av kommandoen, altså det som har blitt dekryptert
            print(uttak)
            #legger til en ny linje for hver kommando sånn at det ikke skal bli så masete å se på
            print("----------------------------------\n")

    # denne her legger vi til i tilfelle noe går galt så ser vi hvor det skjedde 
    #feil i brukernavn og/eller passord 
    except paramiko.AuthenticationException:
        print("bruker navn og/eller passord er feil")
    #feil i ssh 
    except paramiko.SSHException as ssh_feil:
        print(f"det oppsto en feil i ssh{str(ssh_feil)}")
    #bare en feil generelt som ikke er knyttet til ssh eller brukernavn/passord
    except Exception as feil:
        print(f"det oppsto ett problem {str(feil)}")
    
    finally:
        #stenger ssh kobling 
        ssh_client.close()

    #vent 60 sekunder for den kjører while løkken på nytt
    time.sleep(60) 