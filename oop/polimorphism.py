# polimorfismo é o principio pelo qual duas ou mais classes
# derivadas de uma mesma superclasse podem invocar métodos
# que tem a mesma identificação mas comportamentos distintos.

# Quando o polimorfismo está sendo utilizado, o comportamento que será adotado
# por um método só será definido durante a execução.

# https://www.dca.fee.unicamp.br/cursos/PooJava/polimorf/index.html

class Bear:
  def sound(self):
    print('Groooarrr!')

class Dog:
  def sound(self):
    print('Woof! woof!')

def makeSound(animal):
  animal.sound()

bear = Bear()
dog = Dog()

makeSound(bear)
makeSound(dog)


