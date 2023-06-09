from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class crud():
    def __init__(self):
        # Configuracoes da janela
        self.root = Tk()
        self.root.title("CRUD ALUNOS")
        self.root.geometry(self.center(self.root,650,500))
        
        self.root.config(bg="black")
        self.root.resizable(False, False)
        
        # Variaveis de iniciais
        self.img_btn_add = PhotoImage(file=r'img\btn_add.png')
        self.img_btn_refresh = PhotoImage(file=r'img\btn_refresh.png')
        self.img_btn_delete = PhotoImage(file=r'img\btn_delete.png')
        self.var_id = StringVar()
        self.var_id.set('?')
        
        self.containers()
        self.itens_container01()
        self.itens_container02()
        self.preencher_tabela()
        self.ajustar_colunas()
        # Inicializacao da janela
        self.root.mainloop()
        
    def containers(self):
        self.fr_container01 = Frame(
            self.root,
            height=200,
            width=650,
            bg='#3d4957'
        )
            
        self.fr_container02 = Frame(
            self.root,
            height=300, 
            width=650,
            bg="#eef2f5"
        )
              
        self.fr_container01.propagate(0)
        self.fr_container02.propagate(0)
        self.fr_container01.pack()
        self.fr_container02.pack()
    
    def itens_container01(self):
        self.fr_container_logo = Frame(
            self.fr_container01,
            bg=self.fr_container01.cget("bg")
        )
        
        self.fr_container_infos_user = Frame(
            self.fr_container01,
            bg=self.fr_container01.cget("bg")
        )
        
        self.fr_container_buttons = Frame(
            self.fr_container01,
            bg=self.fr_container01.cget("bg")
        )
        
        #Itens container logo
        self.lb_img_logo = Label(
            self.fr_container_logo,
            # image=self.img_logo_linklooter,
            text='Sistema de cadastro de alunos',
            font='Calibri 19 bold',
            fg='#ffd546',
            bg=self.fr_container01.cget("bg"),
        )
        
        #Itens container info user
        # ID
        self.lb_id_aluno = Label(
            self.fr_container_infos_user,
            text='Id do aluno:',
            font='Calibri 11 bold',
            fg='white',
            bg=self.fr_container_infos_user.cget('bg')
        )
        
        self.lb_id_aluno_value = Label(
            self.fr_container_infos_user,
            textvariable=self.var_id,
            font='Calibri 11 bold',
            fg='white',
            bg=self.fr_container_infos_user.cget('bg')
        )
        
        # Nome
        self.lb_nome_aluno = Label(
            self.fr_container_infos_user,
            text='Nome do aluno:',
            font='Calibri 11 bold',
            fg='white',
            bg=self.fr_container_infos_user.cget('bg')
        )
       
        self.en_nome_aluno = Entry(
            self.fr_container_infos_user,
            width=30,
            font='Calibri 11',
            bd=0,
            fg='white',
            insertbackground="white",
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor='#ffd444',
            bg=self.fr_container_infos_user.cget('bg')
        )
        
        # Email
        self.lb_email_aluno = Label(
            self.fr_container_infos_user,
            text='Email do aluno:',
            font='Calibri 11 bold',
            fg='white',
            bg=self.fr_container_infos_user.cget('bg')
        )
       
        self.en_email_aluno = Entry(
            self.fr_container_infos_user,
            width=30,
            font='Calibri 11',
            bd=0,
            fg='white',
            insertbackground="white",
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor='#ffd444',
            bg=self.fr_container_infos_user.cget('bg')
        )
        
        # Curso
        self.lb_curso_aluno = Label(
            self.fr_container_infos_user,
            text='Curso:',
            font='Calibri 11 bold',
            fg='white',
            bg=self.fr_container_infos_user.cget('bg')
        )
       
        self.en_curso_aluno = Entry(
            self.fr_container_infos_user,
            width=30,
            font='Calibri 11',
            bd=0,
            fg='white',
            insertbackground="white",
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor='#ffd444',
            bg=self.fr_container_infos_user.cget('bg')
        )
        
        # Valor
        self.lb_valor_aluno = Label(
            self.fr_container_infos_user,
            text='Valor do curso:',
            font='Calibri 11 bold',
            fg='white',
            bg=self.fr_container_infos_user.cget('bg')
        )
       
        self.en_valor_aluno = Entry(
            self.fr_container_infos_user,
            width=30,
            font='Calibri 11',
            bd=0,
            fg='white',
            insertbackground="white",
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor='#ffd444',
            bg=self.fr_container_infos_user.cget('bg')
        )
        
        #Itens container Botões
        self.btn_adicionar = Button(
            self.fr_container_buttons,
            image=self.img_btn_add,
            activebackground=self.fr_container01.cget("bg"),
            bg=self.fr_container01.cget("bg"),
            bd=0,
            cursor="hand2",
            command=self.adicionar_registro
        )
        
        self.btn_atualizar_registros = Button(
            self.fr_container_buttons,
            image=self.img_btn_refresh,
            activebackground=self.fr_container01.cget("bg"),
            bg=self.fr_container01.cget("bg"),
            bd=0,
            cursor="hand2",
            command=self.update_registro
        )
        
        self.btn_deletar_registros = Button(
            self.fr_container_buttons,
            image=self.img_btn_delete,
            bg=self.fr_container01.cget("bg"),
            activebackground=self.fr_container01.cget("bg"),
            bd=0,
            cursor="hand2",
            command=self.excluir_registro
        )
        
        # Posicionando containers
        
        self.fr_container_logo.pack(anchor=W)
        self.fr_container_infos_user.pack(anchor=W)
        self.fr_container_buttons.pack(anchor=W,padx=215, pady=5)
        
        # Posicionando itens container logo
        self.lb_img_logo.pack()
        
        #posicionando itens container infos
        self.lb_id_aluno.grid(row=0, column=0, sticky=W)
        self.lb_id_aluno_value.grid(row=0, column=1, sticky=W)
        
        self.lb_nome_aluno.grid(row=2, column=0, sticky=W)
        self.en_nome_aluno.grid(row=2, column=1, sticky=W)
        
        self.lb_email_aluno.grid(row=3, column=0, sticky=W)
        self.en_email_aluno.grid(row=3, column=1, sticky=W)
        
        self.lb_curso_aluno.grid(row=4, column=0, sticky=W)
        self.en_curso_aluno.grid(row=4, column=1, sticky=W)
        
        self.lb_valor_aluno.grid(row=5, column=0, sticky=W)
        self.en_valor_aluno.grid(row=5, column=1, sticky=W)
        
        # Posicionando itens container buttons
        self.btn_adicionar.grid(row=0, column=0, sticky=W)
        self.btn_atualizar_registros.grid(row=0, column=1, sticky=W)
        self.btn_deletar_registros.grid(row=0, column=2, sticky=W)
    
    def itens_container02(self):
        self.treeview = ttk.Treeview(
            self.fr_container02,
            columns=('id','nome','email','curso','valor_curso'),
            show='headings'
        )
        
        self.treeview.heading('id', text='ID')
        self.treeview.heading('nome', text='Nome')
        self.treeview.heading('email', text='Email')
        self.treeview.heading('curso', text='Curso')
        self.treeview.heading('valor_curso', text='Valor do Curso')
        
        self.treeview.bind('<Double-1>', self.captar_registros)
        
        self.treeview.pack(fill='both', expand=True,padx=10, pady=10)
        
    def preencher_tabela(self):
        registros = self.atualiza_tabela()
        
        # Limpar a tabela existente na janela
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        # Preencher a tabela com os novos registros
        for registro in registros:
            if registro == None:
                print(registro)
            self.treeview.insert("", "end", values=registro)
            
        self.ajustar_colunas()
       
    def atualiza_tabela(self):
        try:
            # Conectar ao banco de dados
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123root.',
                database='crud'
            )

            # Selecionar todos os registros da tabela "Usuarios"
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM aluno")
            registros = cursor.fetchall()
            cursor.close()
            conexao.close()
            # Retornar os registros encontrados
            return registros
        
        except:
            print("Erro ao conectar ou listar registros")
    
    def adicionar_registro(self):

        if self.var_id.get() == '?':
            if self.validar_entry() == True:
                try:
                    
                    # Conectar ao banco de dados
                    conexao = mysql.connector.connect(
                        host='localhost',
                        user='SEU_USUARIO',
                        password='SUA_SENHA',
                        database='crud'
                    )
                    
                    nome = self.en_nome_aluno.get()
                    email = self.en_email_aluno.get()
                    curso = self.en_curso_aluno.get()
                    valor = self.en_valor_aluno.get()
                    
                    query = f"INSERT INTO aluno (nome, email, curso, valor) VALUES ('{nome}','{email}', '{curso}', '{valor}')"
                    
                    cursor = conexao.cursor()
                    cursor.execute(query)
                    
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    
                    self.resetar_entrys()
                    self.preencher_tabela()
                    
                except:
                    print("Erro ao conectar com servidor")
            else:
                messagebox.showinfo("","Existem campos vazios por favor preencha")
        else:
            confirmed = messagebox.askyesno("Confirmação", "Existe um outro registro selecionado!\nDeseja que limpe os campos para adicionar um novo registro?")
            if confirmed:
                self.resetar_entrys()
            else:
                pass
            
    def update_registro(self):
        id_aluno = self.var_id.get()
        
        if id_aluno != '?':
            confirmed = messagebox.askyesno("Confirmação", "Deseja atualizar registro?")
            if confirmed:
            
                try:
                    # Conectar ao banco de dados
                    conexao = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='123root.',
                        database='crud'
                    )
                    nome = self.en_nome_aluno.get()
                    email = self.en_email_aluno.get()
                    curso = self.en_curso_aluno.get()
                    valor = self.en_valor_aluno.get()
                    
                    cursor = conexao.cursor()
                    
                    query = f"UPDATE aluno SET nome = '{nome}', email = '{email}', curso = '{curso}', valor = '{valor}' WHERE id = {id_aluno}"
                    cursor.execute(query)
                    
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    
                    messagebox.showinfo("",f"Registro {id_aluno} Atualizado com sucesso!")
                    
                    self.resetar_entrys()
                    self.preencher_tabela()
                except:
                    print("Erro ao conectar ou listar registros")
            else:
                pass
        else:
            messagebox.showinfo("","Por favor selecione um registro para ser excluio")
            
    def excluir_registro(self):
        id_aluno = self.var_id.get()
        
        if id_aluno != '?':
            confirmed = messagebox.askyesno("Confirmação", "Deseja excluir registro?")
            if confirmed:
            
                try:
                    # Conectar ao banco de dados
                    conexao = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='123root.',
                        database='crud'
                    )

                    cursor = conexao.cursor()
                    
                    query = f"DELETE FROM aluno WHERE id = {id_aluno}"
                    cursor.execute(query)
                    
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    
                    messagebox.showinfo("",f"Registro {id_aluno} Excluido com sucesso!")
                    
                    self.resetar_entrys()
                    self.preencher_tabela()
                except:
                    print("Erro ao conectar ou listar registros")
            else:
                pass
        else:
            messagebox.showinfo("","Por favor selecione um registro para ser excluio")
    
    def validar_entry(self):
        campos = [self.en_nome_aluno.get(), self.en_email_aluno.get(), self.en_curso_aluno.get(), self.en_valor_aluno.get()]

        if all(campo.strip() for campo in campos):
            return True
        else:
            return False
    
    def resetar_entrys(self):
        #exclui valores das entrys
        self.en_nome_aluno.delete(0, 'end') 
        self.en_email_aluno.delete(0, 'end') 
        self.en_curso_aluno.delete(0, 'end') 
        self.en_valor_aluno.delete(0, 'end')
        self.var_id.set('?')
            
    def ajustar_colunas(self):
        registros = self.atualiza_tabela()
        if len(registros) != 0:
            last_item = self.treeview.get_children()[-1]
            last_item_id = self.treeview.index(last_item)
            # Calcula a largura necessária para cada coluna com base no conteúdo
            for col in self.treeview['columns']:
                max_width = max([len(str(self.treeview.set(row, col))) for row in self.treeview.get_children()])
                self.treeview.column(col, width=max_width * 10)
        
    def captar_registros(self, event):
        item = self.treeview.focus()
        self.valores = self.treeview.item(item, 'values')
        
        #exclui valores anteriores
        self.en_nome_aluno.delete(0, 'end') 
        self.en_email_aluno.delete(0, 'end') 
        self.en_curso_aluno.delete(0, 'end') 
        self.en_valor_aluno.delete(0, 'end') 
        
        # Incluindo valores nos campos 
        self.var_id.set(self.valores[0])
        self.en_nome_aluno.insert(0, self.valores[1]) 
        self.en_email_aluno.insert(0, self.valores[2]) 
        self.en_curso_aluno.insert(0, self.valores[3]) 
        self.en_valor_aluno.insert(0, self.valores[4]) 
           
    def center( self,janela, largura, altura):
        janela = janela
        largura = largura
        altura = altura
        largura_screen = janela.winfo_screenwidth()
        altura_screen = janela.winfo_screenheight()
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        centro = '%dx%d+%d+%d' % (largura, altura, posx, posy)
        return centro       

crud()