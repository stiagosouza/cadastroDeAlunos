import sqlite3 #Importação da biblioteca SQL

#criando coneção

try:
    conexao = sqlite3.connect('alunos.db')
    print('Conexão realizada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao conectar ao Banco de Dados',e)

#comandos para inseriar os alunos a tabela cursos------------------------------------------

    #criar cursos (Insert)
def criarCursos(i):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO cursos (nome, turno) VALUES (?,?)"
        cursor.execute(query,i)

#Listar cursos(Select S)
def verCurso():
    list = []
    with conexao:
        cursor =conexao.cursor()
        cursor.execute('SELECT * FROM cursos')
        linha = cursor.fetchall()

        for i in linha:
            list.append(i)
    return list


#atualizar Cursos(Update U)
def atualizarCursos(i):
    with conexao:
        cursor = conexao.cursor()
        query = "UPDATE cursos SET  nome=?, turno =? WHERE id=?"
        cursor.execute(query,i)

#deletar Cursos(Delete D)
def deletCursos(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM cursos WHERE id=?"
        cursor.execute(query,i)


#comandos para inseriar os alunos a tabela alunos------------------------------------------

def criarAlunos(i):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO alunos(cpf,nome,nascimento,sexo,curso,idade,av1,av2,media) VALUES (?,?,?,?,?,?,?,?,?)"
        cursor.execute(query,i)

#Listar cursos(Select S)
def ver_alunos():
    lista = []
    with conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM alunos')
        linhas = cursor.fetchall()

        for linha in linhas:
            lista.append(linha)
    return lista

#atualizar Cursos(Update U)
def atualizarAlunos(i):
    with conexao:
        cursor = conexao.cursor()
        query = "UPDATE alunos SET cpf=?, nome=?,nascimento=?,sexo=?,curso=?,idade=?,av1=?,av2=?,media=? WHERE cpf=?"
        cursor.execute(query,i)

#deletar Cursos(Delete D)
def deletAlunos(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM alunos WHERE cpf=?"
        cursor.execute(query,i)