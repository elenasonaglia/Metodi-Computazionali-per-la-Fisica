
gg_settimana=['lunedì', 'martedì','mercoledì','giovedì','venerdì','sabato','domenica']
gg_settimana_ott=gg_settimana[ 1:]+gg_settimana*3+gg_settimana[:5]
print(len(gg_settimana_ott))



dict={ 1: gg_settimana_ott[0]}
for i in range (1,31):
 dict.update({ i+1:gg_settimana_ott[i] })
print (dict)
