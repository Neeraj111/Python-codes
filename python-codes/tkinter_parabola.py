import math
try:
    import Tkinter
except ImportError:
    import tkinter


def drawaxis(canvas_param):
    canvas_param.update()
    x_origin = canvas_param.winfo_width()//2
    y_origin = canvas_param.winfo_height()//2
    canvas_param.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas_param.create_line(x_origin, 0,-x_origin,0, fill='green')
    canvas_param.create_line(0,y_origin, 0,-y_origin, fill='green')


def plot(canvas_param,x,y):
    canvas_param.create_line(x, y, x+1, y+1, fill="red")


def parabola(canvas_param, size):
    for x in range(-size, size):
        y = x*x/size
        plot(canvas_param, x, y)
        plot(canvas_param, -x, y)



def circle(canvas_param, radius, g, h, colour='red'):
    canvas_param.create_oval(g + radius, h + radius, g - radius, h - radius, outline = colour)
    # for x in range(g, g + radius):
    #     print(x)
    #     y = h + (math.sqrt(radius **2 -((x-g) ** 2 )))
    #     plot(canvas_param, x, y)
    #     plot(canvas_param, x, 2 * h -y)
    #     plot(canvas_param, 2 * g - x, y)
    #     plot(canvas_param, 2 * g - x, 2 * h - y)


mainwindow = tkinter.Tk()
mainwindow.title('parabola')
mainwindow.geometry('640x480')
canvas = tkinter.Canvas(mainwindow, width= 640, height= 480)
canvas.grid(row=0, column=0)
drawaxis(canvas)

parabola(canvas,100)
circle(canvas, 100, 100, 100)
circle(canvas, 100, -100, -100,'yellow')
circle(canvas, 100, -100, 100,'pink')
circle(canvas, 100, 100, -100,'blue')


mainwindow.mainloop()

