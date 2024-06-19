import json
from pypinyin import pinyin, Style

answer_dict = json.load(open('answers_arknights.json', 'r'))
pinyin_dict = json.load(open('pinyin_arknights.json', 'r'))

count = 0
for answer in answer_dict:
    pys = [py[0] for py in pinyin(answer['word'], style=Style.TONE3, v_to_u=True)]
    if pys != pinyin_dict[answer['word']]:
        print(answer['word'], pinyin_dict[answer['word']], pys)
        count += 1

print('unmatched/total = {}/{}({:.2f}%)'.format(count, len(answer_dict), 100 * count / len(answer_dict)))