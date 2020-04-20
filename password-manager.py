import sqlite3

SENHA_MESTRE = '123'

senha = input('Insira a senha mestre: ')
if senha != SENHA_MESTRE:
    print('\nSenha incorreta! Encerrando...\n')
    exit(42)

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
); 
''')


def show_services():
    cursor.execute('''SELECT service FROM users;''')
    for service in cursor.fetchall():
        print(service)


def insert_password(service, username, password):
    cursor.execute(f'''
    INSERT INTO users (service, username, password) 
    VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()


def get_password(service):
    cursor.execute(f'''SELECT username, password FROM users
    WHERE service = '{service}'
''')

    if cursor.rowcount == 0:
        print('Serviço não cadastrado. Use "L" para listar os serviços disponíveis.')
    else:
        for user in cursor.fetchall():
            print(user)


def menu():
    print('\n*******************************')
    print('-> I: Inserir novo serviço.')
    print('-> L: Listar serviços salvos.')
    print('-> R: Recuperar senha.')
    print('-> S: Sair.')
    print('*******************************\n')


while True:
    menu()
    op = input('O que deseja fazer??\n')
    op = op.upper()

    if op not in 'ILRS':
        print('Opção inválida.')
        continue

    if op == 'S':
        break

    if op == 'I':
        service = input('Qual o nome do serviço?\n')
        username = input('Qual o nome do usuário?\n')
        password = input('Qual a senha?\n')
        insert_password(service, username, password)

    if op == 'L':
        show_services()

    if op == 'R':
        service = input('De qual serviço deseja recuperar a senha?\n')
        get_password(service)

conn.close()
