from sys import stdin
import math
"""
    La funcion suma recibe dos numeros : c_1 y c_2 (que deben ser listas de longitud 2) y retorna un complejo 
    (lista de longitud 2) correspondiente a la operacion c_1 + c_2
    """
def suma(c_1,c_2):
    real=c_1[0]+c_2[0]
    ima=c_1[1]+c_2[1]
    return [real,ima]

    """
    La funcion resta recibe dos numeros : c_1 y c_2 (que deben ser listas de longitud 2) y retorna un complejo 
    (lista de longitud 2) correspondiente a la operacion c_1 - c_2
    """
def resta(c_1,c_2):
    real=c_1[0]-c_2[0]
    ima=c_1[1]-c_2[1]
    return [real,ima]
    """
    La funcion producto recibe dos numeros : c_1 y c_2 (que deben ser listas de longitud 2) y retorna un complejo 
    (lista de longitud 2) correspondiente a la operacion c_1 * c_2
    """
def producto(c_1,c_2):
    real= (c_1[0]*c_2[0])+((c_1[1]*c_2[1])*-1)
    ima=(c_1[0]*c_2[1])+(c_1[1]*c_2[0])
    return [real,ima]
    """
    La funcion fase recibe un numero : c_1 y retorna los grados 
    correspondiente a la operacion math.atan2(c_1)
    """
def fase(c_1):
    return math.degrees(math.atan2(c_1[1],c_1[0]))
"""
    La funcion conjugado recibe un numero : c_1  (que deben ser listas de longitud 2) y retorna un complejo 
    (lista de longitud 2).
"""
def conjugado(c_2):
    conju=(c_2[1]*-1)
    return [c_2[0],conju]
"""
    La funcion division recibe dos numeros : c_1 y c_2 (que deben ser listas de longitud 2) y retorna un complejo 
    (lista de longitud 2) correspondiente a la operacion c_1 / c_2
"""
def division(c_1,c_2):
    arriba= producto(c_1,conjugado(c_2))
    abajo= producto(c_2,conjugado(c_2))
    return [arriba[0]//abajo[0],arriba[1]//abajo[0]]
    """
    La funcion convertir de cartesiano a polar recibe un numero : c_1 (que deben ser lista de longitud 2)
    y retorna r y alpha correspondiente a la operacion r=math.sqrt(c_1[0]**2 + c_1[1]**2) y
    alpha=math.degrees(math.atan2(c_1[1],c_1[0]))
    """
def convertirCaPo(c_1):
    r=math.sqrt(c_1[0]**2 + c_1[1]**2)
    alpha=math.degrees(math.atan2(c_1[1],c_1[0]))
    return [r,alpha]
    """
    La funcion convertir de  polar cartesiano a recibe r y alpha  y retorna un complejo (lista de longitud 2)
    correspondiente a la operacion a=c_1[0]*math.cos(math.radians(c_1[1])) y
    b=c_1[0]*math.sin(math.radians(c_1[1]))
    """
def convertirPoCa(c_1):
    a=c_1[0]*math.cos(math.radians(c_1[1]))
    b=c_1[0]*math.sin(math.radians(c_1[1]))
    return [a,b]
    """
    La funcion modulo recibe un numero : c_1 y retorna el modulo  
    correspondiente a la operacion math.sqrt(c_1[0]**2 + c_1[1]**2)
    """
def modulo(c_1):
    a=math.sqrt(c_1[0]**2 + c_1[1]**2)
    return a
    """
    La funcion imprimir exponencial recibe un numero : c_1 y retorna la impresion
    de c_1 en formal exponencial
    """
def imprimirExponencial(c_1):
    return str(modulo(c_1))+"e^i"+"("+str(fase(c_1))+")"
    """
    La funcion potencia recibe un numero : c_1 y retorna la potencia
    del c_1 n veces 
    """
def potencia(c_1,n):
    m,a=modulo(c_1),int(fase(c_1))
    if n==1:
        return c1
    else:
        for i in range(1,n+1):
            return [int(m**n),a*n]
"""
    La funcion imprimir recibe un numero complejo de la forma, a+b y retorna un complejo de la forma
    a+bi
"""
def imprimir(c_1):
    c_1.append(str(c_1[1])+"i")
    c_1.remove(c_1[1])
    return c_1


