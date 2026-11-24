import tkinter as tk
from tkinter import messagebox
import math

## incidentes a notar:

        ## reflexão interna total implementada a custo de ângulos de abertura maiores do que 60º.

# erros menores:

        # prolongação do eixo normal à superfície do lado direito às vezes aparenta não ser, de fato, normal. isso foi
        # de certo modo "consertado", ou seja, estava mais aparente antes, mas restam dúvidas.


# cria ambiente das caixas de texto
texto = tk.Tk()
caixatexto = tk.Canvas(texto, width=100, height=40)
caixatexto.pack()

texto1 = tk.Label(text='Ângulo de abertura (graus):')
abr = tk.Entry()
texto1.pack()
abr.pack()

texto2 = tk.Label(text='Ângulo de incidência (graus):')
theta = tk.Entry()
texto2.pack()
theta.pack()

texto3 = tk.Label(text='Índice de refração 1:')
ene1 = tk.Entry()
texto3.pack()
ene1.pack()

texto4 = tk.Label(text='Índice de refração 2:')
ene2 = tk.Entry()
texto4.pack()
ene2.pack()


def programa_inteiro_lol():

    # pega valores
    abertura = float(abr.get())
    theta1 = float(theta.get())
    n1 = float(ene1.get())
    n2 = float(ene2.get())

    # cria canvas
    height = 500
    width = 1000

    ambiente = tk.Tk()
    canvas = tk.Canvas(ambiente, width=width, height=height)
    canvas.pack()

    # cria linhas do ambiente
    normal = canvas.create_line(500, 0, 500, 500, dash=40, width=2, fill="#808080")
    divisor = canvas.create_line(0, 250, 1000, 250, width=2)
     
    # define prisma
    
    if abertura > 180 or abertura <= 0:
        messagebox.showerror('Erro', 'ValueError: Ângulo de abertura deve ser menor que 60° e maior que 0°.', parent=canvas)
        raise ValueError('Ângulo de abertura deve ser menor que 60° e maior que 0°.')
        

    beta = (180-abertura)/2 # angulos agudos da base
    thetaN = 90 - beta # angulo para traço do raio incidente // angulo entre horizontal e reta normal


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

    ### normal direita desenhada após traço do raio interno para coincidir com ponto de incidencia ###

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


    if theta2 < thetaN2: # raio de dentro abaixo da horizontal

        basepequena = xnd-xne 

        angcim = thetaN - theta2
        angcimrad = (angcim*math.pi)/180

        gmm = beta - angcim
        gmmrad = (gmm*math.pi)/180

        lado = (math.sin(angcimrad)/math.sin(gmmrad))*(basepequena) # lei dos senos para calcular desvio lateral da incidencia do raio no lado esquerdo

        xi = lado*(math.cos(betarad)) # projeçao do lado em x
        yi = lado*(math.sin(betarad)) # projeçao do lado em y

        canvas.create_line(xne, yn, xne+basepequena+xi, yn+yi, width=2, fill='#0000ff')

        ## NORMAL DIREITA PARTINDO DO PONTO DE INCIDENCIA NO LADO DIREITO

        xne = X1 - (B/2)     #COORDS DE PARTIDA
        XD = xne+basepequena+xi
        YD = yn+yi

        y_inc = (math.tan(math.pi*thetaN/180))*(width-XD)
        x_inc = ((height/2) - yi)/(math.tan(math.pi*thetaN/180))

        canvas.create_line(XD, YD, width, YD - y_inc, dash=40, fill='grey') # NORMAL DIREITA
        canvas.create_line(XD, YD, XD - x_inc, height, dash=40, fill='#d6d6d6') # NORMAL DIREITA: PROLONGADA

        # RAIO PRA FORA:

        theta3 = angcim + thetaN
        theta3rad = (theta3*math.pi)/180

        if math.sin(theta3rad) > n1/n2 or math.sin(theta3rad) == n1/n2: # REFLEXAO INTERNA TOTAL

            A = 90 - (thetaN + theta3)
            Arad = (A*math.pi)/180
            xA = yi*math.tan(Arad)
            
            canvas.create_line(XD, YD, XD-xA, height*(3/4), width=2, fill='#0000ff')

            # raio transmitido:
            theta4 = math.asin(math.sin(Arad)*(n2/n1))
            theta4rad = (theta4*math.pi)/180

            xB = (height/4)*math.tan(theta4rad)

            canvas.create_line(XD-xA, height*(3/4), XD-xA-xB, height, width=2, fill='#0000ff')

            canvas.create_text((1, height-37), text=f'Ângulo incidindo para fora: {A:.3f}º', font=('Arial', 10), anchor='w')
            canvas.create_text((1, height-21), text=f'Ângulo transmitido: {theta4:.3f}º', font=('Arial', 10), anchor='w')

        else: 

            theta4rad = math.asin((n2/n1)*math.sin(theta3rad))
            theta4 = (theta4rad*180)/math.pi

            canvas.create_text((1, height-37), text=f'Ângulo transmitido: {theta4:.3f}º', font=('Arial', 10), anchor='w')

            if theta4 < thetaN:

                G = thetaN - theta4
                Grad = (G*math.pi)/180

                xf = width - XD
                yf = math.tan(Grad)*xf

                xf = width - XD
                yf = math.tan(theta4rad)*xf
                
                canvas.create_line(XD, YD, width, yn-yf, width=2, fill='#0000ff')

            elif theta4 == thetaN:
            
                xf = width - XD
                yf = math.tan(theta4rad)*xf
                
                canvas.create_line(XD, YD, width, YD, width=2, fill='#0000ff')
            
            elif theta4 < 90:

                P = theta4 - thetaN
                Prad = (P*math.pi)/180

                xf = width - XD
                yf = math.tan(Prad)*xf

                canvas.create_line(XD, YD, width, yn+yf, width=2, fill='#0000ff')


    elif theta2 == thetaN2: # raio de dentro na horizontal
        canvas.create_line(xne, yn, width, yn, width=2, fill='#0000ff')

        # RAIO PRA FORA:
        
        theta3 = thetaN
        theta3rad = (theta3*math.pi)/180

        if math.sin(theta3rad) > n1/n2 or math.sin(theta3rad) == n1/n2: # REFLEXAO INTERNA TOTAL

            A = 90 - (thetaN + theta3)
            Arad = (A*math.pi)/180
            xA = yi*math.tan(Arad)
            
            canvas.create_line(XD, YD, XD-xA, height*(3/4), width=2, fill='#0000ff')

            # raio transmitido:
            theta4 = math.asin(math.sin(Arad)*(n2/n1))
            theta4rad = (theta4*math.pi)/180

            xB = (height/4)*math.tan(theta4rad)

            canvas.create_line(XD-xA, height*(3/4), XD-xA-xB, height, width=2, fill='#0000ff')

            canvas.create_text((1, height-37), text=f'Ângulo incidindo para fora: {A:.3f}º', font=('Arial', 10), anchor='w')
            canvas.create_text((1, height-21), text=f'Ângulo transmitido: {theta4:.3f}º', font=('Arial', 10), anchor='w')

        else:
        
            theta4rad = math.asin((n2/n1)*math.sin(theta3rad))
            theta4 = (theta4rad*180)/math.pi

            canvas.create_text((1, height-37), text=f'Ângulo transmitido: {theta4:.3f}º', font=('Arial', 10), anchor='w')

    elif theta2 < 90: # raio de dentro acima da horizontal

        basepequena = xnd-xne

        angcim = theta2 - thetaN
        angcimrad = (angcim*math.pi)/180

        gmm = beta - angcim
        gmmrad = (gmm*math.pi)/180

        lado = (math.sin(angcimrad)/math.sin(gmmrad))*(basepequena) # lei dos senos para calcular desvio lateral da incidencia do raio no lado esquerdo

        xi = lado*(math.cos(betarad)) # projeçao do lado em x
        yi = lado*(math.sin(betarad)) # projeçao do lado em y

        canvas.create_line(xne, yn, xne+basepequena-xi, yn-yi, width=2, fill='#0000ff')

        ## NORMAL DIREITA PARTINDO DO PONTO DE INCIDENCIA NO LADO DIREITO

        xne = X1 - (B/2)     #COORDS DE PARTIDA
        XD = xne+basepequena-xi
        YD = yn-yi

        y_inc = (math.tan(math.pi*thetaN/180))*(width-XD)
        x_inc = ((height/2) - yi)/(math.tan(math.pi*thetaN/180))

        canvas.create_line(XD, YD, width, YD - y_inc, dash=40, fill='grey') # NORMAL DIREITA
        canvas.create_line(XD, YD, XD - x_inc, height, dash=40, fill='#d6d6d6') # NORMAL DIREITA: PROLONGADA

        ################### RAIO INDO P/ FORA

        theta3 = 90 - angcim - beta
        theta3rad = (theta3*math.pi)/180

        if math.sin(theta3rad) > n1/n2 or math.sin(theta3rad) == n1/n2: # REFLEXÃO INTERNA TOTAL

            A = 90 - (thetaN + theta3)
            Arad = (A*math.pi)/180
            xA = yi*math.tan(Arad)
            
            canvas.create_line(XD, YD, XD-xA, height*(3/4), width=2, fill='#0000ff')

            
            # raio transmitido:
            theta4 = math.asin(math.sin(Arad)*(n2/n1))
            theta4rad = (theta4*math.pi)/180

            xB = (height/4)*math.tan(theta4rad)

            canvas.create_line(XD-xA, height*(3/4), XD-xA-xB, height, width=2, fill='#0000ff')

            canvas.create_text((1, height-37), text=f'Ângulo incidindo para fora: {A:.3f}º', font=('Arial', 10), anchor='w')
            canvas.create_text((1, height-21), text=f'Ângulo transmitido: {theta4:.3f}º', font=('Arial', 10), anchor='w')

        else:

            theta4rad = math.asin((n2/n1)*math.sin(theta3rad))
            theta4 = (theta4rad*180)/math.pi

            canvas.create_text((1, height-37), text=f'Ângulo transmitido: {theta4:.3f}º', font=('Arial', 10), anchor='w')

            if theta4 < thetaN:

                G = thetaN - theta4
                Grad = (G*math.pi)/180

                xf = width - XD
                yf = math.tan(Grad)*xf
                
                canvas.create_line(XD, YD, width, yn-yf, width=2, fill='#0000ff')

            elif theta4 == thetaN:
            
                xf = width - XD
                yf = math.tan(theta4rad)*xf
                
                canvas.create_line(XD, YD, width, YD, width=2, fill='#0000ff')

            elif theta4 > thetaN:

                P = theta4 - thetaN
                Prad = (P*math.pi)/180

                xf = width - XD
                yf = math.tan(Prad)*xf

                canvas.create_line(XD, YD, width, yn+yf, width=2, fill='#0000ff')

    canvas.create_text((1, height-200), text=f'Coef. refração externo: {n1}', font=('Arial', 10), anchor='w')
    canvas.create_text((1, height-184), text=f'Coef. refração interno: {n2}', font=('Arial', 10), anchor='w')
        
    canvas.create_text((1, height-80), text=f'Ângulo de incidência: {theta1}º', font=('Arial', 10), anchor='w')
    canvas.create_text((1, height-65), text=f'Ângulo refratado: {theta2:.3f}º', font=('Arial', 10), anchor='w')
    canvas.create_text((1, height-52), text=f'Ângulo incidente interno: {theta3:.3f}º', font=('Arial', 10), anchor='w')

    
# bota o botao pra funcionar
botao = tk.Button(text='fazer', command=programa_inteiro_lol)
botao.pack()
        

