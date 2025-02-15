from distutils.cmd import Command
from importlib.resources import path
import tkinter as tk 
from tkinter.ttk import Treeview
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo
from urllib import response
from PIL import ImageTk, Image


import os
import sqlite3



root = tk.Tk()
root.geometry('800x600')
root.title('Cadastro de Imagens')


def carregar_dados_tree():
    connection = sqlite3.connect('cadastro_alunos.db')
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM dados
    """)

    connection.commit()
    dados = cursor.fetchall()
    connection.close()

    if dados:
        for item in tree_table.get_children():
            tree_table.delete(item)
            
        for r in range(len(dados)):
            tree_table.insert(parent='', iid=r, index='end', values=dados[r][0:6])

    else:
        for item in tree_table.get_children():
            tree_table.delete(item) 


image_data = b''

def ler_abrir_image():
    global image_data, img

    path = askopenfilename()
    if path:
        ler_image = open(path, 'rb')
        image_data = ler_image.read()
        ler_image.close()

        img = ImageTk.PhotoImage(Image.open(path))
        img_label.config(image=img)


def deletar_image():
    global image_data
    image_data = b''
    img_label.config(image=img_padrao)


def checar_id_bd_existe(_id, update):
    connection = sqlite3.connect('cadastro_alunos.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM dados WHERE id = ?", (_id,))

    connection.commit()

    response = cursor.fetchall()
    connection.close()

    if update == 'update':
        if tree_table.selection():
            index = int(tree_table.selection()[0])
            select_id = tree_table.item(index, 'values')[0]

            if _id == select_id:
                return False
            elif response:
                return True
            else:
                return False
    return bool(response)


def checar_campos_data(order):
    if id_numero.get() !='':
        if not checar_id_bd_existe(id_numero.get(), update=order):
            if order == 'add':
                add_cadastro(_id=id_numero.get(), _nome=nome.get(),
                            _idade=idade.get(), _sexo=sexo.get(),
                            _telefone=telefone.get(), _email=email_entry.get())
            elif order == 'update':
                atualizar_cadastro(_id=id_numero.get(), _nome=nome.get(),
                            _idade=idade.get(), _sexo=sexo.get(),
                            _telefone=telefone.get(), _email=email_entry.get())
        else:
            showerror("Erro", "Este ID já está cadastrado no banco de dados")
            id_numero.focus()
    else:
        showerror("Erro", "Favor preencher o campo ID")


def limpar_dados():
    global image_data
    id_numero.delete(0, tk.END)
    nome.delete(0, tk.END)
    idade.delete(0, tk.END)
    sexo.set('masculino')
    telefone.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    img_label.config(image=img_padrao)
    image_data = b''


def iniciar_database():
    if os.path.exists('cadastro_alunos.db'):
        carregar_dados_tree()
    else:
        connection = sqlite3.connect('cadastro_alunos.db')
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE dados (
            id int,
            nome text,
            idade text,
            sexo text,
            telefone text,
            email text, 
            image blog
        
        )
                       
        """)

        connection.commit()
        connection.close()


def add_cadastro(_id, _nome,_idade,_sexo,_telefone,_email):
    connection = sqlite3.connect('cadastro_alunos.db')
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO dados (id, nome, idade, sexo, telefone, email, image) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (_id, _nome, _idade, _sexo, _telefone, _email, image_data))

    connection.commit()
    connection.close()

    limpar_dados()
    carregar_dados_tree()


def atualizar_cadastro(_id, _nome,_idade,_sexo,_telefone,_email):
    if tree_table.selection():
        index = int(tree_table.selection()[0])
        select_id = tree_table.item(index, 'values')[0]

        connection = sqlite3.connect('cadastro_alunos.db')

        cursor = connection.cursor()
        cursor.execute("""
        UPDATE dados 
        SET id = ?, nome = ?, idade = ?, sexo = ?, telefone = ?, email = ?, image = ? 
        WHERE id = ?
        """, (_id, _nome, _idade, _sexo, _telefone, _email, image_data, select_id))


        connection.commit()

        if _id != select_id:
            cursor.execute(""" UPDATE dados SET id = ? WHERE id = ? """, (_id, select_id))
            connection.close()

            limpar_dados()
            carregar_dados_tree()


