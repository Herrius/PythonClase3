class ControlDeFlujo:
    def __init__(self):
        # Este constructor podría inicializar alguna variable si fuera necesario
        pass

    def demo_condicionales(self):
        # Demostración de condicionales
        numero = 15
        if numero > 10:
            print("El número es mayor que 10.")
        elif numero == 10:
            print("El número es exactamente 10.")
        else:
            print("El número es menor que 10.")

        # Uso de operadores lógicos
        edad = 25
        tiene_licencia = True
        if edad >= 18 and tiene_licencia:
            print("Puede conducir.")
        else:
            print("No puede conducir.")

    def demo_bucles(self):
        # Demostración de un bucle for
        print("Bucle for que imprime números del 1 al 5:")
        for i in range(1, 6):
            print(i)

        # Demostración de un bucle while
        print("Bucle while que cuenta hacia atrás desde 5:")
        contador = 5
        while contador > 0:
            print(contador)
            contador -= 1

        # Uso de break y continue dentro de bucles
        print("Ejemplo de uso de 'break' y 'continue':")
        for num in range(1, 10):
            if num == 3:
                continue  # Salta el resto del código en el bucle para num == 3
            if num == 8:
                break  # Rompe el bucle completamente
            print(num)

def main():
    control = ControlDeFlujo()
    print("Demostración de condicionales:")
    control.demo_condicionales()
    print("\nDemostración de bucles:")
    control.demo_bucles()

if __name__ == "__main__":
    main()
