import math
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[Tiempo] {func.__name__}: {end - start:.6f} segundos")
        return result

    return wrapper


class ZeroSlopeError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Point:
    definition: str = (
        "Entidad geométrica abstracta que representa una ubicación en un espacio."
    )

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def set_x(self, x: float):
        self.__x = x

    def set_y(self, y: float):
        self.__y = y

    def move(self, new_x: float, new_y: float) -> None:
        self.set_x(new_x)
        self.set_y(new_y)

    def reset(self) -> None:
        self.__x = 0
        self.__y = 0

    @measure_time
    def compute_distance(self, point: "Point") -> float:
        return ((self.__x - point.x) ** 2 + (self.__y - point.y) ** 2) ** 0.5


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.__start = start
        self.__end = end
        self.__length = self.compute_length()
        self.__slope = self.compute_slope()

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    @property
    def length(self):
        return self.__length

    @property
    def slope(self):
        return self.__slope

    def set_start(self, start: Point):
        self.__start = start
        self.__length = self.compute_length()

    def set_end(self, end: Point):
        self.__end = end
        self.__length = self.compute_length()

    @measure_time
    def compute_length(self) -> float:
        return self.__start.compute_distance(self.__end)

    @measure_time
    def compute_slope(self) -> float:
        try:
            slope = (self.__end.y - self.__start.y) / (self.__end.x - self.__start.x)
        except ZeroDivisionError:
            slope = float("inf")
        self.__slope = slope
        return slope

    @measure_time
    def compute_horizontal_cross(self) -> float:
        if self.__slope == float("inf"):
            return float("inf")
        return self.__start.y - (self.__slope * self.__start.x)

    @measure_time
    def compute_vertical_cross(self) -> float:
        try:
            return self.__start.x - (self.__start.y / self.__slope)
        except ZeroDivisionError:
            return float("inf")

    def __str__(self) -> str:
        slope_str = (
            "Infinita" if self.__slope == float("inf") else f"{self.__slope:.2f}"
        )
        string = f"""
        Línea desde ({self.__start.x}, {self.__start.y}) hasta ({self.__end.x}, {self.__end.y})
        Longitud: {self.__length:.2f}
        Pendiente: {slope_str}
        Corte horizontal (eje y): {self.compute_horizontal_cross():.2f}
        Corte vertical (eje x): {self.compute_vertical_cross():.2f}
        """
        return string


class Shape:
    shape_type = "Generic Shape"

    @classmethod
    def set_shape_type(cls, new_type: str):
        cls.shape_type = new_type

    @property
    def is_regular(self):
        return self.__is_regular

    def __init__(self):
        self.__is_regular = False

    @measure_time
    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")

    @measure_time
    def compute_perimeter(self):
        raise NotImplementedError("Subclases deben implementar compute_perimeter()")


class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__()
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__update_sides()

    @property
    def p1(self):
        return self.__p1

    @property
    def p2(self):
        return self.__p2

    @property
    def p3(self):
        return self.__p3

    @property
    def sides(self):
        return (self.__a, self.__b, self.__c)

    def set_points(self, p1: Point, p2: Point, p3: Point):
        self.__p1, self.__p2, self.__p3 = p1, p2, p3
        self.__update_sides()

    def __update_sides(self):
        self.__a = self.__p2.compute_distance(self.__p3)
        self.__b = self.__p1.compute_distance(self.__p3)
        self.__c = self.__p1.compute_distance(self.__p2)

    @measure_time
    def compute_perimeter(self):
        return self.__a + self.__b + self.__c

    @measure_time
    def compute_area(self):
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def compute_inner_angles(self):
        try:
            A = math.degrees(
                math.acos(
                    (self.__b**2 + self.__c**2 - self.__a**2)
                    / (2 * self.__b * self.__c)
                )
            )
            B = math.degrees(
                math.acos(
                    (self.__a**2 + self.__c**2 - self.__b**2)
                    / (2 * self.__a * self.__c)
                )
            )
            C = math.degrees(
                math.acos(
                    (self.__a**2 + self.__b**2 - self.__c**2)
                    / (2 * self.__a * self.__b)
                )
            )
            return (A, B, C)
        except ValueError:
            C = 180 - (A + B)
            return (A, B, C)

    def __str__(self):
        string = f"""
            Triángulo:
            A({self.__p1.x}, {self.__p1.y}),
            B({self.__p2.x}, {self.__p2.y}),
            C({self.__p3.x}, {self.__p3.y})
            Lados: a={self.__a:.2f}, b={self.__b:.2f}, c={self.__c:.2f}
            Área: {self.compute_area():.2f}
            Perímetro: {self.compute_perimeter():.2f}
        """
        return string


