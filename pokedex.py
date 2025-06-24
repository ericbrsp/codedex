
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f'{self.name}! {self.name}!')

  def details(self):
    print(f'Entry Number: {self.entry}')
    print(f'Name: {self.name}')
    if len(self.types) == 1:
      print('Type: ' + self.types[0])
    else:
      print('Type: ' + self.types[0] + '/' + self.types[1])
    print(f'Description: {self.description}')
    if self.is_caught:
      print(self.name + ' has already been caught!')
    else:
      print(self.name + ' hasn\'t been caught yet.')



#Crie um Pokémon com essas informações e guarde ele na variável pika
pika = Pokemon(25, 'Pikachu', ['Eletric'], 'It has small electric sacs on both its cheeks.If threatened, it looses electric charges from the sacs', True)

charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', False)
gyarados = Pokemon(130, 'Gyarados', ['Water', 'Flying'], 'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.', False)

pika.speak()
pika.details()
