unit tests

python -m unittest test_functions.py

el archivo de pruebas debe llamarse siempre "test_" cuando empieza el nonmbre del archivo

al igual que las funciones, tambien debe llamarse "test_"

python -m unittest .\testing_funtions.py

pasando la tupla como 2 argumentos:
se utiliza el *inputs

inputs = (3, -5, 2)
        expected = -30
        self.assertEqual(multiply(*inputs), expected)

type hinting: es cuando se declara de antemano en la funcion que va a recibir solo un valor de un tipo (int, float, etc)

ej:
def greet(name: str) -> str: \ return f"Hello, {name}

ahí resibe un string y retorna un string


--------------------------------


El guion bajo (_) delante de capacity es una convención en Python para indicar que el atributo _capacity es de "uso interno" y que no debería accederse o modificarse directamente desde fuera de la clase, aunque sigue siendo accesible. No es una restricción formal, solo una práctica recomendada para señalar a otros programadores que este atributo está pensado para ser usado dentro de la implementación de la clase.

------------------------

el metodo SetUp sirve para settear el objeto o valor que quieres que se prueben en las funciones de las pruebas unitarias de esa clase

def seUp

tambien lo puedes declarar 1 por clase

@classmethod
def SetUpClass((cls))

lo recomendado es utilizar el SetUp Normal