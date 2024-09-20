import os

restaurantes=[{'nome':'Praca', 'categoria':'Japonesa', 'ativo':False},{'nome':'Pizza Suprema','categoria':'italiana','ativo':True},
 {'nome':'Cantina','categoria':'Francesa','ativo':False}
              ]


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def exibir_nome_do_programa():
        print("Sabor-express")


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar_app():
    os.system('cls')
    exibir_subtitulo('encerrando o app\n')


def opcao_invalida():
    print('Opcao invalida\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o Nome do restaurante que deseja cadastrar: ')
    categoria=input("Digite a categoria do restaurante: ")
    dados_do_restaurante={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado')


    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_restaurantes():
    print('Listando os restaurantes\n')
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria=restaurante['categoria']
        situacao=restaurante['ativo']
        print(f'-{nome_restaurante} | {categoria}|{situacao}')

def alterar_estado_restaurante():
    exibir_subtitulo('Alterando status ')
    nome_restaurante=input('Digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado=False

    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante ['ativo']
            print(f'Status do Restaurante {nome_restaurante} foi alterado')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    print(texto)
    print('****************************')

def voltar_ao_menu_principal():
    main()


def opcao_invalida():
    print('Opcao inválida\n')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida==1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida==2:
            exibir_subtitulo('Listar Restaurantes')
            listar_restaurantes()
            print('----------------------------------')
            voltar_ao_menu_principal()
        elif opcao_escolhida==3:
            alterar_estado_restaurante()

        elif opcao_escolhida==4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
            opcao_invalida()
    

if __name__=='__main__':
    main()
