class Cliente:
    # construtor
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    # exibir dados
    def __str__(self):
        return f'{self.nome} - {self.email} - {self.telefone} {"-" * 30}'

    # cadastro
class Cadastrou:
    def __init__(self):
        # lista vazia
        self.clientes = []

    def cadastrar(self, cliente):
        # adiconar o cliente na lista vazia ( clientes)
        # append = adicionar
        self.clientes.append(cliente)

    def listar(self):
       if not self.clientes:
           print('Nenhum cliente cadastrado')
       else:
           print('Clientes cadastrados:')
           for cliente in self.clientes:
               print(cliente)


cadastrados = Cadastrou()

while True:
    print('1. Cadastrar cliente')
    print('2. Listar todos os clientes')
    print('3. sair')

    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Por favor, insira um número válido.')
        continue

    if opcao == 1:
        nome = input('Nome: ')
        email = input('Email: ')
        telefone = input('Telefone: ')
        cliente = Cliente(nome, email, telefone)
        cadastrados.cadastrar(cliente)

    elif opcao == 2:
        cadastrados.listar()

    elif opcao == 3:
        print('Saindo...')
        break

    else:
        print('Opção invalida... ')
