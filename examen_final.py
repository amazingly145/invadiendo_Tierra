import math
#Función del alien con preguntas de trabajo, para calcular la velocidad final
def alien_trabajador(score):
    print("Crees que me vas a vencer\n")
    print("Pondremos a prueba tus conocimientos\n")
    print("Porque soy buena onda, te dejaré colocar tus valores, pero debes hacer lo que te pido:")
    masa = float(input("Insinuando que tienes un bloque de (en kg): "))
    velocidad_inicial = float(input("Que tiene una velocidad inicial de (en m/s): "))
    print("Se desplaza en una superficie sin fricción.")
    fuerza = float(input("Que es movido por una fuerza de (en N): "))
    desplazamiento = float(input("Ingresa la distancia que jaló la fuerza (en m): "))
    resultado = float(input("Calcula la velocidad después que fue jalado (en m/s): "))
    velocidad_final = velocidadfinal_trabajo(masa, velocidad_inicial, fuerza, desplazamiento)
    if abs(velocidad_final - resultado) < 0.01:
        print("¡No! Me has vencido")
        score += 1
    else:
        print("Suerte para la próxima")
        score -= 1
    return score
#función del alien chocante, para calcular la velocidad compartida.
def alien_chocante(score):
    print("Crees que me vas a vencer")
    print("Pondremos a prueba tus conocimientos")
    print("Porque soy buena onda, te dejaré colocar tus valores, pero debes hacer lo que te pido:")
    masa_a = float(input("Insinuando que tienes un bloque de masa (en kg): "))
    velocidad_inicial_a = float(input("Que tiene una velocidad inicial de (en m/s): "))
    masa_b = float(input("Después choca con otro bloque (juntándonse) con masa de(en kg): "))
    velocidad_inicial_b = float(input("El cual tenía una velocidad de (en m/s): "))
    print("Ambos se desplazan en una superficie sin fricción.")
    resultado = float(input("Calcula la velocidad compartida al final de la colisión: "))
    velocidad_compartida = choques(masa_a,velocidad_inicial_a,masa_b,velocidad_inicial_b)
    if abs(velocidad_compartida - resultado) < 0.01:
        print("¡No! Me has vencido")
        score += 1
    else:
        print("Suerte para la próxima")
        score -= 1
    return score

def velocidadfinal_trabajo(masa, velocidad_inicial, fuerza, desplazamiento):
    #Para calcular trabajo necesitamos fuerza y desplazamiento, su producto es el trabajo total
    #Calculamos el trabajo que se hace con los valores del jugador
    trabajo = fuerza * desplazamiento
    # Calculamos la energía cinética inicial
    energia_cinetica = (1 / 2) * masa * (velocidad_inicial ** 2)
    # Calculampos la velocidad final usando la conservación de energía y despejando el valor de velocidad final
    velocidad_final = ((2 * (trabajo + energia_cinetica)) / masa) ** 0.5
    return velocidad_final

def choques(masa_a,velocidad_inicial_a,masa_b,velocidad_inicial_b):
    #Sumamos las masas compartidas después de la colisión
    despues_colision = masa_a + masa_b
    #Hacemos las sumas y multiplicaciones necesarias para calcular antes de la colisión
    antes_colision = (masa_a*velocidad_inicial_a) + (masa_b * velocidad_inicial_b)
    #Como ambas se unieron, comparten una velocidad.
    velocidad_compartida = antes_colision/despues_colision
    return velocidad_compartida
def menu():
    print("1. Alien chambeador")
    print("2. Alien chocante")
    print("3. Salida")
def main():
    score=0
    print("El planeta Tierra ha sido invadido por dos aliens de Marte, sin tú ayuda la humanidad no permanecerá\n")
    print("Para poder derrotarlos necesitas contestar correctamente todas las preguntas que te pidan\n")
    print("Cuidado porque son muy engañosos y te pueden confundir")
    print("Recuerda que solo necesitas terminar con uno para su definitiva extinsión ")
    print("Suerte en tu misión camarada creemos en ti\n")
    while True:
        menu()
        usuario = int(input("Selecciona el alien que derrotarás primero: "))
        if usuario == 1:
            print("Esta Ronda tu score fue de: "+ str(alien_trabajador(score)))
        elif usuario == 2:
            print("Esta Ronda tu score fue de: "+ str(alien_chocante(score)))
        elif score == 1:
            print("Felicidades has ganado!")
            break
        elif usuario==3:
            print("Gracias por jugar con nosotros!")
            break
main()