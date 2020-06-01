#Fase 4: Entrega final 
#Proyecto: Sboard
#Autores: Alejandro Gómez 20347, Marco Jurado 20308, Racso1624, Ana Paola de León 20361
#Fecha 21/04/2020

menu = ['1) Ingresar el horario de sus cursos', '2) Agregar actividades extracurriculares', '3) Ingresar tareas', '4) Visualizar la tareas','5) Visualizar horario', '6) Bienestar Estudiantil', '7) Editar', '8) Estadísticas', '9) Salir']
menu_BE = ['1) Información general', '2) Contacto a Unidad de Bienestar Estudiantil', "3) Salir"]
opciones_BE = ["1) UVG","2) USAC","3) Galileo","4) UFM","5) URL","6) Otras Universidades"]
opciones_editar = ["1) Cursos","2) Actividades","3) Tareas", "4) Salir"]
opciones_graficas = ['1) Tabla de los 5 usuarios más frecuentes', '2) Los cursos con mayor presencia',"3) Mostrar gráfica de usuarios más frecuentes","4) Mostrar gráfica con cursos con más presencia","5) Salir"]

import webbrowser
import PruebaFunciones as PF
import Opciones as op
import logo as l
from tabulate import tabulate
import PersistenciayEstadisticas as pe
import os

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
    opcion = PF.rango(opcion, menu)

#Esta opción llama a la función de numero cursos que realiza un ingreso por medio
#de ciclos en donde le permite al usuario ingresar los cursos que tiene cada día.
    if opcion == 1: #Se ingresa el horario de los cursos
        os.system('cls')
        print("\n\033[1m********OPCIÓN 1 SELECCIONADA*******\033[0m")

        nombre_archivo_actividades = "actividades_dia.csv"
        datos_actividades = ["Carné", "Día", "Tipo.de.actividad", "Nombre.actividad", "Hora.inicio", "Hora.final"]
        op.comprobar_archivo(nombre_archivo_actividades, datos_actividades) #abriendo archivo o creando si no existe

        print('Ingrese las clases que recibe cada día')
        op.numerocursos(carne, nombre_archivo_actividades)

#Esta opción llama a la función de actividades que por medio de ciclos le permite
#al usuario ingresar las actividades de los días de la semana.
    if opcion == 2: #Se permite agregar actividades extracurriculares.
        os.system('cls')
        print("\033[1m********OPCIÓN 2 SELECCIONADA*******\033[0m")

        nombre_archivo_actividades = "actividades_dia.csv"
        datos_actividades = ["Carné", "Día", "Tipo.de.actividad", "Nombre.actividad", "Hora.inicio", "Hora.final"]
        op.comprobar_archivo(nombre_archivo_actividades, datos_actividades) #abriendo archivo o creando si no existe

        op.actividades(carne, nombre_archivo_actividades)

#Esta opción pedirá una cantidad y se comprobará por medio de una función.
#Luego se llamará a la función tareas que esta pedirá y guardará las tareas en el archivo csv.
    if opcion == 3: #Ingresar tareas
        os.system('cls')
        print("\n\033[1m********OPCIÓN 3 SELECCIONADA*******\033[0m")
        nombre_archivo_tareas = "tareas.csv"
        datos_tareas = ["Carné", "Nombre", "Fecha.entrega", "Estado"]
        op.comprobar_archivo(nombre_archivo_tareas, datos_tareas) #abriendo archivo o creando csv para tareas

        cant = input('Ingrese la cantidad de tareas: ')
        cant = PF.comprobar(cant)
        archivo = "tareas.csv"
        op.tareas(cant, carne, archivo)

#Esta opción llama a la función de tablas esta realizará la impresión
#de las tareas que tiene disponibles, o que tiene por realizar.
    if opcion == 4: #Visualizar tareas
        os.system('cls')
        print("\n\033[1m********OPCIÓN 4 SELECCIONADA*******\033[0m")
        print('\n\t\tTO DO LIST')
        datos_tareas = ["Carné", "Nombre", "Fecha.entrega", "Estado"]
        path = "tareas.csv"
        op.comprobar_archivo(path, datos_tareas)
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

