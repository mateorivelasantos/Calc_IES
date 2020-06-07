#!/usr/bin/env python
#-*- coding: utf-8 -*-

from tkinter import *
import math
import sys
from tkinter import PhotoImage
from PIL import Image,ImageTk


ventana = Tk()
ventana.title("BACH")
ventana.geometry("400x600")
ventana.configure(background="white")
ventana.wait_visibility(ventana)
ventana.wm_attributes("-alpha", 0.95)
ventana.iconbitmap("Calcico.ico")



#Definimos dimensiones de todos los botones y variables
alto = 2
ANCHO =7
var = StringVar()
i = ""
base = IntVar()
base0 = IntVar()
base00 = IntVar()
estado = "DEC"
p = "desactivado"
continuar = "no"
x = 0
c =""
u = ""
e = ""
sol1 = 1
b = "a"
ANS = ""
Calc = "menu"

def ans():
	global ANS
	global i
	i = i + ANS
	var.set(ANS)
	

def borrar():
	global i
	caja.delete(1)
	i = str(caja.get())

	global u
	caja3.delete(1)
	u = str(caja3.get())

	global e
	caja4.delete(1)
	e = str(caja4.get())


def cerrar():
	ventana.destroy()


def imprimir(valor):
	global p,i
	global ANS

	if p == "desactivado":
		global i
		
		i = i + str(valor)
		var.set(i)
		

	if p == "activado":
		global c

		c = c + str(valor)
		base.set(c)

	if p == "activado1":
		global u

		u = u + str(valor)
		base0.set(u)

	if p == "activado2":
		global e

		e = e + str(valor)
		base00.set(e)

		

def eliminar():
	global i,c,e
	global p
	if p == "desactivado":
		i = ("")
		var.set("")
	elif p == "activado":
		c = ("")
		base.set("")
	elif p =="activado2":
		c=""
		base00.set("")
	else:
		u = ("")
		base0.set("")
		
		

def ejecutar():

	global p
	global c,u,e
	global i
	global N2,N1
	global b,base1a,base11
	global ANS

	if b == "ac":
			base1a.place_forget()
			base11.place_forget()


	if p == "desactivado":
		try:
			operacion=str(eval(i))
			ANS = operacion
		except:
			eliminar()
			operacion=("ERROR")
		var.set(operacion)

	elif p == "activado":
		try:
			
			if c != "0":

				N1 = c
				N2 = float(eval(i))

			sol = math.log(N2,int(N1))
			var.set(sol)
			i = str(var.get())
			caja2.place_forget()
			base1.place_forget()
			p = "desactivado"
			ANS = str(sol)
		
		except:

			eliminar()
			operacion=("ERROR")
			var.set(operacion)
		base.set("")

	elif p == "activado2":

		try:
			
			if e != "0":

				N1 = e
				N2 = float(eval(i))

			sol = N2**(1/int(N1))

			var.set(sol)
			i = str(var.get())
			caja4.place_forget()
			base3.place_forget()
			base00.set(0)
			e = ""
			p = "desactivado"
			ANS = str(sol)
		

		except:

			eliminar()
			operacion=("ERROR")
			var.set(operacion)
			base0.set("")


	else:

		try:
			
			if u != "0":

				N1 = u
				N2 = float(eval(i))

			sol = N2/int(u)
			resto = N2 % int(u)
				
			mn2 = math.floor(sol)

			base1a = Label(ventana,font= "Times 10",text="Resto > " + str(resto))
			base1a.place(x = 670 ,y = 15)

			base11 =Label(ventana,font= "Times 10",text="Dividendo > " + str(mn2))
			base11.place(x = 660 ,y = 30)
			b = "ac"

			var.set(sol)
			i = str(var.get())
			caja3.place_forget()
			base2.place_forget()
			base0.set(0)
			u = ""
			ANS = str(sol)


			p = "desactivado"
		

		except:

			eliminar()
			operacion=("ERROR")
			var.set(operacion)
			base0.set("")
		p = "desactivado"
		

	

def aproximar():

	global i
	global base

	try:
		my = math.ceil(float(eval(i)))
		mn = math.floor(float(eval(i)))

		numero_medio = (2*my + 2*mn)/4

		if float(eval(i)) >= numero_medio:
			var.set(str(my))
			i =str(my)
		else:
			var.set(str(mn))
			i = str(i)

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)
		base.set("")

