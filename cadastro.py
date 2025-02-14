import tkinter as tk 


root = tk.Tk()
root.geometry('600x620')
root.title('Cadastro de Imagens')


frame_Principal = tk.Frame(root)

Cabecalho = tk.Label(frame_Principal, text='Cadastro de alunos com imagens', bg='orange', font=('bold', 18))
Cabecalho.pack(fill=tk.X)

img_frame = tk.Frame(frame_Principal)
img_padrao = tk.PhotoImage(file='aluno.png')
img_label = tk.Label(img_frame, image=img_padrao, bd=2, relief=tk.SOLID,)
img_label.pack(side=tk.LEFT)
img_frame.configure(bg='green')
img_frame.pack(anchor=tk.W, pady=5)

abrir_img_btn = tk.Button(img_frame, text='Abrir_Foto', font=('bold', 12), bg='green', fg='white')
abrir_img_btn.pack(side=tk.LEFT, anchor=tk.S, padx=5)

fechar_img_btn = tk.Button(img_frame, text='Fechar_Foto', font=('bold', 12), bg='red', fg='yellow')
fechar_img_btn.pack(side=tk.LEFT, anchor=tk.S, padx=5)

formulario_frame = tk.Frame(frame_Principal)


id_lbl = tk.Label(formulario_frame, text='Usuário ID:', font=('bold', 12))
id_lbl.grid(row=0, column=0, sticky=tk.W, pady=2)

id_numero = tk.Entry(formulario_frame, font=('bold', 12))
id_numero.grid(row=0, column=1)

nome_lbl = tk.Label(formulario_frame, text='Nome Usuário:', font=('bold', 12))
nome_lbl.grid(row=1, column=0, sticky=tk.W, pady=2)

nome = tk.Entry(formulario_frame, font=('bold', 12))
nome.grid(row=1, column=1)

idade_lbl = tk.Label(formulario_frame, text='Idade Usuário:', font=('bold', 12))
idade_lbl.grid(row=2, column=0, sticky=tk.W, pady=2)

idade = tk.Entry(formulario_frame, font=('bold', 12))
idade.grid(row=2, column=1)

sexo = tk.Label(formulario_frame, text='Selecione Sexo:', font=('bold', 12))
sexo.grid(row=3, column=0, sticky=tk.W, pady=2)

sexo_btn_frame = tk.Frame(formulario_frame)

sexo = tk.StringVar()
sexo.set('masculino')

masculino_btn = tk.Radiobutton(sexo_btn_frame, text='Masculino', font=('bold', 12), variable=sexo, value='masculino')
masculino_btn.pack(side=tk.LEFT)

feminino_btn = tk.Radiobutton(sexo_btn_frame, text='Feminino', font=('bold', 12), variable=sexo, value='feminino')
feminino_btn.pack(side=tk.LEFT)

sexo_btn_frame.grid(row=3, column=1)


telefone_lbl = tk.Label(formulario_frame, text='Telefone Usuário:', font=('bold', 12))
telefone_lbl.grid(row=4, column=0, sticky=tk.W, pady=2)

telefone = tk.Entry(formulario_frame, font=('bold', 12))
telefone.grid(row=4, column=1)

endereco_lbl = tk.Label(formulario_frame, text='Endereço Usuário:', font=('bold', 12))
endereco_lbl.grid(row=5, column=0, sticky=tk.W, pady=2)

endereco = tk.Entry(formulario_frame, font=('bold', 12))
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


root.mainloop()
