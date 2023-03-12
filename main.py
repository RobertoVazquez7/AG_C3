from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd

def extraer_datos_tk(municipio,medicamento):
    print('-> Extraer datos')
    # poblacion_inicial = Entry_pob_inicial.get()
    # generaciones = Entry_cant_generaciones.get()
    # prob_cruza = Entry_prob_cruza.get()
    # prob_mutIndividuo = Entry_prob_mutIndividuo.get()
    # prob_mutGen = Entry_prob_mutGen.get()
    # precision = Entry_precision.get()
    minimo = Entry_minimo.get()
    maximo = Entry_maximo.get()
    paquete = Entry_paquete.get()
    origen = Entry_origen.get()
    destino = Entry_destino.get()
    fecha_entrega = Entry_fecha_maxima.get()
    fecha_salida = Entry_fecha_salida.get()
    hora_salida = Entry_hora_salida.get()
    print(municipio)
    print(medicamento)

def extraer_datos_CSV():
    print('Datos de CSV: ')
    filename = 'Datos.csv'
    data = pd.read_csv(filename, header=0)
    #print(data.shape)
    #print(data.head(10)) # cantidad de datos a extraer del CSV
    municipio = data['Municipio'].to_numpy()
    medicamento = data['Medicamento'].to_numpy()
    extraer_datos_tk(municipio,medicamento)

ventana = Tk()
ventana.title('IA.AG_C3')
ventana.geometry('500x350')

label = Label(ventana, text='DISTRIBUCIÓN DE MULTISITIOS').place(x=180,y=5)
# label = Label(ventana, text='Población inicial:').place(x=40,y=40)
# Entry_pob_inicial = Entry(ventana)
# Entry_pob_inicial.place(x=40, y=60)

# label = Label(ventana, text='Generaciones:').place(x=40,y=80)
# Entry_cant_generaciones = Entry(ventana)
# Entry_cant_generaciones.place(x=40, y=100)

# label = Label(ventana, text='Prob. de Cruza:').place(x=40,y=140)
# Entry_prob_cruza = Entry(ventana)
# Entry_prob_cruza.place(x=40, y=160)
# label = Label(ventana, text='Prob. Mutación Individuo:').place(x=40,y=180)
# Entry_prob_mutIndividuo = Entry(ventana)
# Entry_prob_mutIndividuo.place(x=40, y=200)
# label = Label(ventana, text='Prob. Mutación Gen:').place(x=40,y=220)
# Entry_prob_mutGen = Entry(ventana)
# Entry_prob_mutGen.place(x=40,y=240)
# label = Label(ventana, text='Precisión:').place(x=40,y=260)
# Entry_precision = Entry(ventana)
# Entry_precision.place(x=40,y=280)

label = Label(ventana, text='Minimo:').place(x=40,y=80)
Entry_minimo = Entry(ventana)
Entry_minimo.place(x=40,y=100)
label = Label(ventana, text='Maximo:').place(x=40,y=120)
Entry_maximo = Entry(ventana)
Entry_maximo.place(x=40,y=140)

label = Label(ventana, text='Paquete:').place(x=300,y=40)
Entry_paquete = Entry(ventana)
Entry_paquete.place(x=300,y=60)
label = Label(ventana, text='Origen:').place(x=300,y=80)
Entry_origen = Entry(ventana)
Entry_origen.place(x=300,y=100)
label = Label(ventana, text='Destino:').place(x=300,y=120)
Entry_destino = Entry(ventana)
Entry_destino.place(x=300,y=140)
label = Label(ventana, text='Fecha maxima entrega:').place(x=300,y=160)
Entry_fecha_maxima = Entry(ventana)
Entry_fecha_maxima.place(x=300,y=180)
label = Label(ventana, text='Fecha de Salida:').place(x=300,y=200)
Entry_fecha_salida = Entry(ventana)
Entry_fecha_salida.place(x=300,y=220)
label = Label(ventana, text='Hora de salida:').place(x=300,y=240)
Entry_hora_salida = Entry(ventana)
Entry_hora_salida.place(x=300,y=260)

button = Button(ventana, text='Aceptar', command=extraer_datos_CSV).place(x=230,y=300)

ventana.mainloop()