def deletar_dados():
    if tree_table.selection():
        index = int(tree_table.selection()[0])
        select_id = tree_table.item(index, 'values')[0]

        connection = sqlite3.connect('cadastro_alunos.db')
        cursor = connection.cursor()

        cursor.execute("""
        DELETE FROM dados WHERE id = ?
        """, (select_id,))

        connection.commit()
        connection.close()

        limpar_dados()
        carregar_dados_tree()


def colocar_dados():
    global image_data, img
    if tree_table.selection():
        index = int(tree_table.selection()[0])

        dados = tree_table.item(index, 'values')

        limpar_dados()

        id_numero.insert(tk.END,dados[0])
        nome.insert(tk.END,dados[1])
        idade.insert(tk.END,dados[2])
        sexo.set(dados[3])
        telefone.insert(tk.END,dados[4])
        email_entry.insert(tk.END,dados[5])

        connection = sqlite3.connect('cadastro_alunos.db')
        cursor = connection.cursor()

        cursor.execute("SELECT image FROM dados WHERE id = ?", (dados[0],))

        connection.commit()
        response = cursor.fetchall()
        connection.close()

        if response[0] != (b'',):
            image_data = response[0][0]
            img_data = response[0][0]

            with open('.temp_pic', 'wb') as write_img:
                write_img.write(img_data)
                write_img.close()

                img = ImageTk.PhotoImage(Image.open('.temp_pic'))
                img_label.config(image=img)


def pesquisar_cadastro(_id):
    if _id != '':

        connection = sqlite3.connect('cadastro_alunos.db')
        cursor = connection.cursor()
        pesquisar_id_query = """SELECT id, nome, idade, sexo, telefone, email FROM dados WHERE id == ?"""
        cursor.execute(pesquisar_id_query, (_id,))


        connection.commit()
        response = cursor.fetchall()
        connection.close()

        if response:
            for item in tree_table.get_children():
                tree_table.delete(item)
            
            for r in range(len(response)):
                tree_table.insert(parent='', iid=r, index='end', values=response[r])
        else:
            for item in tree_table.get_children():
                tree_table.delete(item)
    else:
        carregar_dados_tree()

frame_Principal = tk.Frame(root)

Cabecalho = tk.Label(frame_Principal, text='Cadastro de alunos com imagens', bg='orange', font=('bold', 18))
Cabecalho.pack(fill=tk.X)

img_frame = tk.Frame(frame_Principal)
img_padrao = tk.PhotoImage(file='aluno.png')

img_label = tk.Label(img_frame, image=img_padrao, bd=2, relief=tk.SOLID)
img_label.pack(side=tk.LEFT)
img_frame.configure(bg='green')
img_frame.pack(anchor=tk.W, pady=5)

abrir_img_btn = tk.Button(img_frame, text='Abrir_Foto', font=('bold', 12), command=ler_abrir_image, bg='green', fg='white')
abrir_img_btn.pack(side=tk.LEFT, anchor=tk.S, padx=5)

fechar_img_btn = tk.Button(img_frame, text='Fechar_Foto', font=('bold', 12), command=deletar_image, bg='red', fg='yellow')
fechar_img_btn.pack(side=tk.LEFT, anchor=tk.S, padx=5)

formulario_frame = tk.Frame(frame_Principal)


id_lbl = tk.Label(formulario_frame, text='Usuário ID:', font=('bold', 12))
id_lbl.grid(row=0, column=0, sticky=tk.W, pady=2)

id_numero = tk.Entry(formulario_frame, width=50, font=('bold', 12))
id_numero.grid(row=0, column=1)

nome_lbl = tk.Label(formulario_frame, text='Nome Usuário:', font=('bold', 12))
nome_lbl.grid(row=1, column=0, sticky=tk.W, pady=2)

nome = tk.Entry(formulario_frame, width=50, font=('bold', 12))
nome.grid(row=1, column=1)

idade_lbl = tk.Label(formulario_frame, text='Idade Usuário:', font=('bold', 12))
idade_lbl.grid(row=2, column=0, sticky=tk.W, pady=2)

idade = tk.Entry(formulario_frame, width=50, font=('bold', 12))
idade.grid(row=2, column=1)

sexo = tk.Label(formulario_frame, text='Selecione Sexo:', font=('bold', 12))
sexo.grid(row=3, column=0, sticky=tk.W, pady=2)

sexo_btn_frame = tk.Frame(formulario_frame)

sexo = tk.StringVar()
sexo.set('masculino')

