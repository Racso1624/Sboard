#Fase 4: Entrega final 
#Módulo: Funciones de Comprobación
#Proyecto: Sboard
#Autores: Alejandro Gómez 20347, Marco Jurado 20308, Oscar López 20679, Ana Paola de León
#Fecha 21/04/2020

def opciones(ops):
    """ La función genera un menú con las especificaciones que
    le de el usuario. """

    for i in ops:
        print(i)


def comprobar(numero):
    """ La función comprueba si un número es un entero o no"""
    var = False
    while var == False:
        try:
            numero = int(numero)
            var = True
        except ValueError:
            print('Error, solo se permite el ingreso de números enteros')
            numero = input('Ingrese la cantidad de nuevo: ')
    return numero


def verifHora(hora):
    """Esta función verfica que las horas de inicio que le usuario ingrese sean correctas,
    además revisa que sean reales y que no haya errores al ingresarlas"""
    var = False
    while var == False:
        if ':' in hora and len(hora) == 5: 
            hr = []
            hr = hora.split(':')
            try:
                h = int(hr[0])
                m = int(hr[1])
                if 0 <= h < 24 and 0 <= m < 60:
                    var = True
                else:
                    print('Solo se permiten horas reales')
                    hora = input('Ingrese la hora nuevamente: ')
            except:
                print('ERROR, Solo se permiten números para indicar la hora')
                hora = input('Ingrese la hora nuevamente: ')
        else:
            print('Error al ingresar la hora')
            hora = input('Ingrese la hora nuevamente: ')
    return hora


def verifHora2(hora, hora1):
    """Esta función verifica que las horas de finalización de una actividad o curso
    sean verdaderas, además hace la verificación para que la hora sea mayor a la otra"""
    var = False
    while var == False:
        hr = []
        hr = hora.split(':')
        try:
            h = int(hr[0])
            m = int(hr[1])
            if 0 <= h < 24 and 0 <= m < 60:
                hr2 = []
                hr2 = hora1.split(':')
                h2 = int(hr2[0])
                m2 = int(hr2[1])
                if h2 < h:
                    var = True
                elif h2 == h:
                    if m2 < m:
                        var = True
                    else:
                        print('La hora de finalización debe ser mayor que la de inicio')
                        hora = input('Ingrese la hora de nuevo: ')
                else:
                    print('La hora de salida debe ser mayor que la de entrada')
                    hora = input('Ingrese la hora de nuevo: ')
            else:
                print('Solo se permiten horas reales')
                hora = input('Ingrese la hora de nuevo: ')
        except:
            print('ERROR, Solo se permiten números para indicar la hora')
            hora = input('Ingrese la hora de nuevo: ')
    return hora


def rango(numero, lista):
    """ La función comprueba si un número es un entero o no, además
    en esta se puede comprobar si el número está dentro del rango especificado"""
    var = False
    while var == False:
        try:
            numero = int(numero)
            if 1 <= numero <= len(lista):
                var = True
            else:
                print('El numero esta fuera de rango')
                numero = input('Ingrese el número de nuevo: ')
        except ValueError:
            print('Error, Solo se permite el ingreso de números enteros')
            numero = input('Ingrese el número de nuevo: ')
    return numero 


def rango_BE(numero):
    """ La función comprueba si un número es un entero o no, además
    en esta se puede comprobar si el número está dentro del rango especificado"""
    var = False
    while var == False:
        try:
            numero = int(numero)
            if 1 <= numero <= 6:
                var = True
            else:
                print('El numero esta fuera de rango')
                numero = input('Ingrese el número de nuevo: ')
        except ValueError:
            print('Error, Solo se permite el ingreso de números enteros')
            numero = input('Ingrese el número de nuevo: ')
    return numero 


def rango_BE2(numero):
    """ La función comprueba si un número es un entero o no, además
    en esta se puede comprobar si el número está dentro del rango especificado"""
    var = False
    while var == False:
        try:
            numero = int(numero)
            if 1 <= numero <= 3:
                var = True
            else:
                print('El numero esta fuera de rango')
                numero = input('Ingrese el número de nuevo: ')
        except ValueError:
            print('Error, Solo se permite el ingreso de números enteros')
            numero = input('Ingrese el número de nuevo: ')
    return numero 


def rangoedit(numero):
    """ La función comprueba si un número es un entero o no, además
    en esta se puede comprobar si el número está dentro del rango especificado"""
    var = False
    while var == False:
        try:
            numero = int(numero)
            if 1 <= numero <= 4:
                var = True
            else:
                print('El numero esta fuera de rango')
                numero = input('Ingrese el número de nuevo: ')
        except ValueError:
            print('Error, Solo se permite el ingreso de números enteros')
            numero = input('Ingrese el número de nuevo: ')
    return numero 