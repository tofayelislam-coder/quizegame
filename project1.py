




print("\t\t\tpython PROGRAM QUIZ GAME\n")
print('\n\t\t________________________________________')
print('"\n\t\t\t   WELCOME"')
print('\n\t\t\t      to ')
print('\n\t\t\t   THE GAME ')
print('\n\t\t________________________________________')
print('\n\t\t________________________________________')
print('\n\t\t   BECOME A MILLIONAIRE!!!!!!!!!!!   ')
print('\n\t\t > Press your id(last 3 digits)to start the game')
print('\n\t\t >  press your id(first 3 digit)to know the rules ')
print('\n\t\t________________________________________')
print('\n\t\t________________________________________')




rule =int(input('enter pass-code:'))
if rule>=34:
    print('THW RULES')
    print('#################')
    print('1.enter any number in your choice the range of your number is 1 to 10')
    print('2.after insert your choice then press enter')
    print('3.only five times you insert your number')
    print('4.in the end of the game was show your score and show the number you loss ')
    print('5.enjoy the game')
    print('6.you start the game')
else:
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('s o r  ry y o u t y p e w r o n g c o d e')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@')




print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
game =int(input('enter pass-cde to start the game:'))
if game>=33:
    print('............................................')
    import random

    count = 0
    counts = 0
    score = 0
    for x in range(1, 6):
        guessNumber = int(input('Enter any number 1 t0 10:'))
        randomNumber = int(random.random() * 10)
        if guessNumber == randomNumber:
            print('win')
            count = count + 1
            score = count * 25
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        else:
            print('loss')
            counts = counts + 1
            print('the randomnumber is:', randomNumber)
            print('-------------------------------------')
            print('-------------------------------------')
            continue

    print('-----------------------')
    print('your score is:', count)
    print('your wrong answer is :', counts)
    print('your total score:', score)
    print('T H A N K Y O U')
else:
    print('@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('s o r r y y o u t y p e w r o n g c o d e')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@')
















