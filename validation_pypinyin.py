import json
from pypinyin import pinyin, Style

answers = json.load(open('answers_arknights.json', 'r'))

count = 0
for answer in answers:
    pys = [py[0] for py in pinyin(answer['word'], style=Style.TONE3, v_to_u=True)]
    if pys != answer['pinyin']:
        print(answer['word'], answer['pinyin'], pys)
        count += 1

print('unmatched/total = {}/{}({:.2f}%)'.format(count, len(answers), 100 * count / len(answers)))