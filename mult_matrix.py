import numpy as np

def run():
    matriz_clave=input('Escribe la matriz clave separada por comas: ').split(',')
    matriz_clave =[int(n) for n in matriz_clave]
    encriptada = [18,20,15,4,17,12,4,11,17]
    encriptada =[int(n) for n in encriptada]
    
    numero = []
    
    for n in range(0,3):
        valor = encriptada[n] * matriz_clave[n] 
        print(valor)
        numero.append(valor)
        
    num1 = sum(numero)
    print(num1)

if __name__ == '__main__':
    run()