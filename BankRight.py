'''
BANK MANAGEMENT SYSTEM
1. User should be able to create account, with name and account balance
2. User should be able to deposit
3. User should be able to withdraw
4. user should be able to view account balance
5. Every transaction must be recorded, and user must be able to see previous transactions
6. Use TKinter to create a graphical user interface according to how you want it
Advanced: Store user details and account details in a json file such that they can
be retrieved and used again when the program is opened again.
'''
from tkinter import*
from tkinter import messagebox

window=Tk()
window.title('BankRight')
window.geometry('500x300')

username_label=Label(window,text='username:')
username_label.grid(row=0,column=0)
username_entry=Entry(window,width=30,justify='left')
username_entry.grid(row=0,column=4)

password_label=Label(window,text='password:')
password_label.grid(row=1,column=0)
password_entry=Entry(window,width=30,justify='left',show='*')
password_entry.grid(row=1,column=4)

balance_label=Label(window,text='balance:')
balance_label.grid(row=2,column=0)
balance_entry=Entry(window,width=30,justify='left')
balance_entry.grid(row=2,column=4)

users={}

balancer=balance_entry.get()
username=username_entry.get()
def check():
    username=username_entry.get()
    password=password_entry.get()

    if username in users and password ==users[username]:
        messagebox.showinfo('You have logged in successfully!')
        username=username_entry.delete(0, END)
        password_entry.delete(0, END)


    else:
        messagebox.showerror('message', 'errrrror,your username or password is incorrect')
        password_entry.delete(0, END)


def create_account():
    username=username_entry.get()
    password=password_entry.get()


    if username and password :
        if username not in users:
            users[username] = password
            messagebox.showinfo('An account has been created for you successfully!')
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            balance_entry.delete(0, END)
        else:
            messagebox.showerror('This username already exists,please choose a different one.')
            username_entry.delete(0,END)
            password_entry.delete(0, END)
            balance_entry.delete(0,END)
    else:
        messagebox.showerror('Invalid input,please try again')


login_button=Button(window,text='Log in',width=12,height=3,command=check)
login_button.grid(row=3,column=0)

create_account=Button(window,text='Create Account',width=12,height=3,command=create_account)
create_account.grid(row=4,column=0)


class BankRight:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            return self.balance

    def view_balance(self):
        return self.balance

    def view_transactions(self):
        return "\n".join(self.transactions)


account=BankRight('olivia',100000)



frame =Frame(window)
frame.grid()

name_label =Label(frame, text=f"Account name: {account.name}")
name_label.grid(row=0, column=0, columnspan=2, sticky="w")

balance_label =Label(frame, text=f"Account balance: {account.balance}")
balance_label.grid(row=1, column=0, columnspan=2, sticky="w")

amount_label =Label(frame, text="Enter amount:")
amount_label.grid(row=2, column=0, sticky="e")

amount_entry =Entry(frame)
amount_entry.grid(row=2, column=1, sticky="w")

deposit_button =Button(frame, text="Deposit", command=lambda: deposit())
deposit_button.grid(row=3, column=0, sticky="w")

withdraw_button =Button(frame, text="Withdraw", command=lambda: withdraw())
withdraw_button.grid(row=3, column=1, sticky="w")

transactions_button =Button(frame, text="View transactions", command=lambda:transactions())
transactions_button.grid(row=4, column=0, columnspan=2, sticky="w")

output_text = Text(frame, width=40, height=10)
output_text.grid(row=5, column=0, columnspan=2, sticky="w")

def deposit():
    amount = float(amount_entry.get())
    balance = account.deposit(amount)
    balance_label.config(text=f"Account balance: {balance}")
    amount_entry.delete(0,END)
    output_text.insert(END, f"You deposited {amount}\n")

def withdraw():
    amount = float(amount_entry.get())
    balance = account.withdraw(amount)
    if isinstance(balance, str):
        output_text.insert(END, f"{balance}\n")

    else:
        balance_label.config(text=f"Account balance: {balance}")
        amount_entry.delete(0,END)
        output_text.insert(END, f"You withdrew {amount}\n")

def transactions():
    transactions = account.view_transactions()
    output_text.insert(END, f"Your transactions are:\n{transactions}\n")


window.mainloop()

