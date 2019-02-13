# coding: utf-8
import json
from pprint import pprint

json_file = '/Users/ke/Documents/DATASET/DrQA/webQA/data/training.json'


"""
The QA json file, format:
'{"question": "q1", "answer": ["a11", ..., "a1i"]}'
...
'{"question": "qN", "answer": ["aN1", ..., "aNi"]}'
"""
train_file = open("webQA.json", 'w')


def clean_text(text):
    text = text.replace(' ', '')
    text = text.replace('＜＜', '《')
    text = text.replace('＞＞', '》')
    text = text.replace('<<', '《')
    text = text.replace('>>', '《')
    text = text.replace('我国', '中国')
    return text


"""
count = 0
no_answer = 0
with open(json_file) as f:
    for line in f:
        count += 1
        data = json.loads(line)
        question = data['question_tokens']

        no_answer_flag = True
        for item in data['evidences']:
            for dic, val in item.items():
                # print(dic, val)
                if dic == 'golden_answers' and val[0][0] != 'no_answer':
                    no_answer_flag = False
                    _dic = {"question": ''.join(data['question_tokens']), "answer": [''.join(val[0])]}
                    # print(question, val[0])
                    print(''.join(data['question_tokens']), ''.join(val[0]))
                    j_str = json.dumps(_dic)
                    train_file.write(j_str + '\n')

                    break
            if not no_answer_flag:
                break
        if no_answer_flag:
            no_answer += 1
            # print(''.join(data['question_tokens']))
            
print(no_answer)
print("Has answer percent: {} %".format(100.0 * (count - no_answer) / float(count)))
"""