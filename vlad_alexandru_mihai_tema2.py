import pandas as pd
import matplotlib.pyplot as plot

X = 4 
Y = 14 

data = pd.read_csv('data.csv')

plot.figure(figsize=(15, 8))
plot.plot(data.index, data['Durata'], label='Durata', marker='o', color = 'm')
plot.plot(data.index, data['Puls'], label='Puls', marker='*', color = 'r')
plot.plot(data.index, data['MaxPuls'], label='MaxPuls', marker='*')
plot.plot(data.index, data['Calorii'], label='Calorii', marker='o', color = 'c')
plot.title('Grafic pentru toate valorile')
plot.legend()
plot.show()

plot.figure(figsize=(15, 8))
plot.plot(data.index[:X], data['Durata'][:X], label='Durata', marker='o', color = 'b')
plot.plot(data.index[:X], data['Puls'][:X], label='Puls', marker='*', color = 'r')
plot.plot(data.index[:X], data['MaxPuls'][:X], label='MaxPuls', marker='*')
plot.plot(data.index[:X], data['Calorii'][:X], label='Calorii', marker='o', color = 'c')
plot.title(f'Primele {X} valori')
plot.xlabel('Puls')
plot.ylabel('Durata')
plot.legend()
plot.show()

plot.figure(figsize=(15, 8))
plot.plot(data.index[-Y:], data['Durata'].tail(Y), label='Durata', marker='o', color = 'm')
plot.plot(data.index[-Y:], data['Puls'].tail(Y), label='Puls', marker='o', color = 'g')
plot.title(f'Ultimele {Y} valori. Doar puls si durata')
plot.xlabel('Puls')
plot.ylabel('Durata')
plot.legend()
plot.show()