# VAMOS COMPLETAR A INTERFACE GRÁFICA...
import sqlite3 # banco de dados
import tkinter as tk # interface basica
from tkinter import messagebox # caixas de mensagens
from tkinter import ttk # interface grafica tb
from PIL import Image, ImageTk # para adicionar imagem 
def conectar():
    return sqlite3.connect('teste.db')
# criar o banco 

def criar_tabela():
    conn = conectar()
    c= conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        endereco TEXT NOT NULL,
        telefone TEXT NOT NULL              
        )       
    ''')
    conn.commit()
    conn.close()

# CREATE
def inserir_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    cpf =  entry_cpf.get()
    endereco =  entry_endereco.get()
    telefone = entry_telefone.get()
    
    if nome and email and endereco and telefone:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(id, nome, email, endereco, telefone) VALUES(?,?,?,?,?)', (cpf, nome, email, endereco, telefone))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS COM SUCESSO!') 
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!') 

# READ
def mostrar_usuario():
    for row in tree.get_children():   
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1],usuario[2],usuario[3],usuario[4]))
    conn.close()    

# DELETE
def delete_usuario():
    dado_del = tree.selection()
    if dado_del:
       user_id = tree.item(dado_del)['values'][0]
       conn = conectar()
       c = conn.cursor()    
       c.execute('DELETE FROM usuarios WHERE id = ? ',(user_id,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()
    else:
       messagebox.showerror('', 'OCORREU UM ERRO')  

# UPDATE 
def editar():
     selecao = tree.selection()
     if selecao:
         user_id = tree.item(selecao)['values'][0]
         novo_nome = entry_nome.get()
         novo_email = entry_email.get()
         novo_endereco = entry_endereco.get()
         novo_telefone = entry_telefone.get()

         if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()    
            c.execute('UPDATE usuarios SET nome = ? , email = ? , endereco = ?, telefone = ? WHERE id = ? ',(novo_nome,novo_email,novo_endereco,novo_telefone,user_id))
            conn.commit()
            conn.close()  
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()
         else:
             messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')
     else:
            messagebox.showerror('','ALGO DEU ERRADO!')

# VAMOS COMPLETAR A INTERFACE GRÁFICA...

janela = tk.Tk()
janela.title('XYZ COMÉRCIO - Sistema de Cadastros')
janela.configure(bg="#e0e0e0")  # cor de fundo da janela

# Adicionar imagem 
imagem = Image.open("7891770.png")  # nome do arquivo da img
imagem = imagem.resize((100, 100))  # tamanho da img
img = ImageTk.PhotoImage(imagem)
label_img = tk.Label(janela, image=img, bg="#e0e0e0")  # adiciona img na janela 
label_img.pack(pady=10)  

frame_form = tk.Frame(janela, bg="#e0e0e0")  
frame_form.pack(pady=10)


label_nome = tk.Label(frame_form, text='Nome:', bg="#e0e0e0")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nome = tk.Entry(frame_form)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(frame_form, text='E-mail:', bg="#e0e0e0")
label_email.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(frame_form)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_endereco = tk.Label(frame_form, text='Endereço:', bg="#e0e0e0")
label_endereco.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_endereco = tk.Entry(frame_form)
entry_endereco.grid(row=2, column=1, padx=10, pady=5)

label_telefone = tk.Label(frame_form, text='Telefone:', bg="#e0e0e0")
label_telefone.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_telefone = tk.Entry(frame_form)
entry_telefone.grid(row=3, column=1, padx=10, pady=5)

label_cpf = tk.Label(frame_form, text='CPF:', bg="#e0e0e0")
label_cpf.grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_cpf = tk.Entry(frame_form)
entry_cpf.grid(row=4, column=1, padx=10, pady=5)


frame_botoes = tk.Frame(janela, bg="#e0e0e0")  
frame_botoes.pack(pady=10)

btn_salvar = tk.Button(frame_botoes, text='SALVAR',
                       bg="green", fg="white", font=("Arial", 12, "bold"), width=12, height=2, command=inserir_usuario)
btn_salvar.grid(row=0, column=0, padx=10)

btn_atualizar = tk.Button(frame_botoes, text='ATUALIZAR',
                          bg="blue", fg="white", font=("Arial", 12, "bold"), width=12, height=2, command=editar)
btn_atualizar.grid(row=0, column=1, padx=10)

btn_deletar = tk.Button(frame_botoes, text='DELETAR',
                        bg="red", fg="white", font=("Arial", 12, "bold"), width=12, height=2, command=delete_usuario)
btn_deletar.grid(row=0, column=2, padx=10)

# personalizaçao tabela
style = ttk.Style()
style.configure("Treeview", background="#f0f0f0", fieldbackground="#ffffff")  # cor cinza claro

frame_tabela = tk.Frame(janela)
frame_tabela.pack(pady=10)

# arvore
columns = ('ID','NOME', 'EMAIL', 'ENDEREÇO', 'TELEFONE')
tree = ttk.Treeview(frame_tabela, columns=columns, show='headings')
tree.pack()

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()

janela.mainloop()
