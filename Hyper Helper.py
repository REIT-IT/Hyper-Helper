import os 

nmap = "1"
ssh = "2"
bitchx = "3"
s_e_t = "4"
esci = "99"
o = "-O"
a = "-A"
nop = "nessun parametro"
x = "-X"
chiocciola = "@"
si = "si"
Si = "Si"
SI = "SI"
no = "no"
No = "No"
NO = "NO"

print ("Seleziona l'azione che ti interessa ")
print (" ")
print ("   1) Nmap")
print ("   2) SSH")
print ("   3) BitchX")
print ("   4) Social-Engineering-Toolkit")
print (" ")
print ("   99) Esci")

scelta = input(">> ")
#INIZIO SEZIONE NMAP
if scelta == nmap:
    parametro = input(">> -O,-A o nessun parametro? ")
    ip = input(">> Inserisci l'IP o il DNS che vuoi scansionare: ")
    if parametro == o:
        os.system("sudo nmap -O " + str(ip))
        print (" ")
        print (">> Scansione eseguita alla perfezione :D ")
    elif parametro == a:
        os.system("sudo nmap -A " + str(ip))
        print (" ")
        print (">> Scansione eseguita alla perfezione :D ")
    elif parametro == nop:
        os.system("nmap " + str(ip))
        print (" ")        
        print (">> Scansione eseguita alla perfezione :D ")
#FINE SEZIONE NMAP
#INIZIO SEZIONE SSH
elif scelta == ssh:
    parametro = input(">> -X o nessun parametro? ")
    nomeutente = input(">> Inserisci il nome dell'utente al quale ti vuoi collegare: ")
    ip = input(">> Inserisci l'IP a cui ti vuoi collegare: ")
    porta = input(">> Inserisci la porta alla quale ti vuoi collegare, es. 22: ")
    if parametro == x:
        os.system("ssh -X " + nomeutente + chiocciola + str(ip) + " -p " + porta)
        print (" ")
        print (">> Ti sei disconnesso con successo dalla porta " + porta + " :D ")
    elif parametro == no:
        os.system("ssh " + nomeutente + chiocciola + str(ip) + " -p " + porta)
        print (" ")
        print (">> Ti sei disconnesso con successo dalla porta " + porta + " :D ")
#FINE SEZIONE SSH
#INIZIO SEZIONE BITCHX
elif scelta == bitchx:
    print (">> Apertura BitchX in corso... ")
    os.system("sudo BitchX")
    print (" ")
    print (">> Chiusura BitchX riuscita correttamente :D ")
#FINE SEZIONE BITCHX
#INIZIO SEZIONE SET
elif  scelta == s_e_t:
    print (">> Apertura SET in corso ... ")
    os.system("sudo setoolkit")
    print (" ")
    print (">> Chiusura SET riuscita correttamente :D ")
#FINE SEZIONE SET
#INIZIO SEZIONE USCITA
elif scelta == esci:
    si_o_no = input(">> Vuoi veramente uscire? ")
    if si_o_no == si:
        os.system("exit")
    elif si_o_no == Si:
        os.system("exit")
    elif si_o_no == SI:
        os.system("exit")
    elif si_o_no == no:
        print (">> Mi prendi in giro? Ora esci lo stesso. :O ")
    elif si_o_no == No:
        print (">> Mi prendi in giro? Ora esci lo stesso. :O ")
    elif si_o_no == No:
        print (">> Mi prendi in giro? Ora esci lo stesso. :O ")
