print('Ile masz piesków?')
numDogs = input()
try:
    if int(numDogs) >= 2:
        print('To wystarczy')
    else:
        print('To za mało')
except ValueError:
    print('You did not enter a number.')

print('Kochasz je?')
odp = input()
if odp.lower() == 'tak':
    print('One Ciebie też!')
else:
    print('Chyba jesteś GOPI')
    
