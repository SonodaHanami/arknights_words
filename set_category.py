# deprecated
import json

operators = [
    "推进之王", "风笛", "嵯峨", "琴柳", "焰尾", "伺夜", "伊内丝", "缪尔赛思",
    "银灰", "斯卡蒂", "陈", "赫拉格", "煌", "棘刺", "史尔特尔", "山", "帕拉斯", "耀骑士临光",
    "艾丽妮", "百炼嘉维尔", "玛恩纳", "重岳", "仇白", "圣约送葬人", "赫德雷", "止颂", "薇薇安娜", "锏",
    "星熊", "塞雷娅", "年", "森蚺", "瑕光", "泥岩", "号角", "斥罪", "涤火杰西卡",
    "能天使", "黑", "W", "早露", "迷迭香", "空弦", "灰烬", "假日威龙陈", "远牙", "菲亚梅塔", "鸿雪", "提丰",
    "伊芙利特", "艾雅法拉", "莫斯提马", "刻俄柏", "夕", "异客", "卡涅利安", "澄闪", "黑键", "林", "霍尔海雅",
    "闪灵", "夜莺", "凯尔希", "流明", "焰影苇草", "纯烬艾雅法拉",
    "安洁莉娜", "麦哲伦", "铃兰", "浊心斯卡蒂", "灵知", "令", "白铁", "淬羽赫默", "塑心",
    "阿", "傀影", "温蒂", "歌蕾蒂娅", "水月", "老鲤", "归溟幽灵鲨", "多萝西", "缄默德克萨斯", "麒麟R夜刀", "琳琅诗怀雅",
    "凛冬", "德克萨斯", "格拉尼", "苇草", "极境", "贾维", "野鬃", "夜半", "晓歌", "谜图", "青枳",
    "芙兰卡", "因陀罗", "拉普兰德", "幽灵鲨", "暴行", "诗怀雅", "星极", "炎客", "布洛卡", "柏喙",
    "铸铁", "断崖", "燧石", "鞭刃", "阿米娅(近卫)", "战车", "赤冬", "龙舌兰", "羽毛笔", "海沫",
    "达格达", "铎铃", "火龙S黑角", "摩根", "苍苔", "烈夏",
    "临光", "雷蛇", "可颂", "火神", "拜松", "吽", "石棉", "闪击", "暴雨", "灰毫",
    "极光", "暮落", "车尔尼", "火哨", "洋灰", "深律",
    "蓝毒", "白金", "陨星", "普罗旺斯", "守林人", "送葬人", "灰喉", "慑砂", "安哲拉", "四月",
    "奥斯塔", "熔泉", "寒芒克洛丝", "埃拉托", "承曦格雷伊", "子月", "截云", "玫拉", "隐现", "冰酿",
    "阿米娅", "天火", "夜魔", "惊蛰", "苦艾", "莱恩哈特", "蜜蜡", "特米米", "薄绿", "爱丽丝",
    "炎狱炎熔", "蚀清", "耶拉", "洛洛", "星源", "至简", "雪绒", "和弦", "寒檀", "戴菲恩",
    "折光",
    "白面鸮", "赫默", "华法琳", "锡兰", "微风", "亚叶", "絮雨", "图耶", "桑葚", "蜜莓",
    "濯尘芙蓉", "明椒", "刺玫", "哈洛德",
    "梅尔", "初雪", "真理", "空", "格劳克斯", "巫恋", "月禾", "稀音", "九色鹿", "夏栎",
    "海蒂", "掠风", "但书", "凛视",
    "红", "崖心", "狮蝎", "食铁兽", "槐琥", "雪雉", "罗宾", "卡夫卡", "乌有", "霜华",
    "贝娜", "绮良", "见行者", "风丸", "空构", "杏仁",
    "讯使", "清道夫", "红豆", "桃金娘", "豆苗",
    "杜宾", "缠丸", "霜叶", "艾丝黛尔", "慕斯", "猎蜂", "宴", "断罪者", "刻刀", "芳汀", "杰克", "罗小黑", "石英", "休谟斯",
    "角峰", "蛇屠箱", "古米", "坚雷", "泡泡",
    "杰西卡", "流星", "白雪", "红云", "梅", "安比尔", "酸糖", "松果", "铅踝", "跃跃",
    "夜烟", "远山", "格雷伊", "卡达", "深靛", "布丁",
    "末药", "嘉维尔", "调香师", "苏苏洛", "清流", "褐果",
    "深海色", "地灵", "波登可", "罗比菈塔",
    "砾", "暗索", "阿消", "伊桑", "孑", "维荻",
    "芬", "香草", "翎羽", "玫兰莎", "月见夜", "泡普卡", "卡缇", "米格鲁", "斑点",
    "克洛丝", "安德切尔", "空爆", "炎熔", "史都华德", "芙蓉", "安赛尔", "梓兰",
    "夜刀", "黑角", "巡林者", "杜林", "12F",
    "Castle-3", "Friston-3", "正义骑士号", "泰拉大陆调查团", "Lancet-2", "U-Official", "THRM-EX",
    "郁金香", "Pith", "Sharp", "Stormeye", "Touch",
    '火龙黑角', '麒麟夜刀', '预备干员'
]

