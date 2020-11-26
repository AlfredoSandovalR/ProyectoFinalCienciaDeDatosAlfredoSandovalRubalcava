import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

# Se lee el CSV, cambias a tu csv este archivo
c220_c959m13_18ConAcumular = pd.read_csv('c220-c959m13-18ConAcumularGrupo.csv')
# Se imprime la cabeza del archivo para ver que se haya leído ben el CSV
#cabeza = c220_c959m13_18ConAcumular.head()
#print(cabeza)

# Se genera la estadística descriptiva de las edades y los canceres columna por columna y al final todas juntas
dfCancer = pd.DataFrame(c220_c959m13_18ConAcumular)
datosTotalesEdad = dfCancer['c220-c249m'].describe()
print(datosTotalesEdad)

#normc220_c249m= random.normal(loc=366.927273,scale=442.252153,size=(110))
#print(normc220_c249m)

#sns.distplot(normc220_c249m,bins=20)
#sns.lineplot(x='edad', y=normc220_c249m, data=c220_c959m13_18ConAcumular)
#plt.show()

#sns.distplot(c220_c959m13_18ConAcumular['c220-c249m'],bins=20)

# Para graficar en ambos ejes del plano dando dos columnas numéricas distintas
#sns.jointplot(x='edad', y='c220-c249m', data=c220_c959m13_18ConAcumular)
#sns.jointplot(x='edad', y='c340-c349m', data=c220_c959m13_18ConAcumular)
#sns.jointplot(x='edad', y='c500-c509m', data=c220_c959m13_18ConAcumular)
#sns.jointplot(x='edad', y='c530-c55Xm', data=c220_c959m13_18ConAcumular)
#sns.jointplot(x='edad', y='c901-c959m', data=c220_c959m13_18ConAcumular)
#plt.show()



#sns.set_theme( style='darkgrid')
#f, ax=plt.subplots(figsize=(150,100))
defunciones= c220_c959m13_18ConAcumular.sort_values("c220-c249m",ascending=False)
#print(defunciones)
##NOTA: EL PRIMER SUBSET DEBE SER MAYOR AL SEGUDO, EN caso de que no, se comerá la segunada gráfica, la primera
#sns.lineplot(x="edad",y="c220-c249m",data=defunciones,label="Cáncer de hígado")
#Se crea el segundo subset a guardar en el subplot
#sns.lineplot(x="edad",y="c340-c349m",data=defunciones,label="Cáncer de pulmón")
#Se crea el tercer subset a guardar en el subplot
#sns.lineplot(x="edad",y="c500-c509m",data=defunciones,label="Cáncer de mama")
#Se crea el cuarto subset a guardar en el subplot
#sns.lineplot(x="edad",y="c530-c55Xm",data=defunciones,label="Cáncer de cervicouterino")
#Se crea el quinto subset a guardar en el subplot
#sns.lineplot(x="edad",y="c901-c959m",data=defunciones,label="Leucemia")
#ax.legend(ncol=2, loc="lower right",frameon=True)
#ax.set(xlim=(0),ylabel="Defunciones",xlabel="Edades")
#sns.despine(top=True,right=True)
#plt.show()






#Para Dany
#sns.set_theme(style="ticks")
#sns.jointplot(x="c340-c349m", y="c220-c249m", kind="hex", color="#4CB391",data=defunciones)
#plt.show()

#El de la galaxia que combina 3 gráficas en 1, la X y la Y están igualadas a las columnas deseadas del data set
#f, ax = plt.subplots(figsize=(6, 6))
#x=c220_c959m13_18ConAcumular['edad']
#y=c220_c959m13_18ConAcumular['c220-c249m']
#sns.scatterplot(x=x, y=y, s=5, color=".15",data=defunciones)
#sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako",data=defunciones)
#sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1,date=defunciones)
#plt.show()

#El parámetro hue de este es para la clasificación ej. mujer/hombre
#sns.set_theme( style='whitegrid')
#a=sns.relplot(x="edad", y="c340-c349m", size="c340-c349m",
#            sizes=(40,200), alpha=.5, palette="muted",hue='grupo',
#            height=7, data=defunciones)
#a.fig.suptitle("Defunciones a causa de cáncer de pulmón por etapa de vida")
#plt.show()

#sns.set_theme( style='whitegrid')
#b=sns.relplot(x="edad", y="c220-c249m", size="c220-c249m",
#            sizes=(40,200), alpha=.5, palette="muted",hue='grupo',
#            height=7, data=defunciones)
#b.fig.suptitle("Defunciones a causa de cáncer de hígado por etapa de vida")

#sns.set_theme( style='whitegrid')
#c=sns.relplot(x="edad", y="c500-c509m", size="c500-c509m",
#            sizes=(40,200), alpha=.5, palette="muted",hue='grupo',
#            height=7, data=defunciones)
#c.fig.suptitle("Defunciones a causa de cáncer de mama por etapa de vida")

#sns.set_theme( style='whitegrid')
#d=sns.relplot(x="edad", y="c530-c55Xm", size="c530-c55Xm",
#            sizes=(40,200), alpha=.5, palette="muted",hue='grupo',
#            height=7, data=defunciones)
#d.fig.suptitle("Defunciones a causa de cáncer cervicouterino por etapa de vida")

#sns.set_theme( style='whitegrid')
#d=sns.relplot(x="edad", y="c901-c959m", size="c901-c959m",
#            sizes=(40,200), alpha=.5, palette="muted",hue='grupo',
#            height=7, data=defunciones)
#d.fig.suptitle("Defunciones a causa de leucemia por etapa de vida")

#plt.show()

#Por si les sirve aunque el resultado es una colisión de datps en forma matricial
#c220_c959m13_18ConAcumularSinEdad = pd.read_csv('c220-c959m13-18ConAcumularSinEdad.csv')
#sns.pairplot(c220_c959m13_18ConAcumularSinEdad, hue="grupo")
#plt.show()

#Mapa de calor
#defun = c220_c959m13_18ConAcumular.pivot("grupo", "edad", "c220-c249m")
# Draw a heatmap with the numeric values in each cell
#f, ax = plt.subplots(figsize=(150,150))
#sns.heatmap(defun, annot=True, linewidths=5, ax=ax)
#plt.show()

#sns.set_theme( style='darkgrid')
#f, ab=plt.subplots(figsize=(150,100))
#print(defunciones)
##NOTA: EL PRIMER SUBSET DEBE SER MAYOR AL SEGUDO, EN caso de que no, se comerá la segunada gráfica, la primera
#sns.relplot(x="edad", y="c220-c249m", size="c220-c249m",
#           sizes=(40,200), alpha=.5, palette="muted",hue='grupo',
#           height=7, data=defunciones)

#sns.relplot(x="edad", y="c901-c959m", size="c901-c959m",
#           sizes=(40,200), alpha=.5, palette="muted",hue='grupo',
#           height=7, data=defunciones)

#ab.legend(ncol=2, loc="lower right",frameon=True)
#ab.set(xlim=(0),ylabel="Defunciones",xlabel="Edades")
#sns.despine(top=True,right=True)
#plt.show()
