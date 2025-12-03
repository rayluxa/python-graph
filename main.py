import tkinter as tk
from tkinter import ttk, messagebox
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_numbers(n): #функуция для генерации рандомных чисел
    return [random.randint(1, 200) for x in range(n)]

def zero_each_t(data, t): #функция для замены каждой n переменной на 0
    data = data[:] #срез
    for i in range(t - 1, len(data), t): #t воодит пользователь, t-1 так как индексация с нуля
        data[i] = 0 #заменяем каждую n-переменную на 0
    return data

def draw_graph(canvas_frame, data): #функция что очищает контейнер для новго графика
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    fig = Figure(figsize=(6,3), dpi=90) #создаем контейнер для графика
    ax = fig.add_subplot(111)  #111 это 1 строка, 1 столбец, 1 график
    ax.bar(range(1, len(data)+1), data, color='skyblue') #рисуем прямоугольники которые будут на графике ( их высота случайно снегерированные числа)
    ax.set_xlabel("Index") #название оси Ох
    ax.set_ylabel("Hodnota") #название оси Оу
    ax.grid(True, axis='y', linestyle='--', alpha=0.5) #рисует линии паралельно оси Ох, так график лучше выглдяит

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame) #превращает график matplotlib (fig) в обычный Tkinter-виджет, который можно вставить в окно
    canvas.draw() #рисует наш график
    canvas.get_tk_widget().pack(fill="both", expand=True) # Берёт график matplotlib, чтобы он занял всё доступное пространство


#берёт N и T из полей → проверяет → генерирует числа → заменяет каждое T-е → выводит результат → строит график
def on_generate():
    try:
        N = int(entry_n.get()) #берем полученные числа из полей ввода на экране
        T = int(entry_t.get())
        if N <= 0 or T <= 0: #проверяем что числа больше или равны нулю
            raise ValueError
    except: #если нет выводим ошибку
        messagebox.showerror("Chyba", "Zadajte kladné celé čísla N a T")
        return

    nums = generate_numbers(N)
    modified = zero_each_t(nums, T)
    txt_output.delete("1.0", "end") #очищает весь текст где будут наши числа
    txt_output.insert("end", " ".join(map(str, modified))) #вставляет наши числа
    draw_graph(canvas_frame, modified) #построение графика

root = tk.Tk()
root.title("Zadanie: N čísel, každé T-te = 0")
root.geometry("800x600") #размер окна


#кнопки, функции этих кнопок, надписи, поля ввода и так далее
frame_top = ttk.Frame(root)
frame_top.pack(pady=10)
ttk.Label(frame_top, text="N:").grid(row=0, column=0)
entry_n = ttk.Entry(frame_top, width=8)
entry_n.grid(row=0, column=1, padx=5)
ttk.Label(frame_top, text="T:").grid(row=0, column=2)
entry_t = ttk.Entry(frame_top, width=8)
entry_t.grid(row=0, column=3, padx=5)
ttk.Button(frame_top, text="Generovať", command=on_generate).grid(row=0, column=4, padx=10)
ttk.Button(frame_top, text="Ukončiť", command=root.destroy).grid(row=0, column=5, padx=10)

txt_output = tk.Text(root, height=5) #создаёт многстрочное поле высотой 5 строк куда будут выводиться наши числа
txt_output.pack(fill="x", padx=10, pady=10)     #расстяжение

canvas_frame = ttk.Frame(root)
canvas_frame.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
