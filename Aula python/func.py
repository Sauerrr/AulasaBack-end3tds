def login(nome, senha):
    if nome == 'maria' and senha == 'db':
        return f'pode ficar para sempre {nome}'

print(login('maria', 'db'))