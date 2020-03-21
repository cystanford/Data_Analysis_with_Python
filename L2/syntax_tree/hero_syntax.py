import random

# 定语从句语法
grammar = '''
战斗 => 施法  ， 结果 。
施法 => 主语 动作 技能 
结果 => 主语 获得 效果
主语 => 张飞 | 关羽 | 赵云 | 典韦 | 许褚 | 刘备 | 黄忠 | 曹操 | 鲁班七号 | 貂蝉
动作 => 施放 | 使用 | 召唤 
技能 => 一骑当千 | 单刀赴会 | 青龙偃月 | 刀锋铁骑 | 黑暗潜能 | 画地为牢 | 守护机关 | 狂兽血性 | 龙鸣 | 惊雷之龙 | 破云之龙 | 天翔之龙
获得 => 损失 | 获得 
效果 => 数值 状态
数值 => 1 | 1000 |5000 | 100 
状态 => 法力 | 生命
'''

# 得到语法字典
def getGrammarDict(gram, linesplit = "\n", gramsplit = "=>"):
    #定义字典
    result = {}

    for line in gram.split(linesplit):
        # 去掉首尾空格后，如果为空则退出
        if not line.strip(): 
            continue
        expr, statement = line.split(gramsplit)
        result[expr.strip()] = [i.split() for i in statement.split("|")]
    #print(result)
    return result

# 生成句子
def generate(gramdict, target, isEng = False):
    if target not in gramdict: 
        return target
    find = random.choice(gramdict[target])
    #print(find)
    blank = ''
    # 如果是英文中间间隔为空格
    if isEng: 
        blank = ' '
    return blank.join(generate(gramdict, t, isEng) for t in find)

gramdict = getGrammarDict(grammar)
print(generate(gramdict,"战斗"))
print(generate(gramdict,"战斗", True))


