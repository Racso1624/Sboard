#Fase 3: Prototipo funcional
#Módulo: Funciones de persistencia de datos y estadísticas
#Proyecto: Sboard
#Autores: Alejandro Gómez 20347, Marco Jurado 20308, Oscar López 20679, Ana Paola de León 20361
#Fecha 21/04/2020

import csv
import pandas as pd

def editar(archivo, carne):
    """ La función busca un dato sobre el precio en el archivo especificado"""
    with open(archivo, 'r') as dato:
        leer = csv.reader(dato)
        for i in leer:
            if carne == i[0]:
                precio = float(i[2])
    return precio


def comprobarcarneac(archivo, carne):
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