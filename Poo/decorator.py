def verifica_usuario_logado(p_funcao):

   def verifica():
       print('[Antes vamos verificar se o usuario esta logado]')
       retorno = p_funcao()
       return retorno

   return verifica


@verifica_usuario_logado
def salva_postagem():
    print('Executando....')
    print('Post criado')