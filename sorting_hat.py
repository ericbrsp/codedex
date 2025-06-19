gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print(gryffindor)

print('Do you like Dawn or Dusk? ')
print('1 for Dawn | 2 for Dusk')
q1 = int(input())

if q1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw = ravenclaw + 1
elif q1 == 2:
  hufflepuff = hufflepuff + 1 
  slytherin = slytherin + 1
else:
  print('Wrong input')


print('When I’m dead, I want people to remember me as ')
print('1 The Good | 2 The Great | 3 The Wise | 4 The Bold ')
q2 = int(input())

if q2 == 1:
  hufflepuff = hufflepuff + 2
elif q2 == 2:
  slytherin = slytherin + 2
elif q2 == 3:
  ravenclaw = ravenclaw + 2
elif q2 == 4:
  gryffindor = gryffindor + 2
else:
  print('Wrong input')

print('Which kind of instrument most pleases your ear? ')
print('1 The violin | 2 The trumpet | 3 The piano | 4 The drum ')
q3 = int(input())

if q3 == 1:
  slytherin = slytherin + 3
elif q3 == 2:
  hufflepuff = hufflepuff + 4
elif q3 == 3:
  ravenclaw = ravenclaw + 4
elif q3 == 4:
  gryffindor = gryffindor + 4
else:
  print('Wrong input')


print(f'Gryffindor points: {gryffindor}')
print(f'Ravenclaw points: {ravenclaw}')
print(f'Hufflepuff points: {hufflepuff}')
print(f'Slytherin points: {slytherin}')
