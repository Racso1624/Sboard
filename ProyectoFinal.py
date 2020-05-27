#Fase 3: Prototipo funcional
#Proyecto: Sboard
#Autores: Alejandro Gómez 20347, Marco Jurado 20308, Racso1624, Ana Paola de León 20361
#Fecha 21/04/2020

Diccionario_Semana = {'Lunes':[], 'Martes':[], 'Miércoles':[], 'Jueves':[], 'Viernes':[], 'Sábado':[], 'Domingo':[]}
tabla = []
menu = ['1) Ingresar el horario de sus cursos', '2) Agregar actividades extracurriculares', '3) Ingresar tareas', '4) Visualizar la tareas', '5) Visualizar horario', '6) Bienestar Estudiantil', '7) Editar', '8) Salir']
tareasd = {}
menu_BE = ['1) Información general', '2) Contacto a Unidad de Bienestar Estudiantil', "3) Salir"]
opciones_BE =["1) UVG","2) USAC","3) Galileo","4) UFM","5) URL","6) Otras Universidades"]
opciones_editar =["1) Cursos","2) Actividades","3) Tareas"]

import webbrowser
import PruebaFunciones as PF
import Opciones as op
import logo as l
from tabulate import tabulate
import PersistenciayEstadisticas as pe

#Creando archivo CSV de datos de usuario 
nombre_archivo_usuario = "datos_usuario.csv"
datos_usuario = ["Carné", "Nombre", "Edad", "Carrera"]
op.comprobar_archivo(nombre_archivo_usuario, datos_usuario) #abriendo archivo o creando si no existe


l.logo()
print("\n\tINGRESO DE DATOS PERSONALES")
#Ingreso del carne del usuario
carne = input('Ingrese su carné:  ')

#Ingreso del nombre del usuario
nombre = input('Ingrese su nombre completo:  ')

#Ingreso de edad
edad = input('Ingrese su edad:  ')
edad = PF.comprobar(edad)

#Ingreso de carrera
carrera = input('Ingrese su carrera:  ')

datos_del_usuario = [carne, nombre, edad, carrera]
op.agregar(nombre_archivo_usuario, datos_del_usuario)
                

#MENU
#En esta  parte se dan las opciones, además se hace un ciclo hasta que el usuario quiera parar de usar
#el programa. También se revisa que las opciones ingresadas estén correctas.
var = False
while var == False:
    print("\n\t\tMENU")
    PF.opciones(menu)
    opcion = input('Ingrese la opción que desea eligir: ')
    opcion = PF.rango(opcion)

#Esta opción llama a la función de numero cursos que realiza un ingreso por medio
#de ciclos en donde le permite al usuario ingresar los cursos que tiene cada día.
    if opcion == 1: #Se ingresa el horario de los cursos
        print("\n\033[1m********OPCIÓN 1 SELECCIONADA*******\033[0m")

        nombre_archivo_actividades = "actividades_dia.csv"
        datos_actividades = ["Carné", "Día", "Tipo.de.actividad", "Nombre.actividad", "Hora.inicio", "Hora.final"]
        op.comprobar_archivo(nombre_archivo_actividades, datos_actividades) #abriendo archivo o creando si no existe

        print('Ingrese las clases que recibe cada día')
        Diccionario_Semana = op.numerocursos(Diccionario_Semana, carne, nombre_archivo_actividades)
        print(Diccionario_Semana)

#Esta opción llama a la función de actividades que por medio de ciclos le permite
#al usuario ingresar las actividades de los días de la semana.
    if opcion == 2: #Se permite agregar actividades extracurriculares.
        print("\033[1m********OPCIÓN 2 SELECCIONADA*******\033[0m")

        nombre_archivo_actividades = "actividades_dia.csv"
        datos_actividades = ["Carné", "Día", "Tipo.de.actividad", "Nombre.actividad", "Hora.inicio", "Hora.final"]
        op.comprobar_archivo(nombre_archivo_actividades, datos_actividades) #abriendo archivo o creando si no existe

        Diccionario_Semana = op.actividades(Diccionario_Semana, carne, nombre_archivo_actividades)
        print(Diccionario_Semana)

#Esta opción pedirá una cantidad y se comprobará por medio de una función.
#Luego se llamará a la función tareas que esta pedirá y guardará las tareas en un diccionario.
    if opcion == 3: #Ingresar tareas
        print("\n\033[1m********OPCIÓN 3 SELECCIONADA*******\033[0m")

        nombre_archivo_tareas = "tareas.csv"
        datos_tareas = ["Carné", "Nombre", "Fecha.entrega", "Estado"]
        op.comprobar_archivo(nombre_archivo_tareas, datos_tareas) #abriendo archivo o creando csv para tareas

        cant = input('Ingrese la cantidad de tareas: ')
        cant = PF.comprobar(cant)
        archivo = "tareas.csv"
        tareas = op.tareas(cant, tareasd, carne, archivo)

#Esta opción llama a la función de tablas esta realizará la impresión
#de las tareas que tiene disponibles, o que tiene por realizar.
    if opcion == 4: #Visualizar tareas
        print("\n\033[1m********OPCIÓN 4 SELECCIONADA*******\033[0m")
        print('\n\t\tTO DO LIST')
        path = "tareas.csv"
        matriz = pe.crearMatriz(path)
        tareas = pe.tareasCarne(carne, matriz)
        if len(tareas) == 0:
            print('No tiene tareas.')
        else:
            print('TAREAS: ')
            arch_tareas=('tareas.csv')
            matriz = pe.crearMatriz(arch_tareas)
            tar_carne = pe.tareasCarne(carne, matriz)
            r=[]
            for fila in tar_carne:
                r.append(fila[1:])
            print(tabulate(r))

#Esta opción llama a la función de imprimir diccionarios, esta realiza
#la impresión del diccionario central que incluye a todas las actividades que se realizan.
    if opcion == 5: #Visualizar horario
        print("\n\033[1m********OPCIÓN 5 SELECCIONADA*******\033[0m")
        archivo = "actividades_dia.csv"
        op.imprimirdiccionario(Diccionario_Semana)
        
    if opcion == 6: #Bienestar estudiantil
        print("\n\033[1m********OPCIÓN 6 SELECCIONADA*******\033[0m")
        print("Usted ha seleccionado la opción de Bienestar Estudiantil")
        op.Bienestar_Estudiantil(menu_BE, opciones_BE)
        
    if opcion == 7: #Editar Horario y Tareas
        print("\n\033[1m********OPCIÓN 7 SELECCIONADA*******\033[0m")
        print("Opción en creación, no disponible por el momento.")

#Esta opción termina el ciclo por el que pasa el menú, brinda un mensaje y los créditos.
    if opcion == 8: #Salida
        print("\nSaliendo del programa...")
        print("Créditos: Oscar López, Marco Jurado, Alejandro Gómez, Paola de León ")
        var = True
