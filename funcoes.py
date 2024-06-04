def exibirMensagem(nome, mensagem="Seja bem vindo"):
    print(f"Seja bem vindo, {nome}")
    return f"Usuário logado: {nome}"

nome_usuario = input('Digite o nome de usuário: ')
msg = input('Digite uma mensagem')
usuario = exibirMensagem(nome_usuario)
print(usuario)

print(50 * '-')

nome_usuario = input('Digite o nome de usuário: ')
msg = input('Digite uma mensagem')
usuario = exibirMensagem(nome_usuario)
print(usuario)