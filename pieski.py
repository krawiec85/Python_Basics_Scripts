print('Ile masz piesków?')
numDogs = input()
if int(numDogs) >= 2:
    print('To wystarczy')
else:
    print('To za mało')

print('Kochasz je?')
odp = input()
if odp.lower() == 'tak':
    print('One Ciebie też!')
else:
    print('Chyba jesteś GOPI')

print('A Mateuszka?')
odp = input ()
if odp.lower () == 'tak' or odp.lower () == 'tez':
    print ('On Ciebie też!')

print ('Muszę już iść. Pa!')
odp = input ()
if odp.lower () == 'Pa':
    print ('Pa') 
