'''Projeto - Jogos com interface de linha de comando Proz'''
#Objetivo: treino de habilidades, criação de portifólio, resgate de conteúdos;
#Sugestões de temas: Perguntas e respostas, adivinhe o número, forca, jogo da velha;


#Projeto escolhido: Jogo de adivinhação

print("Bem-vindo ao jogo de adivinhação!")

nome = input("Digite seu nome: ")

num_questoes = 3;
print("{}, você terá {} opções, escolha a correta e avance a GRANDE VITÓRIA!" .format(nome, num_questoes))

#Criar array com questões

lista_perguntas = [
    {
        'pergunta': 'Qual é o propósito da função print() em Python?', 

'opcoes': ['(1)Capturar dados do usuário', '(2)Exibir mensagens na tela', '(3)Calcular valores matemáticos'], 

'resposta': 2
    },
    {
        'pergunta': 'Qual é a forma correta de comentar uma linha em Python?', 

'opcoes': ['(1)# Comentário', '(2)// Comentário', '(3)-- Comentário'], 

'resposta': 1 
    },
    {
        'pergunta': 'Como você declara uma variável em Python?', 

'opcoes': ['(1)var x = 5', '(2)var = 5', '(3)int x = 5'], 

'resposta': 1 
    },
    {
        'pergunta': 'Qual é o operador para realizar uma exponenciação em Python?', 

'opcoes': ['(1)^', '(2)**', '(3)^^'], 

'resposta': 2 
    },
    {
        'pergunta': 'Como você verifica o comprimento de uma lista em Python?', 

'opcoes': ['(1)len(lista)', '(2)length(lista)', '(3)lista.length()'], 

'resposta': 1 
    },
    {
        'pergunta': 'O loop for é usado para?', 

'opcoes': ['(1)Executar uma condição até que seja falsa', '(2)Executar um bloco de código um número específico de vezes', '(3)Executar um bloco de código com base em uma condição'], 

'resposta': 2 
    },
    {
        'pergunta': 'Qual é a função da instrução if em Python?', 

'opcoes': ['(1)Repetir um bloco de código', '(2)Executar uma ação apenas se uma condição for verdadeira', '(3)Interromper a execução do programa'], 

'resposta': 2 
    },
    {
        'pergunta': 'Qual função é utilizada para entrada de informação do usuário em Python?', 

'opcoes': ['(1)input()', '(2)read()', '(3)get_input()'], 

'resposta': 1 
    },
    {
        'pergunta': 'O que é uma função em Python?', 

'opcoes': ['(1)Um bloco de código que executa uma ação específica', '(2)Uma variável que armazena valores', '(3)Uma condição que controla o fluxo do programa'], 

'resposta': 1 
    },
    {
        'pergunta': 'O que o operador == realiza em Python?', 

'opcoes': ['(1)Atribui um valor a uma variável', '(2)Verifica a igualdade entre dois valores', '(3)Retorna um erro'], 

'resposta': 2
    },
    {
        'pergunta': 'Como você arredonda um número para o inteiro mais próximo em Python?', 

'opcoes': ['(1)round(x)', '(2)floor(x)', '(3)ceil(x)'], 

'resposta': 1 
    }

]

pontuacao = 0

for i, pergunta_atual in enumerate(lista_perguntas, start=1):
    print(f"\nQuestão {i}: {pergunta_atual['pergunta']}")
    for opcao in pergunta_atual['opcoes']:
        print(opcao)

    resposta_usuario = input("Escolha a opção correta (1, 2, 3) ou digite 'pular' para pular a pergunta: ")

    if resposta_usuario == 'PULAR':
        print("Pulando para a próxima pergunta.")
        continue

    elif int(resposta_usuario) == int(pergunta_atual['resposta']):
        print("Resposta correta!\n")
        pontuacao += 1
    else:
        print(f"Resposta incorreta. Fim do quiz.\nVocê acertou {pontuacao} perguntas.")
        break

if pontuacao == len(lista_perguntas):
    print("Parabéns! {} você acertou todas as perguntas e se provou digno de ganhar o título de Sir. Python!".format(nome))