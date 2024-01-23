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

perguntas = ('Qual é o propósito da função print() em Python? ',
            'Qual é a forma correta de comentar uma linha em Python? ',
            'Como você declara uma variável em Python? ',
            'Qual é o operador para realizar uma exponenciação em Python? ',
            'O que é uma lista em Python? ')



alternativas = (("1. Capturar dados do usuário", "2. Exibir mensagens na tela", "3. Calcular valores matemáticos"),
                ("1. # Comentário", "2. // Comentário", "3. -- Comentário"),
                ("1. var x = 5", "2. var = 5", "3. int x = 5"),
                ("1. ^", "2. **", "3. ^^"),
                ("1. Um tipo de variável que armazena apenas números", "2. Uma coleção ordenada e mutável de itens", "3. Uma função que exibe informações na tela"))


respostas = ("2", "1", "1", "2", "1")

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
        print("Correto!")
    else:
        print("Resposta errada!")
        print(f"{respostas[num_questao]} é a resposta correta.")
    
    num_questao += 1