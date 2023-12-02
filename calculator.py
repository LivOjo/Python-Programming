from tkinter import*
from tkinter import messagebox

window =Tk()
window .title('calculator')
window.minsize(width=220 ,height=250)
window.config(padx=20 , pady=20)

calc_entry= Entry(window,width=30 ,justify='right')
calc_entry.grid(row=0,column=0,columnspan=4,pady=5)
def solve():
    equation = calc_entry.get()
    try:
        solved = eval(equation)

    except:
        solved='error'
        messagebox.showinfo('message','errrrror')
    clear()
    insert(solved)
def insert(item):
    calc_entry.insert(END,item)

def clear():
    calc_entry.delete(0,END)

def delete():
    current_text=calc_entry.get()
    if current_text:
        new_text=current_text[:-1]
        calc_entry.delete(0,END)
        calc_entry.insert(0,new_text)


button1= Button(window,text="1", width=5,height=3, command=lambda:insert('1'))
button1.grid(row=1 , column=0)

button2= Button(window,text="2", width=5,height=3, command=lambda:insert('2'))
button2.grid(row=1 , column=1)

button3= Button(window,text="3", width=5,height=3, command=lambda:insert('3'))
button3.grid(row=1 , column=2)

button4= Button(window,text="4", width=5,height=3, command=lambda:insert('4'))
button4.grid(row=2 , column=0)

button5= Button(window,text="5", width=5,height=3, command=lambda:insert('5'))
button5.grid(row=2 , column=1)

button6= Button(window,text="6", width=5,height=3, command=lambda:insert('6'))
button6.grid(row=2 , column=2)

button7= Button(window,text="7", width=5,height=3, command=lambda:insert('7'))
button7.grid(row=3 , column=0)

button8= Button(window,text="8", width=5,height=3, command=lambda:insert('8'))
button8.grid(row=3 , column=1)

button9= Button(window,text="9", width=5,height=3, command=lambda:insert('9'))
button9.grid(row=3 , column=2)

button0= Button(window,text="0", width=5,height=3, command=lambda:insert('0'))
button0.grid(row=4 , column=0)

button10= Button(window,text="+", width=5,height=3, command=lambda:insert('+'))
button10.grid(row=1 , column=3)

button11= Button(window,text="-", width=5,height=3, command=lambda:insert('-'))
button11.grid(row=2 , column=3)

button12= Button(window,text="*", width=5,height=3, command=lambda:insert('*'))
button12.grid(row=3 , column=3)

button13= Button(window,text="/", width=5,height=3, command=lambda:insert('/'))
button13.grid(row=4 , column=3)

button14= Button(window,text="clear", width=10,height=3, command=clear)
button14.grid(row=5 , column=2,columnspan=2)

button15= Button(window,text=".", width=5,height=3, command=lambda:insert('.'))
button15.grid(row=4 , column=2)

button16= Button(window,text="del", width=5,height=3, command=delete)
button16.grid(row=4 , column=1)

button17= Button(window,text="=", width=10,height=3, command=solve)
button17.grid(row=5 , column=0,columnspan=2)

window.mainloop()