answer_path = './answers_arknights.json'

with open(answer_path, 'r', encoding='utf-8') as f:
    answers = json.load(f)

for answer in answers:
    if not answer.get('category'):
        answer['category'] = []
    if '干员/装置/可部署物品名' in answer['explanation']:
        if '干员代号' in answer['category']:
            answer['category'].remove('干员代号')
        if '装置/可部署物品名' in answer['category']:
            answer['category'].remove('装置/可部署物品名')
        if answer['word'] in operators:
            if '干员代号' not in answer['category']:
                answer['category'].append('干员代号')
        else:
            if '装置/可部署物品名' not in answer['category']:
                answer['category'].append('装置/可部署物品名')

    if '的第1技能' in answer['explanation'] or '的第2技能' in answer['explanation'] or '的第3技能' in answer['explanation']:
        if '干员技能' in answer['category']:
            answer['category'].remove('干员技能')
        if '其他技能' in answer['category']:
            answer['category'].remove('其他技能')
        is_operator = False
        for opr in operators:
            if opr == answer['explanation'].split('的')[0]:
                is_operator = True
                break
        if is_operator:
            if '干员技能' not in answer['category']:
                answer['category'].append('干员技能')
        else:
            if '其他技能' not in answer['category']:
                answer['category'].append('其他技能')
    if '的第1天赋' in answer['explanation']:
        if '干员天赋' not in answer['category']:
            answer['category'].append('干员天赋')
    if '的第2天赋' in answer['explanation']:
        if '干员天赋' not in answer['category']:
            answer['category'].append('干员天赋')
    if '模组' in answer['explanation']:
        if '干员模组' not in answer['category']:
            answer['category'].append('干员模组')
    if '解锁的基建技能' in answer['explanation']:
        if '干员基建技能' not in answer['category']:
            answer['category'].append('干员基建技能')

    if '的收藏品' in answer['explanation']:
        if '收藏品' not in answer['category']:
            answer['category'].append('收藏品')
        if '傀影与猩红孤钻' in answer['explanation']:
            if '傀影与猩红孤钻中的收藏品' not in answer['category']:
                answer['category'].append('傀影与猩红孤钻中的收藏品')
        if '水月与深蓝之树' in answer['explanation']:
            if '水月与深蓝之树中的收藏品' not in answer['category']:
                answer['category'].append('水月与深蓝之树中的收藏品')
        if '探索者的银凇止境' in answer['explanation']:
            if '探索者的银凇止境中的收藏品' not in answer['category']:
                answer['category'].append('探索者的银凇止境中的收藏品')

    if '傀影与猩红孤钻中的关卡' in answer['explanation'] or '水月与深蓝之树中的关卡' in answer['explanation'] or '探索者的银凇止境中的关卡' in answer['explanation']:
        if '集成战略关卡' not in answer['category']:
            answer['category'].append('集成战略关卡')
        if '傀影与猩红孤钻中的关卡' in answer['category']:
            answer['category'].remove('傀影与猩红孤钻中的关卡')
        if '水月与深蓝之树中的关卡' in answer['category']:
            answer['category'].remove('水月与深蓝之树中的关卡')
        if '探索者的银凇止境中的关卡' in answer['category']:
            answer['category'].remove('探索者的银凇止境中的关卡')
        if '傀影与猩红孤钻中的关卡' in answer['explanation']:
            if '傀影与猩红孤钻中的关卡' not in answer['category']:
                answer['category'].append('傀影与猩红孤钻中的关卡')
        if '水月与深蓝之树中的关卡' in answer['explanation']:
            if '水月与深蓝之树中的关卡' not in answer['category']:
                answer['category'].append('水月与深蓝之树中的关卡')
        if '探索者的银凇止境中的关卡' in answer['explanation']:
            if '探索者的银凇止境中的关卡' not in answer['category']:
                answer['category'].append('探索者的银凇止境中的关卡')

    if '傀影与猩红孤钻中的事件' in answer['explanation'] or '水月与深蓝之树中的事件' in answer['explanation'] or '探索者的银凇止境中的事件' in answer['explanation']:
        if '集成战略事件' not in answer['category']:
            answer['category'].append('集成战略事件')
        if '傀影与猩红孤钻中的事件' in answer['category']:
            answer['category'].remove('傀影与猩红孤钻中的事件')
        if '水月与深蓝之树中的事件' in answer['category']:
            answer['category'].remove('水月与深蓝之树中的事件')
        if '探索者的银凇止境中的事件' in answer['category']:
            answer['category'].remove('探索者的银凇止境中的事件')
        if '傀影与猩红孤钻中的事件' in answer['explanation']:
            if '傀影与猩红孤钻中的事件' not in answer['category']:
                answer['category'].append('傀影与猩红孤钻中的事件')
        if '水月与深蓝之树中的事件' in answer['explanation']:
            if '水月与深蓝之树中的事件' not in answer['category']:
                answer['category'].append('水月与深蓝之树中的事件')
        if '探索者的银凇止境中的事件' in answer['explanation']:
            if '探索者的银凇止境中的事件' not in answer['category']:
                answer['category'].append('探索者的银凇止境中的事件')

    if '傀影与猩红孤钻中的节点' in answer['explanation'] or '水月与深蓝之树中的节点' in answer['explanation'] or '探索者的银凇止境中的节点' in answer['explanation']:
        if '集成战略节点' not in answer['category']:
            answer['category'].append('集成战略节点')
        if '傀影与猩红孤钻中的节点' in answer['category']:
            answer['category'].remove('傀影与猩红孤钻中的节点')
        if '水月与深蓝之树中的节点' in answer['category']:
            answer['category'].remove('水月与深蓝之树中的节点')
        if '探索者的银凇止境中的节点' in answer['category']:
            answer['category'].remove('探索者的银凇止境中的节点')
        if '傀影与猩红孤钻中的节点' in answer['explanation']:
            if '傀影与猩红孤钻中的节点' not in answer['category']:
                answer['category'].append('傀影与猩红孤钻中的节点')
        if '水月与深蓝之树中的节点' in answer['explanation']:
            if '水月与深蓝之树中的节点' not in answer['category']:
                answer['category'].append('水月与深蓝之树中的节点')
        if '探索者的银凇止境中的节点' in answer['explanation']:
            if '探索者的银凇止境中的节点' not in answer['category']:
                answer['category'].append('探索者的银凇止境中的节点')

    if '集成战略分队' in answer['explanation']:
        if '集成战略分队' not in answer['category']:
            answer['category'].append('集成战略分队')

    if '傀影与猩红孤钻中的' in answer['explanation'] or '水月与深蓝之树中的' in answer['explanation'] or '探索者的银凇止境中的' in answer['explanation']:
        if '层' in answer['explanation']:
            if '集成战略层数' not in answer['category']:
                answer['category'].append('集成战略层数')
        if '难度选项' in answer['explanation']:
            if '集成战略难度选项' not in answer['category']:
                answer['category'].append('集成战略难度选项')
        if '结局' in answer['explanation']:
            if '集成战略结局' not in answer['category']:
                answer['category'].append('集成战略结局')

    if '水月肉鸽排异反应' in answer['explanation'] or '水月与深蓝之树中的排异反应' in answer['explanation']:
        answer['explanation'] = '水月与深蓝之树中的排异反应'
        if '水月与深蓝之树中的排异反应' not in answer['category']:
            answer['category'].append('水月与深蓝之树中的排异反应')

    if '物品，可能来自不同活动' in answer['explanation']:
        if '物品' not in answer['category']:
            answer['category'].append('物品')

    if '普通敌人' in answer['explanation'] or '精英敌人' in answer['explanation'] or '领袖敌人' in answer['explanation']:
        if '敌人' not in answer['category']:
            answer['category'].append('敌人')

    if '活动名' in answer['explanation']:
        if '活动' not in answer['category']:
            answer['category'].append('活动')
    if '危机合约赛季名' in answer['explanation']:
        if '活动' not in answer['category']:
            answer['category'].append('活动')

no_category_answers = []
new_answers = []
for answer in answers:
    if answer.get('category'):
        new_answers.append(answer)
    else:
        answer['category'].append('其他')
        new_answers.append(answer)
        no_category_answers.append(answer)
print(f'{len(no_category_answers)}/{len(answers)}')
print(no_category_answers)


# print(answers)
with open(answer_path, 'w', encoding='utf-8') as f:
    json.dump(new_answers, f, indent=4, ensure_ascii=False, sort_keys=False)