#Esta opción llama a la función para mostrar los registros de las tareas
    if opcion == 5: #Visualizar horario
        os.system('cls')
        print("\n\033[1m********OPCIÓN 5 SELECCIONADA*******\033[0m")
        archivo = "actividades_dia.csv"
        datos_actividades = ["Carné", "Día", "Tipo.de.actividad", "Nombre.actividad", "Hora.inicio", "Hora.final"]
        op.comprobar_archivo(archivo, datos_actividades)

        lista = pe.actividadescarne(archivo, carne)
        op.imprimirdiccionario(lista)
        
    if opcion == 6: #Bienestar estudiantil
        print("\n\033[1m********OPCIÓN 6 SELECCIONADA*******\033[0m")
        print("Usted ha seleccionado la opción de Bienestar Estudiantil")
        op.Bienestar_Estudiantil(menu_BE, opciones_BE)
        
    if opcion == 7: #Editar Horario y Tareas. Esta función permite al usuario hacer cambios de su horario y tareas, el usuario podrá borrar la información.
        os.system('cls')
        print("\n\033[1m********OPCIÓN 7 SELECCIONADA*******\033[0m")
        print("Usted ha seleccionado la opción para editar información")
        print("OJO: Solamente puede borrar información.")
        var1 = False
        while var1 == False:
            print('¿Qué desea editar? ')
            PF.opciones(opciones_editar)
            opeditar = input('Ingrese la opción que desee:  ')
            opeditar = PF.rangoedit(opeditar)
            
            if opeditar == 1:
                """ Se editan los cursos """
                print("Usted ha elegido la opción para borrar cursos: ")
                archivo = 'actividades_dia.csv'
                ac = 'Curso'
                opcion = input('Ingrese el curso:  ')
                dia = input('Ingrese el dia del curso a editar, de forma correcta:  ')
                pe.editarcurso(archivo, carne, opcion, dia, ac)

            if opeditar == 2:
                """ Se editan las actividades a editar """
                print("Usted ha elegido la opción para borrar actividades: ")
                archivo = 'actividades_dia.csv'
                ac = 'Actividad'
                opcion = input('Ingrese el curso:  ')
                dia = input('Ingrese el dia de la actividad a editar, de forma correcta:  ')
                pe.editarcurso(archivo, carne, opcion, dia, ac)

            if opeditar == 3:
                print("Usted ha elegido la opción para borrar tareas: ")
                archivo = 'tareas.csv'
                opcion = input('Ingrese el curso:  ')
                dia = input('Ingrese el dia de la tarea a editar, de forma correcta:  ')
                pe.editartarea(archivo, carne, opcion, dia)
                
            if opeditar == 4:
                print('Saliendo al Menú...')
                var1 = True

    if opcion == 8: #Esta opción muestra al usuario las gráficas disponibles.
        os.system('cls')
        ik = False
        while ik == False:
            PF.opciones(opciones_graficas)
            selec = input('Ingrese su selección:  ')
            selec = PF.rango(selec, opciones_graficas)
            if selec == 1:
                archivo = 'datos_usuario.csv'
                pe.usuariosfrecuentes(archivo)

            if selec == 2:
                archivo = 'actividades_dia.csv'
                pe.cursosregistrados(archivo)

            if selec == 3:
                archivo = 'datos_usuario.csv'
                pe.grafica1(archivo)

            if selec == 4:
                archivo = 'actividades_dia.csv'
                pe.grafica2(archivo)

            if selec == 5:
                print("Regresando al menú...")
                ik = True

#Esta opción termina el ciclo por el que pasa el menú, brinda un mensaje y los créditos.
    if opcion == 9: #Salida
        print("\nSaliendo del programa...")
        print("Créditos: Oscar López, Marco Jurado, Alejandro Gómez, Paola de León ")
        var = True
