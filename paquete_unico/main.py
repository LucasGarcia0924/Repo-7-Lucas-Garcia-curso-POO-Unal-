from paquete.Shape import (
    Point,
    Rectangle,
    Square,
    Equilateral,
    Isosceles,
    Scalene,
    TriRectangle,
    Line,
)


def safe_float_input(prompt: str, default: float = 0.0) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Entrada inválida. Inténtalo de nuevo.", e)


while True:
    print(
        "\nMenú de figuras geométricas:\nElige una opción:\n1. Crear un rectángulo\n2. Crear un cuadrado\n3. Crear una línea"
    )
    elegir = int(
        input(
            "4. Crear un Triángulo\n5. Ver intersecciones\n6. Ver información de figuras\n7. Terminar el programa\nElige: "
        )
    )
    if elegir == 1:
        print("Creando un rectángulo, elige un método")
        while True:
            method = input(
                "Esquina inferior izquierda (1), centro (2), 2 esquinas opuestas (3) o 4 líneas (4): "
            )
            if method not in ["1", "2", "3", "4"]:
                print("Opción no válida. Inténtalo de nuevo.")
                continue
            break

        if method in ["1", "2"]:
            width = safe_float_input("Ancho del rectángulo: ")
            height = safe_float_input("Alto del rectángulo: ")

        if method == "1":
            x = safe_float_input("Coordenada x de la esquina inferior izquierda: ")
            y = safe_float_input("Coordenada y de la esquina inferior izquierda: ")
            corner = Point(x, y)
            Rectangle_1 = Rectangle(
                method="1", corner=corner, width=width, height=height
            )

        elif method == "2":
            x = safe_float_input("Coordenada x del centro: ")
            y = safe_float_input("Coordenada y del centro: ")
            center = Point(x, y)
            Rectangle_1 = Rectangle(
                method="2", center=center, width=width, height=height
            )

        elif method == "3":
            x1 = safe_float_input("Coordenada x de la primera esquina: ")
            y1 = safe_float_input("Coordenada y de la primera esquina: ")
            x2 = safe_float_input("Coordenada x de la segunda esquina: ")
            y2 = safe_float_input("Coordenada y de la segunda esquina: ")
            corner1 = Point(x1, y1)
            corner2 = Point(x2, y2)
            Rectangle_1 = Rectangle(method="3", corner1=corner1, corner2=corner2)

        else:
            print("Creando líneas, inicia por la base:")
            lines: list = []
            bandera: bool = True
            while bandera:
                for i in range(4):
                    print(f"Línea {i + 1}:")
                    x1 = safe_float_input("x inicio: ")
                    y1 = safe_float_input("y inicio: ")
                    x2 = safe_float_input("x fin: ")
                    y2 = safe_float_input("y fin: ")
                    start = Point(x1, y1)
                    end = Point(x2, y2)
                    line = Line(start, end)
                    lines.append(line)
                # Validación sencilla: las líneas deben conectar (esto propuesto en tu código original)
                valid = True
                for i in range(1, 4):
                    if not (
                        lines[i].get_start().get_x() == lines[i - 1].get_end().get_x()
                        and lines[i].get_start().get_y()
                        == lines[i - 1].get_end().get_y()
                    ):
                        valid = False
                        break
                if not valid:
                    print("Las líneas no forman un rectángulo. Inténtalo de nuevo.")
                    lines.clear()
                else:
                    bandera = False
            Rectangle_1 = Rectangle(method="4", lines=lines)

        print(f"Área: {Rectangle_1.compute_area()}")
        print(f"Perímetro: {Rectangle_1.compute_perimeter()}")

    elif elegir == 2:
        side = safe_float_input("Lado del cuadrado: ")
        x = safe_float_input("Coordenada x del centro: ")
        y = safe_float_input("Coordenada y del centro: ")
        center = Point(x, y)
        Square_1 = Square(side, center)
        print(f"Área: {Square_1.compute_area()}")
        print(f"Perímetro: {Square_1.compute_perimeter()}")

    elif elegir == 3:
        print("Creando una línea:")
        x1 = safe_float_input("x inicio: ")
        y1 = safe_float_input("y inicio: ")
        x2 = safe_float_input("x fin: ")
        y2 = safe_float_input("y fin: ")
        start = Point(x1, y1)
        end = Point(x2, y2)
        Line_1 = Line(start, end)
        # Usar propiedades 'length' y 'slope' (o métodos legacy)
        print(f"Longitud: {Line_1.length:.6f}")
        slope = Line_1.slope
        print("Pendiente:", "Infinita" if slope == float("inf") else slope)
        print(f"Corte horizontal (eje y): {Line_1.compute_horizontal_cross()}")
        print(f"Corte vertical (eje x): {Line_1.compute_vertical_cross()}")

    elif elegir == 4:
        print("Elige el tipo de triángulo:")
        print("1. Escaleno")
        print("2. Isósceles")
        print("3. Equilátero")
        print("4. Rectángulo")
        tipo = input("Tipo: ")

        if tipo == "1":
            print("Introduce los 3 vértices:")
            p1 = Point(safe_float_input("x1: "), safe_float_input("y1: "))
            p2 = Point(safe_float_input("x2: "), safe_float_input("y2: "))
            p3 = Point(safe_float_input("x3: "), safe_float_input("y3: "))
            tri = Scalene(p1, p2, p3)

        elif tipo == "2":
            base = safe_float_input("Base: ")
            side = safe_float_input("Lado igual: ")
            tri = Isosceles(base, side)

        elif tipo == "3":
            side = safe_float_input("Lado del equilátero: ")
            tri = Equilateral(side)

        elif tipo == "4":
            base = safe_float_input("Base: ")
            height = safe_float_input("Altura: ")
            tri = TriRectangle(base, height)
        else:
            print("Opción no válida.")
            continue
        print(f"Perímetro: {tri.compute_perimeter():.2f}")
        print(f"Área: {tri.compute_area():.2f}")
        print(f"Ángulos internos: {tri.compute_inner_angles()}")

    elif elegir == 5:
        choice2 = str(
            input(
                "¿Con qué figura quieres ver intersecciones?\n1. Rectángulo\n2. Cuadrado\n"
            )
        )
        choice3 = str(
            input("¿Con qué figura quieres ver intersecciones?\n1. Punto\n2. Línea\n")
        )
        if choice2 == "1":
            if "Rectangle_1" not in locals():
                print("No has creado un rectángulo aún.")
                continue
            if choice3 == "1":
                x = safe_float_input("Coordenada x del punto: ")
                y = safe_float_input("Coordenada y del punto: ")
                point = Point(x, y)
                Rectangle_1.compute_interference_point(point)
            elif choice3 == "2":
                if "Line_1" not in locals():
                    print("No has creado una línea aún.")
                    continue
                Rectangle_1.compute_interference_line(Line_1)
        elif choice2 == "2":
            if "Square_1" not in locals():
                print("No has creado un cuadrado aún.")
                continue
            if choice3 == "1":
                x = safe_float_input("Coordenada x del punto: ")
                y = safe_float_input("Coordenada y del punto: ")
                point = Point(x, y)
                Square_1.compute_interference_point(point)
            elif choice3 == "2":
                if "Line_1" not in locals():
                    print("No has creado una línea aún.")
                    continue
                Square_1.compute_interference_line(Line_1)
            continue

    elif elegir == 6:
        while True:
            try:
                print(
                    "\nDe que figura quieres ver su información?\n1. Rectángulo\n2. Cuadrado\n3. Línea\n4. Triángulo \n5. Ninguna, salir"
                )
                figura = int(input("Elige una opción: "))
                if figura == 1:
                    if "Rectangle_1" not in locals():
                        print("No has creado un rectángulo aún.\n")
                        continue
                    print(Rectangle_1)
                elif figura == 2:
                    if "Square_1" not in locals():
                        print("No has creado un cuadrado aún.\n")
                        continue
                    print(Square_1)
                elif figura == 3:
                    if "Line_1" not in locals():
                        print("No has creado una línea aún.\n")
                        continue
                    print(Line_1)
                elif figura == 4:
                    if "tri" not in locals():
                        print("No has creado un triángulo aún.\n")
                        continue
                    print(tri)
                elif figura == 5:
                    break
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
                    continue
            except ValueError as e:
                print(f"Entrada no válida. Inténtalo de nuevo. {e}")
                continue

    elif elegir == 7:
        print("Terminando el programa.")
        break

    else:
        print("Opción no válida, intenta de nuevo.")
