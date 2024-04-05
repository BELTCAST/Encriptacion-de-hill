import abecedario

def run():
    
    mensaje = list(input("Escribe el mensaje: ").upper())
    
    def encriptador(mensaje):
        numeracion =[]
        for letra in mensaje:
            valor = abecedario.abc[letra]
            numeracion.append(valor)
        return numeracion
    
    print(encriptador(mensaje))
    
    









if __name__ == '__main__':
    run()