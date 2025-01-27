import json
from pypinyin import pinyin, Style

answer_dict = json.load(open('answers_arknights.json', 'r'))
pinyin_dict = json.load(open('pinyin_arknights.json', 'r'))
pinyin_whitelist = json.load(open('pypinyin_diff_whitelist.json', 'r'))

count = 0
whitelist_count = 0
whitelist_details = []
whitelist_same_details = []
# is_show_whitelist_details = False
is_show_whitelist_details = True

for answer in answer_dict:
    pys = [py[0] for py in pinyin(answer['word'], style=Style.TONE3, v_to_u=True)]
    if answer['word'] in pinyin_whitelist:
        whitelist_count += 1
        if is_show_whitelist_details:
            if pys == pinyin_dict[answer['word']]:
                whitelist_same_details.append('{} {} {} {} {}'.format(
                    answer['word'],
                    ''.join(['x_'[int(pinyin_dict[answer['word']][i] == pys[i])] for i in range(4)]),
                    pinyin_dict[answer['word']],
                    pys,
                    pinyin_whitelist[answer['word']]
                ))
            else:
                whitelist_details.append('{} {} {} {} {}'.format(
                    answer['word'],
                    ''.join(['x_'[int(pinyin_dict[answer['word']][i] == pys[i])] for i in range(4)]),
                    pinyin_dict[answer['word']],
                    pys,
                    pinyin_whitelist[answer['word']]
                ))
        continue
    if pys != pinyin_dict[answer['word']]:
        print('{} {} {} {}'.format(
            answer['word'],
            ''.join(['x_'[int(pinyin_dict[answer['word']][i] == pys[i])] for i in range(4)]),
            pinyin_dict[answer['word']],
            pys,
        ))
        count += 1

print('{}/{}({:.2f}%)词语在pypinyin_diff_whitelist.json中'.format(whitelist_count, len(answer_dict), 100 * whitelist_count / len(answer_dict)))
if is_show_whitelist_details:
    for line in whitelist_details:
        print(line)
    if len(whitelist_same_details):
        print('{}词语在pypinyin_diff_whitelist.json中但是在pinyin_arknights.json中的拼音与pypinyin的结果匹配'.format(len(whitelist_same_details)))
        for line in whitelist_same_details:
            print(line)
print('{}/{}({:.2f}%)词语在pinyin_arknights.json中的拼音与pypinyin的结果不匹配'.format(count, len(answer_dict), 100 * count / len(answer_dict)))
