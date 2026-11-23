import tkinter as tk
import math

### modelo atual comporta comportamento simples para um espelho esferico concavo/convexo e seus equivalentes em lentes simplificadas;
### sem traço de raios; calculo diretamente nas formulas de foco / ampliaçao

# cria canvas
largura=1020
altura=600
ambiente = tk.Tk()
canvas = tk.Canvas(ambiente, width=largura, height=altura)
canvas.pack()

# cria linhas do ambiente
lente = canvas.create_line(largura/2, 0, largura/2, altura, width=2)
divisor = canvas.create_line(0, altura/2, largura, altura/2, dash=40, width=2, fill="#808080")

# delimita pontos no canvas
canvas.create_oval(largura/6 - 2, altura/2 - 2, largura/6 + 2, altura/2 + 2, fill='black') #centro esquerdo 
canvas.create_oval(largura*2/6 - 2, altura/2 - 2, largura*2/6 + 2, altura/2 + 2, fill='black') #foco esquerdo
canvas.create_oval(largura*4/6 - 2, altura/2 - 2, largura*4/6 + 2, altura/2 + 2, fill='black') #foco direito
canvas.create_oval(largura*5/6 - 2, altura/2 - 2, largura*5/6 + 2, altura/2 + 2, fill='black') #centro direito

# pega valores
p = float(input('p'))
r = float(input('r1'))
y_obj = float(input('y'))

if p <= 0:
    raise ValueError('Objeto deve ter posição positiva.')
if r == 0:
    raise ValueError('Raio de curvatura deve ser diferente de zero.')

f = r/2

if f > 0:
    print('concavo')
    if p == f:
        raise ValueError('Objeto no foco em espelho côncavo: imagem formada é imprópria.')
elif f == 0:
    print('lente plana')
else:
    print('convexo')

q = (p*f)/(p-f)
y_img = (y_obj*q*-1)/(p)


# print p/ verificaçao
print(f'p: {p}, r: {r}, f: {f}, q: {q}, y: {y_obj}, y´: {y_img}')

#adapta proporçoes de foco e altura informados às proporções do canvas

foco_esquerdo_canvas = largura/6

f_p = f/p # proporçao foco/posiçao do objeto
f_q = f/q # proporção foco/posição da imagem
f_y = f/y_obj # proporção foco/tamanho do objeto
f_yi = f/y_img # proporção foco/tamanho da imagem

#converte proporções para tamanhos reais no canvas

if f > 0:
    foco = largura/6
elif f < 0:
    foco = -1*(largura/6)

P = foco/(f_p)
Q = foco/(f_q)
altura_obj = foco/(f_y)
altura_img = foco/(f_yi)

print(f'p: {P}, f: {foco}, q: {Q}, y: {altura_obj}, y´: {altura_img}')

limite = largura/2

if abs(Q) >= limite:
    print('Imagem localizada além dos limites do programa.')
    print(f'(Valor absoluto de q: {abs(Q)} / Limite de renderização: {limite}')

#traça linhas do objeto e imagem

ox = largura/2 # x do vertice da lente
oy = altura/2 # y do vertice da lente

objeto = canvas.create_line(ox - P, oy, ox - P, oy - altura_obj, width=2, fill='#0000ff')
imagem = canvas.create_line(ox - Q, oy, ox - Q, oy - altura_img, width=2, fill='#00aaff')





