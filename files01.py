liked_songs = {
    'Bad Habits': 'Ed Sheeran',
    'Shape of You': 'Ed Sheeran',
    'Blinding Lights': 'The Weeknd',
    'Levitating': 'Dua Lipa',
    'Peaches': 'Justin Bieber'
}

def write_liked_songs_to_file(lista, arquivo):
    with open(arquivo, 'w') as file:
        file.write('Liked Songs:\n')
        for song, artist in lista.items():
            file.write(f'{song} by {artist}\n')


write_liked_songs_to_file(liked_songs, 'songs.txt')
