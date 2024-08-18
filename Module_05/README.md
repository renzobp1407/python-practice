## Built in Errors in Python

- IndexError: cuando el indice que buscas no existe en lo que buscas o está incorrecto
 
 IndexErropr: list index out of range

- KeyError: ocurre cuando tu usas una Key o llave de forma incorrecta

  ej:
  ```python
   movie[release]
   KeyError 'release' 
  ```
- NameError: cuando la variable no existe o no está definida

  NameError:  name 'hello' is not defined

- AttributeError: cuando utilizamos mal una funcion o atributo definido en la funcion

ej: 
  friends.intersection(friends_nearby)
 'list' object has no attribure 'intersection'
 solo se puede utilizar interseccion con diccionarios, no con listas

- NotImplementedError: remplaza el error de algo que no se tiene implementado 

  ```python
   def login (self):
     raise NotImplementedError ('This feature has not been implemented yet')
  ```

- RuntimeError: error generico cuando se ejecuta un codigo en el tiempo de ejecucuón puede ser cualquier cosa


- SyntaxError: son errores es cuando estas escribiendo mal el codigo de python sin seguir las reglas

  ```python
   class user
     def__init__ (self, name, password)
  ```

  en este caso hace falta `:` despues del nombre de la clase `user`

- IndentationError:  error al momento de adecuar la indentacion de las lines de codigo y los espacios
 ej: espacios no definidos entre class y def

  ```python
   class user
   def__init__ (self, name, password)
  ```

- TabError: es un error comun cuando se cambian de editores, es cuando se mezcla espacios con tabulacion, eso Python lo reconoce cuando está mezclado



- TypeError: es cuando se intenta combinar diferentes tipos de variables o funciones con distinta naturaleza, como numero con strings o booleans con int

  ```python
   5 + 'hello'
   TypeError: unsupported operand type(s) for +: 'int' and 'str'
  ```
- ValueError: cuando se esta asignando un valor incorrecto a la naturaleza de la variable

  ```python
   int('20.5')
   TypeError: invalid literal for +: int)  with base 10: '20.5'
  ```

- ImportError: cuando se importa mal o no se importa la libreria o archivo que se está implementando, tambien con los circular imports cuando se importan 2 archivos circularmente


- DeprecationWarning: es cuando se avisa que lo que estas intentando hacer o la funcion está desactualizada o se va a dejar de usar



