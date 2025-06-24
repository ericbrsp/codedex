
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
    print(f'Type: {self.types}')
    print(f'Description: {self.description}')
    print(f'{self.is_caught}')



pika = Pokemon(25, 'Pikachu', 'Eletric', 'It has small electric sacs on both its cheeks.If threatened, it looses electric charges from the sacs', 'Pikachu has already been caught!')


pika.speak()
pika.details()
