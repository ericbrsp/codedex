import random as rd

def play():
  print(' ♣️  ♦️  Welcome to Vegas Baby!  ♦️  ♠️ ' )
  print('------------------------------------')
  print('||| Use Y to YES and use N to NO |||')
  print('------------------------------------')
  answer = input('Do you want to play? ' )
  #options = ['🍒','7️⃣', '7️⃣', '7️⃣']
  options = ['🍒', '🍇', '🍉', '7️⃣', '🔔', '⭐']
  venceu = False


  while (answer.upper() == 'Y') and venceu == False:
    jogada = rd.choices(options, k=3)
    print(' | '.join(jogada))
    if jogada[0] == '7️⃣' and jogada[1] == '7️⃣' and jogada[2] == '7️⃣':
      print('Jackpot! 💰')
      venceu = True
    else:
      print('Ups! Não foi nesta tentativa :(')
      if venceu == False:
        answer2 = input('Quer jogar novamente? ')
        if answer2.upper() != 'Y':
          print('👋 Saindo do jogo... Volte sempre!')
          break

  if answer.upper() != 'Y' and not venceu:
    print('👋 Saindo do jogo... Volte sempre!')
  elif venceu:
    print('🎈 Obrigado por jogar! Você é um campeão! 🎈')
