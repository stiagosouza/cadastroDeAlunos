import sqlite3 #Importação da biblioteca SQL

#criando coneção

try:
    conexao = sqlite3.connect('alunos.db')
    print('Conexão realizada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao conectar ao Banco de Dados',e)

#Table de curso

try:
    with conexao:
        curso = conexao.cursor()
        curso.execute("""  CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            turno TEXT   
        ) """)
        print ('Tabela criada com sucesso!!')
    
except sqlite3.Error as e:
    print('Erro ao criar a tabela Curso',e)

#criando coneção
try:
    conexao = sqlite3.connect('alunos.db')
    print('Conexão realizada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao conectar ao Banco de Dados',e)



#Tabela de alunos

try:
    with conexao:
        curso = conexao.cursor()
        curso.execute(""" CREATE TABLE IF NOT EXISTS alunos (
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            nascimento DATE NOT NULL,
            sexo TEXT NOT NULL,
            curso TEXT NOT NULL,
            idade INTEGER NOT NULL,
            av1 REAL NOT NULL,
            av2 REAL NOT NULL,
            media REAL NOT NULL,
            FOREIGN KEY (curso) REFERENCES cursos (nome) ON DELETE CASCADE
        ) """)
        print ('Tabela criada com sucesso!!')
    
except sqlite3.Error as e:
    print('Erro ao criar a tabela Alunos',e)
