from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado
if __name__ == "__main__":
    ecuacionSegundoGrado = EcuacionSegundoGrado()

    print("Solución: ax^2 + bx + b");
    ecuacionSegundoGrado.a = float(input("Parámetro a: "))
    ecuacionSegundoGrado.b = float(input("Parámetro b: "))
    ecuacionSegundoGrado.c = float(input("Parámetro c: "))
    raiz1, raiz2 = ecuacionSegundoGrado.solucionESG()
    print(f"{ecuacionSegundoGrado.a}x^2 +" \
                f"{ecuacionSegundoGrado.b}x +" \
                f"{ecuacionSegundoGrado.b} --> " + \
                f"raiz1= {raiz1} Raiz2={raiz2}")