import sqlite3

# Função para exibir o resultado das consultas
def exibe_resultado_consulta(nome_exercicio, dados):
    print(f'Exibindo resultado do : {nome_exercicio}')
    for usuario in dados:
        print(usuario)
    print (' ') 

# Abre conexão com o banco de dados
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# Apagando as tabelas criadas durante o exercício, caso o programa já tenha sido executado anteriormente
cursor.execute('DROP TABLE IF EXISTS alunos')
cursor.execute('DROP TABLE IF EXISTS clientes')
cursor.execute('DROP TABLE IF EXISTS compras')

# EXERCICIO 1
# Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto),
# idade (inteiro) e curso (texto)
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# EXERCICIO 2 
# Insira pelo menos 5 registros de alunos na tablea que você criou no exercício anteior
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Isadora", 33, "Engenharia");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Maria", 48, "Nutrição");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "José", 20, "Letras");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Márcia",27, "Administração");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Antonio", 65, "Ciências da computação");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (6, "Carlos", 18, "Farmácia");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (7, "Romeu", 29, "Engenharia");')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (8, "Andressa", 19, "Engenharia");')

# confirma comandos
conexao.commit()

# EXERCICIO 3 - Consultas básicas
#
# a) Selecionar todos os registros da tabela "alunos" 
dados = cursor.execute('SELECT * FROM alunos;')
exibe_resultado_consulta('Exercício 3.a', dados)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos
dados = cursor.execute('SELECT * FROM alunos WHERE idade > 20;')
exibe_resultado_consulta('Exercício 3.b', dados)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome;')
exibe_resultado_consulta('Exercício 3.c', dados)

# d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT count(*) FROM alunos;')
exibe_resultado_consulta('Exercício 3.c', dados)

# EXERCICIO 4 - Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela
dados = cursor.execute('UPDATE alunos SET NOME = "Mauricio" WHERE id = 7;')

# b) Remova um aluno pleo seu ID
dados = cursor.execute('DELETE FROM alunos WHERE id = 5;')

# confirma comandos
conexao.commit()

# EXERCICIO 5 - Criar uma tabela e inserir dados
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto)
# idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela

cursor.execute('CREATE TABLE clientes(id INT NOT NULL PRIMARY KEY, nome VARCHAR(100) NOT NULL, idade INT, saldo FLOAT);')

# Insira pelo menos 5 registros de alunos na tablea que você criou no exercício anteior
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Isadora", 33, 0.0);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Maria", 48, 10000.0);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "José", 20, 2000.0);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Márcia",27, 500.0);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Antonio", 65, 0.0);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (6, "Carlos", 18, 6000.0);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (7, "Romeu", 29, 950.0);')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (8, "Andressa", 19, 400.0);')

# confirma comandos
conexao.commit()

# EXERCICIO 6 - Consultas e funções agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
exibe_resultado_consulta('Exercício 6.a', dados)

# b) Calcule o saldo médio dos clientes.
dados = cursor.execute('Select AVG(saldo) from clientes;')
exibe_resultado_consulta('Exercício 6.b', dados)

# c) Encontre o cliente com o saldo máximo.
dados = cursor.execute('select max(saldo) FROM clientes;')
max_saldo_clientes = [line[0] for line in dados][0]
print(f'Exercício 6.c - O maior saldo do cliente é de:{max_saldo_clientes}')

# d) Conte quantos clientes têm saldo acima de 1000 
dados = cursor.execute('select count(id) FROM clientes WHERE saldo > 1000.0;')
qtde_cliente_acima_mil = [line[0] for line in dados][0]
print(f'Exercício 6.d - A quantidade de clientes com saldo acima de 1000 é de: {qtde_cliente_acima_mil} cliente(s).')

# EXERCÍCIO 7 - Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico
cursor.execute('UPDATE clientes SET saldo = 3525.0 WHERE id = 1;')

# b) Remova um cliente pelo seu ID
cursor.execute('DELETE FROM clientes WHERE ID = 2;')

# confirma comandos
conexao.commit()

# EXERCÍCIO 8 - Junção de tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"),
# produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

cursor.execute('CREATE TABLE compras(id INT NOT NULL PRIMARY KEY, cliente_id INT NOT NULL, produto VARCHAR(50), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes (id));')

cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 1, "Monitor", 3000.0);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 1, "Celular", 1900.0);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 3, "Caminha para cachorro", 200.0);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 4, "Arroz", 20.0);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (5, 4, "Feijão", 8.0);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (6, 5, "Perfume", 250.0);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (7, 5, "Shampoo", 50.0);')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (8, 6, "Carro", 50000.0);')

dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id;')
exibe_resultado_consulta('Exercício 8', dados)

# fecha conexao
conexao.close
