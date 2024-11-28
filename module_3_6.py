import tkinter as tk

def add():
    unswer.delete(0,tk.END)
    unswer.insert(0, str(str(int(number1.get()) + int(number2.get()))))

def sub():
    unswer.delete(0,tk.END)
    unswer.insert(0, str(str(int(number1.get()) - int(number2.get()))))

def mul():
    unswer.delete(0,tk.END)
    unswer.insert(0, str(str(int(number1.get()) * int(number2.get()))))

def div():
    unswer.delete(0,tk.END)
    unswer.insert(0, str(str(int(number1.get()) / int(number2.get()))))

window= tk.Tk()
window.title("Калькулятор v1.0")
window.geometry("275x350")
window.resizable(False,False)
btn_add=tk.Button(window,text="+", width=2, height=1, command=add)
btn_add.place(x=50,y=150)
btn_sub=tk.Button(window,text="-", width=2, height=1, command=sub)
btn_sub.place(x=100,y=150)
btn_mul=tk.Button(window,text="*", width=2, height=1, command=mul)
btn_mul.place(x=150,y=150)
btn_div=tk.Button(window,text="/", width=2, height=1, command=div)
btn_div.place(x=200,y=150)
number1=tk.Entry(window,width=28)
number1.place(x=50,y=75)
number1_text = tk.Label(window, text="Введите первое число 1:")
number1_text.place(x=50,y=50)
number2=tk.Entry(window,width=28)
number2.place(x=50,y=125)
number2_text = tk.Label(window, text="Введите первое число 2:")
number2_text.place(x=50,y=100)
unswer=tk.Entry(window, width=28)
unswer.place(x=50,y=225)
unswer_text = tk.Label(window, text="Результат:")
unswer_text.place(x=50, y=200)
window.mainloop()
