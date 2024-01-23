'''Projeto - Jogos com interface de linha de comando Proz'''
#Objetivo: treino de habilidades, criação de portifólio, resgate de conteúdos;
#Sugestões de temas: Perguntas e respostas, adivinhe o número, forca, jogo da velha;


#Projeto escolhido: Jogo de adivinhação

#Etapas: Formular Início do jogo
print("Bem-vindo ao jogo de adivinhação!")

nome = input("Digite seu nome: ")

num_questoes = 3;
print("{}, você terá {} opções, escolha a correta e avance a GRANDE VITÓRIA!" .format(nome, num_questoes))

print("Questão 1")
print("'Qual é o propósito da função print() em Python?'")
print("(1)Capturar dados do usuário,  (2)Exibir mensagens na tela,  (3)Calcular valores matemáticos")
opcao = int(input("Qual a opção correta? "))

if opcao == 2:
    print("Correto!")
elif opcao == 1 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")

print("Questão 2")
print("'Qual é a forma correta de comentar uma linha em Python?'")
print("(1)# Comentário,  (2)// Comentário,  (3)-- Comentário")
opcao = int(input("Qual a opção correta? "))

if opcao == 1:
    print("Correto!")
elif opcao == 2 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")

print("Questão 3")
print("'Como você declara uma variável em Python?'")
print("(1)var x = 5,  (2)x = 5,  (3)int x = 5")
opcao = int(input("Qual a opção correta? "))

if opcao == 1:
    print("Correto!")
elif opcao == 2 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")


print("Questão 4")
print("'Qual é o operador para realizar uma exponenciação em Python?'")
print("(1) ^,  (2) **,  (3) ^^")
opcao = int(input("Qual a opção correta? "))

if opcao == 2:
    print("Correto!")
elif opcao == 1 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")

print("Questão 5")
print("'O que é uma lista em Python?'")
print("(1)Um tipo de variável que armazena apenas números,  (2)Uma coleção ordenada e mutável de itens,  (3)Uma função que exibe informações na tela")
opcao = int(input("Qual a opção correta? "))

if opcao == 1:
    print("Correto!")
elif opcao == 2 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")


print("Questão 6")
print("'Como você verifica o comprimento de uma lista em Python?'")
print("(1)length(lista),  (2)lista.length(),  (3)len(lista)")
opcao = int(input("Qual a opção correta? "))

if opcao == 3:
    print("Correto!")
elif opcao == 1 and opcao == 2:
    print("Opção incorreta")
else:
    print("Opção inválida!")



print("Questão 7")
print("'O loop for é usado para?'")
print("(1)'Executar uma condição até que seja falsa,  (2)Executar um bloco de código um número específico de vezes,  (3)Executar um bloco de código com base em uma condição")
opcao = int(input("Qual a opção correta? "))

if opcao == 2:
    print("Correto!")
elif opcao == 1 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")


print("Questão 8")
print("'Qual é a função da instrução if em Python?'")
print("(1)Repetir um bloco de código,  (2)Executar uma ação apenas se uma condição for verdadeira,  (3)Interromper a execução do programa")
opcao = int(input("Qual a opção correta? "))

if opcao == 1:
    print("Correto!")
elif opcao == 2 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")


print("Questão 9")
print("'Qual função é utilizada para entrada de informação do usuário em Python?'")
print("(1)get_input(),  (2)read(),  (3)input()")
opcao = int(input("Qual a opção correta? "))

if opcao == 3:
    print("Correto!")
elif opcao == 1 and opcao == 2:
    print("Opção incorreta")
else:
    print("Opção inválida!")



print("Questão 10")
print("'O que é uma função em Python?'")
print("(1)Um bloco de código que executa uma ação específica,  (2)Uma variável que armazena valores,  (3)Uma condição que controla o fluxo do programa")
opcao = int(input("Qual a opção correta? "))

if opcao == 1:
    print("Correto!")
elif opcao == 2 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")

def mostra_opcoes():
    print("Opção 1")
    print("Opção 2")
    print("Opção 3")

