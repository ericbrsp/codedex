

translations = {
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
    'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}
    

lingua = input('Digite a lingua: ' )
palavra = input('Digite a palavra: ')


if lingua in translations and palavra in translations[lingua]: 
     print(translations[lingua][palavra])
else:
     print('erro')