masculino_btn = tk.Radiobutton(sexo_btn_frame, text='Masculino', font=('bold', 12), variable=sexo, value='masculino')
masculino_btn.pack(side=tk.LEFT)

feminino_btn = tk.Radiobutton(sexo_btn_frame, text='Feminino', font=('bold', 12), variable=sexo, value='feminino')
feminino_btn.pack(side=tk.LEFT, padx=98)

sexo_btn_frame.grid(row=3, column=1)


telefone_lbl = tk.Label(formulario_frame, text='Telefone Usuário:', font=('bold', 12))
telefone_lbl.grid(row=4, column=0, sticky=tk.W, pady=2)

telefone = tk.Entry(formulario_frame, width=50, font=('bold', 12))
telefone.grid(row=4, column=1)

email_lbl = tk.Label(formulario_frame, text='E-mail:', font=('bold', 12))
email_lbl.grid(row=5, column=0, sticky=tk.W, pady=2)

email_entry = tk.Entry(formulario_frame, width=50, font=('bold', 12))
email_entry.grid(row=5, column=1)


formulario_frame.pack(anchor=tk.W, pady=5, padx=5)


botao_frame = tk.Frame(frame_Principal, bg='green')
botao_frame.pack(anchor=tk.W, padx=10)

add_btn = tk.Button(botao_frame, text='Cadastrar', bg='green', fg='white', font=('bold', 12), 
                    command= lambda: checar_campos_data('add'))
add_btn.pack(side=tk.LEFT, padx=10)

atualizar_btn = tk.Button(botao_frame, text='Atualizar', bg='yellow', fg='black', font=('bold', 12), 
                          command= lambda:checar_campos_data('update'))
atualizar_btn.pack(side=tk.LEFT, padx=10)

deletar_btn = tk.Button(botao_frame, text='Deletar', bg='red', fg='yellow', font=('bold', 12), command=deletar_dados)
deletar_btn.pack(side=tk.LEFT, padx=10)

limpar_btn = tk.Button(botao_frame, text='Limpar', bg='orange', fg='blue', font=('bold', 12), command=limpar_dados)
limpar_btn.pack(side=tk.LEFT, padx=10)



frame_Principal.pack(anchor=tk.W, pady=5, padx=5)
frame_Principal.pack_propagate(False)
frame_Principal.configure(width=500, height=400, bg='green')


frame_tabela = tk.Frame(root)
frame_tabela.pack(side= tk.TOP, fill= tk.X)

pesquisar_lbl = tk.Label(frame_tabela, text='Pesquisar Usuário por ID', font=('bold', 12))
pesquisar_lbl.pack(anchor= tk.W, padx=5)

pesquisar = tk.Entry(frame_tabela, font=('bold', 12))
pesquisar.pack(anchor= tk.W, padx=5, pady=10)
pesquisar.bind('<KeyRelease>', lambda e: pesquisar_cadastro(pesquisar.get()))


framerodape = tk.Frame(root, bg='grey')
framerodape.pack(side= tk.BOTTOM, fill= tk.X)
rodape_lbl = tk.Label(framerodape, text='carlos140k@gmail.com', bg='grey', fg='white', font=('Arial', 12, 'bold'))
rodape_lbl.pack(side= tk.BOTTOM, fill= tk.X)

tree_table = Treeview(frame_tabela)
tree_table.pack(fill= tk.X)

tree_table.bind('<<TreeviewSelect>>', lambda e: colocar_dados())

tree_table['column'] = ['ID', 'Nome', 'Idade', 'Sexo', 'Telefone', 'Email']
tree_table.column('#0', stretch= tk.NO, width=0)

tree_table.heading('ID', text='ID', anchor= tk.W)
tree_table.column('ID', width=30, anchor= tk.W)

tree_table.heading('Nome', text='Nome', anchor= tk.W)
tree_table.column('Nome', width=110, anchor= tk.W)

tree_table.heading('Idade', text='Idade', anchor= tk.W)
tree_table.column('Idade', width=33, anchor= tk.W)

tree_table.heading('Sexo', text='Sexo', anchor= tk.W)
tree_table.column('Sexo', width=65, anchor= tk.W)

tree_table.heading('Telefone', text='Telefone', anchor= tk.W)
tree_table.column('Telefone', width=80, anchor= tk.W)

tree_table.heading('Email', text='Email', anchor= tk.W)
tree_table.column('Email', width=150, anchor= tk.W)


iniciar_database()
root.mainloop()
