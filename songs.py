from functools import reduce

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def five_minutes(lista):
    return lista[1] > 5.00 # retorna True para os números da tupla dentro da lista na posicao 1

def minutes_to_seconds(lista):
  duration = lista[1]
  minutes = int(duration) 
  seconds = (duration - minutes) * 100  
  return minutes * 60  + round(seconds)

def add_durations(total, song):
  duration = song[1]
  return total + duration


filtering_songs = filter(five_minutes, playlist) # aplica a função a cada elemento da lista

total_playtime = reduce(add_durations, playlist, 0)

convert_to_seconds = list(map(minutes_to_seconds, playlist))


print(convert_to_seconds)

print(list(filtering_songs))

print(total_playtime)
