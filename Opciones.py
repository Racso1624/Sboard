#Fase 3: Prototipo funcional
#Módulo: Opciones
#Proyecto: Sboard
#Autores: Alejandro Gómez 20347, Marco Jurado 20308, Oscar López 20679, Ana Paola de León 20361
#Fecha 21/04/2020

import PruebaFunciones as PF
from tabulate import tabulate
import csv
import webbrowser

def numerocursos(dic, carne, archivo):
    """ Esta función le permite al usuario ingresar la cantidad de cursos que lleva
    por día, se realiza un ciclo que pide los cursos que lleva cada día de la semana.
    Tambien añade dichos datos a un csv."""
    Dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    for i in Dias:
        print("--------------------------------------------\n'Cursos del día: ", i)
        num = input('Ingrese la cantidad de cursos que tiene este día: ')
        num = PF.comprobar(num)
        lista = dic.get(i)
        if num == 0:
            pass
        else:
            for n in range(num):
                curso = input('Ingrese el curso: ')
                horai = input('Ingrese la hora de inicio de la clase (hh:mm): ')
                horai = PF.verifHora(horai)
                horaf = input('Ingrese la hora de en que termina la clase (hh:mm): ')
                horaf = PF.verifHora2(horaf, horai)
                curso_n = [curso, horai, horaf]
                lista.append(curso_n)
                dic[i] = lista
                print('')

                datos_cursos = [carne, i, "Curso", curso, horai, horaf]
                agregar(archivo, datos_cursos)
    return dic
        
def actividades(dic, carne, archivo):
    """ Esta función le permite al usuario ingresar la cantidad de actividades que realiza
    cada día, se hace un ciclo para que el usuario pueda ingresar las diversas actividades por día"""
    Dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    for i in Dias:
        print("--------------------------------------------\n'Actividades del día: ", i)
        num = input('Ingrese la cantidad de actividades extracurriculares que tiene: ')
        num = PF.comprobar(num)
        lista = dic.get(i)
        if num == 0:
            pass
        else:
            for n in range(num):
                actividad = input('Ingrese la actividad: ')
                horai = input('Ingrese la hora de inicio de la actividad (hh:mm): ')
                horai = PF.verifHora(horai)
                horaf = input('Ingrese la hora de en que termina actividad (hh:mm): ')
                horaf = PF.verifHora2(horaf, horai)
                actividad_n = [actividad, horai, horaf]
                lista.append(actividad_n)
                dic[i] = lista
                print('')

                datos_actividades = [carne, i, "Actividad", actividad, horai, horaf]
                agregar(archivo, datos_actividades)
    return dic

def tareas(cant, dic, carne, archivo):
    """Esta función permite ingresar los datos de las tareas para guardarlas en un diccionario"""
    for i in range(cant):
        tar=input("Ingrese el nombre de la tarea por realizar:" )
        fecha=input("Ingrese la fecha de entrega de su tarea: ")
        proc = input("Ingrese el estado de la tarea: ")
        lista = [fecha, proc]
        dic[tar] = lista

        datos_tareas = [carne, tar, fecha, proc]
        agregar(archivo, datos_tareas)
    return dic

def tablas(tareas):
    """Esta función permite imprimir los datos de un diccionario de forma tabulada"""
    print("Sus tareas son: ")
    tabla = [['Nombre', 'Fecha de Entrega', 'Estado']]
    for i in tareas:
        tabla_i = [i, tareas[i][0], tareas[i][1]]
        tabla.append(tabla_i)
    return tabla


def Bienestar_Estudiantil(menu_BE, opciones_BE):
    """Esta función va ligada con los cursos ingresados, brinda consejos
    al usuario dependiendo de las horas que el mismo les dedica."""
    var = False
    while var == False:
        print("\n\t\tMENU")
        PF.opciones(menu_BE)
        opcion = input("Ingrese la opción que desee realizar: ")
        opcion = PF.rango_BE2(opcion)
        
        if opcion == 1:
            print("\n********OPCIÓN 1 SELECCIONADA*******")
            print("A continuación se le desplegará la informacion general de Bienestar Estudiantil")
            print("Es una unidad de apoyo donde a través de consejería puedes mejorar tu bienestar mental, físico y académico.")
            
        if opcion == 2:
            print("\n********OPCIÓN 2 SELECCIONADA*******")
            PF.opciones(opciones_BE)
            Universidad_BE = input("¿En qué universidad te encuentras? ")
            Universidad_BE = PF.rango_BE(Universidad_BE)
            
            if Universidad_BE == 1:
                print("\nHas seleccionado la Universidad del Valle")
                print("En tu navegador se abrirá el link")
                webbrowser.open("https://www.uvg.edu.gt/vida-estudiantil/unidad-bienestar-estudiantil/")

            if Universidad_BE == 2:
                print("\nHas seleccionado la Universidad de San Carlos de Guatemala")
                print("En tu navegador se abrirá el link")
                webbrowser.open("https://diged.usac.edu.gt/dbeu/")
                
            if Universidad_BE == 3:
                print("\nHas seleccionado la Universidad Galileo")
                print("En tu navegador se abrirá el link")
                webbrowser.open("https://www.galileo.edu/servicios/servicios-academicos/academicos-administrativos/bienestar-estudiantil/")
                
            if Universidad_BE == 4:
                print("\nHas seleccionado la Universidad Francisco Marroquín")
                print("En tu navegador se abrirá el link")
                webbrowser.open("http://www.url.edu.gt/otros_sitios/notabaco/directorio/UFM.pdf")
                
            if Universidad_BE == 5:
                print("\nHas seleccionado la Universidad Rafael Landivar")
                print("En tu navegador se abrirá el link")    
                webbrowser.open("https://principal.url.edu.gt/index.php/vida-estudiantil/vicerrectoria-de-integracion")

            if Universidad_BE == 6:
                print("\nHas seleccionado la opción de otros")
                webbrowser.open("https://www.iutepi.edu/bienestar.php")
                print("Comunicate con las autoridades de tu institución para casos especificos. ")
            
        if opcion == 3:
            print("\n********OPCIÓN 5 SELECCIONADA*******")
            print("Regresando al menú principal...")
            var = True
        


def imprimirdiccionario(dic):
    """Esta función imprime el horario de las actividades que el usuario
    tiene que realizar durante cada día de la semana"""
    Dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    for i in Dias:
        print(i,':')
        valor = dic.get(i)
        if len(valor) == 0:
            print('No Tiene Nada Por Hacer Este Dia')
        else:
            for n in valor:
                print(n[0], n[1],'-',n[2])


def comprobar_archivo(nombre, datos):
    """ La función comprueba si un archivo esta en la carpeta asignada para este, si no está lo crea
    con el nombre de catalogo y le coloca el encabezado"""
    try:
        with open(nombre, 'r') as archivo:
            pass
    except:
        with open(nombre,'w', newline='') as archivo:
            write = csv.writer(archivo)
            write.writerow(datos)


def agregar(archivo, datos):
    """ La función agrega datos de por medio de listas a un archivo csv"""
    with open(archivo, 'a', newline='') as name:
        write = csv.writer(name)
        write.writerow(datos)
