import os 

nmap = "1"
ssh = "2"
bitchx = "3"
s_e_t = "4"
esci = "99"
o = "-O"
a = "-A"
nop = "nessun parametro"
noop = "no parameter"
x = "-X"
chiocciola = "@"
si = "si"
Si = "Si"
SI = "SI"
no = "no"
No = "No"
NO = "NO"

print (" _    _   __    __   _ ___    ______    ____                   _    _       ")
print ("| |  | |  \ \  / /  | '_  \  |  ____|  |  _ \                 (_)  | |___     ")
print ("| |__| |   \ \/ /   | |_)    | |___    | |_) )   ___           _   |  ___|  ___ ")
print ("|  __  |    |  |    | .___/  |  ___|   |    /   / __|  |   |  | |  | |     / _ \ ")
print ("| |  | |    |  |    | |      | |____   | |\ \   \__ \  |   |  | |  | |       __/ ")
print ("|_|  |_|    |__|    |_|      |______|  |_| \_\  |___/  |___|  |_|  |_|     \___| ")
print (" ")
print ("                                        Developed by REIT            ")
print ("                                     REIT on Twitter @reitswh ")
print ("                                  Developed by Riccardo Berbeglia ")
print ("                              Riccardo Berbeglia on Twitter @HackingRed ")
print (" ")
print ("                                        Select the language")
print ("                                           [1]: English. ")
print ("                                           [2]: Italiano. ")
print (" ")
print ("                                           [99]: Exit. ")

Inglese = "1"
Italiano = "2"
Exit = "99"
sceltalingua = input(">> ")
if sceltalingua == Italiano:
    os.system("clear")
    print ("Seleziona l'azione che ti interessa ")
    print (" ")
    print ("[1] Nmap. ")
    print ("[2] SSH. ")
    print ("[3] BitchX. ")
    print ("[4] Social-Engineering-Toolkit. ")
    print (" ")
    print ("[99] Esci. ")

    scelta = input(">> ")
#INIZIO SEZIONE NMAP
    if scelta == nmap:
        os.system("clear")
        parametro = input(">> -O,-A o nessun parametro? ")
        os.system("clear")
        ip = input(">> Inserisci l'IP o il DNS che vuoi scansionare: ")
        if parametro == o:
            os.system("clear")
            os.system("sudo nmap -O " + str(ip))
            print (" ")
            print (">> Scansione eseguita alla perfezione :D ")
        elif parametro == a:
            os.system("clear")
            os.system("sudo nmap -A " + str(ip))
            print (" ")
            print (">> Scansione eseguita alla perfezione :D ")
        elif parametro == nop:
            os.system("clear")
            os.system("nmap " + str(ip))
            print (" ")        
            print (">> Scansione eseguita alla perfezione :D ")
#FINE SEZIONE NMAP
#INIZIO SEZIONE SSH
    elif scelta == ssh:
        os.system("clear")
        parametro = input(">> -X o nessun parametro? ")
        nomeutente = input(">> Inserisci il nome dell'utente al quale ti vuoi collegare: ")
        ip = input(">> Inserisci l'IP a cui ti vuoi collegare: ")
        porta = input(">> Inserisci la porta alla quale ti vuoi collegare, es. 22: ")
        if parametro == x:
            os.system("clear")
            os.system("ssh -X " + nomeutente + chiocciola + str(ip) + " -p " + porta)
            print (" ")
            print (">> Ti sei disconnesso con successo dalla porta " + porta + " :D ")
        elif parametro == no:
            os.system("clear")
            os.system("ssh " + nomeutente + chiocciola + str(ip) + " -p " + porta)
            print (" ")
            print (">> Ti sei disconnesso con successo dalla porta " + porta + " :D ")
#FINE SEZIONE SSH
#INIZIO SEZIONE BITCHX
    elif scelta == bitchx:
        os.system("clear")
        print (">> Apertura BitchX in corso... ")
        os.system("sudo BitchX")
        print (" ")
        print (">> Chiusura BitchX riuscita correttamente :D ")
#FINE SEZIONE BITCHX
#INIZIO SEZIONE SET
    elif  scelta == s_e_t:
        os.system("clear")
        print (">> Apertura SET in corso ... ")
        os.system("sudo setoolkit")
        print (" ")
        print (">> Chiusura SET riuscita correttamente :D ")
#FINE SEZIONE SET
#INIZIO SEZIONE USCITA
    elif scelta == esci:
        os.system("exit")


#INGLESE
#INGLESE

elif sceltalingua == Inglese:
    os.system("clear")
    print ("Select the action that want carry out: ")
    print (" ")
    print ("   1) Nmap")
    print ("   2) SSH")
    print ("   3) BitchX")
    print ("   4) Social-Engineering-Toolkit")
    print (" ")
    print ("   99) Exit")

    scelta = input(">> ")
#INIZIO SEZIONE NMAP
    if scelta == nmap:
        os.system("clear")
        parametro = input(">> -O,-A or no parameter? ")
        ip = input(">> Enter the IP you want to scan: ")
        if parametro == o:
            os.system("clear")
            os.system("sudo nmap -O " + str(ip))
            print (" ")
            print (">> Scan successfully completed :D ")
        elif parametro == a:
            os.system("clear")
            os.system("sudo nmap -A " + str(ip))
            print (" ")
            print (">> Scan successfully completed :D ")
        elif parametro == noop:
            os.system("clear")
            os.system("nmap " + str(ip))
            print (" ")        
            print (">> Scan successfully completed :D ")
#FINE SEZIONE NMAP
#INIZIO SEZIONE SSH
    elif scelta == ssh:
        os.system("clear")
        parametro = input(">> -X or no parameter? ")
        nomeutente = input(">> Enter the username you want to connect to: ")
        ip = input(">> Insert the IP to which you want connect : ")
        porta = input(">> Enter the port to which you want to connect, example 22: ")
        if parametro == x:
            os.system("clear")
            os.system("ssh -X " + nomeutente + chiocciola + str(ip) + " -p " + porta)
            print (" ")
            print (">> You have disconnected successfully from the port " + porta + " :D ")
        elif parametro == noop:
            os.system("clear")
            os.system("ssh " + nomeutente + chiocciola + str(ip) + " -p " + porta)
            print (" ")
            print (">> You have disconnected successfully from the port " + porta + " :D ")
#FINE SEZIONE SSH
#INIZIO SEZIONE BITCHX
    elif scelta == bitchx:
        os.system("clear")
        print (">> Opening BitchX... ")
        os.system("sudo BitchX")
        print (" ")
        print (">> Closing successfully BitchX :D ")
#FINE SEZIONE BITCHX
#INIZIO SEZIONE SET
    elif  scelta == s_e_t:
        os.system("clear")
        print (">> Opening SET ... ")
        os.system("sudo setoolkit")
        print (" ")
        print (">> Closing successfully S.E.T :D ")
#INIZIO SEZIONE USCITA

    elif scelta == Exit:
        os.system("exit")
