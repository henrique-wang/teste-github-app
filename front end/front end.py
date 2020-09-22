# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 07:37:39 2020

@author: rubel
"""
from tkinter import *
from tkinter import messagebox

LARGE_FONT= ("Verdana", 12)


adm={"a": ""}
comentarios=[['a','b','c']]
funcionarios=[["jorge","jorge@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["roberto","roberto@gmail"],["alfredo","alfredo@email"]]

class ScrollFrame(Frame):#https://gist.github.com/mp035/9f2027c3ef9172264532fcd6262f3b01 by mp035
    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

        self.canvas = Canvas(self, borderwidth=0, background="#ffffff")          #place canvas on self
        self.viewPort = Frame(self.canvas, background="#ffffff")                    #place a frame on the canvas, this frame will hold the child widgets
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.


class Window(Tk):

     def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home_page, Login_page, Pontuacao_page, Adicionar_funcionario_page,
                  Editar_funcionario_tabela_page,Editar_funcionario_individual_page,Comentarios_page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login_page)

     def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

     def atualizar_usuario(self,ID):
         self.frames[Editar_funcionario_individual_page].atualizar(ID)
         self.show_frame(Editar_funcionario_individual_page)

     def mostrar_comentario(self,ID):
         print("mostrando comentario " + str(ID))
        
class Home_page(Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        Frame.__init__(self,parent)
        label = Label(self, text="Home Page", font=LARGE_FONT)
        label.grid(row=0, column=0, columnspan=3,)
        self.grid_columnconfigure(0,weight=1)
        
        button1 = Button(self, text="Ver pontuação",
                            command=self.pontuacao,width=21)
        button1.grid(row=5, column=0,sticky="e")
        self.grid_columnconfigure(1,weight=1)
        
        space=Label(self)
        space.grid(row=2,rowspan=3)
        
        button2 = Button(self, text="Adicionar funcionário",
                            command=self.adicionar_funcionario,width=21)
        button2.grid(row=5, column=1,sticky="w")
        
        button3 = Button(self, text="Editar funcionários",
                            command=self.editar_funcionarios,width=21)
        button3.grid(row=6, column=0,sticky="e")
        
        button4 = Button(self, text="Comentários",
                            command=self.comentarios,width=21)
        button4.grid(row=6, column=1,sticky="w")
        
        button5 = Button(self, text="sair",
                            command=self.sair,width=4)
        button5.grid(row=7, column=2,sticky="w")
        
    def sair(self,*args):
        self.controller.show_frame(Login_page)
        
    def comentarios(self,*args):
        self.controller.show_frame(Comentarios_page)
        
    def editar_funcionarios(self,*args):
       self.controller.show_frame(Editar_funcionario_tabela_page)

    def pontuacao(self,*args):
       self.controller.show_frame(Pontuacao_page)
        
    def adicionar_funcionario(self,*args):
        self.controller.show_frame(Adicionar_funcionario_page)
    
class Login_page(Frame):
    
    
    
    def __init__(self,parent,controller):
        self.controller=controller
        Frame.__init__(self,parent)
        self.label = Label(self, text="Log in", font=LARGE_FONT)
        self.nomel = Label(self,text="Nome de usuário:", font="Verdana 10")
        self.senhal = Label(self,text="Senha:", font="Verdana 10")
        self.nome = Entry(self)
        self.senha = Entry(self,show="*")
        self.label.grid(row=0,column=0,columnspan=3,sticky="ew")
        self.nomel.grid(row=1,column=0,sticky="e")
        self.senhal.grid(row=2,column=0,sticky="e")
        self.nome.grid(row=1,column=1,sticky="w")
        self.senha.grid(row=2,column=1,sticky="w")
        
        self.grid_columnconfigure(3, weight=1)

        self.button = Button(self, text="Log in",
                            command=self.testar)
        self.button.grid(row=3,column=2)
        
        
    def testar(self,*args):
        try:
            ID=self.nome.get()
            password=self.senha.get()
            if adm[ID]!=password:
                raise()
            self.nome.delete(0,'end')
            self.senha.delete(0,'end')
            self.controller.show_frame(Home_page)
        except:
            messagebox.showinfo("erro de login","usuário ou senha inválida")
            self.controller.show_frame(Login_page)  
            self.nome.delete(0,'end')
            self.senha.delete(0,'end')
    

    
    
class Pontuacao_page(Frame):
    
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        self.label = Label(self, text="Pontuação", font=LARGE_FONT)
        self.label.grid(row=0,column=0)

        self.button1 = Button(self, text="Voltar",
                            command=self.sair)
        self.button1.grid(row=10,column=10)
        
        self.buscal=Label(self,text="Procurar:",font="Verdana 8")
        self.buscal.grid(row=4,column=0)
        self.busca= Entry(self)
        self.busca.grid(row=4,column=1)
        self.button2 = Button(self, text="procurar",font="verdana 8",
                            command=self.buscar)
        self.button2.grid(row=4,column=2)
    
    def sair(self,*args):
        self.busca.delete(0,'end')
        self.controller.show_frame(Home_page)
        
    def buscar(self,*args):
        print("busca por nome")

class Adicionar_funcionario_page(Frame):
    
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        self.label = Label(self, text="Adicionar funcionário", font=LARGE_FONT)
        self.label.grid(row=0,column=0)
        
        self.nomel=Label(self,text='Nome: ', font=LARGE_FONT)
        self.nome=Entry(self)
        self.nomel.grid(row=1,column=0)
        self.nome.grid(row=1,column=1)
        
        self.emaill=Label(self,text='Email: ', font=LARGE_FONT)
        self.email=Entry(self)
        self.emaill.grid(row=2,column=0)
        self.email.grid(row=2,column=1)
        
        self.senhal=Label(self,text='Senha: ',font=LARGE_FONT)
        self.senha=Entry(self,show='*')
        self.senhal.grid(row=3,column=0)
        self.senha.grid(row=3,column=1)
        
        self.adm=Checkbutton(self,text='Administrador')
        self.adm.grid(row=4,column=0)
        

        self.button1 = Button(self, text="Voltar",
                            command=self.voltar)
        self.button1.grid(row=5,column=0)
        
        self.button2 = Button(self, text="Confirmar",
                            command=self.confirmar)
        self.button2.grid(row=5,column=1)
        
    def voltar(self,*args):
        self.nome.delete(0, 'end')
        self.email.delete(0, 'end')
        self.senha.delete(0, 'end')
        self.adm.deselect()
        self.controller.show_frame(Home_page)
    
    def confirmar(self,*args):
        print("adicionar")
        messagebox.showinfo("Ação completada","Usuário adicionado com sucesso")
        self.nome.delete(0,'end')
        self.email.delete(0,'end')
        self.senha.delete(0,'end')
        self.adm.deselect()

class Editar_funcionario_tabela_page(Frame):
    
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        self.label = Label(self, text="Funcionários", font=LARGE_FONT)
        self.label.grid(row=0,column=0,columnspan=5)
        self.grid_columnconfigure(0,weight=1)

        self.button = Button(self, text="Voltar",
                            command=self.voltar)
        self.button.grid(row=4,column=5)
        
        self.button2= Button(self,text='procurar',
                             command=self.procurar)
        self.button2.grid(row=4,column=3)
        
        self.procura=Entry(self)
        self.procura.grid(row=4,column=1)

        self.scrollframe = ScrollFrame(self)
        self.scrollframe.grid(row=1,column=1,columnspan=5)
        self.editar_lista()


        
    def editar_lista(self,*args):
        for row in range(len(funcionarios)):
            Label(self.scrollframe.viewPort, text=funcionarios[row][0]).grid(row=row, column=0)
            Label(self.scrollframe.viewPort, text=funcionarios[row][1]).grid(row=row, column=1)
            a=row
            Button(self.scrollframe.viewPort, text=funcionarios[row][0], command=lambda x=a:
                                        self.controller.atualizar_usuario(x)).grid(row=row, column=2)
        
    def voltar(self,*args):
        self.controller.show_frame(Home_page)
        
    def procurar(self,*args):
        print('procurar')

class Editar_funcionario_individual_page(Frame):
    
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        self.ID=None
        self.label1 = Label(self, text="Editar usuáro", font=LARGE_FONT)
        self.label1.grid(row=0,column=0)

        self.label2=Label(self,text="Nome:",font="verdano 10")
        self.label2.grid(row=1,column=0)

        self.email=Entry(self)
        self.email.grid(row=2,column=1)

        self.button1 = Button(self, text="Apagar",
                            command=self.apagar)
        self.button1.grid(row=10,column=1)

        self.button1 = Button(self, text="Confirmar",
                              command=self.confirmar)
        self.button1.grid(row=10, column=2)

        self.button1 = Button(self, text="Voltar",
                              command=self.voltar)
        self.button1.grid(row=10, column=3)

    def atualizar(self,ID):
        print("atualizar")
        self.ID=ID
        self.label2.configure(text="Nome: " + funcionarios[ID][0])

    def apagar(self,*args):
        print("apagar")
        messagebox.showinfo("Ação completada", "Usuário apagado com sucesso")
        self.email.delete(0, 'end')
        self.controller.show_frame(Editar_funcionario_tabela_page)


    def confirmar(self,*args):
        print("confirmar")
        messagebox.showinfo("Ação completada", "Usuário atualizado com sucesso")
        self.email.delete(0,'end')
        self.controller.show_frame(Editar_funcionario_tabela_page)

    def voltar(self,*args):
        self.email.delete(0,'end')
        self.controller.show_frame(Editar_funcionario_tabela_page)
        
class Comentarios_page(Frame):
    
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        self.label = Label(self, text="Comentários", font=LARGE_FONT)
        self.label.grid(row=0, column=0, columnspan=5)
        self.grid_columnconfigure(0, weight=1)

        self.button1 = Button(self, text="Voltar",
                             command=self.voltar)
        self.button1.grid(row=4, column=5)

        self.button2 = Button(self, text='procurar',
                              command=self.procurar)
        self.button2.grid(row=4, column=3)

        self.procura = Entry(self)
        self.procura.grid(row=4, column=1)

        self.scrollframe = ScrollFrame(self)
        self.scrollframe.grid(row=1, column=1, columnspan=5)
        self.editar_lista()

    def editar_lista(self, *args):
        for row in range(len(comentarios)):
            Label(self.scrollframe.viewPort, text=comentarios[row][0]).grid(row=row, column=0)
            Label(self.scrollframe.viewPort, text=comentarios[row][1]).grid(row=row, column=1)
            a = row
            Button(self.scrollframe.viewPort, text="vizualizar", command=lambda x=a:
                        self.controller.mostrar_comentario(x)).grid(row=row, column=2)

    def voltar(self, *args):
        self.procura.delete(0,'end')
        self.controller.show_frame(Home_page)

    def procurar(self, *args):
        print('procurar')


app = Window()
app.mainloop()