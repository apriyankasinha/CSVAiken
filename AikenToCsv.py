import os
import pandas as pd
import codecs

#print('Place the questions in aikenquestions.txt file and proceed')

filepath = 'aikenquestions.txt'

aikenfile = open(filepath, encoding='utf-8')
questionlist = aikenfile.readlines()
#print(questionlist)

questions = pd.DataFrame(columns=['Question', 'OptionA', 'OptionB', 'OptionC', 'OptionD', 'CorrectOption'])
#print(questions)

def divideQuesion(questionlist, n):
    for i in range(0, len(questionlist), n):
        yield questionlist[i:i+n]

questionlist = list(divideQuesion(questionlist, 6))
#print(questionlist)
#print('\n\n')
for question in questionlist:
    #print(question)
    for i in range(len(question)):
        #print(question[i])
        if question[i].startswith(('A)', 'B)', 'C)', 'D)')):
            question[i] = question[i][2:-1]
            #print('*******'+question[i] + '***\n')
        elif question[i].startswith('ANSWER:'):
            question[i] = question[i][8:-1]
        else:
            question[i] = question[i][:-1]
    #print(question)
    questions.loc[len(questions)] = question
#   questions = questions.append(question)
print(questions)
questions.to_csv('CSVFromAiken.csv', index=False)