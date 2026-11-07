import tkinter as tk
import math

# cria ambiente das caixas de texto
texto = tk.Tk()
caixatexto = tk.Canvas(texto, width=100, height=40)
caixatexto.pack()

texto1 = tk.Label(text='Índice de refração 1:')
ene1 = tk.Entry()
texto1.pack()
ene1.pack()

texto2 = tk.Label(text='Índice de refração 2:')
ene2 = tk.Entry()
texto2.pack()
ene2.pack()

texto3 = tk.Label(text='Ângulo de incidência (graus):')
theta = tk.Entry()
texto3.pack()
theta.pack()

def fazer_as_linha():

    # pega valores
    n1 = float(ene1.get())
    n2 = float(ene2.get())
    th1 = float(theta.get())
    th1 = (th1*math.pi)/180
        
    # cria canvas 
    ambiente = tk.Tk()
    canvas = tk.Canvas(ambiente, width=1000, height=500)
    canvas.pack()

    # cria linhas do ambiente
    normal = canvas.create_line(500, 0, 500, 500, dash=40, width=2, fill="#808080")
    divisor = canvas.create_line(0, 250, 1000, 250, width=2)

    # verifica se o angulo é coerente
    if th1 < 0 or th1 >= math.pi/2:
        raise ValueError('Ângulo de incidência deve ser maior ou igual a zero e menor que 90º.')

    # condicional p/ reflexao total:
    
    ox = 500 # coords do ponto de incidencia
    oy = 250
    
    if n1 <= n2:
        th2 = math.asin((n1/n2)*math.sin(th1))
        
        ix = abs(oy*math.tan(th1))
        iy = 0

        rx = abs(oy*math.tan(th2))
        ry = 2*oy

        incidente = canvas.create_line(ox - ix, iy, ox, oy, width=2, fill='#0000ff')
        refratado = canvas.create_line(ox, oy, rx + ox, ry, width=2, fill='#FF78B3')

    else:
        ix = abs(oy*math.tan(th1))
        iy = 0

        incidente = canvas.create_line(ox - ix, iy, ox, oy, width=2, fill='#0000ff')
        refratado = canvas.create_line(ox + ix, iy, ox, oy, width=2, fill='#FF78B3')

# bota o botao pra funcionar
botao = tk.Button(text='vai la!', command=fazer_as_linha)
botao.pack()