def logbase():

	global c
	global i
	global p
	global N2,N1
	global base1,caja2

	p = "activado"


	caja2 = Entry(ventana,font=("arial",10,"bold"),width = 4,insertwidth="3",textvariable = base ,bg="powderblue",bd=10,justify="right")
	caja2.place(x =670 ,y = 60)


	base1 =Label(ventana,font= "Times 10",text="Base log")
	base1.place(x = 670 ,y = 30)

def log():
	global i
	global base
	try:
		N2 = float(eval(i))
		sol = math.log(N2,10)
		eliminar()
		var.set(sol)
		i = str(sol)
	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)

		

def ln():
	global i
	global base

	try:
		N2 = float(eval(i))
		sol = math.log(N2,2.7182)
		eliminar()
		var.set(sol)
		i = str(sol)
	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)
		

def factorial():


	global i
	global base

	try:
		my = math.ceil(float(eval(i)))
		mn = math.floor(float(eval(i)))

		numero_medio = (2*my + 2*mn)/4

		if float(eval(i)) >= numero_medio:
			for x in (1,my):
				sol = 1

				for y in range(1, x + 1):
					sol *= y
		else:
			for x in (1,my):
				sol = 1
				for y in range(1, x + 1):
					sol *= y

		var.set(sol)
		i = str(sol)

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)
		


def sin():
	global i
	global base

	try:
		N2 = float(eval(i))
		sol= math.sin(N2)
		eliminar()
		var.set(sol)
		i = str(sol)

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)



def cos():
	global i
	global base

	try:
		N2 = float(eval(i))
		sol= math.cos(N2)
		eliminar()
		var.set(sol)
		i = str(sol)

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)


def tan():
	global i
	global base

	try:
		N2 = float(eval(i))
		sol= math.tan(N2)
		eliminar()
		var.set(sol)
		i = str(sol)

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)

def atan():
	global i
	global base

	try:
		N2 = float(eval(i))
		sol= math.atan(N2)
		eliminar()
		var.set(sol)
		i = str(sol)

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)

def asin():
	global i
	global base

	try:
		N2 = float(eval(i))
		sol= math.asin(N2)
		eliminar()
		var.set(sol)
		i = str(sol)

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)

def acos():
	global i
	global base

	try:
		N2 = float(eval(i))
		sol= math.acos(N2)
		eliminar()
		var.set(sol)
		i = str(sol)

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)


def resto():

	global p
	global i
	global base,base0
	global base2,caja3

	p = "activado1"

	caja3 = Entry(ventana,font=("arial",10,"bold"),width = 4,insertwidth="3",textvariable = base0 ,bg="powderblue",bd=10,justify="right")
	caja3.place(x =670 ,y = 60)


	base2 =Label(ventana,font= "Times 10",text="Divisor")
	base2.place(x = 670 ,y = 30)


def raiz2():

	global p
	global i
	global base,base0
	global base3,caja4

	p = "activado2"

	caja4 = Entry(ventana,font=("arial",10,"bold"),width = 4,insertwidth="3",textvariable = base00 ,bg="powderblue",bd=10,justify="right")
	caja4.place(x =670 ,y = 60)


	base3 =Label(ventana,font= "Times 10",text="exponente")
	base3.place(x = 670 ,y = 30)



def binarizar(decimal):
	global bina
	binario = ''
	while decimal // 2 != 0:

		binario = str(decimal % 2) + binario
		decimal = decimal // 2
	bina = (str(decimal) + binario)


def dec():

	aproximar()
	global i
	global base
	global estado

	if estado=="BIN":

		try:
			N2 = int(eval(i))
			sol= int(str(N2), 2)
			eliminar()
			var.set(sol)
			i = str(sol)

			estado = "DEC"

		except:
			eliminar()
			operacion=("ERROR")
			var.set(operacion)

		
	if estado=="HEX":

		try:
			N2 = int(eval(i))
			sol= int(str(N2), 16)
			eliminar()
			var.set(sol)
			i = str(sol)

			estado = "DEC"

		except:
			eliminar()
			operacion=("ERROR")
			var.set(operacion)

	if estado=="OCT":

		try:
			N2 = int(eval(i))
			sol= int(str(N2), 8)
			eliminar()
			var.set(sol)
			i = str(sol)

			estado = "DEC"

		except:
			eliminar()
			operacion=("ERROR")
			var.set(operacion)