print("PARABÉNS!")
print("Você se provou digno de ganhar o título de Sir. Python!")    

#Questões para implementação futura da opção pular
'''print("Questão x")
print("'O que o operador == realiza em Python?'")
print("(1)Atribui um valor a uma variável,  (2)Verifica a igualdade entre dois valores,  (3)Retorna um erro")
opcao = int(input("Qual a opção correta? "))

if opcao == 2:
    print("Correto!")
elif opcao == 1 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")



print("Questão x")
print("'Como você arredonda um número para o inteiro mais próximo em Python?'")
print("(1)round(x),  (2)floor(x),  (3)ceil(x)")
opcao = int(input("Qual a opção correta? "))

if opcao == 1:
    print("Correto!")
elif opcao == 2 and opcao == 3:
    print("Opção incorreta")
else:
    print("Opção inválida!")

def mostra_opcoes():
    print("Opção 1")
    print("Opção 2")
    print("Opção 3")

print("PARABÉNS!")
print("Você se provou digno de ganhar o título de Sir. Python!")'''

'''questions = [
    {
        'question': 'Qual é o propósito da função print() em Python?',
        'options': ['Capturar dados do usuário', 'Exibir mensagens na tela', 'Calcular valores matemáticos'],
        'correct_option': 2
    },
    {
        'question': 'Qual é a forma correta de comentar uma linha em Python?',
        'options': ['# Comentário', '// Comentário', '-- Comentário'],
        'correct_option': 1
    },
    {
        'question': 'Como você declara uma variável em Python?',
        'options': ['var x = 5', 'x = 5', 'int x = 5'],
        'correct_option': 1
    },
    {
        'question': 'Qual é o operador para realizar uma exponenciação em Python?',
        'options': ['^', '**', '^^'],
        'correct_option': 2
    },
    {
        'question': 'O que é uma lista em Python?',
        'options': ['Um tipo de variável que armazena apenas números', 'Uma coleção ordenada e mutável de itens', 'Uma função que exibe informações na tela'],
        'correct_option': 1
    },
    {
        'question': 'Como você verifica o comprimento de uma lista em Python?',
        'options': ['len(lista)', 'length(lista)', 'lista.length()'],
        'correct_option': 1
    },
    {
        'question': 'O que é um loop "for" usado para?',
        'options': ['Executar uma condição até que seja falsa', 'Executar um bloco de código um número específico de vezes', 'Executar um bloco de código com base em uma condição'],
        'correct_option': 2
    },
    {
        'question': 'Qual é a função da instrução "if" em Python?',
        'options': ['Repetir um bloco de código', 'Executar uma ação apenas se uma condição for verdadeira', 'Interromper a execução do programa'],
        'correct_option': 1
    },
    {
        'question': 'Como você lê a entrada do usuário em Python?',
        'options': ['input()', 'read()', 'get_input()'],
        'correct_option': 0
    },
    {
        'question': 'O que é uma função em Python?',
        'options': ['Um bloco de código que executa uma ação específica', 'Uma variável que armazena valores', 'Uma condição que controla o fluxo do programa'],
        'correct_option': 0
    },
    {
        'question': 'Qual é a diferença entre "==" e "is" em Python?',
        'options': ['Ambos testam a igualdade de valores', '"==" compara valores, "is" compara identidade de objetos', '"is" compara valores, "==" compara identidade de objetos'],
        'correct_option': 1
    },
    {
        'question': 'O que é um dicionário em Python?',
        'options': ['Uma coleção ordenada de itens', 'Uma estrutura de dados que armazena pares chave-valor', 'Uma função que retorna valores'],
        'correct_option': 1
    },
    {
        'question': 'Como você arredonda um número para o inteiro mais próximo em Python?',
        'options': ['round(x)', 'floor(x)', 'ceil(x)'],
        'correct_option': 0
    },
]

# quiz = Quiz(questions)
# quiz.run_quiz()





#Etapas: Formular regras de funcionamento'''
