from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
from datos import *
import random as random
from datetime import datetime, timedelta
#from random import *

origen = 'Suchiapa'
destino = 'Villaflores'

poblacion_inicial = 10
poblacion_maxima = 10
generaciones = 20
prob_cruza = 0.60 # 0.60
prob_mutacion_individuo = 0.15 # 0.25
prob_mutacion_gen = 0.10 # 0.50 
# precision = 1
# minimo = 10
# maximo = 20
poblacion = []
datos = []
municipios = ['Acala','Altamirano','Amatenango','Bochil','Cintalapa',
            'Huixtla','Ixtapa','Oxchuc','Suchiapa','Reforma',
            'Montecristo','Parral','Teopisca','Tapachula','Arriaga',
            'Simojovel','Ocosingo','Juarez','Palenque','Villaflores']

seccionA = ['Palenque','Altamirano','Reforma','Simojovel']
seccionB = ['Bochil','Huixtla','Amatenango','Juarez','Arriaga']
seccionC = ['Ocosingo','Cintalapa','Parral','Ixtapa','Montecristo']
seccionD = ['Acala', 'Oxchuc', 'Teopisca', 'Tapachula']

def extraer_datos_tk():
    medicamento = str(Entry_medicamento.get())
    # origen = str(Entry_origen.get())
    # destino = str(Entry_destino.get())
    fecha_entrega = Entry_fecha_maxima.get()
    fecha_salida = Entry_fecha_salida.get()
    hora_salida = Entry_hora_salida.get()
    #fecha_hora = datetime.strptime(fecha_salida + ' ' + hora_salida, '%Y-%m-%d %H:%M:%S')
    print('> Origen:', origen+' | Destino:',destino+' | Medicamento:',medicamento+' | FechaMax:',fecha_entrega+' | FechaSalida:',fecha_salida+' | HoraSalida:',hora_salida)
    algoritmo_genetico(origen,destino)

def algoritmo_genetico(origen,destino):
    print('==> Generación de individuos')
    for _ in range(generaciones):
        generar_individuos(origen,destino)
    parejas = seleccion()
    cruzas = cruza(parejas)
    mutaciones = mutacion(cruzas,origen,destino)
    poda(mutaciones)

def generar_individuos(origen,destino):
    ruta = []
    ruta.append(origen)
    while ruta[-1] != destino:
        municipio_aleatorio = random.choice(municipios)
        if municipio_aleatorio != origen:
            pos = ruta[-1]
            mun_random = random.choice(rutas[pos]['ruta'])
            if mun_random != origen and mun_random != ruta[-1]:
                ruta.append(mun_random)
    poblacion.append(ruta)
    print('RUTAS:', ruta)

def seleccion():
    parejas = []
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('==> Seleccion')
    j = 1
    for i in range(len(poblacion)):
        parejas_aux = []
        if j < len(poblacion):
            parejas_aux.append(poblacion[i])
            parejas_aux.append(poblacion[j])
            parejas.append(parejas_aux)
            #poblacion.append(parejas_aux)
            j += 1
        if j > len(poblacion):
            posicion_aleatoria = random.randint(0, len(poblacion))
            parejas_aux.append(poblacion[i])
            parejas_aux.append(poblacion[posicion_aleatoria])
            parejas.append(parejas_aux)
            #poblacion.append(parejas_aux)
    for j in range(len(parejas)):
        print('> Parejas:',parejas[j])
    poblacion.clear()
    return parejas

def cruza(selecciones):
    cruzas = []
    posiciones = []
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('==> Cruza')
    for i in range(len(selecciones)):
        probabilidad_aleatoria = random.uniform(0,1)
        if probabilidad_aleatoria <= prob_cruza:
            print('+ SI se puede cruzar:', selecciones[i])
            pareja = selecciones[i] # [[pareja1,pareja2],[pareja1,pareja2],[pareja1,pareja2]...]
            individuo1 = pareja[0] # [pareja1]
            print(' Individuo 1:', individuo1)
            individuo2 = pareja[1] # [pareja2]
            print(' Individuo 2:', individuo2)
            parte1 = individuo1[:3]
            print(' > Parte 1:', parte1)
            parte2 = individuo1[3:]
            print(' > Parte 2:', parte2)
            parte3 = individuo2[:3]
            print(' > Parte 3:', parte3)
            parte4 = individuo2[3:]
            print(' > Parte 4:', parte4)
            cruzas.append(parte1+parte4)
            print('Resultado 1:', parte1+parte4)
            cruzas.append(parte3+parte2)
            print('Resultado 2:', parte3+parte2)
            print(' - - - - - - - - - - - - ')
        else:
            print('- NO se puede Cruzar:',selecciones[i])
            pareja = selecciones[i]
            individuo1 = pareja[0]
            individuo2 = pareja[1]
            cruzas.append(individuo1)
            cruzas.append(individuo2)
            print(' - - - - - - - - - - - - ')
    print('=> Individuos despues de CRUZA')
    for j in range(len(cruzas)):
        print(cruzas[j])
        bandera = evaluar_rutas(cruzas[j])
        if bandera == -1:
            posiciones.append(cruzas[j])
    for k in posiciones:
        cruzas.remove(k)
    return cruzas

