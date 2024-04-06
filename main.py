import abecedario

def run():
    # Recibe el mensaje que desea encriptar.
    mensaje = list(input('Escribe el mensaje: ').upper())
    clave = list(input('Digita la clave de descifrado separado por comas: ').split(','))
    
    def encriptador(mensaje,clave):
        numeracion =[]
        
    # Convertir las letras del mensaje a numeros
        for letra in mensaje:
            valor = abecedario.encriptacion[letra]
            numeracion.append(valor)
            
    # Agrupa los numeros en sub listas de 3 filas x n columnas
        columnas = len(numeracion)
        filas = 3
        if columnas % 3!=0:
            numeracion.append(0)
            if columnas % 3!=0:
                numeracion.append(0)

    # Seccionador de lista a matriz deacuerdo a la cantidad de numeros
        matriz = [numeracion[i:i + 3] for i in range(0,columnas,filas)]
        clave = [clave[i:i + 3] for i in range(0,9,3)]
        return  matriz, clave
    
    print(encriptador(mensaje,clave))
    
    









if __name__ == '__main__':
    run()