print('What is yout height? (Use cm) ')
height = int(input())
print('How many credits you have? ')
credits = int(input())

if height >= 137 and credits == 10:
  print('Enjoy the ride!')
elif height < 137 and credits == 10:
  print('You are not tall enough to ride')
elif height >= 137 and credits < 10:
  print('You dont have enough credits')
else:
  print('You have not met either requirement')
