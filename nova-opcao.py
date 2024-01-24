#Menu inicialização/apresentação

print("Bem vindo ao desafio de Python!")
print("--------------------------------------")
nome = input("Informe seu nome para começarmos: ")

print(f"{nome}, você será desafiado por questões relacionadas a programação na linguagm Python, está pronto?") 
print("--------------------------------------")

iniciar = input(("Digite 's' para iniciar ou qualquer outra tecla para sair: "))

if iniciar.lower() == 's':
    print("Iniciando")
    print("--------------------------------------")
else:
    print("Saindo! Quiz finalizado com sucesso.")
    
    
    
#Desenvolvimento questões

perguntas = ('1. Qual é o propósito da função print() em Python? ',
            '2. Qual é a forma correta de comentar uma linha em Python? ',
            '3. Como você declara uma variável em Python? ',
            '4. Qual é o operador para realizar uma exponenciação em Python? ',
            '5. O que é uma lista em Python? ',
            '6. Como você verifica o comprimento de uma lista em Python?',
            '7. O loop for é usado para?',
            '8. Qual é a função da instrução if em Python?',
            '9. Qual função é utilizada para entrada de informação do usuário em Python?',
            '10. O que é uma função em Python?')



alternativas = (("1. Capturar dados do usuário", "2. Exibir mensagens na tela", "3. Calcular valores matemáticos"),
                ("1. # Comentário", "2. // Comentário", "3. -- Comentário"),
                ("1. var x = 5", "2. var = 5", "3. int x = 5"),
                ("1. ^", "2. **", "3. ^^"),
                ("1. Um tipo de variável que armazena elementos de diferentes tipos, incluindo números inteiros (int), strings (str), e outros tipos de dados.", "2. Uma coleção ordenada e imutável de itens", "3. Uma função que exibe informações na tela"),
                ("1. len(lista)","2. length(lista)", "3. lista.length()"),
                ("1. Executar uma condição até que seja falsa","2. Executar um bloco de código um número específico de vezes", "3. Executar um bloco de código com base em uma condição"),
                ("1. Repetir um bloco de código","2. Executar uma ação apenas se uma condição for verdadeira", "3. Interromper a execução do programa"),
                ("1. input()","2. read()", "3. get_input()"),
                ("1. Um bloco de código que executa uma ação específica","2. Uma variável que armazena valores", "3. Uma condição que controla o fluxo do programa")
                )


respostas = ("2", "1", "1", "2", "1", "1", "2", "2", "1", "1")

escolhas = []

pontuacao = 0

num_questao = 0


for pergunta in perguntas:
    print("---------------------------------------")
    print(pergunta)
    for alternativa in alternativas[num_questao]:
        print(alternativa)
        
    escolha = input(" Escolha a opção (1, 2, 3): ")
    escolhas.append(escolha)
    if escolha == respostas[num_questao]:
        pontuacao += 1
        print("CERTA RESPOSTA!")
    else:
        print("RESPOSTA ERRADA!")
        print(f"A opção {respostas[num_questao]} é a correta.")
    num_questao += 1
    
    
print("---------------------------------------")
print("------------Resultado------------------")
print("---------------------------------------")


print('Respostas: ', end=" ")
for resposta in respostas:
    print("", resposta, end=" ")
print()

print("Palpites: ", end="")
for escolha in escolhas:
    print("", escolha, end=" ")
print()

pontuacao = int(pontuacao / len(perguntas) * 100)
print(f"Sua pontuação é: {pontuacao}%")