#Fase 4: Entrega final 
#Módulo: Logo
#Proyecto: Sboard
#Autores: Alejandro Gómez 20347, Marco Jurado 20308, Racso1624, Ana Paola de León
#Fecha 21/04/2020
#Impresión del logo en forma de cascada utilizando el módulo de tiempo
import time as t
import sys

def logo():
    """Esta función imprime el nombre el programa de una forma de cascada"""
    texto = ("\t       Bienvenido a Sboard   \n ")
    for i in texto:
        sys.stdout.write(i)
        sys.stdout.flush()
        t.sleep(0.1)

    print("      _____ _                         _ ")
    t.sleep(0.19)
    print("     / ____| |                       | |")
    t.sleep(0.19)
    print("    | (___ | |__   ___   __ _ _ __ __| |")
    t.sleep(0.19)
    print("     \___ \| '_ \ / _ \ / _` | '__/ _` |")
    t.sleep(0.19)
    print("     ____) | |_) | (_) | (_| | | | (_| |")
    t.sleep(0.19)
    print("    |_____/|_.__/ \___/ \__,_|_|  \__,_|")
