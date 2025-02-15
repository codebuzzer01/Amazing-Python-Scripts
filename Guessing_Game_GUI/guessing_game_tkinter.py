# -*- coding: utf-8 -*-
"""guessing_game_tkinter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OzOm77jUVrxo1jWWlQoXkj19Pc8D_GdC
"""

from tkinter import *
import random

root = Tk()
root.title('Number Guessing Game')
root.geometry('450x450+50+50')

font_used = ('Arial', 12)
#lower limit number
num1 = IntVar()
#upper limit number
num2 = IntVar()
#user guessed value
guessed_num = IntVar()
#value is the random value generated
global value
value= None
global attempts
attempts = 3

#generate random number
def get_rand():
  b4.configure(state=DISABLED)
  global value
  value = random.randint(num1.get(), num2.get())
  

#resets the window
def reset():
  num1.set(0)
  num2.set(0)
  guessed_num.set(0)
  global attempts
  attempts = 3
  b4.configure(state=NORMAL)
  b1.configure(state = NORMAL)
  l4.configure(text = '')
  l5.configure(text = 'You have 3 attempts left')
  b2.configure(state = DISABLED)


def check():
  global value
  #Label(root, text=str(value)).grid(row=8)

  #tells the user how many attempts are left
  global attempts
  attempts -= 1

  #if all attempts are over
  if attempts == 0 and guessed_num.get() != value:
    b1.configure(state=DISABLED)
    l5.configure(text = 'You have 0 attempts left')
    l4.configure(text='Sorry! All attempts done. The correct answer is ' + str(value), fg='red')
    b2.configure(text = 'Play Again', command=reset, state=NORMAL)
    b2.grid(row=9, column=1)
    b3.configure(text = 'Quit', command = root.quit)
    b3.grid(row = 9, column=2)
  else:
    #if attempts are still left 

    #if guessed value is correct
    if guessed_num.get() == value:
      l4.configure(text='Congratulations! You are right')
      b2.configure(text = 'Play Again', command=reset, state =NORMAL)
      b2.grid(row=9, column=1)
      b3.configure(text = 'Quit', command = root.quit)
      b3.grid(row = 9, column=2)
    
    #if guessed value is incorrect
    else:
      if guessed_num.get() > value:
        l4.configure(text='Better Luck Next time! Try a lesser number')
      else:
        l4.configure(text='Better Luck Next time! Try a greater number')
      l5.configure(text = 'You have ' + str(attempts) + ' attempts left')

l6 = Label(root, text = 'Input fields cannot be 0', font=font_used, fg='red')
l6.grid(row=0, columnspan=3, pady=5)

# from i.e lower limit
l1 = Label(root, text = 'From', font=font_used, fg='red')
l1.grid(row=1, column=0, sticky=W)
e1 = Entry(root, textvariable = num1, font=font_used, fg='blue')
e1.grid(row=1, column=1, padx=5, pady=5)

# to i.e upper limit
l2 = Label(root, text = 'To', font=font_used, fg='red')
l2.grid(row=2, column=0, sticky=W, padx=5, pady=5)
#locking numbers is neccessary as it generates only a single random number for the limit
b4 = Button(root, text = 'Lock Numbers', fg='magenta', command=get_rand)
b4.grid(row=3, columnspan=3, pady=5)
e2 = Entry(root, textvariable = num2, font=font_used, fg='blue')
e2.grid(row=2, column=1, padx=5, pady=5)


#guess the number
l3 = Label(root, text = 'Guess any number', font=font_used, fg='darkviolet')
l3.grid(row=4, columnspan=3,pady=5)

#label for showing the number of attempts
l5 = Label(root, text = 'You have 3 attempts left', font=font_used, fg='darkviolet')
l5.grid(row=5, columnspan=3,pady=5)

#the user enters the guessed number
e3 = Entry(root, textvariable = guessed_num, font=font_used, fg='darkorchid')
e3.grid(row=6, columnspan=3,pady=5)

#checks whether the guessed number is correct or not
b1 = Button(root, text='Check', font=font_used, fg='darkviolet', command=check)
b1.grid(row=7, columnspan=3, pady=5)

#displays the result
l4 = Label(root, text = 'Result', font=font_used, fg='magenta')
l4.grid(row=8, columnspan=3,pady=5)

#button for play again
b2 = Button(root)
#button for quit which closes the window
b3 = Button(root)


root.mainloop()

