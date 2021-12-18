from mysql.connector import connect
from mysql.connector import ProgrammingError

from parametros import parametros as parametros

try:
    conexao = connect(**parametros)
    print(conexao)  # mostrar que deu certo, caso não tenha lana excessao

    cursor = conexao.cursor()
    """cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')

    cursor.execute('SHOW DATABASES')
    for i, database in enumerate(cursor, start=10):
        print(f'Banco de dados {i}: {database[0]}')

    sql = 'CREATE TABLE IF NOT EXISTS contatos (' + \
          'id INTEGER PRIMARY KEY,' + \
          'nome VARCHAR(50) UNIQUE NOT NULL,' + \
          'telefone CHAR(11)' + \
          ')'
    cursor.execute(sql)"""
    #sql = 'INSERT INTO contatos (id, nome, telefone) VALUES (%s,%s,%s)'
    #args = (40, 'Lucas', '1112456870')
    #cursor.execute(sql,args)
    """args = (
        (37, 'João', '11924574784'),
        (214, 'Maria', '11924574784'),
        (789456, 'Carlos', '11924574784'),
        (2, 'Ana', '11924574784'),
    )
    cursor.executemany(sql,args)
    conexao.commit()"""
    '''sql = 'SELECT * FROM contatos'
    cursor.execute(sql)
    contatos = cursor.fetchall()
    for contato in contatos:
        print(f'{contato[0]:6d}')
    
    sql = 'SELECT nome, telefone FROM contatos'
    cursor.execute(sql)
    for nome, telefone in cursor.fetchall():
        print(f'{nome:6s} {telefone:11s}')'''
        #print('\t'.join(str(campo) for campo in contato))

    sql = 'SELECT telefone, nome FROM contatos WHERE nome LIKE "%a%" ORDER BY telefone, nome'
    cursor.execute(sql)
    resgistro = cursor.fetchone()
    while resgistro:
        print(resgistro)
        resgistro = cursor.fetchone()
except ProgrammingError as error:
    print(f'ERRO!\n{error.msg}')
else:
    print(f'{cursor.rowcount} linhas foram alteradas!')
finally:
    if(conexao and conexao.is_connected()):
        conexao.close()
        print('Fechou')

class Teste:
    def __end__(self):
        print('Morreu')

t = Teste()
