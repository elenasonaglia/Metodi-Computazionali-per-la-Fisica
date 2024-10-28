# import
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('ExoplanetsPars_2024.csv.1', comment='#')
print (df.columns)
print(df['pl_orbperlim'])

#produca un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale;
plt.title( 'log massa dei pianeti', fontsize=15)
plt.scatter(df['pl_orbper'],df['pl_bmassj'], color='pink')
plt.xlabel('tempo[giorni]')
plt.ylabel('massa ')
plt.xscale('log')
plt.yscale('log')
plt.show()

plt.title('log rapporto Rmax^2/massa stellare', fontsize=15)
y1= df['pl_orbsmax']**2/df['st_mass']
plt.scatter(df['pl_orbper'],y1, color='pink')
plt.xlabel('tempo[giorni]')
plt.ylabel('massa ')
plt.xscale('log')
plt.yscale('log')
plt.show()


print(df['discoverymethod'])
m1= df.loc[df['discoverymethod']== 'Radial Velocity']
m2= df.loc[df['discoverymethod']== 'Transit']
plt.title( 'log massa dei pianeti', fontsize=15)
plt.scatter(m1['pl_orbper'],m1['pl_bmassj'], alpha=0.4, color='red',label='by radial velocity')
plt.scatter(m2['pl_orbper'],m2['pl_bmassj'], alpha=0.4, color='blue',label='by transit')
plt.xlabel('tempo[giorni]')
plt.ylabel('massa ')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()


print(df['pl_bmassj'])
#binning=(len(df['pl_bmassj'])**(1/2))
min=min(df['pl_bmassj'])
max=max(df['pl_bmassj'])
#istogramma
plt.title( ' massa dei pianeti', fontsize=15)
n1, bis1, p1 = plt.hist(m1['pl_bmassj'], bins=75, range=(0, max),alpha=0.40, color='blue',label='by radial velocity' )
n2, bis2, p2 = plt.hist(m2['pl_bmassj'], bins=75, range=(0, max),alpha=0.40, color='red',label='by transit' )
plt.xlabel('masse ', fontsize=16)
plt.legend()
plt.show()

#istogramma
plt.title( 'log massa dei pianeti', fontsize=15)
n1, bis1, p1 = plt.hist(m1['pl_bmassj'], bins=75, range=(0, max),alpha=0.40, color='blue',label='by radial velocity' )
n2, bis2, p2 = plt.hist(m2['pl_bmassj'], bins=75, range=(0, max),alpha=0.40, color='red',label='by transit' )
plt.xlabel('masse ', fontsize=16)
plt.yscale('log')
plt.legend()
plt.show()
