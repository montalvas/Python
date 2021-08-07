class Pessoa:
    def __init__(self, nome):
        self.__nome = nome #atributo privado

p1 = Pessoa('Lucas')
print(p1._Pessoa__nome) #Acessa/modifica um atributo privado, não recomendado
p1.__nome = 'Miguel' #Ele não modifica o atributo, ele cria outro