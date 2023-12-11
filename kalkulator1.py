#python
import os
os.system("clear")

print("\033[1;32;40m CALCULATOR PROGRAM MADE BY DR490Nv99 \n")
print("\033[1;33;40m THIS TOOL WILL HELP IN SOLVING BASIC MATHEMATICAL OPERATIONS FOR EDUCATIONAL PURPOSES\n")

print("""                                                                               _____
          — — —   ————     ___       ____  _    ____      ___    ______  ____ | __  |
        /   __ \ / __ \    | |      / ___ | |  | | |     / _  \  |__  _|/ __ \||__| /
        |  |    / /__\ \   | |      | |   | |  | | |    / /__\ \    ||  ||  |||     \

        |  |___/   __   \  | |_____ | |___| |__| | |___/  ___   \   ||  ||__|||   _  \

        \ ____/___|  |___\_|_______|\____/|______|_____|__|  |__|___||  \____/|__| \__\
                                   ==================Beta Version 2.0==============""")

print("\033[96m  :::::::::::::: CALCULATOR IS NOW WORKING.:::::::::::::\n") 
print("\033[94m Owner : BY DR490Nv99 \n")

def calculate():
    operation = input('''
Kamu pilih ( +,-,÷,× ) misal pilih + maka ketik + lalu Enter!
____________________________
| Type + for addition      |
| Type - for subtraction   |
| Type * for multiplication|
| Type / for division      |
----------------------------
=> ''')

    number_1 = int(input('•Ketik Angka Berapa: '))
    number_2 = int(input('•Ketik Angka Berapa: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("\033[1;31;40m You have not typed a valid operator, please run the program again\n.")

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
___________________________________
|Do you want to calculate again?   |
|Please type Y for YES or N for NO.|
------------------------------------
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
      print("\033[2;37;40m {÷}THANKS FOR USING THIS CALCULATOR SEE YOU LATER, By DR490Nv99\n")
    else:
        again()

calculate()