def bin():

	aproximar()
	global i
	global base
	global estado

	dec()

	try:
		N2 = int(eval(i))
		binarizar(N2)
		sol = int(bina)
		eliminar()
		var.set(sol)
		i = str(sol)

		estado = "BIN"

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)

def hex():

	aproximar()
	global i
	global base
	global estado

	dec()

	try:
		N2 = int(eval(i))
		sol = format(N2,"x")
		eliminar()
		var.set(sol)
		i = str(sol)

		estado = "HEX"

	except:
		eliminar()
		operacion=("ERROR")
		var.set(operacion)

def oct():

	aproximar()
	global i
	global base
	global estado

	dec()


	N2 = int(eval(i))
	sol = format(N2,"o")
	eliminar()
	var.set(sol)
	i = str(sol)

	estado = "OCT"

def menu():
	titulo_menu = Label(ventana,font= "Times 18",text="Calculadora IES O Ribeiro",bg = "dim gray",fg = "#FFF")
	titulo_menu.place(x = 65 ,y = 10)

	boton_ESO = Button(ventana,text="Calculadora ESO",height=7,width=15,font=(30),command = fmenu2)
	boton_ESO.place(x = 20,y = 300)

	boton_bach = Button(ventana,text="Calculadora BACH",height=7,width=15,font=(30),command = fmenu)
	boton_bach.place(x = 210,y = 300)

	panel = Label(ventana, image = img)
	panel.place(x = 50, y = 70)

def fCalc_Bach():
	ventana.geometry("400x600")
	ventana.configure(background="white")
	ventana.wm_attributes("-alpha", 0.95)
	global menubar

	menubar.delete(0, END)

	Titulo1.place_forget()
	Boton_0.place_forget()
	Boton_1.place_forget()
	Boton_2.place_forget()
	Boton_3.place_forget()
	Boton_4.place_forget()
	Boton_5.place_forget()
	Boton_6.place_forget()
	Boton_7.place_forget()
	Boton_8.place_forget()
	Boton_9.place_forget()


	
	Boton_mas.place_forget()
	Boton_menos.place_forget()
	Boton_por.place_forget()
	Boton_entre.place_forget()
	Boton_igual.place_forget()
	Boton_borrar.place_forget()
	Boton_punto.place_forget()
	Boton_elevar.place_forget()
	Boton_raiz.place_forget()
	Boton_parA.place_forget()
	Boton_Apar.place_forget()
	Boton_log.place_forget()
	Boton_aprox.place_forget()


	Boton_LOG.place_forget()
	boton_ln.place_forget()
	Boton_raiz_base.place_forget()
	Boton_elevar_2.place_forget()
	Boton_e.place_forget()
	Boton_ex.place_forget()
	Boton_off.place_forget()
	Boton_pi.place_forget()
	Boton_factorial.place_forget()

	
	Boton_sen.place_forget()
	Boton_cos.place_forget()
	Boton_tan.place_forget()
	Boton_sen2.place_forget()
	Boton_cos2.place_forget()
	Boton_tan2.place_forget()


	Boton_ans.place_forget()
	Boton_P.place_forget()

	Boton_Bin.place_forget()
	Boton_HEX.place_forget()
	Boton_OCT.place_forget()
	Boton_DEC.place_forget()


	Boton_entreR.place_forget()
	Boton_borrar2.place_forget()
	Costantes_k.place_forget()
	Costantes_G.place_forget()

	caja.place_forget()
	menu()

