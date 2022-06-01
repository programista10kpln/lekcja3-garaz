from random import randint

garage = ['volkswagen golf', 'ferrari laferrari', 'lexus lfa']

print('witaj w garażu!')


def afterChoice():
    while True:
        try:
            end = input('Czy to wszystko na dziś? [tak] lub [nie]\n')
            if end == 'tak':
                print('bywaj')
                exit()
            elif end == 'nie':
                makingChoice()
            else:
                print('zła wartość')
                continue
        except ValueError:
            print('zła wartość')


def makingChoice():
    while True:
        try:
            print('co chcesz zrobić?')
            print(
                '[1] wyświetlić posiadane auta\n[2] dodać auto\n[3] usunąć auto\n[4] przejechać się autem\n[0] zakończyć')
            choice = int(input())
            if 0 <= choice <= 4:
                break
            else:
                print('nie ma takiej opcji')
                continue
        except ValueError:
            print('zła wartość')
    match choice:
        case 1:
            print(garage)
            afterChoice()
        case 2:
            garage.append(input('wpisz jakie auto chcesz dodać\n'))
            print('zrobione')
            afterChoice()
        case 3:
            while True:
                try:
                    print(garage)
                    carToDelete = int(input('podaj numer auta, które idzie na złom\n'))
                    if carToDelete > 0 and carToDelete <= len(garage):
                        garage.pop(carToDelete - 1)
                        print('zrobione')
                        afterChoice()
                    else:
                        print('nie masz auta o takim ID')
                        continue
                except ValueError:
                    print('zła wartość')
        case 4:
            while True:
                try:
                    print(garage)
                    carToDrive = int(input('podaj numer auta, którym chcesz się przejechać\n'))
                    if carToDrive > 0 and carToDrive <= len(garage):
                        speed = randint(10, 320)
                        print('pojechałeś ' + str(speed) + ' km/h')
                        afterChoice()
                    else:
                        print('nie masz auta o takim ID')
                        continue
                except ValueError:
                    print('zła wartość')
        case 0:
            print('bywaj')
            exit()


makingChoice()
