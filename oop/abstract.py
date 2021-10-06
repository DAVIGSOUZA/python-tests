# CLASSES ABSTRATAS
# possuem pelo menos UM método abstrato
# não podem ser instanciadas, necessitam de uma subclasse 
# que forneça implementações para os métodos abstratos.

# classes abstratas podem ser consideradas uma blueprint para outras classes

# MÉTODOS ABSTRATOS
# métodos declarados na classe parent sem implementação.
# são implementados na classe child

# Para criar uma classe e métodos abstratos em python:
# é preciso importar abc(abstract base class) e abstractmethod
# caso contrário python tratará como classes e métodos normais.

# antes de declarar um método abstrato é necessário o decorator @abstractmethod

from abc import ABC, abstractmethod

# Herdando ABC informa ao python que uma classe abstrata está sendo criada
class Abstrata(ABC):
  # com o decorator @abstractmethod informa ao python que um método abstrata está sendo criado
  @abstractmethod
  def add(self, a, b):
    pass
  @abstractmethod
  def sub(self, a, b):
    pass

# Qualquer classe herdando de uma classe abstrata 
# PRECISA implementar TODOS métodos abstratos
class MostreResultado(Abstrata):
  def add(self, a, b):
    print(a + b)
  
  def sub(self, a, b):
    print(a - b)

class RetorneResultado(Abstrata):
  def add(self, a, b):
    return a + b
  
  def sub(self, a, b):
    return a - b

mostre = MostreResultado()
retorne = RetorneResultado()

mostre.add(3, 2)
mostre.sub(10, 3)

print(retorne.add(6, 4))
print(retorne.sub(20, 6))
