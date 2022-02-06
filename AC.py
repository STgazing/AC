# from operator import truediv
import os
from re import L
# from tkinter.messagebox import NO

#this is color class
class color:
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'

#this func print banner
def banner():
    print(color.Magenta+'''
  
▄▀█ █▀█ █▀▀ ▄▀█   █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
█▀█ █▀▄ ██▄ █▀█   █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄''')
    print(f'{color.Cyan+"    Follow us in github:"} {color.Cyan+"https://github.com/STgazing"}')
    print('''

    ''')    

#this func displays the menue
def menue():
    print(color.Green+'[',color.Yellow+'1',color.Green+']' , color.Cyan+'Circle')
    print(color.Green+'[',color.Yellow+'2',color.Green+']' , color.Cyan+'Square')
    print(color.Green+'[',color.Yellow+'3',color.Green+']' , color.Cyan+'Rectangle')
    print(color.Green+'[',color.Yellow+'4',color.Green+']' , color.Cyan+'Triangle')
    print(color.Green+'[',color.Yellow+'5',color.Green+']' , color.Cyan+'Exit')
    print()
    
#this class calculate shapes area
class Area:

    def circle():
        r = int(input(f'{color.Green+"["} {color.Yellow+"+"} {color.Green+"]"} {color.Magenta+"Please enter radius of the circle:"}{color.Yellow+""} '))
        print(f'{color.Green+"["} {color.Yellow+"-"} {color.Green+"]"} {color.Green+"Circle Area: "}{3.14159*(r**2)}')
        print() 
    
    def square():
        s = int(input(f'{color.Green+"["} {color.Yellow+"+"} {color.Green+"]"} {color.Magenta+"Please enter a side of square: "}{color.Yellow+""} '))
        print(f'{color.Green+"["} {color.Yellow+"-"} {color.Green+"]"} {color.Green+"Square Area: "}{s*s}')
        print()
    
    def rectangle():
        l = int(input(f'{color.Green+"["} {color.Yellow+"+"} {color.Green+"]"} {color.Magenta+"Please enter lenth of the rectangle: "}{color.Yellow+""} '))
        w = int(input(f'{color.Green+"["} {color.Yellow+"+"} {color.Green+"]"} {color.Magenta+"Please enter width of the rectangle: "}{color.Yellow+""} '))
        print(f'{color.Green+"["} {color.Yellow+"-"} {color.Green+"]"} {color.Green+"Rectangle Area: "}{l*w}')
        print()
    
    def triangle():
        b = int(input(f'{color.Green+"["} {color.Yellow+"+"} {color.Green+"]"} {color.Magenta+"Please enter triangle base: "}{color.Yellow+""} '))
        h = int(input(f'{color.Green+"["} {color.Yellow+"+"} {color.Green+"]"} {color.Magenta+"Please enter triangle heigh: "}{color.Yellow+""} '))
        print(f'{color.Green+"["} {color.Yellow+"-"} {color.Green+"]"} {color.Green+"Triangle Area: "}{(b*h)/2}')
        print()
#this func clear the screen
def clear():
    os.system('clear')

#this func try the program again
def tryagain():
    msg = input(color.Cyan+'Do yo want try again? Y/n: ')
    if msg.upper() == 'Y':
        run()
    elif msg.upper() == 'N':
        print()
        print(color.Yellow+'See You Later :)')
        print()
        quit()
    else:
        tryagain()       
        
choose = None

#this func takes you to the selected option
def cond():
    if choose == 1:
        Area.circle()
    elif choose == 2:
        Area.square()
    elif choose == 3:
        Area.rectangle()
    elif choose ==4:
        Area.triangle()
    elif choose == 5:
        print()
        print(color.Yellow+'See You Later :)')
        print()
        quit()
    else:
        clear()
        run()    
        
def run():
    global choose
    clear()
    banner()
    menue()
    choose = int(input(f'{color.Green+"["} {color.Yellow+"+"} {color.Green+"]"} {color.Magenta+"Please choose a shape:"}{color.Yellow+""} '))
    cond()
    tryagain()

run()


# Mobin Ghanbarpour
# Mahyar Nasiri           