def Calc_Bach():
	
	ventana.geometry("740x610")
	ventana.configure(background="white")
	ventana.wm_attributes("-alpha", 0.95)
	global Titulo1,Boton_0,Boton_1,Boton_2,Boton_3,Boton_4,Boton_5,Boton_6,Boton_7,Boton_8,Boton_9,Boton_mas,Boton_menos,Boton_por,Boton_entre,Boton_igual,Boton_borrar,Boton_punto,Boton_elevar,Boton_raiz,Boton_parA
	global Boton_Apar,Boton_log,Boton_aprox,Boton_LOG,boton_ln,Boton_raiz_base,Boton_elevar_2,Boton_e,Boton_ex,Boton_off,Boton_pi,Boton_factorial,Boton_sen,Boton_sen2,Boton_cos,Boton_cos2,Boton_tan,Boton_tan2
	global Boton_entreR,Boton_P,Boton_Bin,Boton_HEX,Boton_OCT,Boton_DEC,Boton_ans,Boton_borrar2,Costantes_k,Costantes_G,caja
	


	Titulo1 = Label(ventana,font= "Times 18",text="Calculadora BACH",bg = "dim gray",fg = "#FFF")
	Titulo1.place(x = 300 ,y = 10)

				#NUMEROS

	Boton_0 = Button(ventana,text="0",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(0))
	Boton_0.place(x = 100,y = 520)
	Boton_1 = Button(ventana,text="1",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(1))
	Boton_1.place(x = 10,y = 440)
	Boton_2 = Button(ventana,text="2",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(2))
	Boton_2.place(x = 100,y = 440)
	Boton_3 = Button(ventana,text="3",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(3))
	Boton_3.place(x = 190,y = 440)
	Boton_4 = Button(ventana,text="4",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(4))
	Boton_4.place(x = 10,y = 360)
	Boton_5 = Button(ventana,text="5",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(5))
	Boton_5.place(x = 100,y = 360)
	Boton_6 = Button(ventana,text="6",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(6))
	Boton_6.place(x = 190,y = 360)
	Boton_7 = Button(ventana,text="7",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(7))
	Boton_7.place(x = 10,y = 280)
	Boton_8 = Button(ventana,text="8",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(8))
	Boton_8.place(x = 100,y = 280)
	Boton_9 = Button(ventana,text="9",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(9))
	Boton_9.place(x = 190,y = 280)


        		#ESENCIALES

	Boton_mas = Button(ventana,text="+",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("+"))
	Boton_mas.place(x = 280,y = 440)
	Boton_menos = Button(ventana,text="-",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("-"))
	Boton_menos.place(x = 280,y = 360)
	Boton_por = Button(ventana,text="*",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("*"))
	Boton_por.place(x = 280,y = 280)
	Boton_entre = Button(ventana,text="/",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("/"))
	Boton_entre.place(x = 280,y = 200)
	Boton_igual = Button(ventana,text="=",height=alto,width=ANCHO,font=(20),command =ejecutar)
	Boton_igual.place(x = 280,y = 520)
	Boton_borrar = Button(ventana,text="AC",height=alto,width=ANCHO,font=(20),command =eliminar)
	Boton_borrar.place(x = 10,y = 120)
	Boton_punto = Button(ventana,text=".",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("."))
	Boton_punto.place(x = 190,y = 520)
	Boton_elevar = Button(ventana,text="^",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("**"))
	Boton_elevar.place(x = 280,y = 120)
	Boton_raiz = Button(ventana,text="Raiz",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("**(1/2)"))
	Boton_raiz.place(x = 370,y = 200)
	Boton_parA = Button(ventana,text="(",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("("))
	Boton_parA.place(x = 100,y = 120)
	Boton_Apar = Button(ventana,text=")",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(")"))
	Boton_Apar.place(x = 190,y = 120)
	Boton_log = Button(ventana,text="log",height=alto,width=ANCHO,font=(20),command =log)
	Boton_log.place(x = 100,y = 200)
	Boton_aprox = Button(ventana, text ="aprox", height= alto,width= ANCHO, font=(20),command=aproximar)
	Boton_aprox.place(x = 10, y = 520)

				#AÑADIDOS

	Boton_LOG = Button(ventana, text="logn de x", height = alto, width = ANCHO, font=(20),command = logbase)
	Boton_LOG.place(x = 10, y = 200)
	boton_ln = Button(ventana,text="ln",height=alto,width=ANCHO, font=(20), command= ln)
	boton_ln.place(x = 190, y = 200)
	Boton_raiz_base = Button(ventana,text="x raiz x",height=alto,width=ANCHO, font=(20),command = raiz2)
	Boton_raiz_base.place(x = 460, y = 200)
	Boton_elevar_2 = Button(ventana,text="^2",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("**2")) 
	Boton_elevar_2.place(x = 370,y = 120)
	Boton_e = Button(ventana,text="e",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("2.7182"))
	Boton_e.place(x = 460,y = 120)
	Boton_ex = Button(ventana,text="e^",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("2.7182**"))
	Boton_ex.place(x = 550,y = 120)
	Boton_off = Button(ventana, text ="OFF", height= alto,width= ANCHO, font=(20),command=cerrar)
	Boton_off.place(x = 640, y = 120)
	Boton_pi = Button(ventana,text="π",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("3.1416"))
	Boton_pi.place(x = 550,y = 200)
	Boton_factorial = Button(ventana,text="x!",height=alto,width=ANCHO,font=(20),command =factorial)
	Boton_factorial.place(x = 640,y = 200)

				#TRIGONOMETRIA

	Boton_sen = Button(ventana, text="sen",height = alto, width = ANCHO, font=(20), command = sin)		
	Boton_sen.place(x = 370,y = 280)
	Boton_cos = Button(ventana, text="cos",height = alto, width = ANCHO, font=(20), command = cos)		
	Boton_cos.place(x = 460,y = 280)
	Boton_tan = Button(ventana, text="tan",height = alto, width = ANCHO, font=(20), command = tan)		
	Boton_tan.place(x = 550,y = 280)
	Boton_sen2 = Button(ventana, text="arcsen",height = alto, width = ANCHO, font=(20), command = asin)	
	Boton_sen2.place(x = 370,y = 360)
	Boton_cos2 = Button(ventana, text="arccos",height = alto, width = ANCHO, font=(20), command = acos)
	Boton_cos2.place(x = 460,y = 360)
	Boton_tan2 = Button(ventana, text="arctan",height = alto, width = ANCHO, font=(20), command = atan)
	Boton_tan2.place(x = 550,y = 360)


	Boton_entreR = Button(ventana,text="÷ & R",height=alto,width=ANCHO,font=(20),command = resto)
	Boton_entreR.place(x = 640,y = 360)
	Boton_P = Button(ventana,text="%",height=alto,width=ANCHO,font=(20), command = lambda:imprimir("/100"))
	Boton_P.place(x = 640,y = 280)


				#Numeros

	Boton_Bin = Button(ventana,text="BIN",height=alto,width=ANCHO,font=(20),command = bin)
	Boton_Bin.place(x = 370,y = 440)
	Boton_HEX = Button(ventana,text="HEX",height=alto,width=ANCHO,font=(20),command = hex)
	Boton_HEX.place(x = 460,y = 440)
	Boton_OCT = Button(ventana,text="OCT",height=alto,width=ANCHO,font=(20),command = oct)
	Boton_OCT.place(x = 550,y = 440)
	Boton_DEC = Button(ventana,text="DEC",height=alto,width=ANCHO,font=(20),command = dec)
	Boton_DEC.place(x = 640,y = 440)



	Boton_ans = Button(ventana,text="ANS",height=alto,width=ANCHO,font=(20),command = ans)												#ERROR
	Boton_ans.place(x = 550,y = 520)

	Boton_borrar2 = Button(ventana,text="«",height=alto,width=ANCHO,font=(20),command=borrar)
	Boton_borrar2.place(x = 640,y = 520)

	Costantes_k = Button(ventana,text="K",height=alto,width=ANCHO,font=(20),command=lambda:imprimir("9*(10**9)"))
	Costantes_k.place(x = 370,y = 520)

	Costantes_G = Button(ventana,text="G",height=alto,width=ANCHO,font=(20),command=lambda:imprimir("6.67*10**(-11)"))
	Costantes_G.place(x = 460,y = 520)


	#Creamos la barra y la definimos.


	caja = Entry(ventana,font=("arial",20,"bold"),width = 30,insertwidth="3",textvariable = var,bg="powderblue",bd=10,justify="right")
	caja.place(x =160 ,y = 50)


