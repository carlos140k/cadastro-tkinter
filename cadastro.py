import tkinter as tk 


root = tk.Tk()
root.geometry('600x620')
root.title('Cadastro de Imagens')


frame_Principal = tk.Frame(root)

Cabecalho = tk.Label(frame_Principal, text='Cadastro de alunos com imagens', bg='orange', font=('bold', 18))
Cabecalho.pack(fill=tk.X)

img_frame = tk.Frame(frame_Principal)
img_padrao = tk.PhotoImage(file='aluno.png')
img_label = tk.Label(img_frame, image=img_padrao, bd=2, relief=tk.SOLID)
img_label.pack(side=tk.LEFT)
img_frame.pack(anchor=tk.W, pady=5)

frame_Principal.pack(anchor=tk.W, pady=5, padx=5)
frame_Principal.pack_propagate(False)
frame_Principal.configure(width=500, height=400, bg='green')


root.mainloop()
