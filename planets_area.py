from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
  area = (4*pi)*(2440*2440)
elif random_planet == 'Venus':
  area = (4*pi)*(6052*6052)
elif random_planet == 'Earth':
  area = (4*pi)*(6371*6371)
elif random_planet == 'Earth':
  area = (4*pi)*(6052*6052)
elif random_planet == 'Mars':
  area = (4*pi)*(3390*3390)
elif random_planet == 'Saturn':
  area = (4*pi)*(58232*58232)
else:
  print('"Oops! An error occurred')

print(random_planet)
print(area)
