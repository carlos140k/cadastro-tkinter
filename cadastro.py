import tkinter as tk 
from tkinter.ttk import Treeview
from turtle import right
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image



root = tk.Tk()
root.geometry('500x700')
root.title('Cadastro de Imagens')


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

endereco_lbl = tk.Label(formulario_frame, text='Endereço Usuário:', font=('bold', 12))
endereco_lbl.grid(row=5, column=0, sticky=tk.W, pady=2)

endereco = tk.Entry(formulario_frame, width=50, font=('bold', 12))
endereco.grid(row=5, column=1)



formulario_frame.pack(anchor=tk.W, pady=5, padx=5)




botao_frame = tk.Frame(frame_Principal, bg='green')
botao_frame.pack(anchor=tk.W, padx=10)

add_btn = tk.Button(botao_frame, text='Cadastrar', bg='green', fg='white', font=('bold', 12))
add_btn.pack(side=tk.LEFT, padx=10)

atualizar_btn = tk.Button(botao_frame, text='Atualizar', bg='yellow', fg='black', font=('bold', 12))
atualizar_btn.pack(side=tk.LEFT, padx=10)

deletar_btn = tk.Button(botao_frame, text='Deletar', bg='red', fg='yellow', font=('bold', 12))
deletar_btn.pack(side=tk.LEFT, padx=10)

limpar_btn = tk.Button(botao_frame, text='Limpar', bg='orange', fg='blue', font=('bold', 12))
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


framerodape = tk.Frame(root, bg='grey')
framerodape.pack(side= tk.BOTTOM, fill= tk.X)
rodape_lbl = tk.Label(framerodape, text='carlos140k@gmail.com', bg='grey', fg='white', font=('bold', 12))
rodape_lbl.pack(side= tk.BOTTOM, fill= tk.X)

tree_table = Treeview(frame_tabela)
tree_table.pack(fill= tk.X)

tree_table['column'] = ['ID', 'Nome', 'Idade', 'Sexo', 'Telefone', 'Email']
tree_table.column('#0', stretch= tk.NO, width=0)

tree_table.heading('ID', text='Numero ID', anchor= tk.W)
tree_table.column('ID', width=80, anchor= tk.W)

tree_table.heading('Nome', text='Nome', anchor= tk.W)
tree_table.column('Nome', width=110, anchor= tk.W)

tree_table.heading('Idade', text='Idade', anchor= tk.W)
tree_table.column('Idade', width=80, anchor= tk.W)

tree_table.heading('Sexo', text='Sexo', anchor= tk.W)
tree_table.column('Sexo', width=80, anchor= tk.W)

tree_table.heading('Telefone', text='Telefone', anchor= tk.W)
tree_table.column('Telefone', width=100, anchor= tk.W)

tree_table.heading('Email', text='Email', anchor= tk.W)
tree_table.column('Email', width=150, anchor= tk.W)

root.mainloop()
