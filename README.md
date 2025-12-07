# Reto 7 POO
Para el reto # 7 se pedían tres cosas, añadir el decorador @property en el paquete Shape, trabajado en retos anteriores, para que se acceda de esta forma a la información protegida, luego, se debía agregar el decorador @classmethod para cambiar la definición y tipo de forma de cada clase, y finalmente, usar un decorador personalizado para llevar el conteo de cuanto demora al menos un cálculo realizado, cómo el área de una figura.
***
## Logo del grupo
![Logo](https://github.com/NotName-K/POO-R2/blob/main/Screenshot%202025-09-23%20110719.png?raw=true)

```python
class TipoInvalidoException(Exception):
  def __init__(self, message):
    super().__init__(message)
```

```
paquete_unico/
├── paquete/
│   ├── __init__.py
│   └── Shape.py
└── main.py
```
