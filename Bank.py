import tkinter as tk
from PIL import Image, ImageTk
import time

root = tk.Tk()
root.geometry('450x475')
root.title("K.RS Bank")
root.iconbitmap("C:/Users/rs914/Downloads/bank.ico")
root.maxsize(450, 550)
root.minsize(450, 500)
root.configure(bg='#333333')

def showAndSave():
    Holder = Holder_entry.get()
    Number = Number_entry.get()
    deposite = deposite_entry.get()

    if not Holder.strip():
        show.config(text='WARNING: Enter Account holder Name!', fg='red')
    elif not Number.strip():
        show.config(text='WARNING: Enter Account Number!', fg='red')
    elif check_box.get() != 1:
        show.config(text='WARNING: You not choose payment method!', fg='red')
    elif not deposite.strip():
        show.config(text='WARNING: Enter Amount for deposite!', fg='red')
    else:
        show.config(text='Amount deposite successfully.', anchor='se', fg='white')
         # save the depostie info
        with open('Deposite', 'w') as d:
            d.writelines(f'''
            K.RS Bank\n
    Account Hander: {acc_holder_value.get()}
    Account Number: {acc_number_value.get()}
    Deposite Method: Cash
    Deposite Amount: {cash_amount.get()}
    \nDeposite Time: {time.strftime('%H:%M:%S')} Date: {time.strftime('%d/%m/%Y')}
    ''')
        

   

frame1 = tk.Frame(root, bg='#333333')
frame1.pack()
frame2 = tk.Frame(root, bg='#333333')
frame2.pack(anchor='nw', pady=25, padx=10)
frame3 = tk.Frame(root, bg='#333333')
frame3.pack(side='bottom', pady=50, padx=0)

tk.Label(text='K.RS Bank .privacy', fg='white', bg='#333333').pack(anchor='se', side='bottom', padx=35)

title = tk.Label(frame1,bg='#333333', text='DEPOSITE  MONEY', fg='#FFFFFF', font='Serif 15 bold')
title.pack(pady=8)

tk.Label(frame2,font='Serif 10 ',bg='#333333', fg='#FFFFFF',  anchor='nw', text='Account Holder: ').grid(row=2, column=0, padx=5)
tk.Label(frame2,font='Serif 10 ',bg='#333333', fg='#FFFFFF', anchor='nw', text='Account Number: ').grid(row=3, column=0, padx=5)
tk.Label(frame2,font='Serif 10 ',bg='#333333', fg='#FFFFFF',  anchor='nw', text='Deposite Method: ').grid(row=4, column=0, padx=5)
tk.Label(frame2,font='Serif 9 ',bg='#333333', fg='#FFFFFF',  anchor='nw', text='DEFAULT CASH METHOD AVAILABE').grid(row=4, column=1)

acc_holder_value  = tk.StringVar()
acc_number_value = tk.StringVar()
cash_amount = tk.StringVar()
check_box = tk.IntVar()

Holder_entry = tk.Entry(frame2, bg='silver', textvariable=acc_holder_value)
Holder_entry.grid(row=2, column=1)
Number_entry = tk.Entry(frame2,bg='silver', textvariable=acc_number_value)
Number_entry.grid(row=3, column=1)
deposite_entry = tk.Entry(frame2,bg='silver', textvariable=cash_amount)
deposite_entry.grid(row=6, column=1)

tk.Checkbutton(frame2,variable=check_box, selectcolor='#5C5C5C', bg='#333333', fg='white', text='Cash Amount').grid(row=5, column=1)

show = tk.Label(frame3,bg='#333333', text='', font='Serif 12 bold')
show.pack(side='bottom', padx=0, pady=30)

tk.Button(frame2, bg='#B501B5', fg='white', text="Deposit", padx=10, pady=4, relief='raised', command=showAndSave).grid(row=9, column=1, pady=20, padx=40)

root.mainloop()