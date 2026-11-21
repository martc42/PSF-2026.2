import tkinter as tk
import math

# cria canvas
height = 500
width = 1000

ambiente = tk.Tk()
canvas = tk.Canvas(ambiente, width=width, height=height)
canvas.pack()

# cria linhas do ambiente
normal = canvas.create_line(500, 0, 500, 500, dash=40, width=2, fill="#808080")
divisor = canvas.create_line(0, 250, 1000, 250, width=2)
 
# define prisma // pega dados
abertura = float(input('abertura em °: '))
theta1 = float(input('angulo de incidencia em °: '))
n1 = float(input('n1: '))
n2 = float(input('n2: '))

if abertura >= 180 or abertura <= 0:
    raise ValueError('Ângulo de abertura deve ser menor que 180° e maior que 0°.')

beta = (180-abertura)/2 # angulos agudos da base
thetaN = 90 - beta # angulo para traço do raio incidente


abertura = (abertura*math.pi)/180 #conversao p/ rad
betarad = (beta*math.pi)/180
theta1rad = (theta1*math.pi)/180

B = math.tan(abertura/2)*height/2 # metade da base do prisma para def de coord
#width = 2*B

X1 = width/2
Y1 = height/4
X2 = width/2
Y2 = height*3/4

prisma = canvas.create_polygon(X1, Y1, X2 - B, Y2, X2 + B, Y2, outline='black', fill='white')

# desenha normais

xne = X1 - (B/2)     #COORDS DE PARTIDA: MEIO DO LADO
xnd = X1 + (B/2)
yn = height/2

y_inc = (math.tan(math.pi*thetaN/180))*(xne)
x_inc = (height/2)/(math.tan(math.pi*thetaN/180))
    
canvas.create_line(xne, yn, 0, yn - y_inc, dash=40, fill='grey') # NORMAL ESQUERDA
canvas.create_line(xne, yn, xne + x_inc, height, dash=40, fill='#d6d6d6') # NORMAL ESQUERDA: PROLONGADA
canvas.create_line(xnd, yn, width, yn - y_inc, dash=40, fill='grey') # NORMAL DIREITA
canvas.create_line(xnd, yn, xnd - x_inc, height, dash=40, fill='#d6d6d6') # NORMAL DIREITA: PROLONGADA

### RAIO INCIDENTE ###

if theta1 > thetaN: # raio abaixo da linha horizontal

    G = theta1 - thetaN
    x_inc1 = (height/2)/(math.tan(math.pi*G/180))

    xne = X1 - (B/2)     #COORDS DE PARTIDA: MEIO DO LADO
    yn = height/2

    canvas.create_line(xne, yn, xne - x_inc1, height, width=2, fill='#0000ff')
    
    
elif theta1 >= 0: # raio acima da/na linha horizontal

    G = thetaN - theta1

    y_inc1 = (math.tan((math.pi*G)/180))*(xne)

    xne = X1 - (B/2)     #COORDS DE PARTIDA: MEIO DO LADO
    yn = height/2
    
    if G == 0: # raio horizontal
        canvas.create_line(xne, yn, 0, yn, width=2, fill='#0000ff')
    else:      # raio acima da linha horizontal
        canvas.create_line(xne, yn, 0, yn - y_inc1, width=2, fill='#0000ff')

### RAIO REFRATADO ###

theta2rad = math.asin((n1/n2)*math.sin(theta1rad)) # lei de snell
theta2 = (theta2rad*180)/math.pi

thetaN2 = 90 - beta

xne = X1 - (B/2)     #COORDS DE PARTIDA: MEIO DO LADO ESQUERDO
yn = height/2


if theta2 < thetaN2: # raio abaixo da horizontal

    basepequena = xnd-xne

    angcim = thetaN - theta2
    angcimrad = (angcim*math.pi)/180

    gmm = beta - angcim
    gmmrad = (gmm*math.pi)/180

    lado = (math.sin(angcimrad)/math.sin(gmmrad))*(basepequena)

    xi = lado*(math.cos(betarad))
    yi = lado*(math.sin(betarad))

    canvas.create_line(xne, yn, xne+basepequena+xi, yn+yi, width=2, fill='#0000ff')

elif theta2 == thetaN2: # raio na horizontal
    canvas.create_line(xne, yn, width, yn, width=2, fill='#0000ff')

elif theta2 < 90: # raio acima da horizontal

    basepequena = xnd-xne

    angcim = theta2 - thetaN
    angcimrad = (angcim*math.pi)/180

    gmm = beta - angcim
    gmmrad = (gmm*math.pi)/180

    lado = (math.sin(angcimrad)/math.sin(gmmrad))*(basepequena)

    xi = lado*(math.cos(betarad))
    yi = lado*(math.sin(betarad))

    canvas.create_line(xne, yn, xne+basepequena-xi, yn-yi, width=2, fill='#0000ff')
    

        

