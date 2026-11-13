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
    canvas = tk.Canvas(ambiente, width=1000, height=600, bg='#ffffff')
    canvas.pack()

    # cria linhas do ambiente
    normal = canvas.create_line(500, 0, 500, 600, dash=40, width=2, fill="#808080")
    divisor1 = canvas.create_line(0, 200, 1000, 200, width=2)
    divisor2 = canvas.create_line(0, 400, 1000, 400, width=2)

    # verifica se o angulo é coerente
    if th1 < 0 or th1 >= math.pi/2:
        raise ValueError('Ângulo de incidência deve ser maior ou igual a zero e menor que 90º.')

    # condicional p/ reflexao total:
    
    ox = 500 # coords do ponto de incidencia
    oy = 200
    
    if n1 <= n2: # caso 1 - "ar pra vidro"
        th2 = math.asin((n1/n2)*math.sin(th1)) # lei de snell
        th3 = math.asin((n2/n1)*math.sin(th2))
        
        ix = abs(oy*math.tan(th1))
        iy = 0

        rx = abs(oy*math.tan(th2))
        ry = 2*oy

        tx = abs(oy*math.tan(th3))
        ty = 600

        Ro = ((n1-n2)/(n1+n2))**2 # quantia refletida por aproximação de schlick 
        R = Ro + (1-Ro)*((1 - math.cos(th1))**5)
        T = 1 - R

        print(f'Fração refletida: {R*100:.2f}%')
        print(f'Fração transmitida/refratada): {T*100:.2f}%')

        # TRANSFORMAÇAO DOS VALORES DE R E T EM TRANSPARENCIA: RGB pra hexadecimal
        
        CRefletido = int(255*T) # devido à adição das cores, números maiores criariam cores mais escuras na conversão, portanto troquei os coeficientes de lugar pra compensar
        CRefratado = int(255*R)

        def converter_cores(parte): # função condicional pra valores hex individuais (1, a, etc) não estragarem a cor final
            if parte.isdigit() == True:
                if int(parte) < 10:
                    hexe = '#' + '0' + parte + '0' + parte + 'ff' # função funciona exclusivamente para variantes da cor azul escura
                else:      
                    hexe = '#' + parte + parte + 'ff'
            else:
                if len(parte) == 1:
                    hexe = '#' + '0' + parte + '0' + parte + 'ff'
                else:
                    hexe = '#' + parte + parte + 'ff'
            return hexe

        parteRefratada = '{0:x}'.format(CRefratado) # transforma coeficiente em pedaços de hex para compor a cor final
        parteRefletida = '{0:x}'.format(CRefletido)
        hexrefratado = converter_cores(parteRefratada) 
        hexrefletido = converter_cores(parteRefletida)
        
        cor_incidente = '#0000ff'
        cor_refletido = hexrefletido
        cor_refratado = hexrefratado
        cor_transmitido = cor_refratado
        
        incidente = canvas.create_line(ox - ix, iy, ox, oy, width=2, fill=cor_incidente)
        refratado = canvas.create_line(ox, oy, rx + ox, ry, width=2, fill=cor_refratado)
        refletido = canvas.create_line(ox + ix, iy, ox, oy, width=2, fill=cor_refletido)
        transmitido = canvas.create_line(rx + ox, ry, rx + ox + tx, ty, width=2, fill=cor_transmitido)

        print(f'refletido: {cor_refletido}, refratado: {cor_refratado}, incidente: {cor_incidente}')

    else: # caso 2 - "vidro pro ar" - CONDICIONAL INCOMPLETA!
        ix = abs(oy*math.tan(th1))
        iy = 0

        incidente = canvas.create_line(ox - ix, iy, ox, oy, width=2, fill='#0000ff')
        refratado = canvas.create_line(ox + ix, iy, ox, oy, width=2, fill='#FF78B3')

# bota o botao pra funcionar
botao = tk.Button(text='vai la', command=fazer_as_linha)
botao.pack()










