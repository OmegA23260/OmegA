import tkinter as tk
from tkinter import messagebox

def chtotot():
    try:
        summa = float(SUMMA1.get())
        hochu_val = float(hochu1.get())
        itogo = summa / (1 - hochu_val / 100)
        result_var.set(f"Тогда сумма договора, должна быть: {itogo:.2f}")
        result_label.config(bg="#A9A9A9", fg="black")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа", bg="#A9A9A9")

def reset():
    SUMMA1.delete(0, tk.END)
    hochu1.delete(0, tk.END)
    result_var.set("")
    result_label.config(bg="#A9A9A9", fg="black")

window = tk.Tk()
window.title("Обратный Процент")
window.resizable(width=False, height=False)
window.geometry("600x250")
window["bg"] = "#D3D3D3"

SUMMA = tk.Label(window, text="Сумма после вычета %:", font=("Arial", 15), fg="black", bg="#D3D3D3")
SUMMA.place(x=10, y=5)

SUMMA1 = tk.Entry(window, width=20, font=("Arial", 15), bg="#A9A9A9")
SUMMA1.place(x=20, y=35)

hochu = tk.Label(window, text="% который будет удержан:", font=("Arial", 15), fg="black", bg="#D3D3D3")
hochu.place(x=10, y=70)

hochu1 = tk.Entry(window, width=20, font=("Arial", 15), bg="#A9A9A9")
hochu1.place(x=20, y=100)

btn = tk.Button(window, text="Высчитать", command=chtotot)
btn.place(x=30, y=140)

reset_btn = tk.Button(window, text="Сбросить", command=reset)
reset_btn.place(x=150, y=140)

result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, font=("Arial", 15), fg="black", bg="white")
result_label.place(x=20, y=180)

window.mainloop()