class Scalene(Triangle):
    def __str__(self):
        return f"Triángulo Escaleno: {super().__str__()}"


class Isosceles(Triangle):
    def __init__(self, base: float, side: float, origin: Point = Point(0, 0)):
        p1 = origin
        p2 = Point(origin.x + base, origin.y)
        altura = math.sqrt(side**2 - (base / 2) ** 2)
        p3 = Point(origin.x + base / 2, origin.y + altura)
        super().__init__(p1, p2, p3)

    def __str__(self):
        return f"Triángulo Isósceles: {super().__str__()}"


class Equilateral(Triangle):
    def __init__(self, side: float, origin: Point = Point(0, 0)):
        p1 = origin
        p2 = Point(origin.x + side, origin.y)
        altura = math.sqrt(3) / 2 * side
        p3 = Point(origin.x + side / 2, origin.y + altura)
        super().__init__(p1, p2, p3)

    def compute_inner_angles(self):
        return (60.0, 60.0, 60.0)

    @measure_time
    def compute_area(self):
        a, _, _ = self.sides
        return (math.sqrt(3) / 4) * a**2

    def __str__(self):
        return f"Triángulo Equilátero: {super().__str__()}"


class TriRectangle(Triangle):
    def __init__(self, base: float, height: float, origin: Point = Point(0, 0)):
        p1 = origin
        p2 = Point(origin.x + base, origin.y)
        p3 = Point(origin.x, origin.y + height)
        super().__init__(p1, p2, p3)

    @measure_time
    def compute_area(self):
        a, b, c = self.sides
        return (a * b) / 2

    def __str__(self):
        return f"Triángulo Rectángulo: {super().__str__()}"


class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__()
        method = kwargs.get("method", "1")

        if method == "1":
            corner = kwargs.get("corner", Point())
            self.__width = kwargs.get("width", 1)
            self.__height = kwargs.get("height", 1)
            self.__center = Point(
                (corner.x + self.__width) / 2, (corner.y + self.__height) / 2
            )

        elif method == "2":
            center = kwargs.get("center", Point())
            self.__center = center
            self.__width = kwargs.get("width", 1)
            self.__height = kwargs.get("height", 1)

        elif method == "3":
            corner1 = kwargs.get("corner1", Point())
            corner2 = kwargs.get("corner2", Point())
            self.__width = abs(corner2.x - corner1.x)
            self.__height = abs(corner2.y - corner1.y)
            self.__center = Point(
                (corner1.x + corner2.x) / 2, (corner1.y + corner2.y) / 2
            )

        else:
            lines = kwargs.get("lines", [])
            self.__width = lines[0].length
            self.__height = lines[1].length
            self.__center = Point(
                (lines[0].start.x + lines[0].end.x) / 2,
                (lines[0].start.y + lines[1].end.y) / 2,
            )

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def center(self):
        return self.__center

    def set_width(self, width: float):
        self.__width = width

    def set_height(self, height: float):
        self.__height = height

    def set_center(self, center: Point):
        self.__center = center

    @measure_time
    def compute_area(self) -> float:
        return self.__width * self.__height

    @measure_time
    def compute_perimeter(self) -> float:
        return 2 * (self.__width + self.__height)

    @measure_time
    def compute_interference_point(self, point: Point) -> bool:
        left = self.__center.x - self.__width / 2
        right = self.__center.x + self.__width / 2
        bottom = self.__center.y - self.__height / 2
        top = self.__center.y + self.__height / 2
        return left <= point.x <= right and bottom <= point.y <= top

    @measure_time
    def compute_interference_line(self, line: "Line") -> None:
        inside_start = self.compute_interference_point(line.start)
        inside_end = self.compute_interference_point(line.end)

        if inside_start and inside_end:
            print("La línea está dentro del rectángulo.")
        elif inside_start or inside_end:
            print("La línea intersecta el rectángulo.")
        else:
            print("La línea está fuera del rectángulo.")

    def __str__(self) -> str:
        string = f"""
        Rectángulo centrado en ({self.__center.x}, {self.__center.y}) con ancho {self.__width} y alto {self.__height}.
        Área: {self.compute_area()}
        Perímetro: {self.compute_perimeter()}
        """
        return string


class Square(Rectangle):
    def __init__(self, side: float = 1, center: Point | None = None):
        if center is None:
            center = Point()
        super().__init__(method="2", width=side, height=side, center=center)

    def __str__(self) -> str:
        string = f"""
        Cuadrado centrado en ({self.center.x}, {self.center.y}) con lado {self.width}.
        Área: {self.compute_area():.2f}
        Perímetro: {self.compute_perimeter():.2f}
        """
        return string
