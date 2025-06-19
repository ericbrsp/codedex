
import random as rd

question = input('')
answer = rd.randint(1, 9)

if answer == 1:
  print(f'Question: {question}')
  print('Magic 8 Ball: Yes - definitely')
elif answer == 2:
  print(f'Question: {question}')
  print('Magic 8 Ball: It is decidedly so')
elif answer == 3:
  print(f'Question: {question}')
  print('Magic 8 Ball: Without a doubt')
elif answer == 4:
  print(f'Question: {question}')
  print('Magic 8 Ball: Reply hazy, try again')
elif answer == 5:
  print(f'Question: {question}')
  print('Magic 8 Ball: Ask again later')
elif answer == 6:
  print(f'Question: {question}')
  print('Magic 8 Ball: Better not tell you now')
elif answer == 7:
  print(f'Question: {question}')
  print('Magic 8 Ball: My sources say no')
elif answer == 8:
  print(f'Question: {question}')
  print('Magic 8 Ball: Outlook not so good')
else: 
  print(f'Question: {question}')
  print('Magic 8 Ball: Very doubtful')



