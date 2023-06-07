# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

# importando pillow
from PIL import ImageTk, Image

#importando  query de cursos da aba query.py
from query import criarCursos
from query import verCurso
from query import atualizarCursos
from query import deletCursos

#importando  query de alunos da aba query.py
from query import criarAlunos
from query import ver_alunos
from query import atualizarAlunos
from query import deletAlunos


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#038cfc"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Criando janela
janela = Tk()
janela.title("Registro de Alunos")
janela.geometry('850x620')
janela.iconbitmap('imagens/logo.ico')
janela.configure(background=co2)
janela.resizable(width=FALSE, height=FALSE) # faz com a janela fique fixada no tamanho defenido

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co0)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co2)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co2)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co2)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

# trabalhando logo no cabeçalho-------
logoEstacio = Image.open('imagens/graduating-student.png')
logoEstacio = logoEstacio.resize((50,50))
logoEstacio = ImageTk.PhotoImage(logoEstacio)
nomeEstacio = Label(frame_logo, image=logoEstacio, text="Cadastro de Alunos",width =850,compound=LEFT,relief=RAISED, anchor=NW, font=('arial black', 18),bg=co0,fg=co1)
nomeEstacio.place(x=0 , y= 0)

 #Função para cadstro de alunos
def alunos():
    frame_tabela_aluno = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_aluno.grid(row=0,column=2,pady=0,padx=0,sticky=NSEW)

#comando query para inserir as informções das disciplinas na tabela------------------------  

