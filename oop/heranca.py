# herança
class Parent:
  def __init__(self):
    print('calling parent constructor')
  
  def parent_method(self):
    print('calling parent method')

  def duplicated_method(self):
    print('método duplicado: parent')


class Child(Parent):
  def __init__(self):
    print('calling child constructor')
  
  def child_method(self):
    print('calling child method')

# quando a classe herda um método com nome já definido nela, 
# o método definido na classe tem prioridade sobre o herdado.
  def duplicated_method(self): 
    print('método duplicado: child')


p = Parent()
c = Child()

p.parent_method()
c.child_method()
# por conta da herança a classe child consegue chamar o método da classe parent
c.parent_method()

p.duplicated_method()
# método definido também em Parent, nesse caso,
# o método definido na classe tem prioridade sobre o herdado.
c.duplicated_method()

# herança multinivel
# a classe OtherChild possui os metodos da classe Child e da classe Parent, pois Child possui herança de Parent
# OtherChild -> herda de -> Child -> que herda de -> Parent
class OtherChild(Child):
  def __init__(self):
    print('calling other child constructor')

  def other_method(self):
    print('calling other child method')

o = OtherChild()
o.parent_method()
o.child_method()
o.other_method()
# nesse caso, o método duplicado assumiu o comportamento descrito na primeira herança(Child).
o.duplicated_method()


# herança hibrida
class Uncle():
  def __init__(self):
      print('calling uncle constructor')
  
  def uncle_method(self):
    print('calling uncle method')

# classe HybridChild herda de duas classes, Parent e Uncle
class HybridChild(Parent, Uncle):
  def __init__(self):
    print('calling hybrid child constructor')
  
  def hybrid_method(self):
    print('calling hybrid method')

h = HybridChild()

h.parent_method()
h.uncle_method()
h.hybrid_method()