import os
import pandas as pd
import codecs

filepath = 'AikenQuestions.txt'

aikenfile = open(filepath, encoding='utf-8')
questionlist = aikenfile.readlines()

questions = pd.DataFrame(columns=['Question', 'OptionA', 'OptionB', 'OptionC', 'OptionD', 'CorrectOption'])

def divideQuesion(questionlist, n):
    for i in range(0, len(questionlist), n):
        yield questionlist[i:i+n]

questionlist = list(divideQuesion(questionlist, 6))
print(questionlist)
for question in questionlist:
    for i in range(len(question)):
        if question[i].startswith(('A)', 'B)', 'C)', 'D)')):
            question[i] = question[i][2:]
        elif question[i].startswith('ANSWER:'):
            question[i] = question[i][8:]
        if question[i].endswith('\n'):
            question[i] = question[i][:-1]
    questions.loc[len(questions)] = question
print(questions)
questions.to_csv('CSVFromAiken.csv', index=False, encoding='utf-8')