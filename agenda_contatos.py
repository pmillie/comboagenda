class Contato:
    def __init__(self, nome, telefone, email, redes_sociais):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.redes_sociais = redes_sociais

    def exibir(self):
        print("=" * 30)
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print("Redes Sociais:")
        for i, rede_social in enumerate(self.redes_sociais, start=1):
            print(f"{i}. {rede_social}")
        print("=" * 30)


agenda = []

while True:
    print("== Agenda de Contatos ==")
    print("1. Adicionar Contato")
    print("2. Exibir Contatos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        redes_sociais = []

        while True:
            rede_social = input("Rede Social (ou deixe em branco para sair): ")
            if not rede_social:
                break
            redes_sociais.append(rede_social)

        contato = Contato(nome, telefone, email, redes_sociais)
        agenda.append(contato)
        print("Contato adicionado com sucesso!")
        print()

    elif opcao == "2":
        if len(agenda) == 0:
            print("Agenda vazia. Adicione contatos.")
        else:
            print("== Contatos ==")
            for i, contato in enumerate(agenda, start=1):
                print(f"{i}.")
                contato.exibir()
        print()

    elif opcao == "3":
        break

    else:
        print("Opção inválida. Tente novamente.")
        print()
