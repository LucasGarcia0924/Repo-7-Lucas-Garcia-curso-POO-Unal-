# Reto 7 POO
Para el reto # 7 se pedían tres cosas, añadir el decorador @property en el paquete Shape, trabajado en retos anteriores, para que se acceda de esta forma a la información protegida, luego, se debía agregar el decorador @classmethod para cambiar la definición y tipo de forma de cada clase, y finalmente, usar un decorador personalizado para llevar el conteo de cuanto demora al menos un cálculo realizado, cómo el área de una figura.
***
## Logo del grupo
![Logo](https://github.com/NotName-K/POO-R2/blob/main/Screenshot%202025-09-23%20110719.png?raw=true)

## Uso de Property
Este decorador se utilizó con el fin de remplazar todos los demás métodos que accedian a atributos privados (get_slope por ejemplo), de forma que fuese más eficiente acceder a estos.
```python
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
```
## Class method
Es utilizado para definir dinámicamente el tipo de figura, redefiniendo el tipo de figura cuándo es necesario.
```python
class Shape:
    shape_type = "Generic Shape"

    @classmethod
    def set_shape_type(cls, new_type: str):
        cls.shape_type = new_type
```
## Medidor de tiempo
Se llama a una función como decorador que registra el tiempo que tarda otra función en realizar cierto cálculo como el area de un rectángulo.
```python
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[Tiempo] {func.__name__}: {end - start:.6f} segundos")
        return result

    return wrapper
```
