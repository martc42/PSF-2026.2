import tkinter as tk
import math

# cria canvas
ambiente = tk.Tk()
canvas = tk.Canvas(ambiente, width=1000, height=500)
canvas.pack()

# cria linhas do ambiente
normal = canvas.create_line(500, 0, 500, 500, dash=40, width=2, fill="#808080")
divisor = canvas.create_line(0, 250, 1000, 250, width=2)

# inserçao de variaveis
n1 = float(input("n1:"))
n2 = float(input("n2:"))
th1 = float(input("θ1 em graus:"))
th1 = (th1*math.pi)/180

if th1 < 0 or th1 >= math.pi/2:
    raise ValueError('Ângulo de incidência deve ser maior ou igual a zero e menor que 90º.')


#faz a magica acontecer:
ox = 500
oy = 250

# condicional p/ reflexao total:
if n1 <= n2:
    th2 = math.asin((n1/n2)*math.sin(th1))
    
    ix = abs(oy*math.tan(th1))
    iy = 0

    rx = abs(oy*math.tan(th2))
    ry = 2*oy

    incidente = canvas.create_line(ox - ix, iy, ox, oy, width=2, fill='#5C77FF')
    refratado = canvas.create_line(ox, oy, rx + ox, ry, width=2, fill='#FF78B3')

else:
    ix = abs(oy*math.tan(th1))
    iy = 0

    incidente = canvas.create_line(ox - ix, iy, ox, oy, width=2, fill='#5C77FF')
    refratado = canvas.create_line(ox + ix, iy, ox, oy, width=2, fill='#FF78B3')

    










