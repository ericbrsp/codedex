class City:
  def __init__(self, name, country, population, landmarks, nickname, sea):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.nickname = nickname
    self.sea = sea



sao_paulo = City('Brasil', 'São Paulo', 12999, 'Sé', 'Sampa', True)
rio_de_janeiro = City('Brasil', 'Rio de Janeiro', 1733, 'Cristo', 'RJ', True)

print(vars(sao_paulo))
