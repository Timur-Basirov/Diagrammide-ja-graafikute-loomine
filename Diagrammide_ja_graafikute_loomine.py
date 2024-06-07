from tkinter import *  #импорт всех функций tkinter
from math import *  #импорт всех функций math
import matplotlib.pyplot as plt  #импорт matplotlib для графиков
import numpy  #импорт numpy для численных заданий

#глобальные переменные
global D, t, graf, K
D = -1  #дискриминант
t = "Lahendusi pole"  #текст по умолчанию если нету решения
graf = False  #виден ли график

#интерфейс
x = 500
y = 500
bg = "#add8e6"  #фон
fg = "#1c4226"  #цвет шрифта
height = 0
roundTo = 2  #точность округления для решений
step = 5
canGraph = False
K = True

#функция для выполнений квадратного уравнения
def solve():
    ent1_ = float(ent1.get())  #a
    ent2_ = float(ent2.get())  #b
    ent3_ = float(ent3.get())  #c
    D = ent2_ * ent2_ - 4 * ent1_ * ent3_  #решение через формулу дискриминанта
    if D > 0:
        x1_ = round((-1 * ent2_ + sqrt(D)) / (2 * ent1_), 2)  #первый корень
        x2_ = round((-1 * ent2_ - sqrt(D)) / (2 * ent1_), 2)  #второй корень
        t = f"X1 = {x1_}, \nX2 = {x2_}"  #текст с решением
        graf = True  #график можно построить
    elif D == 0:
        x1_ = round((-1 * ent2_) / (2 * ent1_), 2)  
        t = f"X1 = {x1_}"  
        graf = True  
    else:
        t = "Lahendusi ei ole"  #текст решений нет
        graf = False 
    lbl5.configure(text=f"D = {D}\n{t}")  #обновление текста с решениями
    return D, graf

#функция для построения графика квадратного уравнения
def graafik(graf: bool, D: float):
    D, graf = solve()  #solve ссылается на функцию для выполнения уравнения и получения значений дискриминанта и графика
    if graf == True:
        ent1_ = float(ent1.get())  #a
        ent2_ = float(ent2.get())  #b
        ent3_ = float(ent3.get())  #c
        x0 = (-ent2_) / (2 * ent1_)  #вершина параболы (x)
        y0 = ent1_ * x0 * x0 + ent2_ * x0 + ent3_  #вершина параболы (y)
        x1 = numpy.arange(x0 - 10, x0 + 10, 0.5)  #диапазон значений x для построения графика
        y1 = ent1_ * x1 * x1 + ent2_ * x1 + ent3_  # Вычисление значений y для построения графика
        fig = plt.figure()  #новое окно для графика
        plt.plot(x1, y1, 'r-d')  #построение графика
        plt.title("Ruutvõrrand")  #заголовок графика
        plt.ylabel('y')  #метка оси y
        plt.xlabel('x')  #метка оси x
        plt.grid(True)  #сетка для графика
        plt.show()  #отображение графика
        text = f"Porabula tipp ({x0}, {y0})"  #текст с координатами вершины параболы
    else:
        text = f"Graafikut ei saa kuidagi luua"  #текст,если график не может быть построен
    lbl5.configure(text=f"D = {D}\n{t}\n{text}") 

#функция для графика кита
def Vaal():
    x1 = numpy.arange(0, 9.5, 0.5)  #x1
    x2 = numpy.arange(-10, 0.5, 0.5)  #x2
    x3 = numpy.arange(-9, -2.5, 0.5)  #x3
    x4 = numpy.arange(-3, 9.5, 0.5)  #x4
    x5 = numpy.arange(5, 9, 0.5)  #x5
    x6 = numpy.arange(5, 8.5, 0.5)  #x6
    x7 = numpy.arange(-13, -8.5, 0.5)  #x7
    x8 = numpy.arange(-15, -12.5, 0.5)  #x8
    x9 = numpy.arange(-15, -10, 0.5)  #x9
    x10 = numpy.arange(3, 4, 0.5)  #x10

    y1 = (2 / 27) * x1 * x1 - 3
    y2 = 0.04 * x2 * x2 - 3
    y3 = (2 / 9) * (x3 + 6) ** 2 + 1
    y4 = (-1 / 12) * (x4 - 3) ** 2 + 6
    y5 = (1 / 9) * (x5 - 5) ** 2 + 2
    y6 = (1 / 8) * (x6 - 7) ** 2 + 1.5
    y7 = -0.75 * (x7 + 11) ** 2 + 6
    y8 = (-0.5) * (x8 + 13) ** 2 + 3
    y9 = [1] * len(x9)
    y10 = [3] * len(x10)

    plt.figure()  #окно для графика

    #построение графиков для всех частей
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10)
    plt.title("Vaal")  
    plt.ylabel("y")  
    plt.xlabel("x")  
    plt.grid(True)  
    plt.show()  

