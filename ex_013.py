age = int(input("Age> "))

access_list = ["Bill", "Jill", "Garry"]
if age>18:
    name = input('Name> ')
    print(f"Your name is {name}")
    if name.capitalize() in access_list:
        print(f'Welcome {name}')
    else:
        print('No enter')
else:
    print ('Too young')