def calc_eso():
	Titulo1 = Label(ventana,font= "Times 18",text="Calculadora ESO",bg = "dim gray",fg = "#FFF")
	Titulo1.place(x = 100 ,y = 10)

				#NUMEROS

	Boton_0 = Button(ventana,text="0",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(0))
	Boton_0.place(x = 100,y = 520)
	Boton_1 = Button(ventana,text="1",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(1))
	Boton_1.place(x = 10,y = 440)
	Boton_2 = Button(ventana,text="2",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(2))
	Boton_2.place(x = 100,y = 440)
	Boton_3 = Button(ventana,text="3",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(3))
	Boton_3.place(x = 190,y = 440)
	Boton_4 = Button(ventana,text="4",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(4))
	Boton_4.place(x = 10,y = 360)
	Boton_5 = Button(ventana,text="5",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(5))
	Boton_5.place(x = 100,y = 360)
	Boton_6 = Button(ventana,text="6",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(6))
	Boton_6.place(x = 190,y = 360)
	Boton_7 = Button(ventana,text="7",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(7))
	Boton_7.place(x = 10,y = 280)
	Boton_8 = Button(ventana,text="8",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(8))
	Boton_8.place(x = 100,y = 280)
	Boton_9 = Button(ventana,text="9",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(9))
	Boton_9.place(x = 190,y = 280)


        		#ESENCIALES

	Boton_mas = Button(ventana,text="+",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("+"))
	Boton_mas.place(x = 280,y = 440)
	Boton_menos = Button(ventana,text="-",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("-"))
	Boton_menos.place(x = 280,y = 360)
	Boton_por = Button(ventana,text="*",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("*"))
	Boton_por.place(x = 280,y = 280)
	Boton_entre = Button(ventana,text="/",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("/"))
	Boton_entre.place(x = 280,y = 200)
	Boton_igual = Button(ventana,text="=",height=alto,width=ANCHO,font=(20),command =ejecutar)
	Boton_igual.place(x = 280,y = 520)
	Boton_borrar = Button(ventana,text="AC",height=alto,width=ANCHO,font=(20),command =eliminar)
	Boton_borrar.place(x = 10,y = 120)
	Boton_punto = Button(ventana,text=".",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("."))
	Boton_punto.place(x = 190,y = 520)
	Boton_elevar = Button(ventana,text="^",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("**"))
	Boton_elevar.place(x = 10,y = 200)
	Boton_raiz = Button(ventana,text="Raiz",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("**(1/2)"))
	Boton_raiz.place(x = 190,y = 200)
	Boton_parA = Button(ventana,text="(",height=alto,width=ANCHO,font=(20),command =lambda:imprimir("("))
	Boton_parA.place(x = 100,y = 120)
	Boton_Apar = Button(ventana,text=")",height=alto,width=ANCHO,font=(20),command =lambda:imprimir(")"))
	Boton_Apar.place(x = 190,y = 120)
	Boton_log = Button(ventana,text="log",height=alto,width=ANCHO,font=(20),command =log)
	Boton_log.place(x = 100,y = 200)
	Boton_aprox = Button(ventana, text ="aprox", height= alto,width= ANCHO, font=(20),command=aproximar)
	Boton_aprox.place(x = 10, y = 520)

	Boton_off = Button(ventana, text ="OFF", height= alto,width= ANCHO, font=(20),command=cerrar)
	Boton_off.place(x = 280, y = 120)

	caja = Entry(ventana,font=("arial",20,"bold"),width = 20,insertwidth="1",textvariable = var,bg="powderblue",bd=10,justify="right")
	caja.place(x =40 ,y = 50)