#функция для графика очки
def Prillid():
    x1 = numpy.arange(-9, -0.5, 0.5)  #диапазоны значений x 
    x2 = numpy.arange(1, 9.5, 0.5) 
    x3 = numpy.arange(-9, -0.5, 0.5) 
    x4 = numpy.arange(1, 9.5, 0.5) 
    x5 = numpy.arange(-9, -5.5, 0.5)  
    x6 = numpy.arange(6, 9.5, 0.5)  
    x7 = numpy.arange(-1, 1.5, 0.5) 

    y1 = (-1 / 16) * (x1 + 5) ** 2 + 2
    y2 = (-1 / 16) * (x2 - 5) ** 2 + 2
    y3 = (1 / 4) * (x3 + 5) ** 2 - 3
    y4 = (1 / 4) * (x4 - 5) ** 2 - 3
    y5 = -1 * (x5 + 7) ** 2 + 5
    y6 = -1 * (x6 - 7) ** 2 + 5
    y7 = -0.5 * x7 ** 2 + 1.5

    plt.figure()  
    
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7)
    plt.title("Prillid")  
    plt.ylabel("y")  
    plt.xlabel("x")  
    plt.grid(True)  
    plt.show()  

# Функция для графика зонт
def Vihmavari():
    x1 = numpy.arange(-12, 12.5, 0.5) 
    x2 = numpy.arange(-4, 4.5, 0.5)  
    x3 = numpy.arange(-12, -3.5, 0.5)  
    x4 = numpy.arange(4, 12.5, 0.5)  
    x5 = numpy.arange(-4, 0.5, 0.5)  
    x6 = numpy.arange(-4, 0.7, 0.5)  

   
    y1 = (-1 / 18) * x1 ** 2 + 12
    y2 = (-1 / 8) * x2 ** 2 + 6
    y3 = (-1 / 8) * (x3 + 8) ** 2 + 6
    y4 = (-1 / 8) * (x4 - 8) ** 2 + 6
    y5 = 2 * (x5 + 3) ** 2 - 9
    y6 = 1.5 * (x6 + 3) ** 2 - 10

    plt.figure() 

    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6)
    plt.title("Vihmavari")  
    plt.ylabel("y") 
    plt.xlabel("x") 
    plt.grid(True)  
    plt.show() 

#функция для добавления, удаления кнопок и радиокнопок для выбора графиков
def extend():
    global K, whaleRB, GlassesRB, UmbrellaRB, solve2B, choice
    if K == True:
        K = not K
        btn4.config(text="Eemalda graafikud")  # Изменение текста кнопки
        choice = IntVar()
        whaleRB = Radiobutton(aken, text="Vaal", bg=bg, fg=fg, font="Arial 24", height=height, width=x, variable=choice, value=1, command=choice)
        GlassesRB = Radiobutton(aken, text="Prillid", bg=bg, fg=fg, font="Arial 24", height=height, width=x, variable=choice, value=2, command=choice)
        UmbrellaRB = Radiobutton(aken, text="Vihmavari", bg=bg, fg=fg, font="Arial 24", height=height, width=x, variable=choice, value=3, command=choice)
        solve2B = Button(aken, text="Näita graafikut", bg=bg, fg=fg, font="Arial 24", height=height, width=x, command=solve2)
        whaleRB.pack(side="top")
        GlassesRB.pack(side="top")
        UmbrellaRB.pack(side="top")
        solve2B.pack(side="top")
    elif K == False:
        K = not K
        btn4.config(text="Näita graafikut")  # Изменение текста кнопки
        whaleRB.destroy()  # Удаление радиокнопки "Вал"
        GlassesRB.destroy()  # Удаление радиокнопки "Очки"
        UmbrellaRB.destroy()  # Удаление радиокнопки "Зонт"
        solve2B.destroy()  # Удаление кнопки "Показать график"

#функция для отображения выбранного графика
def solve2():
    var = choice.get()
    if var == 1:
        Vaal()  #показать график кит
    elif var == 2:
        Prillid()  #график очки
    elif var == 3:
        Vihmavari()  #график зонт
    else:
        pass

#настройка окна 
aken = Tk()
aken.title("Решение квадратного уравнения") 
aken.geometry("600x500")
aken.title("Tkinteri kasutamine")
tekst = "Pealkiri\n"

var = IntVar()

lbl = Label(aken, text="Калькулятор для квадратных уравнений", font="Arial 16", bg=bg)
ent1 = Entry(aken, font="Arial 20", fg=fg, bg=bg, width=4) 
lbl2 = Label(aken, text="x**2+", font="Arial 16")
ent2 = Entry(aken, font="Arial 20", fg=fg, bg=bg, width=4) 
lbl3 = Label(aken, text="x+", font="Arial 16")
ent3 = Entry(aken, font="Arial 20", fg=fg, bg=bg, width=4) 
lbl4 = Label(aken, text="=0", font="Arial 16")
lbl5 = Label(aken, text="Решение", font="Arial 16", bg=bg)
btn1 = Button(aken, text="Решать", font="Arial 12", fg=fg, bg=bg, width=14, height=3, relief=RAISED, command=lambda: solve())
btn2 = Button(aken, text="graafik", font="Arial 12", bg=bg, width=14, height=3, relief=RAISED, command=lambda: graafik(graf, D))
btn4 = Button(aken, text="Graafikud", font="Arial 12", fg=fg, bg=bg, width=14, height=3, command=extend)

lbl5.pack(side=BOTTOM)
lbl.pack()
btn4.pack(side=BOTTOM)
ent1.pack(side=LEFT)
lbl2.pack(side=LEFT)
ent2.pack(side=LEFT)
lbl3.pack(side=LEFT)
ent3.pack(side=LEFT)
lbl4.pack(side=LEFT)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)

aken.mainloop()
