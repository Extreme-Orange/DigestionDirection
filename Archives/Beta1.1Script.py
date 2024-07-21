# Starting and Ending Location Dictionary
CheatSheet = dict()
CheatSheet['holland village'] = {'nus', 'tkk'}
CheatSheet['bugis'] = {'nus', 'bedok'}
CheatSheet['orchard'] = {'nus', 'serangoon'}
CheatSheet['bishan'] = {'tkk', 'serangoon'}
CheatSheet['paya lebar'] = {'bedok', 'serangoon'}
CheatSheet['kallang'] = {'bedok', 'tkk'}

# List of all possible starting locations
PossibleStarts = ['nus', 'tkk', 'serangoon', 'bedok']

# Asking for the first location
x = 0
while True:
    L1 = str.lower(input('First Location:'))
    for location in PossibleStarts:
        if L1 == location:
            x = x + 1
            break
        else:
            continue

    if x > 0:
        break
    else:    
        print('Invalid Location!')
        continue

# Asking for the second location
y = 0
while True:
    L2 = str.lower(input('Second Location:'))
    for location in PossibleStarts:
        if L2 == location:
            y = y + 1
            break
        else:
            continue

    if y > 0:
        break
    else:    
        print('Invalid Location!')
        continue

# Searching for ideal end location
Pair = {L1, L2}
z = 0
while True:
    for end, start in CheatSheet.items():
        if Pair == start:
            z = z + 1
            print('You should go to:', end)
            break
        else:
            continue
    if z > 0:
        break
    else:
        print('Sorry!')
        break