#Função criar
    def criar_aluno():

        cpf = cpfAluno.get()
        nome = nomeAluno.get()
        nascimento = dateAluno.get()
        sexo = sexoAluno .get()
        curso = cursoAluno.get()
        idade = idadeAluno.get()
        av1 = float(av1Aluno.get())
        av2 = float(av2Aluno.get())
        media = float(av1 + av2) /2

        list = [cpf,nome,nascimento,sexo,curso,idade,av1,av2,media]

    #verificando  os valores se estão vazios
        for i in list:
            if i =="":
                messagebox.showerror(' Erro', 'Preencha todos os campos')
                return
    # inserindo os dados aluno 

        criarAlunos(list)
        messagebox.showinfo(' Sucesso', ' Os dados foram  inseridos com sucesso!!')

        cpfAluno.delete(0,END)
        nomeAluno.delete(0,END)
        dateAluno.delete(0,END)
        sexoAluno.delete(0,END)
        cursoAluno.delete(0,END)
        idadeAluno.delete(0,END)
        av1Aluno.delete(0,END)
        av2Aluno.delete(0,END)
        mediaAluno.delete(0,END)

        

        mostrar_aluno()

    #Funçao atualizar
    def atualizando_aluno():

        try:
            tree_iten = tree_aluno.focus()
            tree_dicionario =tree_aluno.item(tree_iten)
            tree_lista = tree_dicionario['values']
            valor_id = tree_lista[0]

                #inserindo os valores atualizdo nas entry
            
            cpfAluno.insert(0,tree_lista[0])
            nomeAluno.insert(0,tree_lista[1])
            dateAluno.insert(0,tree_lista[2])
            sexoAluno.insert(0,tree_lista[3])
            cursoAluno.insert(0,tree_lista[4])
            idadeAluno.insert(0,tree_lista[5])
            av1Aluno.insert(0,tree_lista[6])
            av2Aluno.insert(0,tree_lista[7])
            mediaAluno.insert(0,tree_lista[8])
                #função atualiza
            def update():
                
                nome = nomeAluno.get()
                cpf = cpfAluno.get()
                nascimento = dateAluno.get()
                sexo = sexoAluno .get()
                curso = cursoAluno.get()
                idade = idadeAluno.get()
                av1 = float(av1Aluno.get())
                av2 = float(av2Aluno.get())
                media = (av1 + av2) /2

                list = [cpf,nome,nascimento,sexo,curso,idade,av1,av2,media,valor_id]

            #verificando  os valores se estão vazios
                for i in list:
                    if i =="":
                        messagebox.showerror(' Erro', 'Preencha todos os campos')
                        return
            # inserindo  od=s dados Disciplina 

                atualizarAlunos(list)
                messagebox.showinfo(' SUCESSO', 'Os dados foram atualizados com sucesso!!')

                nomeAluno.delete(0,END)
                cpfAluno.delete(0,END)
                dateAluno.delete(0,END)
                sexoAluno.delete(0,END)
                cursoAluno.delete(0,END)
                idadeAluno.delete(0,END)
                av1Aluno.delete(0,END)
                av2Aluno.delete(0,END)
                mediaAluno.delete(0,END)

                mostrar_aluno()
                botao_salvar.destroy()

            botao_salvar =Button(frame_detalhes,command=update, anchor=CENTER, text='Salvar atualizaçao'.upper(),width=25,overrelief=RIDGE,font=('Ivy 7'),bg=co6,fg=co1)
            botao_salvar.place(x=250,y=170) 

        except IndexError:
            messagebox.showerror('ERRO\n','Selecione o aluno na tabela que deseja atualizar,\n         atualize a informção desejada\nem seguida  clique am Salvar atualização ')

    #Função deletar
    def deletar_aluno():

        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario =tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']
            valor_id = tree_lista[0]

            #Deletar os valoresdo banco de dados
            deletAlunos([valor_id])
            messagebox.showinfo(' SUCESSO', 'dados foram deletados com sucesso!!')

            mostrar_aluno()
        except IndexError:
            messagebox.showerror('ERRO\n','Selecione o aluno na tabela que deseja deletar,\n nem seguida  clique em Excluir')

    def listar_aluno():
        window = Toplevel()
        window.title('Lista de Alunos')
        window.iconbitmap('imagens/logo.ico')
        window.geometry('850x620')
        window.resizable(width=FALSE, height=FALSE)

        style.configure("Custom.Treeview",
                    background=co3,
                    foreground=co1,
                    fieldbackground=co3)
        style.map("Custom.Treeview",
                background=[('selected', co4)],
                foreground=[('selected', co1)])

        tree_aluno = ttk.Treeview(window, columns= ['CPF', 'Nome', 'Nascimento', 'Sexo', 'Curso', 'Idade', 'AV1', 'AV2', 'Média'], show="headings", style="Custom.Treeview")
        
        tree_aluno.heading('#0', text='', anchor=CENTER,)
        tree_aluno.column('#0', anchor=CENTER, width=0)
        tree_aluno.heading('CPF', text='CPF', anchor=CENTER)
        tree_aluno.column('CPF', anchor=CENTER, width=80)
        tree_aluno.heading('Nome', text='Nome', anchor=CENTER)
        tree_aluno.column('Nome', anchor=CENTER, width=150)
        tree_aluno.heading('Nascimento', text='Nascimento', anchor=CENTER)
        tree_aluno.column('Nascimento', anchor=CENTER, width=80)
        tree_aluno.heading('Sexo', text='Sexo', anchor=CENTER)
        tree_aluno.column('Sexo', anchor=CENTER, width=60)
        tree_aluno.heading('Curso', text='Curso', anchor=CENTER)
        tree_aluno.column('Curso', anchor=CENTER, width=100)
        tree_aluno.heading('Idade', text='Idade', anchor=CENTER)
        tree_aluno.column('Idade', anchor=CENTER, width=50)
        tree_aluno.heading('AV1', text='AV1', anchor=CENTER)
        tree_aluno.column('AV1', anchor=CENTER, width=50)
        tree_aluno.heading('AV2', text='AV2', anchor=CENTER)
        tree_aluno.column('AV2', anchor=CENTER, width=50)
        tree_aluno.heading('Média', text='Média', anchor=CENTER)
        tree_aluno.column('Média', anchor=CENTER, width=50)
        tree_aluno.pack(fill=BOTH, expand=1)

        alunos = ver_alunos()
        for aluno in alunos:
            tree_aluno.insert('', 'end', values=aluno)

        window.mainloop()