def evaluar_rutas(individuo):
    bandera = 1
    contador = 0
    posicion = 1
    for i in individuo:
        for j in rutas[i]['ruta']:
            if j == individuo[posicion]:
                if posicion < 5:
                    posicion += 1
                    contador += 1
    if contador == 4:
        return bandera
    else:
        bandera = -1
        return bandera 

def mutacion(cruzas,origen,destino):
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('==> Mutacion')
    for individuo in cruzas:
        print('- - - - - - - - - - - -')
        pos = 0
        probabilidad_aleatoria = random.uniform(1,0)
        if probabilidad_aleatoria <= prob_mutacion_individuo:
            print('Individuo puede mutar', individuo)
            for gen in individuo:
                probabilidad_aleatoria = random.uniform(0,1)
                if probabilidad_aleatoria <= prob_mutacion_gen:
                    if gen != origen and gen != destino:
                        print(' > Gen puede mutar', gen)
                        if gen in seccionA:
                            #print('Seccion A')
                            dato = random.choice(seccionA)
                            individuo[pos] = dato
                        if gen in seccionB:
                            #print('Seccion B')
                            dato = random.choice(seccionB)
                            individuo[pos] = dato
                        if gen in seccionC:
                            #print('Seccion C')
                            dato = random.choice(seccionC)
                            individuo[pos] = dato
                        if gen in seccionD:
                            #print('Seccion D')
                            dato = random.choice(seccionD)
                            individuo[pos] = dato
                else:
                    print(' > Gen no puede mutar',gen)
                pos += 1
        else:
            print('Individuo no puede mutar', individuo)
    return cruzas

def poda(mutaciones):
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('==> Poda')
    print(len(mutaciones))
    print(poblacion_maxima)
    if len(mutaciones) > poblacion_maxima:
        while len(mutaciones) != poblacion_maxima:
            posicion_aleatoria = random.randint(0,len(mutaciones)-1)
            del mutaciones[posicion_aleatoria]
    for i in mutaciones:
        poblacion.append(i)

# def extraer_datos_CSV():
#     print('Datos de CSV: ')
#     filename = 'Datos.csv'
#     data = pd.read_csv(filename, header=0)
#     #print(data.shape)
#     #print(data.head(10)) # cantidad de datos a extraer del CSV
#     municipio = data['Municipio'].to_numpy()
#     medicamento = data['Medicamento'].to_numpy()
#     extraer_datos_tk(municipio,medicamento)

ventana = Tk()
ventana.title('IA.AG_C3')
ventana.geometry('500x350')

label = Label(ventana, text='DISTRIBUCIÓN DE MULTISITIOS').place(x=180,y=5)

label = Label(ventana, text='Medicamento:').place(x=20,y=100)
Entry_medicamento = Entry(ventana)
Entry_medicamento.place(x=20,y=120)

# label = Label(ventana, text='Origen:').place(x=170,y=80)
# Entry_origen = Entry(ventana)
# Entry_origen.place(x=170,y=100)
# label = Label(ventana, text='Destino:').place(x=170,y=130)
# Entry_destino = Entry(ventana)
# Entry_destino.place(x=170,y=150)

label = Label(ventana, text='Fecha maxima entrega (YYYY-MM-DD):').place(x=330,y=60)
Entry_fecha_maxima = Entry(ventana)
Entry_fecha_maxima.place(x=330,y=80)
label = Label(ventana, text='Fecha de Salida (YYYY-MM-DD):').place(x=330,y=120)
Entry_fecha_salida = Entry(ventana)
Entry_fecha_salida.place(x=330,y=140)
label = Label(ventana, text='Hora de salida (HH:MM:SS):').place(x=330,y=180)
Entry_hora_salida = Entry(ventana)
Entry_hora_salida.place(x=330,y=200)

button = Button(ventana, text='Aceptar', command=extraer_datos_tk).place(x=230,y=290)

ventana.mainloop()