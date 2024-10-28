# import
import matplotlib.pyplot as plt
import pandas as pd


df_fromfile = pd.read_csv('kplr010666592-2011240104155_slc.csv')

#file che mi servono
print(df_fromfile['TIME'])
print(df_fromfile['PDCSAP_FLUX'])
print(df_fromfile['PDCSAP_FLUX_ERR'])

print (df_fromfile.columns)


#plot del flusso in funzione del tempo



ax = df_fromfile['TIME']

ay = df_fromfile['PDCSAP_FLUX']

#ayerr=df_fromfile['PDCSAP_FLUX_ERR']

plt.plot(ax,ay)
plt.title = 'FLUSSO'
plt.xlabel('tempo')
plt.ylabel('flusso')

plt.show()


#file con punti
plt.plot(ax, ay, 'o',  color='red'  )
plt.title = 'FLUSSO'
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.show()


#file con errori
plt.errorbar(ax, ay, yerr=df_fromfile['PDCSAP_FLUX_ERR'], fmt='o'  )
plt.title = 'FLUSSO'
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.savefig('plot.png')
plt.show()

#plot intorno ad uno dei minimi
axmasc=df_fromfile.loc[( df_fromfile['TIME']> 938.5) & ( df_fromfile['TIME']< 939.5)]

print (axmasc)
plt.errorbar(axmasc['TIME'], axmasc['PDCSAP_FLUX'] , yerr=axmasc['PDCSAP_FLUX_ERR'], fmt='o'  )
plt.title = 'FLUSSO'
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.savefig('plot.png')
plt.show()

# subplots

fig, asx= plt.subplots(figsize=(12,6))

asx.errorbar(ax, ay, yerr=df_fromfile['PDCSAP_FLUX_ERR'], fmt='o'  )
asx.set_xlabel('tempo')
asx.set_ylabel('flusso')





ins_asx = asx.inset_axes([0.75,  0.15, 0.25, 0.25]) # w.r.t. ax
ins_asx.errorbar(axmasc['TIME'], axmasc['PDCSAP_FLUX'] , yerr=axmasc['PDCSAP_FLUX_ERR'], fmt='o'  )



plt.show()
