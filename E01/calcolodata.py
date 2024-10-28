
###chieda in input la vostra data di nascita;
#calcoli la vostra età in anni, giorni e secondi;
#stampi a schermo i risultati con stringhe formattatate in modo che appaiano incolonnati;

from datetime import datetime, timedelta
# data e ora attuale


data=input ("immettere la propria data di nascita età in anni, giorni e secondi(es=23-9-2003 21:33:45):")
datenow = datetime.now()

mydatehr = datetime.strptime(data, "%d-%m-%Y %H:%M:%S")
timediff=datenow-mydatehr
anni= timediff.days/365
giorni= timediff.days
secondi=timediff.total_seconds()
print (type(secondi))
sec=secondi

print ("anni: {:>12d} ".format (int(anni)))
print ("giorni:{:>12d} ".format (giorni))
print ("secondi:{:>12f} ".format (sec))


