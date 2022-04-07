class Personaje:
    # Constructor de la clase
    # Inicializa los atributos y metodos de mi clase
    def __init__(self,nombre,colorTraje,tipo) -> None:
        
        # Atributos
        self.nombre = nombre
        self.colorTraje = colorTraje
        self.tipo = tipo

    # METODOS = ACCIONES = FUNCIONES    van despues del constructor
    def saludar(self):
        print('Hola...')