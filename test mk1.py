from pyautogui import *
from time import sleep
z=0
print('SpammyV1')
a=input('Please enter the message you want to spam.')
b=int(input('Please enter the number of times you want to spam the message.'))
c= int(input(' Time in between consecutive messages . Please specify time greater than equal to one (Time is considered in seconds). '))
print('Open the Window in which you want to spam messages. before the program begins.\n The program will begin in 20 seconds . Please wait .')
sleep(20)
while True:
    for i in range(0,b):
        write(a)
        press('enter')
        sleep(c)
    while True:
        d=input('Do you want to spam more messages ?(y/n) ')
        if d.lower()=='no' or d.lower()=='n':
            quit()
        elif d.lower()=='yes' or d.lower()=='y':
            z=1
            break
        else: print('What do you want to do ?????')
    while True:
        if z==1:
            e=input('Do you want to use the same message ? (y/n)')
            if e.lower()=='yes' or e.lower()=='y':
                break
            elif  e.lower()=='no'  or e.lower()=='n':
                a=input('Please enter the new message to spam.')
                break
            else: print('what u want to do ?? \n type again ')
    while True:
        f=input('Do you want to spam the messages same number of time ?(y/n)')
        if f.lower()=='no' or f.lower()=='n':
            b=int(input('Please enter the number of times you want to spam messages.'))
            break
        elif f.lower()=='yes' or f.lower()=='y':
            break
        else: print('What do you want to do ?? \n type again .')       
    while True:
        g=input('Do you want to spam the messages after same time interval(y/n)')
        if g.lower()=='yes' or  g.lower()=='y':
            break
        elif g.lower()=='no' or g.lower()=='n':
            c=int(input('Please enter the time interval between two consecutive messages.'))
            break
        else: print('What do you want to do ?? \n type again .')
    print('open the window now.')
    sleep(20)
