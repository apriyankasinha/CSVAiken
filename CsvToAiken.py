import os
import pandas as pd
import codecs

filepath = 'CSVQuestions.csv'

questions = pd.read_csv(filepath, encoding='utf-8')
print(questions)

aiken = codecs.open('AikenFromCSV.txt', 'w', 'utf-8')
for index, question in questions.iterrows():
    aiken.writelines(question['Question'] + '\n')
    aiken.writelines('A)' + question['OptionA'] + '\n')
    aiken.writelines('B)' + question['OptionB'] + '\n')
    aiken.writelines('C)' + question['OptionC'] + '\n')
    aiken.writelines('D)' + question['OptionD'] + '\n')
    aiken.writelines('ANSWER: ' + question['CorrectOption'] + '\n')
aiken.truncate()
aiken.close()