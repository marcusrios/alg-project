# -*- coding: utf-8 -*-

from random import shuffle

# ask_user_name() ask for the user name and return this
def ask_user_name():
    user_name = input('Qual é seu nome? ')

    return user_name

# ask_for_level() ask for the game level and return this
def ask_for_level():
    game_level = input('Informe qual nível você deseja jogar. As opções são fácil, médio ou difícil: ')
    accepted_values = ['fácil', 'médio', 'difícil']

    while game_level.lower() not in accepted_values:
        game_level = input('Nível de difícildade inválido. Selecione entre fácil, médio ou difícil. ')

    return game_level.lower()

# shuffle_questions() receives a list and and shuffles it
def shuffle_questions(vector):
    shuffle(vector)

# ask_for_answer() ask for an answer and return this
def ask_for_answer():
    answer = input('Qual a resposta correta? ')
    accepted_values = ['A', 'B', 'C', 'D']

    while answer.upper() not in accepted_values:
        answer = input('Opção inválida. Seleciona a, b, c ou d. ')

    return answer.upper()

# count_score() increments the score
def count_score(score):
    score += 1
    return score

# blank_line() print's two blank line
def blank_line():
    print('\n')

# suggestion() show a suggestion based on user progress
def suggestion(level, points):
    if level == 'fácil':
        if points > 4:
            print('você obteve %i pontos. Parabéns, sua pontuação foi exelente! Que tal tentar jogar novamente na dificuldade médio?' %(points))
        else:
            print('você obteve %i pontos. Continue praticando.' %(points))
    elif level == 'médio':
        if points > 4:
            print('você obteve %i pontos. Parabéns sua pontuação foi excelente! Que tal tentar novamente na dificuldade difícil?' %(points))
        elif points < 3:
            print('você obteve %i pontos. Ops parece que você não teve um bom desempenho. Que tal tentar novamente na difícildade fácil?' %(points))
        else:
            print('você obteve %i pontos. Continue praticando, em breve você acertará todas as questões.' %(points))
    else:
        if points > 4:
            print('você obteve %i pontos. Parabéns sua pontuação foi incrível e você venceu o jogo na maior dificuldade!' %(points))
        elif points < 3:
            print('você obteve %i pontos. Ops parece que você não teve um bom desempenho. Que tal tentar novamente na difícildade médio?' %(points))    
        else:
            print('você obteve %i pontos. Você está no caminho certo, continue praticando.' %(points))