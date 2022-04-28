# Clientes da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos_disponiveis = ['basic', 'premium']
        if plano in self.planos_disponiveis:
            self.plano = plano
        else:
            print('Plano inválido.')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos_disponiveis:
            print('Plano modificado.')
            self.plano = novo_plano
        else:
            print('Plano inválido.')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}.')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}.')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Faça upgrade para premium para assistir o filme.')
        else:
            print('Plano inválido.')

cliente = Cliente('Edson', 'edson@gmail.com', 'basic')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')

# botão de upgrade
cliente.mudar_plano('premium')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')
