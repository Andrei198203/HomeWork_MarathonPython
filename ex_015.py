while True:
    try:
    number = int(input('Integer number > '))
    print(number)
    break
except ValueError:
     
    print('Not number.Try again') 