#CAMPO NOME DO ALUNO
    nome =Label(frame_detalhes,text='Nome do Aluno*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    nome.place(x=4,y=10)
    nomeAluno = Entry(frame_detalhes,width=50,justify='left',relief='solid')
    nomeAluno.place(x=4,y=35)

#CAMPO CPF DO ALUNO
    cpf =Label(frame_detalhes,text='CPF*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    cpf.place(x=4,y=60)
    cpfAluno = Entry(frame_detalhes,width=25,justify='left',relief='solid')
    cpfAluno.place(x=4,y=85)

#CAMPO NACIMENTO DO ALUNO
    date =Label(frame_detalhes,text='Nascimento*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    date.place(x=4,y=110)
    dateAluno = DateEntry(frame_detalhes,width=10, bg=co2 ,fg=co1, borderwidth=2, year=2000, month=1, day=1)
    dateAluno.place(width=80,x=4,y=135)

#CAMPO GENERO  DO ALUNO 
  
    sexo =Label(frame_detalhes,text='Sexo*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    sexo.place(x=124,y=110)
    sexoAluno = ttk.Combobox(frame_detalhes,values=["Masculino","Feminino"],width=10,font=('Ivy 11'))
    sexoAluno.place(x=124,y=135)

#CAMPO CURSO  DO ALUNO

    nome =Label(frame_detalhes,text='Diciplina*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    nome.place(x=250,y=110)

    nomecursos = ['python','java','C++']
    nomecurso = []

    for i in nomecursos:
        nomecurso.append(i)

    cursoAluno =  ttk.Combobox(frame_detalhes, width=10,font=('Ivy 11'))
    cursoAluno['values'] =(nomecurso)
    cursoAluno.place(x=250,y=135)
#CAMPO IDADE DO ALUNO
    nome =Label(frame_detalhes,text='Idade*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    nome.place(x=220,y=60)
    idadeAluno = Entry(frame_detalhes,width=10,justify='left',relief='solid')
    idadeAluno.place(x=220,y=85)

#CAMPO NOTA AV1 DO ALUNO
    nota =Label(frame_detalhes,text='Av1*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    nota.place(x=390,y=10)
    av1Aluno = Entry(frame_detalhes,width=10,justify='left',relief='solid')
    av1Aluno.place(x=390,y=35)

#CAMPO NOTA AV2 DO ALUNO
    nota =Label(frame_detalhes,text='Av2*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    nota.place(x=390,y=60)
    av2Aluno = Entry(frame_detalhes,width=10,justify='left',relief='solid')
    av2Aluno.place(x=390,y=85)

#CAMPO MEDIA FINAL  DO ALUNO
    nota =Label(frame_detalhes,text='Média',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    nota.place(x=390,y=110)
    mediaAluno = Entry(frame_detalhes,width=10,justify='left',relief='solid')
    mediaAluno.place(x=390,y=135)
                      
    
    #INSERINDO OS BOTÕES

#botão salvar
    botao_carregar =Button(frame_detalhes, command=criar_aluno, anchor=CENTER, text='Salvar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7'),bg=co3,fg=co1)
    botao_carregar.place(x=490,y=90)

#botão atualizar
    botao_atualiza =Button(frame_detalhes, command=atualizando_aluno, anchor=CENTER, text='Atualizar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7'),bg=co6,fg=co1)
    botao_atualiza.place(x=490,y=120)

#botão excluir
    botao_deletar =Button(frame_detalhes, command=deletar_aluno, anchor=CENTER, text='Excluir'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7'),bg=co7,fg=co1)
    botao_deletar.place(x=490,y=150)

#botão buscar  
    botao_procurar =Button(frame_detalhes,command= listar_aluno, text='Buscar Alunos',width =20,compound=LEFT,overrelief=RIDGE,font=('arial', 9),bg=co1,fg=co0)
    botao_procurar.place(x=515,y=40)

# Tabela Cursos
    def mostrar_aluno():
        app_nome = Label(frame_tabela_aluno, text="Tabela de Alunos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 15 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=320, pady=10, sticky=NSEW)

# criando a treeview com dual scrollbars
        list_header = ['CPF','NOME','NASCIMENTO','SEXO','CURSO','IDADE','AV1','AV2','MÉDIA']

        df_list = ver_alunos()

        global tree_aluno

        tree_aluno = ttk.Treeview(frame_tabela_aluno, selectmode="extended",columns=list_header, show="headings")

# vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_aluno, orient="vertical", command=tree_aluno.yview)

# horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_aluno, orient="horizontal", command=tree_aluno.xview)

        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')#barra de rolagem vertical
        hsb.grid(column=0, row=2, sticky='ew')#barra de rolagem horizontal
        frame_tabela_aluno.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","center","center","center","center","center","center"]
        h=[20,80,80,70,70,70,30,30,30]
        n=0

        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor=NW)
            # ajuste a largura da coluna para a string do cabeçalho
            tree_aluno.column(col, width=h[n],anchor=hd[n])

        n+=1

        for item in df_list:
            tree_aluno.insert('', 'end', values=item)

    mostrar_aluno()  


#linha separatoria-----------------------------------
    linha = Label(frame_detalhes,relief=GROOVE,text='h',width=1,height=100,anchor=NW,font=('Ivy 1'),bg=co0,fg=co0)
    linha.place(x=470, y=10)

    linha = Label(frame_detalhes,relief=GROOVE,text='h',width=1,height=100,anchor=NW,font=('Ivy 1'),bg=co1,fg= co0)
    linha.place(x=468, y=10)

    #CAMPO NOME DO ALUNO
    procura_nome =Label(frame_detalhes,text='LISTAR ALUNOS CADASTRADOS',height=1,anchor=NW,font=('Ivy 13'),bg=co2,fg=co4)
    procura_nome.place(x=490,y=10)
   

#função para adicionar cursos  
def adicionar():
# Criando Frames para tabelas-----
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0,column=0,pady=0,padx=0,sticky=NSEW)

#comando query para inserir as informções das disciplinas na tabela------------------------  

#Função criar
    def criar_disciplina():
        nomeC = nomeCurso.get()
        turno = turnoCurso.get()

        list = [nomeC,turno]

#verificando  os valores se estão vazios
        for i in list:
            if i =="":
                messagebox.showerror(' Erro', 'Preencha todos os campos')
                return
# inserindo os dados Disciplina 

        criarCursos(list)
        messagebox.showinfo(' Sucesso', ' Os dados foram  inseridos com sucesso!!')

        nomeCurso.delete(0,END)
        turnoCurso.delete(0,END)

        mostrar_cursos()

#Funçao atualizar
    def atualizando_curso():

        try:
            tree_itens = tree_curso.focus()
            tree_dicionario =tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']
            valor_id = tree_lista[0]

             #inserindo os valores atualizdo nas entry
            nomeCurso.insert(0,tree_lista[1])
            turnoCurso.insert(0,tree_lista[2])
                #função atualiza
            def update():
                nomeC = nomeCurso.get()
                turno = turnoCurso.get()

                list = [nomeC,turno,valor_id]

            #verificando  os valores se estão vazios
                for i in list:
                    if i =="":
                        messagebox.showerror(' Erro', 'Preencha todos os campos')
                        return
            # inserindo  od=s dados Disciplina 

                atualizarCursos(list)
                messagebox.showinfo(' SUCESSO', 'Os dados foram atualizados com sucesso!!')

                nomeCurso.delete(0,END)
                turnoCurso.delete(0,END)

                mostrar_cursos()
                botao_salvar.destroy()

            botao_salvar =Button(frame_detalhes,command=update, anchor=CENTER, text='Salvar atualizaçao'.upper(),width=25,overrelief=RIDGE,font=('Ivy 7'),bg=co6,fg=co1)
            botao_salvar.place(x=160,y=100) 
        except IndexError:
            messagebox.showerror('ERRO\n','Selecione o curso na tabela que deseja atualizar,\n         atualize a informção desejada\nem seguida  clique am Salvar atualização ')

#Função deletar
    def deletar_curso():

        try:
            tree_itens = tree_curso.focus()
            tree_dicionario =tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']
            valor_id = tree_lista[0]

            #Deletar os valoresdo banco de dados
            deletCursos([valor_id])
            messagebox.showinfo(' SUCESSO', 'dados foram deletados com sucesso!!')

            mostrar_cursos()
        except IndexError:
            messagebox.showerror('ERRO\n','Selecione o curso na tabela que deseja deletar,\n nem seguida  clique em Excluir')
#detalhes de cursos------------------------- 

#CAMPO NOME DA DISCIPLINA
   
    nome =Label(frame_detalhes,text='Disciplina*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    nome.place(x=4,y=10)
    disciplanas = ['python','java','C++']
    disciplana = []

    for i in disciplanas:
        disciplana.append(i)

    nomeCurso =  ttk.Combobox(frame_detalhes,width=15,font=('Ivy 11'))
    nomeCurso ['values'] = (disciplana)
    nomeCurso.place(x=7,y=40)

#CAMPO TURNO
    turnoA =Label(frame_detalhes,text='Turno*',height=1,anchor=NW,font=('Ivy 11'),bg=co2,fg=co4)
    turnoA.place(x=4,y=70)
    turnoCurso = ttk.Combobox(frame_detalhes,values=["Manhã","Tarde","Noite"],width=10,font=('Ivy 11'))
    turnoCurso.place(x=7,y=100)

#INSERINDO OS BOTÕES
    botao_carregar =Button(frame_detalhes, command=criar_disciplina, anchor=CENTER, text='Salvar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7'),bg=co3,fg=co1)
    botao_carregar.place(x=4,y=160)

    botao_atualiza =Button(frame_detalhes, command=atualizando_curso, anchor=CENTER, text='Atualizar'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7'),bg=co6,fg=co1)
    botao_atualiza.place(x=80,y=160)

    botao_deletar =Button(frame_detalhes,command=deletar_curso, anchor=CENTER, text='Excluir'.upper(),width=10,overrelief=RIDGE,font=('Ivy 7'),bg=co7,fg=co1)
    botao_deletar.place(x=160,y=160)   
    
# Tabela Cursos
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 15 bold'), bg=co2, fg=co4)
        app_nome.grid(row=0, column=0, padx=80, pady=10, sticky=NSEW)

# criando a treeview com dual scrollbars
        list_header = ['ID','Curso','Turno'] # listagem da tabela de cursos

        df_list = verCurso() # condição para vizualizar as disciplinas na tabela de cursos

        global tree_curso

        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended",columns=list_header, show="headings")

# vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
# horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)

        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')#barra de rolagem vertical
        hsb.grid(column=0, row=2, sticky='ew')#barra de rolagem horizontal
        frame_tabela_curso.grid_rowconfigure(0, weight=12)

        hd=["nw","w","nw"]
        h=[20,80,60]
        n=0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)

            # ajusta a largura da coluna para a string do cabeçalho
            tree_curso.column(col, width=h[n],anchor=hd[n])

        n+=1

        for item in df_list:
            tree_curso.insert('', 'end', values=item)

    mostrar_cursos()

    
#Função para salvar
def salvar():
    print('Salvar')




#funções
def control(i):
   
    if i == 'Cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

            #chamando a função aluno
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

            #chamando a função adicionar
        adicionar()

    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

            #chamando a função salvar
        salvar()    

#adicionando os botoes

img_cadastro = Image.open('imagens/adicionar.png')
img_cadastro = img_cadastro.resize((18,18))   #tamanho da imagem a ser mostrada
img_cadastro = ImageTk.PhotoImage(img_cadastro)
button_cadastro = Button(frame_dados,command=lambda:control('Cadastro'),image=img_cadastro, text="Aluno",width =100,compound=LEFT,overrelief=RIDGE,font=('arial', 12),bg=co1,fg=co0)
button_cadastro.place(x=10, y=30)
# Executando a janela

img_adicionar = Image.open('imagens/adicionar.png')
img_adicionar = img_adicionar.resize((18,18))   #tamanho da imagem a ser mostrada
img_adicionar = ImageTk.PhotoImage(img_adicionar)
button_adicionar = Button(frame_dados,command=lambda:control('adicionar'),image=img_adicionar, text="Curso",width =100,compound=LEFT,overrelief=RIDGE,font=('arial', 12),bg=co1,fg=co0)
button_adicionar.place(x=130, y=30)

img_salvar = Image.open('imagens/salvar.png')
img_salvar = img_salvar.resize((18,18))   #tamanho da imagem a ser mostrada
img_salvar = ImageTk.PhotoImage(img_salvar)
button_salvar = Button(frame_dados,command=lambda:control('salvar'),image=img_salvar, text="Salvar",width =100,compound=LEFT,overrelief=RIDGE,font=('arial', 12),bg=co1,fg=co0)
button_salvar.place(x=250, y=30)

janela.mainloop()