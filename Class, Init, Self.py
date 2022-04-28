# No python, existem duas formas para criar seu código. A primeira é escrever tudo linha a linha.
# A outra forma, é a orientada a objeto. Divida em duas partes, onde a primeira se trata de criar classes e na segunda,
# você utiliza dessas classes em seu código.

# Uma classe define os tipos de informação dentro de um dado, filtrando. Normalmente, assim são formadas as regras.
# Dentro dessas regras, criam-se os acontecimentos. Classe é o mesmo que um objeto, em python.
# Além das características, um objeto também vai ter métodos, funções.
# Tome um controle remoto como exemplo. A classe controle terá os atributos: COR, ALTURA, LARGURA, ESPESSURA e etc.
# O mesmo controle terá os métodos, que nesse caso seriam os botões do controle.

# Quando se cria uma classe, existem alguns padrões a se seguir em python. O primeiro padrão é definir a função
# __init__.
# O init inicializa a classe. É aonde os atributos do controle remoto estarão.
# O self é a própria classe, o próprio controle remoto. É o que define o que é uma característica dentro da classe.
# self.cor == cor do controle remoto que recebe o valor, o atributo cor.

class ControleRemoto:
    def __init__(self, cor, altura, largura, espessura):
        self.cor = cor
        self.altura = altura
        self.largura = largura
        self.espessura = espessura

    def passar_canal(self, botao):
        if botao == '+':
            print('Avançar o canal')
        elif botao == '-':
            print('Retroceder o canal')


controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm')   # Instância de ControleRemoto
controle_remoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm')  # Instância de ControleRemoto
controle_remoto.passar_canal('+')
controle_remoto2.passar_canal('-')
