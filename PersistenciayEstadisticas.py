#Fase 4: Entrega final 
#Módulo: Funciones de persistencia de datos y estadísticas
#Proyecto: Sboard
#Autores: Alejandro Gómez 20347, Marco Jurado 20308, Oscar López 20679, Ana Paola de León 20361
#Fecha 21/04/2020

import csv
import pandas as pd
import matplotlib.pyplot as plt

def editarcurso(archivo, carne, opcion, dia, ac):
    """ La función busca un curso o actividad concreta y la quita de una lista
    luego esta lista se sobreescribe sobre el documento csv"""
    with open(archivo, 'r') as dato:
        leer = csv.reader(dato)
        lista = []
        for i in leer:
            if carne == i[0]:
                if opcion == i[3] and ac == i[2] and dia == i[1]:
                    pass
                else:
                    lista.append(i)
            else:
                lista.append(i)
        with open(archivo, 'w', newline="") as name:
            write = csv.writer(name)
            write.writerows(lista)


def editartarea(archivo, carne, opcion, dia):
    """ La función busca una tarea concreta y la quita de una lista
    luego esta lista se sobreescribe sobre el documento csv"""
    with open(archivo, 'r') as dato:
        leer = csv.reader(dato)
        lista = []
        for i in leer:
            if carne == i[0]:
                if opcion == i[1] and dia == i[2]:
                    pass
                else:
                    lista.append(i)
            else:
                lista.append(i)
        with open(archivo, 'w', newline="") as name:
            write = csv.writer(name)
            write.writerows(lista)


def comprobarcarneac(archivo, carne):
    """ La función se encarga de comprobar que el carné ingresado sea correcto al editar las actividades/cursos"""
    with open(archivo, 'r') as dato:
        leer = pd.read_csv(dato)
        lista = leer['Carné'].unique().tolist()
        var = False
        while var == False:
            if carne in lista:
                var = True
            else:
                print('No se encuentran actividades o cursos relacionadas con el Carné')
                print('Por favor ingrese actividades o cursos a la lista')


def comprobarcarnet(archivo, carne):
    """ La función se encarga de verificar que el carné ingresado sea el correcto al editar tareas"""
    with open(archivo, 'r') as dato:
        leer = pd.read_csv(dato)
        lista = leer['Carné'].unique().tolist()
        var = False
        while var == False:
            if carne in lista:
                var = True
            else:
                print('No se encuentran tareas relacionadas con el Carné')
                print('Por favor ingrese tareas a la lista')


def crearMatriz(path):
    '''Función que convierte un archivo csv en una matriz'''
    with open(path) as file:
        lines=file.readlines()
        matriz = [ [ r.strip() for r in line.split(",") ] for line in lines] 
        return matriz   


def tareasCarne(info, matriz):
    '''Función que muestra las tareas según carné'''
    a=[]
    r = True
    while r:
        for fila in matriz:
            if info in fila:
                a.append(fila)
            r = False
    return a


def actividadescarne(archivo, carne):
    """ La función busca un dato sobre el precio en el archivo especificado"""
    with open(archivo, 'r') as dato:
        leer = csv.reader(dato)
        lista = []
        for i in leer:
            if carne == i[0]:
                lista.append(i)
    return lista


def usuariosfrecuentes(archivo):
    """ La función agrupa la información sobre los usuarios que más ingresaron al programa
    y la imprime como un data frame"""
    with open(archivo, 'r') as name:
        datos = pd.read_csv(name)
        usuarios = datos['Carné'].value_counts()
        usuarios_df = pd.DataFrame(usuarios)
        print('5 Usuarios Más Frecuentes')
        print(usuarios_df.head(7))


def cursosregistrados(archivo):
    """ La función agrupa la información sobre las actividades y cursos más registrados
    y la imprime como un data frame"""
    with open(archivo, 'r') as name:
        datos = pd.read_csv(name)
        cursos = datos['Nombre.actividad'].value_counts()
        cursos_df = pd.DataFrame(cursos)
        print('Cantidad de productos vendidos por sucursal')
        print(cursos_df)


def grafica1(archivo):
    """ La función agrupa la información según carné
    y muestra la gráfica"""
    with open(archivo, 'r') as name:
        datos = pd.read_csv(name)
        x = pd.unique(datos['Carné'])
        y = datos['Carné'].value_counts()
        plt.plot(x, y, marker = 'o', linestyle = '--')
        plt.xticks(rotation = 90)
        plt.title('Usuarios utilizan el programa frecuentemente')
        plt.grid()
        plt.show()


def grafica2(archivo):
    """ La función agrupa la información sobre el tipo de actividad
    y muestra la gráfica"""
    with open(archivo, 'r') as name:
        datos = pd.read_csv(name)
        x = pd.unique(datos['Nombre.actividad'])
        y = datos['Nombre.actividad'].value_counts()
        plt.plot(x, y, marker = 'o', linestyle = '--')
        plt.xticks(rotation = 90)
        plt.title('Actividades más registradas')
        plt.grid()
        plt.show()
