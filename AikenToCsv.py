import os
import pandas as pd
import codecs

filepath = 'aikenquestions.txt'

aikenfile = open(filepath, encoding='utf-8')
questionlist = aikenfile.readlines()

questions = pd.DataFrame(columns=['Question', 'OptionA', 'OptionB', 'OptionC', 'OptionD', 'CorrectOption'])

def divideQuesion(questionlist, n):
    for i in range(0, len(questionlist), n):
        yield questionlist[i:i+n]

questionlist = list(divideQuesion(questionlist, 6))
for question in questionlist:
    for i in range(len(question)):
        if question[i].startswith(('A)', 'B)', 'C)', 'D)')):
            question[i] = question[i][2:-1]
        elif question[i].startswith('ANSWER:'):
            question[i] = question[i][8:-1]
        else:
            question[i] = question[i][:-1]
    questions.loc[len(questions)] = question
questions.to_csv('CSVFromAiken.csv', index=False)