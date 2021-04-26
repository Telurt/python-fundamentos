# Métodos

class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.enderecos = []

    def __str__(self):
        return f'email: {self.email}, senha: {self.senha}'

    def __iter__(self):
        return self.enderecos.__iter__()

    def _validar(self):
        email_cadastro = 'te@gmail.com'
        senha_cadastro = '1234'

        if email_cadastro == self.email and senha_cadastro == self.senha:
            print('Usuário Validado')
        else:
            print('Dados incorretos')

    def logar(self):
        self._validar()
        print('enviar para a tela principal')

    def forca_senha(self):
        if len(self.senha) > 5:
            return True
        else:
            return False

    # def cadastrar_endereco(self, endereco1, endereco2):
    #     print(f'Endereços: {endereco1}, {endereco2}')

    def cadastrar_endereco(self, *enderecos):
      for endereco in enderecos:
          print(f'endereço: {endereco}')


usuario = Usuario('te@gmail.com', '1234') # caixa de texto
usuario.logar()
print(usuario)
usuario.enderecos = ['rua1', 'rua2', 'rua aaaaa']
for endereco in usuario:
    print(f'endereço: {endereco}')

print(usuario)
# if usuario.forca_senha():
#     print('senha forte')
# else:
#     print('senha fraca')
#
# lista = ['rua1', 'rua2']
# usuario.cadastrar_endereco(*lista)
# usuario.cadastrar_endereco('rua1', 'rua2')
