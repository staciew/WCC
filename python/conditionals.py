#temp = int(raw_input('What is the temperature?'))

#print('You should bring the following items:')
#if temp <= 40:
    #print('Coat')
    #print('Hat')
    #print('Gloves')
#elif temp <= 70:
    #print('Coat')
    #print('Hat')
#else:
    #print('Nothing!')

#age = int(raw_input('How old are you?'))
#if age < 3:
    #print('baby')
#elif age < 18:
    #print('child')
#else:
    #print('adult')

age = int(raw_input('How old are you?'))
if age < 3:
    print('baby')
elif age < 16:
    print('child')
elif age < 18:
    print('adolescent')
elif age < 21:
    print('young adult')
else:
    print('adult')