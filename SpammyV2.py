from pyautogui import *
from time import sleep
def input1():
    global message,number,time
    message=input('Please enter the message you want to spam.')
    number=int(input('Please enter the number of times you want to spam the message. '))
    time=int(input('Please enter the timeperiod (taken in as seconds) inbetween the consecutive messages. '))
    Spam(message,time,number)
def Spam(message,time,number):
    print('Messages will start spamming after 20 seconds.')
    sleep(20)
    for i in range(0,number):
        write(message)
        press('enter')
        sleep(time)
def a():
    a1=input('Do you want to use the same message  ?(y/n)')
    if a1.lower()=='y' or a1.lower()=='yes':
        a1=message
        return(a1)
    elif a1.lower()=='no' or a1.lower()== 'n':
        a1=input('Please enter the new message you want to spam.')
        return(a1)
    else : 
        print('You gave a wrong input .')
        a()   
def b():
    b1=input('Do you want to spam the message same number of time?(y/n)')
    if   b1.lower()=='y' or b1.lower()=='yes':
        b1=number
        return(b1)
    elif b1.lower()=='n' or b1.lower()=='no':
        b1=int(input('Please enter the number of times you want to spam the message.'))
        return(b1)
    else: 
        print('You gave a wrong input .')  
        b()  
def c():
    c1=input('Do you want the timeperiod between the consecutive messages same ? (y/n)')
    if c1.lower()=='y' or c1.lower()=='yes':
        c1=time
        return(c1)
    elif c1.lower()=='n' or c1.lower()=='no':
        c1=int(input('Please enter the timeperiod (taken in as seconds) inbetween the consecutive messages.'))
        return(c1)
    else :
        print('You gave a wrong input .') 
        c()
             
            
def repeat():
    x=input('Do you want to spam more messages ?(y/n)')
    if x.lower()=='y' or x.lower()=='yes':
        a2=a()
        b2=b()
        c2=c()
        Spam(a2,c2,b2)   
        repeat()
    elif x.lower()=='n'  or x.lower()=='no':
        exit()
    else:
        print('Hey you have entered a wrong input . Dear try again.') 
        repeat() 
        sleep(3)         
            
                
input1()
sleep(2)
repeat()
       
        