def fmenu():
	Calc = "bach"

	Calc_Bach()
	titulo_menu.place_forget()
	boton_ESO.place_forget()
	boton_bach.place(x = 2000)
	panel.place_forget()
	nombre.place_forget()


def fmenu2():
	calc_eso()
	titulo_menu.place_forget()
	boton_ESO.place_forget()
	boton_bach.place(x = 2000)
	panel.place_forget()
	nombre.place_forget()


#img = ImageTk.PhotoImage(Image.open("C:/Users/mateo/OneDrive/Escritorio/Cole/Tic/Ies.jpeg"))
img=Image.open("C:/Users/mateo/OneDrive/Escritorio/Cole/Tic/Ies.jpeg")

img2=img.resize((370,250),Image.ANTIALIAS)
Imgs2=ImageTk.PhotoImage(img2)
panel = Label(ventana, image = Imgs2)
panel.place(x = 15, y = 280)


titulo_menu = Label(ventana,font= "Times 18",text="Calculadora IES O Ribeiro",bg = "dim gray",fg = "#FFF")
titulo_menu.place(x = 65 ,y = 20)

boton_ESO = Button(ventana,text="Calculadora ESO",height=2,width=30,font=(30),command= fmenu2)
boton_ESO.place(x = 25,y = 100)

boton_bach = Button(ventana,text="Calculadora BACH",height=2,width=30,font=(30),command = fmenu)
boton_bach.place(x = 25,y = 180)

nombre = Label(ventana,font= "Times 10", text="Mateo Rivela Santos",bg = "white")
nombre.place(x = 250,y = 570)

ventana.mainloop()