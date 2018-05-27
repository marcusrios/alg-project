# -*- coding: utf-8 -*-

from content import questions_library
from utils import ask_user_name, ask_for_level, shuffle_questions, ask_for_answer, blank_line, count_score, suggestion
from time import sleep

def main():
    username = ask_user_name()
    level = ask_for_level()

    points = 0
    questions = questions_library()
    shuffle_questions(questions)
    
    for question in questions:
        if level == question['Level']:
            print(question['Intro'])
            sleep(1)
            print(question['Query'])
            for alternative in question['Alternatives']:
                print(alternative)
        
            answer = ask_for_answer()
        
            if answer == question['Answer']:
                print('Resposta correta!')
                points = count_score(points)
            else:
                print('Resposta errada. A respota correta é %s' %(question['Answer']))
        
            sleep(2)
            print('Curiosidade:', question['Curiosity'])
            blank_line()
    
    suggestion(level, points)

if __name__ == '__main__':
    main()