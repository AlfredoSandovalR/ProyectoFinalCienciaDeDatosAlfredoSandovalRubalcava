import pandas as pd

m13 = pd.read_csv('c900-c959m13.csv')
m14 = pd.read_csv('c900-c959m14.csv')
m15 = pd.read_csv('c900-c959m15.csv')
m16 = pd.read_csv('c900-c959m16.csv')
m17 = pd.read_csv('c900-c959m17.csv')
m18 = pd.read_csv('c900-c959m18.csv')

JuntosAB= m13.append(m14)
dfJuntosAB=pd.DataFrame(JuntosAB)
#print(dfJuntosAB)

JuntosABC= dfJuntosAB.append(m15)
dfJuntosABC=pd.DataFrame(JuntosABC)
#print(dfJuntosABC)

JuntosABCD= dfJuntosABC.append(m16)
dfJuntosABCD=pd.DataFrame(JuntosABCD)
#print(dfJuntosABCD)

JuntosABCDE= dfJuntosABCD.append(m17)
dfJuntosABCDE=pd.DataFrame(JuntosABCDE)
#print(dfJuntosABCDE)

JuntosABCDEF= dfJuntosABCDE.append(m18)
dfJuntosABCDEF=pd.DataFrame(JuntosABCDEF)
print(dfJuntosABCDEF)

dfJuntosABCDEF.to_csv (r'C:\Users\alqui\Desktop\Proyectos Finales\Ciencia de datos\Tablas6añosMcxxx\c900-c959m13-18SinAcumular.csv', index = False, header=True)
